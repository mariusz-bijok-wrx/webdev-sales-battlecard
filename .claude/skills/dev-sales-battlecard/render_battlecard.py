"""Render a one-page A4-landscape sales battlecard (.xlsx) from a JSON spec.

Usage: python3 render_battlecard.py spec.json out.xlsx

Spec:
{
  "title": str, "subtitle": str, "assumptions": str, "recommendation": str,
  "currency": "USD", "hourly_rate": number | null,
  "technologies": [str, ...],                       # 2-6 columns
  "costs": {tech: {"licenses_year": number, "hosting_year": number, "hours": number | null}},
  "labels": {"licenses_year": str, "hosting_year": str, "total_3y": str, "technology": str, "no_data": str},
  "sections": [{"name": str, "rows": [{"label": str, "cells": {tech: str}}]}],
  "excluded": str,                                  # optional: named technologies left out, with reasons
  "sources": str
}
"""
import json
import math
import re
import sys

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

FONT = "Avenir"
MAX_TECH = 6
MAX_TEXT_ROWS = 12
MAX_CELL_CHARS = 130           # ~2 short sentences; longer text breaks the one-page layout
MAX_SENTENCES = 2
MIN_PRINT_SCALE = 0.6          # below this the printed text is too small to read
LABEL_WIDTH = 24               # Excel column width units (~characters)
TECH_WIDTH = 34
BODY_PT, HEADER_PT, TITLE_PT = 8, 9, 13
PT_PER_LINE = 11
YEARS = 3

INK, MUTED, BAND, HEAD, LINE = "1F2933", "52606D", "E4E7EB", "243B53", "CBD2D9"
thin = Side(style="thin", color=LINE)
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
WRAP = Alignment(wrap_text=True, vertical="top")


def font(size=BODY_PT, bold=False, color=INK):
    return Font(name=FONT, size=size, bold=bold, color=color)


ABBREVIATIONS = ("np", "tys", "mies", "ok", "in", "itp", "tj", "e.g", "i.e", "approx")


def sentences(text):
    # A sentence ends at .!? + capital letter, except after abbreviations ("np. Black Friday", "tys. Elementy").
    ends = [m for m in re.finditer(r"(\w[\w.]*)?([.!?])\s+(?=[A-ZĄĆĘŁŃÓŚŹŻ])", text)
            if not (m.group(2) == "." and (m.group(1) or "").lower() in ABBREVIATIONS)]
    return len(ends) + 1


def validate(spec):
    errors = []
    techs = spec["technologies"]
    if not 2 <= len(techs) <= MAX_TECH:
        errors.append(f"technologies: need 2-{MAX_TECH}, got {len(techs)}")
    rows = [r for s in spec["sections"] for r in s["rows"]]
    if len(rows) > MAX_TEXT_ROWS:
        errors.append(f"rows: max {MAX_TEXT_ROWS}, got {len(rows)}")
    if sentences(spec["recommendation"]) > MAX_SENTENCES:
        errors.append("recommendation: max 2 sentences")
    for r in rows:
        for t in techs:
            text = r["cells"].get(t, "").strip()
            if not text:
                errors.append(f"empty cell: {r['label']} / {t}")
            elif len(text) > MAX_CELL_CHARS:
                errors.append(f"too long ({len(text)} chars): {r['label']} / {t}")
            elif sentences(text) > MAX_SENTENCES:
                errors.append(f"max 2 sentences: {r['label']} / {t}")
    for t in techs:
        if t not in spec["costs"]:
            errors.append(f"costs missing for {t}")
    return errors


def lines_needed(text, width_units):
    chars_per_line = max(1, int(width_units * 1.15))  # 8pt text fits ~1.15 chars per width unit
    return sum(max(1, math.ceil(len(part) / chars_per_line)) for part in text.split("\n"))


