---
name: dev-sales-battlecard
description: >
  User-invoked workflow that turns a client brief into a one-page (A4 landscape) sales
  battlecard comparing web technologies. Uses knowledge/technologie/, the standard
  scenario in knowledge/battlecard-zalozenia.md and delivery data from db.csv. Output is
  a single .xlsx table sales can copy into an offer.
disable-model-invocation: true
---

# Dev sales battlecard

A **sales card, not technical documentation**. The client sits across the table and asks
"why should I pay for this and not that, and how much will it cost". Every cell answers
that in at most two short sentences. If the result reads like an essay, it has failed.

Invoke explicitly with `/dev-sales-battlecard`. Inputs:

- **client brief** — attached file (read it fully) or pasted text; required;
- **hourly rate** for implementation, with currency — optional; without it the 3-year
  cost covers licences and hosting only, and its row label says so;
- **technologies** to compare — optional.

If the brief is missing, ask only for the brief.

## Sources of truth

| What | Where | Rule |
|---|---|---|
| Our delivery data: hours, performance, portfolio | `db.csv` via `db_stats.py` | Always wins for our numbers |
| Standard scenario and default plan per technology | `knowledge/battlecard-zalozenia.md` | Use unless the brief gives other numbers |
| Prices, limits, strengths, risks | `knowledge/technologie/<tech>/*.md` | Arguments and catalogue prices |

Run `python3 .claude/skills/dev-sales-battlecard/db_stats.py db.csv` at the start. Map
`db.csv` technologies to knowledge folders: `wordpress` → WordPress, `webflow`, `hubspot`,
`shopify`, `headless` → Next.js + Sanity/Prismic/Strapi; WordPress shops (WooCommerce) are
`wordpress` / `ecommerce`. Astro has no projects yet.

If `db.csv`, the assumptions file and a technology file disagree, use the priority above
and mention the conflict in one line of the final chat summary, not in the card.

## 1. Client profile

Read the brief and write a short profile (for yourself, not the card): goal, who edits
content, languages/markets, traffic, editors, integrations, must-haves, deal-breakers, and
these flags — each **yes** only when the brief states or clearly implies it:

| Flag | Examples in the brief |
|---|---|
| `shop` | sells products online, cart, checkout, payments, catalogue |
| `cms` | content changes after launch by non-developers (blog, landing pages, news) |
| `no_code` | marketing/design build pages alone, no developer after launch |
| `design` | brand-heavy site, animations, custom design system |
| `seo` | organic traffic, content marketing, performance targets |
| `multilang` | more than one language or market |
| `integrations` | CRM, ERP, marketing automation, product data |
| `dynamic` | login, personalization, product/app data, logic on the server |
| `hubspot_crm` | client uses or buys HubSpot CRM |
| `ai` | AI content, AI search visibility or AI workflows mentioned |
| `compliance` | public tender, WCAG/accessibility law, 2FA, audit log, versioning, security tests, GDPR records, open-source or licence requirements |

Missing numbers → take them from the standard scenario in `battlecard-zalozenia.md`
(shop: sales scale row there). Do not ask unless a missing fact would change which
technologies are shown.

## 2. Technology selection

All technologies in `knowledge/technologie/` have equal priority. Headless options are
columns such as `Next.js + Sanity`; a shop on WordPress is `WordPress + WooCommerce`.

1. **Exclude** options that cannot meet a critical flag:
   - `shop` → exclude plain Astro, Webflow, HubSpot and headless CMS without a commerce
     platform;
   - `no_code` → exclude options where every new section needs a developer (Astro,
     Next.js + CMS) unless the client explicitly accepts a developer;
   - `dynamic` → exclude static-only setups that would need workarounds;
   - `compliance` with open-source, self-hosting or "no mandatory subscription" in the brief
     → exclude SaaS-only options (Webflow, HubSpot, Shopify, Sanity, Prismic).
2. **Always include** the best fit for a critical flag, even if not named:
   `shop` → Shopify; `no_code` → Webflow; `hubspot_crm` → HubSpot.
3. Named technologies that survive step 1 are included. If none were named, add the most
   relevant remaining options up to 4 columns (max 6).
4. A named technology removed in step 1 goes into the card's `excluded` line with a
   3–6 word reason (`Astro — brak sklepu i płatności`).
5. A named technology without a knowledge folder: tell the user and ask whether to drop it.

## 3. Language and tone

Use the language of the user's prompt for every visible string; keep product names and
established terms (`SEO`, `CMS`, `API`, `Core Web Vitals`) unchanged.

- Business first: what the client gets, pays, or risks. Technical detail only when it
  changes the decision, phrased for a client (`marketing sam składa strony z gotowych
  sekcji`, not `page building via components`).
- **No "to zależy"** and no lists of variants. One default plan per technology, stated
  concretely: `WP Engine Essential (75 tys. wizyt) — $780/rok`.
- Apples to apples: every row answers the same question for every column, in the same unit.
- No data → `brak danych` (or translation). Never invent a number.

## 4. Card structure

Top of the sheet:

- **Title**: `Battlecard: <client> — <technologies>`.
- **Subtitle**: date, one-line client goal.
- **Assumptions** (one line): only the numbers that change the costs — traffic (skip when
  the client hosts it), languages, pages, editors, sales scale for a shop, horizon,
  currency, hourly rate or "bez stawki".
