# Typowe potrzeby biznesowe klienta, które może pokryć Shopify

> **Najważniejsza zasada:** Shopify pokrywa potrzeby **sprzedażowe** lepiej niż jakikolwiek CMS, a potrzeby **treściowe i marketingowe** gorzej niż dedykowany CMS. Koszt rośnie, gdy klient oczekuje od sklepu roli rozbudowanego serwisu treści albo nietypowego procesu zakupowego.

Stan analizy: **13 września 2026 r.**

## Poziomy pokrycia

- **Shopify** — w planie i edytorze motywu;
- **Shopify + aplikacja** — potrzebna aplikacja (zwykle płatna);
- **Shopify + development** — sekcje Liquid, Hydrogen, API;
- **Shopify Plus** — funkcja wymaga planu Plus;
- **poza Shopify** — lepiej inną technologią.

## Potrzeby i pokrycie

| # | Potrzeba | Pokrycie | Komentarz |
|---|---|---|---|
| 1 | Marketing publikuje bez developera | **Shopify** | Edytor motywu, sekcje i bloki; nowe typy sekcji wymagają developera |
| 2 | Spójny design system | **Shopify + development** | Sekcje Liquid z ustawieniami; motyw kontroluje style |
| 3 | Podgląd przed publikacją | **Shopify** | Podgląd motywu i kopie motywu jako staging |
| 4 | Drafty i wycofywanie zmian | **Shopify** | Duplikaty motywu, drafty produktów i stron |
| 5 | Praca wielu osób | **Shopify** | Konta pracowników: Grow 5, Advanced 15, Plus bez limitu |
| 6 | Role i uprawnienia | **Shopify / Plus** | Uprawnienia per konto; zaawansowane organizacje w Plus |
| 7 | Reużywalna treść | **Shopify + development** | Metaobiekty i metapola |
| 8 | Strony, URL-e, nawigacja | **Shopify** | Menu, redirecty URL; stała struktura ścieżek (`/products/`, `/collections/`) |
| 9 | Assety | **Shopify** | CDN, optymalizacja obrazów |
| 10 | Wydajność | **Shopify + development** | CDN w cenie; wydajność zależy od motywu i liczby aplikacji |
| 11 | Wiele języków i rynków | **Shopify + aplikacja** | Shopify Markets (waluty, domeny), Translate & Adapt |
| 12 | Omnichannel | **Shopify** | Sklep, POS, marketplace'y, Storefront API |
| 13 | SEO i AI visibility | **Shopify + aplikacja** | Metadane, sitemap natywnie; schema i zaawansowane SEO przez motyw/aplikacje; stałe prefiksy URL |
| 14 | Formularze i CRM | **Shopify + aplikacja** | Konta klientów natywnie; integracje CRM przez aplikacje |
| 15 | Integracje per strona | **Shopify + development** | Aplikacje osadzane w motywie |
| 16 | Analityka | **Shopify** | Raporty sprzedaży natywnie; GA4 przez integrację |
| 17 | A/B testy | **Shopify + aplikacja** | Aplikacje do testów motywu i cen |
| 18 | Personalizacja | **Shopify + aplikacja** | Rekomendacje produktów; personalizacja przez aplikacje |
| 19 | Interaktywne komponenty i konfiguratory | **Shopify + development** | Konfiguratory to custom development lub aplikacja — wysokie ryzyko wyceny |
| 20 | Wyszukiwanie i filtry | **Shopify / aplikacja** | Search & Discovery natywnie; zaawansowane filtry przez aplikacje |
| 21 | Bezpieczeństwo, SSO, compliance | **Shopify / Plus** | PCI DSS po stronie Shopify; SSO w Plus |
| 22 | Historia i audyt | **Shopify** | Oś czasu zamówień i zmian; pełne logi w Plus |
| 23 | Przenośność | **słabe** | Dane eksportowalne; motyw i aplikacje nie |
| 24 | AI w pracy nad treścią | **Shopify** | Sidekick i generowanie opisów produktów |

## Pytania discovery przed wyceną

1. Jaki jest roczny obrót online (decyduje o opłacalności planu przez prowizje)?
2. Ile produktów i wariantów, czy produkty są standardowe czy konfigurowalne?
3. Ile rynków, walut i języków?
4. Jakie systemy trzeba zintegrować (ERP, magazyn, CRM)?
5. Jak ważny jest content marketing (blog, landing pages) względem sklepu?
6. Czy potrzebny jest custom checkout lub B2B (Plus)?

## Źródła

- [Shopify — Pricing](https://www.shopify.com/pricing)
- Zob. [`co-wyroznia.md`](./co-wyroznia.md)
