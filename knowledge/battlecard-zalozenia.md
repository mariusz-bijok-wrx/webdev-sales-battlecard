# Założenia battlecard — scenariusz standardowy i domyślne plany

Jedno miejsce z domyślnymi odpowiedziami „ile to kosztuje”. Battlecard używa ich, **gdy brief nie podaje innych liczb**. Zmieniasz tutaj → zmieniają się wszystkie kolejne battlecardy.

Stan: **13 września 2026 r.** Ceny katalogowe, rozliczenie roczne, bez podatków. Szczegóły i źródła: `knowledge/technologie/<technologia>/co-wyroznia.md`.

## Scenariusz standardowy

| Parametr | Wartość |
|---|---|
| Typ serwisu | strona marketingowa firmy (bez sklepu) |
| Ruch | **50 tys. wizyt/mies.** |
| Języki | **2** (główny + 1) |
| Strony | ok. **30** stron + blog |
| Osoby edytujące treść | **3** |
| Horyzont kosztów | **3 lata** |
| Stawka godzinowa wdrożenia | podawana przy wywołaniu skilla; bez niej koszt 3 lat obejmuje tylko licencje i hosting |

Dla sklepu: ten sam scenariusz + **500 produktów**, sprzedaż w 1 walucie, **sprzedaż kartą 50 tys. zł/mies.**

## Domyślny plan per technologia (scenariusz standardowy)

Kwoty **roczne** (tak sprzedawane są licencje wtyczek; plany miesięczne × 12 przy rozliczeniu rocznym). EUR przeliczone po kursie **1 EUR = 1,11 USD**.

| Technologia | Licencje i narzędzia / rok | Hosting / rok | Nasze godziny wdrożenia (`db.csv`) |
|---|---|---|---|
| **WordPress** | **$159**: ACF PRO $49 + WPML CMS €99 (≈$110) | **$780**: WP Engine Essential, 3 strony, 75 tys. wizyt/mies. (1. rok promocyjnie $624) | mediana **162 h** (6 nowych stron marketingowych) |
| **Webflow** | **$876**: Workspace Core $228 + 3 miejsca edycji $540 + Localize Essential 1 język $108 | **$300**: Site plan Premium (hosting 50 GB + CMS) | mediana **55 h** (5 projektów) |
| **HubSpot CMS** | **$5400**: Content Hub Professional (3 miejsca) | **$0**: w cenie licencji | **401 h** (1 projekt; pewność niska) |
| **Astro + Sanity** | **$540**: Sanity Growth 3 × $15/mies. | **$60**: Cloudflare Workers Paid | brak danych |
| **Next.js + Sanity** | **$540**: Sanity Growth 3 × $15/mies. | **$240**: Vercel Pro | brak danych (headless: 10 realizacji bez godzin) |
| **Next.js + Prismic** | **$300**: Prismic Small (7 użytkowników, 4 języki) | **$240**: Vercel Pro | brak danych |
| **Next.js + Strapi** | **$540**: Strapi Growth (3 miejsca) | **$1320**: Strapi Cloud Pro $1080 + Vercel Pro $240 | brak danych |
| **Shopify** (sklep) | **$1908**: Grow $948 + aplikacje ≈$960 (szacunek) + prowizje od sprzedaży | **$0**: w cenie planu | brak danych |
| **WordPress + WooCommerce** (sklep) | **$159** + wtyczki sklepu (brak danych) + prowizje operatora | **$780**: WP Engine Essential (opcjonalny dodatek e-commerce $1188/rok) | mediana **245 h** (5 sklepów) |

Hosting po stronie klienta (własny serwer) → hosting **$0** dla porównania, a w wierszu Hosting opis, co klient musi utrzymać.

## Sklep: plan według skali sprzedaży

Ceny Shopify dla Polski (rozliczenie roczne) i stawki Shopify Payments. Próg = miesięczna sprzedaż kartą, przy której niższa prowizja wyższego planu zwraca różnicę abonamentu.

| Sprzedaż kartą / mies. | Rekomendowany stack | Abonament | Prowizja od karty | Uwagi |
|---|---|---|---|---|
| do **ok. 107 tys. zł** | **Shopify Basic**; **Grow**, gdy sklep obsługuje więcej niż 1 osoba | zł79/mies. (Grow zł239) | 1,95% + zł1,20 | Próg Basic → Grow: (239 − 79) / 0,15% ≈ 107 tys. zł; Basic nie ma kont pracowników |
| **107–654 tys. zł** | **Shopify Grow** | zł239/mies. | 1,8% + zł1,20 | Próg Grow → Advanced: (1220 − 239) / 0,15% ≈ 654 tys. zł |
| **powyżej 654 tys. zł** | **Shopify Advanced** | zł1220/mies. | 1,65% + zł1,20 | do 15 kont pracowników |
| **custom checkout, B2B, wiele sklepów** | **Shopify Plus** | od €2100/mies. | 1,45% + zł1,20 | niezależnie od skali |
| **pełna kontrola kodu i danych, nietypowe produkty/konfiguratory** | **WooCommerce** (WordPress) | $0 + hosting WP Engine Essential od $780/rok | wg operatora płatności (brak danych w knowledge) | nasze wdrożenia: mediana **245 h** (5 sklepów, `db.csv`); utrzymanie wtyczek po stronie klienta |

Czysty Astro, Webflow bez planu Ecommerce i headless CMS bez platformy commerce **nie są opcjami dla sklepu**.

## Reguły

- Jedna odpowiedź na technologię. Inny plan tylko wtedy, gdy brief wprost przekracza scenariusz (np. 10 języków, 20 redaktorów, SSO).
- Godziny zawsze z `db_stats.py` (mediana, liczba projektów). Brak danych → `brak danych`, bez zgadywania.
- Aktualizuj tabelę razem z plikami technologii, gdy zmienia się cennik.
