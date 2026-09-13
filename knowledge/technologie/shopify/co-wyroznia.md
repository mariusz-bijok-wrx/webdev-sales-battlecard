# Co wyróżnia Shopify

> **W skrócie:** Shopify warto wybrać wtedy, gdy strona **sprzedaje produkty** i klient chce gotowego koszyka, checkoutu, płatności, podatków i hostingu bez utrzymywania sklepu. Najmocniejsze strony to najszybsze uruchomienie sprzedaży, niezawodny checkout i ogromny ekosystem aplikacji. Ceną są prowizje od sprzedaży, miesięczne opłaty za aplikacje oraz ograniczenia w strukturze danych i checkoutu poza planem Plus.

Stan oferty i cen: **13 września 2026 r.** Ceny w PLN z oficjalnego cennika dla Polski; ceny w USD ze źródeł wtórnych (pewność średnia).

Powiązane: [`potrzeby-biznesowe-klienta.md`](./potrzeby-biznesowe-klienta.md), [`stack-technologiczny.md`](./stack-technologiczny.md).

## Najpierw biznes: ile kosztuje Shopify?

1. **plan Shopify** — hosting, sklep, checkout, CDN, SSL;
2. **prowizje** — od płatności kartą (Shopify Payments) albo dodatkowa opłata przy zewnętrznym operatorze płatności;
3. **aplikacje** — recenzje, subskrypcje, filtry, wyszukiwarka, tłumaczenia, marketing; zwykle płatne miesięcznie;
4. **motyw** — darmowy, płatny z Theme Store lub własny;
5. **wdrożenie i rozwój** — motyw, sekcje, integracje (ERP, magazyn, CRM).

### Cena katalogowa

| Plan | Polska (rocznie / miesięcznie) | USD (rocznie / miesięcznie) | Konta pracowników | Karta (PL) | Opłata przy zewnętrznej bramce |
|---|---:|---:|---:|---:|---:|
| **Basic** | **zł79 / zł109** | $29 / $39 | brak | 1,95% + zł1,20 | 2% |
| **Grow** | **zł239 / zł319** | $79 / $105 | do 5 | 1,8% + zł1,20 | 1% |
| **Advanced** | **zł1220 / zł1630** | $299 / $399 | do 15 | 1,65% + zł1,20 | 0,6% |
| **Plus** | **od €2100/mies.** | od $2300/mies. (umowa 3-letnia), $2500 (1 rok) | bez limitu | 1,45% + zł1,20 | 0,2% |

Przykład: sklep na Grow (zł239/mies. rocznie) + 4 płatne aplikacje po ok. $20 (szacunek) + motyw premium jednorazowo → **ok. zł6000–7000 rocznie** plus prowizje od sprzedaży.

### Gdzie naprawdę powstają oszczędności

- **Checkout i płatności bez developmentu** — najdroższa i najbardziej ryzykowna część sklepu jest gotowa i utrzymywana przez Shopify.
- **Brak kosztów serwera i skalowania** — skoki ruchu (np. Black Friday) nie wymagają pracy DevOps.
- **Aplikacje zamiast custom code** dla typowych funkcji e-commerce.
- **Wiele rynków** (waluty, języki, domeny) w jednym sklepie przez Shopify Markets.

### Ryzyko kosztowe, które trzeba kontrolować

- **Prowizje rosną ze sprzedażą** — przy dużym obrocie różnica stawek między planami przewyższa różnicę abonamentu.
- **Aplikacje się sumują** — 10 aplikacji po kilkadziesiąt dolarów to istotny koszt miesięczny i spadek wydajności motywu.
- **Checkout** można głęboko dostosować dopiero w Plus.
- **Nietypowe produkty** (konfiguratory, złożone warianty, B2B) wymagają aplikacji lub custom development; w portfolio mamy przypadek utraconej oferty z konfiguratorem na Shopify (Fey — `db.csv`).

**Rekomendacja kosztowa:** Grow jako punkt startowy dla sklepu firmowego; Advanced, gdy obrót sprawia, że niższa prowizja zwraca różnicę w abonamencie; Plus dopiero przy potrzebie custom checkoutu, B2B lub dużej skali.

## Co Shopify robi inaczej

1. **Commerce jako usługa** — produkty, magazyn, zamówienia, płatności, podatki i wysyłka są w platformie; klient nie buduje sklepu od zera.
2. **Motywy Liquid z sekcjami** — marketing edytuje strony i sekcje w edytorze motywu; developer tworzy sekcje w Liquid.
3. **Headless przez Hydrogen (React) i Storefront API** — dla sklepów potrzebujących w pełni własnego frontendu; hosting Oxygen w cenie planu.
4. **Ekosystem aplikacji** — tysiące aplikacji dla funkcji, których nie ma w core.
5. **Dane zamknięte w modelu Shopify** — metaobiekty i metapola rozszerzają produkty i treści, ale model jest mniej elastyczny niż w headless CMS.

## Jak Shopify odpowiada na typowe potrzeby klienta

| Potrzeba | Odpowiedź Shopify | Na co uważać |
|---|---|---|
| **Szybkie uruchomienie sprzedaży** | Gotowy sklep, checkout, płatności | Własny design motywu nadal wymaga pracy |
| **Edycja treści przez marketing** | Edytor motywu z sekcjami i blokami | Rozbudowany content marketing jest słabszy niż w CMS-ie |
| **Wiele rynków i języków** | Shopify Markets, aplikacja Translate & Adapt | Tłumaczenia aplikacji i motywu trzeba sprawdzić osobno |
| **Nietypowe produkty i konfiguratory** | Aplikacje lub custom development | Koszt i ryzyko rosną szybko |
| **Integracje ERP/CRM** | Aplikacje, Admin API, webhooks | Złożone integracje często wymagają middleware |
| **Wydajność** | CDN Shopify | Każda aplikacja dokłada skrypty do motywu |
| **Przenośność** | Eksport produktów, klientów i zamówień (CSV/API) | Motyw Liquid i aplikacje nie przenoszą się |

## Kiedy Shopify jest szczególnie dobrym wyborem

- głównym celem strony jest **sprzedaż online**;
- katalog i proces zakupowy są standardowe;
- klient nie chce utrzymywać sklepu, serwera ani bezpieczeństwa płatności;
- potrzebne jest szybkie wejście na kolejne rynki.

## Kiedy lepiej rozważyć inne rozwiązanie

- strona jest **marketingowa, bez sprzedaży** — lepsze Webflow, WordPress, Astro lub headless CMS;
- sprzedaż opiera się na **złożonym konfiguratorze** lub nietypowym modelu (np. wyceny B2B bez Plus);
- klient chce pełnej kontroli nad danymi i kodem sklepu — rozważyć WooCommerce lub Medusa;
- rozbudowany content marketing jest ważniejszy niż sklep — rozważyć CMS + integrację Shopify.

## Nasze doświadczenie (db.csv)

Uruchom `python3 .claude/skills/dev-sales-battlecard/db_stats.py db.csv`. Stan 13.09.2026: 3 zakończone sklepy Shopify, mediana PageSpeed mobile 58; brak zapisanych godzin dla nowego sklepu.

## Źródła

- [Shopify — Pricing](https://www.shopify.com/pricing) (ceny dla Polski, 13.09.2026)
- [Style Factory — Shopify pricing 2026](https://www.stylefactoryproductions.com/blog/shopify-fees), [NerdWallet — Shopify pricing](https://www.nerdwallet.com/article/small-business/shopify-pricing) (ceny USD i Plus; źródła wtórne)
- `db.csv` — portfolio projektów (Rebelhorn, DreamyBlue, MatterPet, Fey)
