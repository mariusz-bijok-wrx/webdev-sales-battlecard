# Stack technologiczny dla Shopify

> **Rekomendacja w jednym zdaniu:** dla sklepu firmowego najlepszym domyślnym stackiem jest **Shopify Grow + motyw Online Store 2.0 (Liquid, sekcje) + minimalny zestaw aplikacji**. **Hydrogen (headless)** ma sens tylko przy bardzo nietypowym frontendzie lub treściach zasilanych z osobnego CMS-a — podwaja koszt developmentu i utrzymania.

Stan analizy: **13 września 2026 r.**

## Rekomendowana architektura bazowa

| Warstwa | Technologia | Odpowiedzialność | Dlaczego opłacalna |
|---|---|---|---|
| Commerce i hosting | **Shopify (Grow/Advanced)** | Produkty, koszyk, checkout, płatności, CDN | Brak serwera i utrzymania |
| Motyw | **Online Store 2.0: Liquid + sekcje JSON**, bazowo motyw Dawn lub premium | Szablony, sekcje edytowane przez marketing | Edytor motywu bez developmentu po wdrożeniu |
| Frontend w motywie | **CSS/Tailwind, vanilla JS / web components** | Interakcje | Mało JS = lepszy performance |
| Development | **Shopify CLI, GitHub integration motywu, Theme Check** | Wersjonowanie, deploy motywu | Standardowy workflow |
| Dane rozszerzone | **Metapola i metaobiekty** | Treści niestandardowe, dane produktu | Bez zewnętrznej bazy |
| Języki i rynki | **Shopify Markets + Translate & Adapt** | Waluty, domeny, tłumaczenia | Natywne, bez licencji |
| Aplikacje | Recenzje, filtry, e-mail marketing, subskrypcje — **tylko potrzebne** | Funkcje spoza core | Każda aplikacja to koszt i skrypty |
| Integracje | **Admin API, webhooks**, Shopify Flow (automatyzacje) | ERP, magazyn, CRM | Flow bez własnego backendu |
| Headless (opcjonalnie) | **Hydrogen (React Router) + Oxygen** | Własny frontend sklepu | Hosting Oxygen w planie; pełna kontrola UI |

## Motyw Liquid czy Hydrogen?

| Kryterium | Motyw Liquid | Hydrogen (headless) |
|---|---|---|
| Czas i koszt wdrożenia | **niski/średni** | **wysoki** |
| Edycja przez marketing | **edytor motywu natywnie** | wymaga CMS-a lub metaobiektów |
| Aplikacje z Theme Store | **działają od razu** | wiele nie działa bez integracji |
| Swoboda UI i interakcji | ograniczona modelem motywu | **pełna** |
| Performance | dobry przy kontroli aplikacji | **bardzo dobry** przy dobrej implementacji |
| Utrzymanie | **niskie** | wyższe (aktualizacje frameworka) |

**Rekomendacja:** Liquid domyślnie. Hydrogen, gdy sklep jest częścią produktu cyfrowego lub treść zarządzana jest w headless CMS (np. Sanity + Shopify).

## Porównanie pod kątem typowego zakresu

| Obszar | Shopify (Liquid) | Komentarz |
|---|---|---|
| Implementation cost | **średni** | Motyw + sekcje; brak godzin w `db.csv` |
| Technical SEO | **dobre** | Stałe prefiksy URL; schema przez motyw |
| Hosting | **w cenie planu** | CDN, SSL, skalowanie |
| Performance | **dobre** | Mediana PageSpeed mobile 58 (3 sklepy, `db.csv`) |
| Content management | **dobre dla sklepu, słabe dla treści** | Blog i strony podstawowe |
| API connection | **bardzo dobre** | Admin/Storefront API, webhooks, aplikacje |
| Design development | **średnie** | Liquid, ograniczenia motywu |
| Admin panel usability | **bardzo dobre** | Jeden panel dla sklepu i treści |

## Czego nie budować w pierwszej wersji

- Hydrogen bez jasnej potrzeby;
- aplikacji na każdą drobną funkcję;
- własnego checkoutu (bez Plus nie jest możliwy w pełni);
- własnej wyszukiwarki, jeśli Search & Discovery wystarcza.

## Warianty wdrożenia

- **A — sklep firmowy:** Grow + motyw premium dostosowany + 3–5 aplikacji.
- **B — sklep z dużym obrotem:** Advanced (niższa prowizja) + Markets.
- **C — enterprise / B2B:** Plus + custom checkout + integracja ERP.
- **D — content-first commerce:** Headless CMS (Sanity) + Hydrogen lub Next.js + Storefront API.

## Źródła

- [Shopify — Pricing](https://www.shopify.com/pricing)
- `db.csv` — portfolio (3 sklepy Shopify)