- **Recommendation** (max 2 sentences): which option, argued by the client's outcome
  (cost, requirement met, risk removed), and the single condition that would change it.
  Our data availability (e.g. "only option with our hours") is never the argument.

Cost rows (numbers, always, rendered with formulas):

- **Licences and plugins / year** — full annual amounts from the assumptions file (plugins
  billed yearly are shown yearly, never divided per month).
- **Hosting / year** — full annual amount of the default plan; `0` when the client hosts it
  on their own server (say so in the Hosting row).
- **Cost for 3 years** — `(licences + hosting) × 3`, plus `hours × hourly rate` when the rate
  was given; without a rate the label says `(licencje + hosting, bez wdrożenia)`.

Adjust plans only when the brief exceeds the standard scenario. The `Basic cost` and
`Hosting` rows name what the numbers contain (`ACF PRO $49/rok + WPML €99/rok`).

Text rows are **chosen from the profile**, max 12. Core rows are always present; add
conditional rows in the priority order below until the limit. Localize labels.

| Priority | Row | Include when | Answers |
|---|---|---|---|
| core | Basic cost | always | Tool + licences: plan names and prices |
| core | Hosting | always | Concrete plan, what is included, what grows the bill |
| core | Implementation cost | always | Our median hours from `db.csv` (n projects) and what drives them |
| core | Pros | always | Two strongest advantages for this client, business first, then the client's developer |
| core | Cons | always | Two biggest drawbacks or risks for this client, incl. maintenance for the client's developer |
| 1 | Sales scale → plan | `shop` | Which plan/stack at the client's monthly sales, fees in % |
| 1 | Payments and checkout | `shop` | Gateways, fees, how far checkout can be customized |
| 1 | Catalogue and variants | `shop` | Products, variants, configurators — native, app or custom |
| 1 | Content management | `cms` | What marketing does alone, what needs a developer |
| 1 | Page building without code | `no_code` | Who builds a new page and a new section |
| 1 | Security and compliance | `compliance` | How each brief requirement (roles, 2FA, audit log, versions, WCAG, licences) is met: core, plugin/paid plan or custom code |
| 2 | Languages and markets | `multilang` | How languages are added and what each costs |
| 2 | Logic and personalization | `dynamic` | Login, personalization, server logic — native or custom |
| 2 | ERP / warehouse integrations | `shop` and `integrations` | Native apps, API, middleware |
| 2 | API connection | `integrations` (not already covered) | CRM/marketing tools: native, apps, custom code |
| 3 | Admin panel usability | `cms` or `shop` | How easy the panel is for a non-technical editor |
| 3 | Technical SEO | `seo`, or `cms` without `shop` | What is built in, what needs work |
| 3 | Performance | `seo` or `design` | Our median mobile PageSpeed from `db.csv` + main risk |
| 3 | Design development | `design` | How design becomes the site, freedom and limits |
| 3 | AI | `ai` | How AI helps edit/build/sell; AI search visibility |
| last | Best when | always | One sentence: the situation in which this column wins |

Never add a row whose flag is **no** (e.g. no CMS → no Content management and no Admin
panel usability). Group rows into sections `KOSZT`, `SPRZEDAŻ` (shop rows),
`BIZNES`, `PODSUMOWANIE` (Pros, Cons, Best when — always last; localized); omit empty
sections. Pros and Cons cells start with the point itself, no `+`/`−` symbols needed.

Each cell: ≤ 2 sentences, ≤ 130 characters, starts with the fact or consequence, not a
rating word. Shared capabilities get the same short text in every column.

## 5. Render

Write the card as JSON in the scratchpad and render it:

```bash
python3 .claude/skills/dev-sales-battlecard/render_battlecard.py spec.json outputs/<YYYY-MM-DD>-<client-slug>/battlecard.xlsx
```

Spec shape is documented at the top of `render_battlecard.py`. `costs` uses the annual
licence and hosting amounts from the assumptions file and median new-website hours from `db_stats.py`
(`null` when missing; shops use the `ecommerce` category). `hourly_rate` is the rate given at
invocation (`null` if none); with a rate but no hours the 3-year cell shows licences +
hosting followed by `+ brak danych`, so a missing implementation cost is never hidden. `excluded` is one line listing named technologies removed in
step 2 with reasons (empty string if none).
`sources` is one short line: `Źródła: db.csv (stan <date>), knowledge/battlecard-zalozenia.md, cenniki dostawców (stan <date>)`.

The script validates limits (2–6 columns, ≤ 12 rows, ≤ 130 characters and ≤ 2 sentences
per cell), sets A4 landscape fit-to-one-page, Avenir, borders and formulas, re-opens the
file to verify it, and fails when the estimated print scale is below 60%. On failure,
shorten the text and render again — never relax the limits.

## 6. Hand-off

Reply in chat with the file path and at most three lines: the recommendation, added or
excluded technologies and why, and any data conflict or `brak danych` sales should know.

## Quality bar

- The table fits one A4 landscape page and is readable (script passes).
- Rows match the profile: shop rows only for shops, no CMS rows without a CMS need.
- A client question from the rows above can be answered by copying one cell.
- Every price names a concrete plan; every hour and PageSpeed figure comes from `db.csv`.
- No "to zależy", no variant lists, no invented numbers.
- Columns are named technologies minus justified exclusions plus mandatory best fits.
- One consistent language, Avenir throughout, formulas for the cost rows.