def render(spec, path):
    techs = spec["technologies"]
    labels = spec["labels"]
    last_col = get_column_letter(1 + len(techs))
    wb = Workbook()
    ws = wb.active
    ws.title = spec.get("sheet_name", "Battlecard")[:31]

    ws.column_dimensions["A"].width = LABEL_WIDTH
    for i in range(len(techs)):
        ws.column_dimensions[get_column_letter(2 + i)].width = TECH_WIDTH
    total_width = LABEL_WIDTH + TECH_WIDTH * len(techs)

    heights = []

    def full_row(row, text, size=BODY_PT, bold=False, color=INK, fill=None):
        ws.merge_cells(f"A{row}:{last_col}{row}")
        cell = ws[f"A{row}"]
        cell.value = text
        cell.font = font(size, bold, color)
        cell.alignment = WRAP
        if fill:
            cell.fill = PatternFill("solid", fgColor=fill)
        height = max(size + 4, lines_needed(text, total_width * BODY_PT / size) * (size + 3))
        ws.row_dimensions[row].height = height
        heights.append(height)

    row = 1
    full_row(row, spec["title"], TITLE_PT, bold=True)
    row += 1
    full_row(row, spec["subtitle"], BODY_PT, color=MUTED)
    row += 1
    full_row(row, spec["assumptions"], BODY_PT, color=MUTED)
    row += 1
    full_row(row, spec["recommendation"], HEADER_PT, bold=True, fill=BAND)

    row += 1
    header_row = row
    ws.cell(row, 1, labels["technology"])
    for i, t in enumerate(techs):
        ws.cell(row, 2 + i, t)
    for c in range(1, 2 + len(techs)):
        cell = ws.cell(row, c)
        cell.font = font(HEADER_PT, True, "FFFFFF")
        cell.fill = PatternFill("solid", fgColor=HEAD)
        cell.alignment = WRAP
        cell.border = BOX
    ws.row_dimensions[row].height = 16
    heights.append(16)

    rate = spec.get("hourly_rate")
    money = '#,##0 "' + spec["currency"] + '"'
    lic_row, host_row, total_row = row + 1, row + 2, row + 3
    row = total_row
    for r, key in ((lic_row, "licenses_year"), (host_row, "hosting_year"), (total_row, "total_3y")):
        ws.cell(r, 1, labels[key])
    for i, t in enumerate(techs):
        col = get_column_letter(2 + i)
        cost = spec["costs"][t]
        ws.cell(lic_row, 2 + i, cost["licenses_year"]).number_format = money
        ws.cell(host_row, 2 + i, cost["hosting_year"]).number_format = money
        yearly = f"({col}{lic_row}+{col}{host_row})*{YEARS}"
        hours = cost.get("hours")
        if rate and hours:
            formula = f"={yearly}+{hours}*{rate}"
        elif rate:
            # Rate given but no hours in db.csv: never show a total that silently omits implementation.
            formula = f'=TEXT({yearly},"#,##0")&" {spec["currency"]} + {labels["no_data"]}"'
        else:
            formula = f"={yearly}"
        ws.cell(total_row, 2 + i, formula).number_format = money
    for r in (lic_row, host_row, total_row):
        for c in range(1, 2 + len(techs)):
            cell = ws.cell(r, c)
            cell.font = font(HEADER_PT, bold=True)
            cell.alignment = WRAP
            cell.border = BOX
        # label wraps in the narrow first column; size the row so it is fully visible
        height = lines_needed(ws.cell(r, 1).value, LABEL_WIDTH * BODY_PT / HEADER_PT) * (HEADER_PT + 3) + 3
        ws.row_dimensions[r].height = height
        heights.append(height)

    for section in spec["sections"]:
        row += 1
        ws.merge_cells(f"A{row}:{last_col}{row}")
        band = ws[f"A{row}"]
        band.value = section["name"]
        band.font = font(BODY_PT, True, MUTED)
        band.fill = PatternFill("solid", fgColor=BAND)
        ws.row_dimensions[row].height = 13
        heights.append(13)
        for r in section["rows"]:
            row += 1
            ws.cell(row, 1, r["label"]).font = font(BODY_PT, bold=True)
            lines = lines_needed(r["label"], LABEL_WIDTH)
            for i, t in enumerate(techs):
                text = r["cells"][t].strip()
                ws.cell(row, 2 + i, text).font = font()
                lines = max(lines, lines_needed(text, TECH_WIDTH))
            for c in range(1, 2 + len(techs)):
                ws.cell(row, c).alignment = WRAP
                ws.cell(row, c).border = BOX
            height = lines * PT_PER_LINE + 3
            ws.row_dimensions[row].height = height
            heights.append(height)

    if spec.get("excluded"):
        row += 1
        full_row(row, spec["excluded"], BODY_PT, color=MUTED)
    row += 1
    full_row(row, spec["sources"], 7, color=MUTED)

    ws.freeze_panes = ws.cell(header_row + 1, 2)
    ws.print_area = f"A1:{last_col}{row}"
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.orientation = ws.ORIENTATION_LANDSCAPE
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 1
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_margins.left = ws.page_margins.right = 0.3
    ws.page_margins.top = ws.page_margins.bottom = 0.35
    ws.print_options.horizontalCentered = True
    wb.save(path)

    width_pt = sum(ws.column_dimensions[get_column_letter(c)].width for c in range(1, 2 + len(techs))) * 5.6
    height_pt = sum(heights)
    page_w_pt, page_h_pt = (297 - 15) / 25.4 * 72, (210 - 18) / 25.4 * 72  # A4 landscape minus margins
    return min(1.0, page_w_pt / width_pt, page_h_pt / height_pt)


def verify(path, spec):
    ws = load_workbook(path).active
    assert ws.page_setup.orientation == "landscape"
    assert ws.sheet_properties.pageSetUpPr.fitToPage
    for row in ws.iter_rows():
        for cell in row:
            if cell.value is not None:
                assert cell.font.name == FONT, f"font at {cell.coordinate}"
            if isinstance(cell.value, str) and cell.value.startswith("="):
                assert not re.search(r"#(REF|VALUE|NAME|DIV/0|N/A)", cell.value), f"formula at {cell.coordinate}"
                assert cell.value.count('"') % 2 == 0, f"unbalanced quotes at {cell.coordinate}"
    assert ws.cell(5, 2).value == spec["technologies"][0]


def main(spec_path, out_path):
    with open(spec_path, encoding="utf-8") as f:
        spec = json.load(f)
    errors = validate(spec)
    if errors:
        sys.exit("Spec errors:\n- " + "\n- ".join(errors))
    scale = render(spec, out_path)
    verify(out_path, spec)
    if scale < MIN_PRINT_SCALE:
        sys.exit(f"Estimated print scale {scale:.0%} < {MIN_PRINT_SCALE:.0%}: shorten cells or remove a row")
    print(f"OK {out_path} — estimated A4 print scale {scale:.0%}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
