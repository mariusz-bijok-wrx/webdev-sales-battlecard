"""Per-technology delivery stats from db.csv (internal portfolio, source of truth).

Usage: python3 db_stats.py [path/to/db.csv]  -> JSON keyed by technology, then by category.
- new_website_hours: "Workload - Dev" of finished new websites (real hours);
- quoted_hours_client: midpoint of "Wycena - Klient" ranges for new websites and redesigns (any status);
- pagespeed_mobile: mobile PageSpeed of finished projects.
"""
import csv
import json
import re
import statistics
import sys

# Normalize the free-text "Przeważająca technologia" column to knowledge/technologie folders.
TECH_ALIASES = {
    "wp": "wordpress",
    "woocommerce": "wordpress",
    "hubspot": "hubspot",
    "webflow": "webflow",
    "shopify": "shopify",
    "headless": "headless",
    "react / nextjs": "headless",
    "react": "headless",
}
CATEGORY_ALIASES = {"marekting web": "marketing", "ecommerce": "ecommerce", "sla": "marketing"}
HEADER_ROW = 1  # row 0 holds only the "PageSpeed / Core Web Vitals" group labels


def hours(value):
    """'~245h' -> 245, '126.5' -> 126.5, '84-101' -> 92.5; '?', packages, multi-variant text -> None."""
    value = (value or "").strip().replace(",", ".")
    single = re.fullmatch(r"~?\s*(\d+(?:\.\d+)?)\s*h?", value)
    if single:
        return float(single.group(1))
    span = re.fullmatch(r"(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)\s*h?", value)
    return (float(span.group(1)) + float(span.group(2))) / 2 if span else None


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    header = rows[HEADER_ROW]
    return [dict(zip(header, row)) for row in rows[HEADER_ROW + 1:] if row and row[0].strip()]


def summary(values):
    if not values:
        return None
    return {"n": len(values), "median": statistics.median(values), "min": min(values), "max": max(values)}


def stats(projects):
    groups = {}
    for p in projects:
        tech = TECH_ALIASES.get(p.get("Przeważająca technologia", "").strip().lower())
        category = CATEGORY_ALIASES.get(p.get("Kategoria", "").strip().lower())
        if not tech or not category:
            continue
        g = groups.setdefault(tech, {}).setdefault(
            category, {"projects_done": 0, "real": [], "quoted": [], "mobile": []})
        done = p.get("Stauts", "").strip() == "Done"
        work_type = p.get("Typ prac", "").strip()
        if done:
            g["projects_done"] += 1
            mobile = hours(p.get("mobile"))  # plain number parser works for scores too
            if mobile is not None:
                g["mobile"].append(mobile)
            if work_type == "New webstie" and "-" not in p.get("Workload - Dev", ""):
                real = hours(p.get("Workload - Dev"))
                if real:
                    g["real"].append(real)
        if work_type in ("New webstie", "Redesign"):
            quoted = hours(p.get("Wycena - Klient"))
            if quoted:
                g["quoted"].append(quoted)

    return {
        tech: {
            category: {
                "projects_done": g["projects_done"],
                "new_website_hours": summary(g["real"]),
                "quoted_hours_client": summary(g["quoted"]),
                "pagespeed_mobile": summary(g["mobile"]),
            }
            for category, g in sorted(categories.items())
        }
        for tech, categories in sorted(groups.items())
    }


def _self_check():
    assert hours("~245h") == 245.0
    assert hours("126.5") == 126.5
    assert hours("84-101") == 92.5
    assert hours("20 / month package") is None
    assert hours("ERR") is None and hours("?") is None
    sample = [
        {"Przeważająca technologia": "WP", "Kategoria": "Marekting web", "Stauts": "Done",
         "Typ prac": "New webstie", "Workload - Dev": "~100h", "Wycena - Klient": "80-120", "mobile": "80"},
        {"Przeważająca technologia": "woocommerce", "Kategoria": "ecommerce", "Stauts": "Done",
         "Typ prac": "New webstie", "Workload - Dev": "1000", "Wycena - Klient": "", "mobile": "ERR"},
        {"Przeważająca technologia": "WP", "Kategoria": "Marekting web", "Stauts": "Lost",
         "Typ prac": "Redesign", "Workload - Dev": "-", "Wycena - Klient": "140-160", "mobile": ""},
    ]
    wp = stats(sample)["wordpress"]
    assert wp["marketing"]["projects_done"] == 1
    assert wp["marketing"]["new_website_hours"]["median"] == 100.0
    assert wp["marketing"]["quoted_hours_client"]["median"] == 125.0
    assert wp["ecommerce"]["new_website_hours"]["median"] == 1000.0
    assert wp["ecommerce"]["pagespeed_mobile"] is None


if __name__ == "__main__":
    _self_check()
    print(json.dumps(stats(load(sys.argv[1] if len(sys.argv) > 1 else "db.csv")), indent=2, ensure_ascii=False))
