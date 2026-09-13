# Stack technologiczny dla WordPress

> **Rekomendacja w jednym zdaniu:** dla serwisu marketingowego najlepszym domyślnym stackiem jest **klasyczny WordPress z lekkim własnym motywem blokowym + ACF PRO + zarządzany hosting + umowa utrzymaniowa**. **Headless WordPress (WPGraphQL + Next.js)** ma sens tylko wtedy, gdy potrzebny jest nowoczesny frontend React lub wiele kanałów, a klient akceptuje wyższy koszt i utratę części wtyczek wpływających na frontend.

Stan analizy: **13 września 2026 r.** Dokument rozwija mapę potrzeb z [`potrzeby-biznesowe-klienta.md`](./potrzeby-biznesowe-klienta.md).

## Najpierw zasada kosztowa: każda wtyczka to umowa utrzymaniowa

WordPress jest tani na starcie, bo większość funkcji daje się dodać wtyczką. Każda wtyczka oznacza jednak:

- kolejną licencję i odnowienie;
- kolejne aktualizacje i testy regresji;
- potencjalną podatność (91% podatności ekosystemu dotyczy wtyczek, Patchstack 2026);
- wpływ na wydajność i bazę danych;
- zależność od autora, który może porzucić projekt.

Ekonomiczny WordPress to **mały zestaw sprawdzonych wtyczek + własne bloki dla rzeczy specyficznych dla marki**.

## Rekomendowana architektura bazowa (klasyczny WordPress)

| Warstwa | Technologia | Odpowiedzialność | Dlaczego jest opłacalna |
|---|---|---|---|
| CMS | **WordPress 7.x** | Treść, użytkownicy, edytor blokowy, rewizje | Brak licencji; dojrzały edytor |
| Język serwera | **PHP 8.x** (wersja zgodna z aktualnymi wymaganiami core i hostingu) | Render stron, logika motywu | Dostępny na każdym hostingu |
| Motyw | **Własny motyw blokowy lub hybrydowy** (`theme.json`) | Design system, szablony, wzorce | Kontrola wydajności i spójności |
| Bloki | **ACF PRO + ACF Blocks** (bloki PHP); bloki React tylko dla bogatych interakcji | Sekcje edytowane przez marketing | Szybki development; starter Pirxey i skille `dev-wp-*` |
| Style | **CSS/SCSS lub Tailwind** w buildzie motywu (Vite) | Tokeny, responsywność | Standardowy workflow frontendowy |
| Interakcje | **Interactivity API**, vanilla JS, GSAP dla złożonych animacji | Interaktywne bloki | Mniej JS niż pełny React |
| SEO | **Yoast SEO lub Rank Math** | Metadane, sitemap, schema, breadcrumbs | Gotowe, dojrzałe |
| Wielojęzyczność | **WPML** lub **Polylang** | Wersje językowe, routing | Gotowe integracje z TMS |
| Formularze | **Gravity Forms** lub embed **HubSpot/GetResponse** | Leady | CRM pozostaje właścicielem danych |
| Hosting | **WP Engine** (domyślnie), Kinsta lub inny zarządzany; **WordPress VIP** dla enterprise | Serwer, cache, CDN, WAF, backup, staging | Przenosi część utrzymania na dostawcę |
| Development | **Git, Composer, WP-CLI, lokalne środowisko (wp-env/DDEV)**, deploy przez CI | Wersjonowanie, powtarzalne wdrożenia | Mniej ręcznych zmian na produkcji |
| Jakość | **PHPStan/PHPCS, Playwright, axe, Lighthouse CI** | Testy regresji po aktualizacjach | Aktualizacje wtyczek bez strachu |
| Bezpieczeństwo | **WAF hostingu + Patchstack lub Wordfence**, 2FA dla administratorów | Ochrona przed podatnościami wtyczek | Szybka reakcja na ujawnione luki |
| AI workflow | **MCP WordPress + skille Claude Code `dev-wp-*`** | Drafty landing pages, nowe bloki, Figma → blok | Sprawdzony wewnętrzny workflow Pirxey |

## Klasyczny czy headless?

### Klasyczny WordPress — domyślny wybór

WordPress renderuje HTML, edytor blokowy pokazuje stronę blisko finalnej, wtyczki SEO/formularzy/cache działają bez dodatkowej pracy.

**Najlepiej pokrywa:**

- strony firmowe, blogi, portale treści;
- landing pages składane z bloków przez marketing;
- serwisy z wieloma redaktorami (brak opłat per użytkownik);
- WooCommerce;
- klientów z ograniczonym budżetem licencyjnym.

**Koszt i ryzyka:**

- utrzymanie i aktualizacje są stałym kosztem;
- personalizacja serwerowa koliduje z cache stron;
- frontend PHP jest mniej atrakcyjny dla zespołów React;
- brak edycji w czasie rzeczywistym.

### Headless WordPress — WPGraphQL + Next.js

WordPress zostaje panelem redakcyjnym, a frontend Next.js/Astro pobiera treść przez **WPGraphQL** (wtyczka rozwijana w ramach WordPress.org jako canonical plugin; wg źródeł wtórnych) lub REST API. Faust.js (WP Engine) dodaje gotowe mechanizmy preview i routingu dla Next.js.

**Kiedy ma sens:**

- klient ma zespół React/Next.js i istniejący design system w React;
- treść ma zasilać stronę i aplikację;
- potrzebne są personalizacja, edge logic i A/B testy server-side;
- redakcja jest przyzwyczajona do WordPressa i nie chce zmieniać panelu.

**Czego pozbawia:**

| Możliwość | Skutek headless | Typowe obejście |
|---|---|---|
| **Podgląd w edytorze** | Edytor nie pokazuje finalnego frontendu | Faust.js lub własny preview z Draft Mode |
| **Wtyczki wpływające na frontend** | SEO, formularze, cache, page buildery nie renderują się automatycznie | Pobierać metadane przez WPGraphQL; formularze embed |
| **Jeden hosting** | Dwa systemy: WordPress i frontend | Zarządzany hosting WP + Vercel/Cloudflare |
| **Bloki jako komponenty** | Bloki trzeba zmapować na komponenty React | Parser bloków i mapa komponentów |
| **Prosty deploy** | Dwa pipeline'y i dwa zestawy testów | CI dla obu |

**Rekomendacja:** headless WordPress łączy koszt utrzymania WordPressa z kosztem frontendu headless. Porównać z Sanity/Prismic/Strapi, jeżeli klient nie jest przywiązany do panelu WordPressa.

## Page buildery — kiedy tak, kiedy nie

| Podejście | Zalety | Wady | Rekomendacja |
|---|---|---|---|
| **Bloki ACF / własne bloki** | Spójny design system, wydajność, kontrola | Wymaga developera przy nowej sekcji | **Domyślnie** |
| **Natywne bloki + wzorce** | Zero licencji, przyszłościowe | Mniej kontroli nad polami | Dla prostych stron |
| **Elementor / Divi / Bricks** | Marketing robi wszystko sam | Wolniejsze strony, niespójność, trudna migracja, dodatkowe podatności | Tylko małe serwisy o niskich wymaganiach |

## Porównanie pod kątem typowego pełnego zakresu serwisu SaaS

| Grupa wymagań | WordPress klasyczny | WordPress headless | Komentarz kosztowy |
|---|---|---|---|
| Ownership marketingu i strony | **bardzo dobre** | **dobre** | Headless traci naturalny podgląd |
| Routing, URL-e i redirecty | **dobre** | **bardzo dobre** | Redirecty przez wtyczkę vs middleware Next.js |
| Page building i komponenty | **bardzo dobre** | **dobre** | Headless wymaga mapowania bloków |
| Template pages i listingi | **bardzo dobre** | **bardzo dobre** | CPT i taksonomie w obu |
| Lokalizacja i Crowdin | **dobre** | **dobre** | WPML/Polylang + WPGraphQL |
| Formularze i thank-you pages | **bardzo dobre** | **dobre** | Headless: embed lub API |
| Motion, embedy, custom components | **dobre** | **bardzo dobre** | React ekosystem w headless |
| Personalizacja | **warunkowe** | **bardzo dobre** | Cache PHP vs edge Next.js |
| A/B testing i analytics | **dobre** | **bardzo dobre** | Server-side testy łatwiejsze w Next.js |
| SEO i LLM readiness | **bardzo dobre** | **bardzo dobre** | Wtyczki SEO vs pełna kontrola HTML |
| Security, role i auth | **warunkowe** | **dobre** | Headless ukrywa panel WP za firewallem |
| Draft, preview, staging | **dobre** | **warunkowe** | Headless preview trzeba zbudować |

## Hosting: koszt rachunku a koszt utrzymania

### Zarządzany hosting WordPress

WP Engine Essential (stan 13.09.2026, rozliczenie roczne, regularna cena; w 1. roku promocja −20%): **1 strona / 25 tys. wizyt — $420/rok**, **3 strony / 75 tys. wizyt — $780/rok**, **10 stron / 100 tys. wizyt — $1560/rok**, **30 stron / 400 tys. wizyt — $3960/rok**. W cenie: automatyczne aktualizacje WordPress i PHP, backupy, staging, EverCache, CDN Cloudflare, ochrona DDoS warstwy 3–4. Dodatki: AI aktualizacje wtyczek, zaawansowany WAF, e-commerce ($1188/rok). Plany Core (izolowane zasoby, 99,99% SLA) od $400/mies. [WP Engine plans](https://wpengine.com/plans/).

Alternatywa — Kinsta (stan 13.09.2026): pojedyncza strona od **$35/mies.** (35 tys. wizyt, 10 GB, CDN 125 GB) do **$375/mies.** (750 tys. wizyt); wiele stron od **$70/mies.** (2 strony); rozliczenie roczne ok. 17% taniej. W cenie: staging jednym kliknięciem, WAF, ochrona DDoS, backup i wsparcie 24/7. [Kinsta pricing](https://kinsta.com/pricing/).

**Wybierać, gdy:** klient chce przerzucić serwer, cache, backup i część bezpieczeństwa na dostawcę.

### WordPress VIP

Wycena indywidualna. Pakiety Standard/Enhanced/Signature: SLA 99,95–99,99%, czas reakcji na pilne zgłoszenia 15–60 minut, do 1000 stron w sieci, wsparcie dla architektury headless. [WordPress VIP pricing](https://wpvip.com/pricing/).

**Wybierać, gdy:** duży ruch, wymagania compliance i SLA, wiele serwisów, budżet enterprise.

### Własna chmura (AWS, GCP, VPS)

Najtańszy rachunek przy dużej skali, ale cała odpowiedzialność za serwer, PHP, bazę, cache, backup i bezpieczeństwo po stronie klienta lub agencji.

**Wybierać, gdy:** klient ma zespół DevOps i politykę chmury.

### Hosting frontendu w headless

Vercel Pro od $20/mies. za miejsce lub Cloudflare Workers od $5/mies. (ceny z analizy Sanity, 27.07.2026) — **dodatkowo** do hostingu WordPressa.

### Reguła TCO

Tani hosting za kilka dolarów miesięcznie bez stagingu, backupu i WAF-u zwykle kosztuje więcej przy pierwszym incydencie niż rok zarządzanego hostingu.

## Technologie opcjonalne — dodawać dopiero po spełnieniu warunku

| Technologia | Dodaj, gdy | Nie dodawaj, gdy |
|---|---|---|
| **WPML/Polylang** | Więcej niż jeden język | Serwis jednojęzyczny |
| **PublishPress / workflow** | Formalne akceptacje treści | Proces draft → publish wystarcza |
| **SearchWP / ElasticPress / Algolia** | Wyszukiwanie jest ważną ścieżką użytkownika | Kilkadziesiąt stron |
| **WooCommerce** | Sprzedaż produktów | Tylko katalog bez koszyka |
| **Multisite** | Wiele stron o wspólnym motywie i zespole | Strony o różnych motywach i cyklach wdrożeń |
| **WPGraphQL + Next.js** | Wiele kanałów, zespół React, personalizacja | Strona marketingowa bez tych potrzeb |
| **WordPress VIP** | SLA, compliance, duży ruch | Serwis firmowy średniej skali |
| **Zewnętrzne A/B** | Ruch i hipotezy istnieją | „A/B” tylko na roadmapie |

## Czego nie budować w pierwszej wersji

- page buildera obok własnych bloków — jeden sposób budowania stron;
- wtyczki na każdą drobną funkcję, którą da się zrobić kilkoma liniami w motywie;
- headless frontendu bez potwierdzonej potrzeby;
- własnego systemu formularzy, jeśli klient ma HubSpot/GetResponse;
- Multisite dla dwóch niezależnych stron;
- własnej personalizacji serwerowej przed ustaleniem strategii cache.

## Rekomendowane warianty wdrożenia

### Wariant A — najniższe TCO dla serwisu marketingowego

**WordPress + własny motyw blokowy + ACF PRO + Yoast/Rank Math + WP Engine Essential + utrzymanie**

Najlepszy dla większości stron firmowych i blogów. Wykorzystuje starter Pirxey i skille `dev-wp-*`.

### Wariant B — wielojęzyczny serwis firmowy

**Wariant A + WPML CMS + integracja TMS/Crowdin**

Dla kilku rynków; wybór wtyczki wielojęzycznej przed migracją treści.

### Wariant C — enterprise

**WordPress VIP + własny motyw + workflow akceptacji + SSO**

Dla dużego ruchu, SLA i compliance.

### Wariant D — headless

**WordPress + WPGraphQL (+ Faust.js) + Next.js + Vercel/Cloudflare**

Dla klienta przywiązanego do panelu WordPress, ale potrzebującego frontendu React, personalizacji lub wielu kanałów. Przed decyzją spike: preview, mapowanie bloków, SEO z wtyczki, formularze.

## Źródła

- WordPress: [7.0 „Armstrong”](https://wordpress.org/news/2026/05/armstrong/), [7.1 „Mary Lou”](https://wordpress.org/news/2026/08/mary-lou/), [releases](https://wordpress.org/news/category/releases/)
- [ACF PRO](https://www.advancedcustomfields.com/pro/), [WPML pricing](https://wpml.org/purchase/)
- Hosting: [WP Engine plans](https://wpengine.com/plans/), [Kinsta pricing](https://kinsta.com/pricing/), [WordPress VIP pricing](https://wpvip.com/pricing/)
- [Patchstack — State of WordPress Security in 2026](https://patchstack.com/whitepaper/state-of-wordpress-security-in-2026/)
- Headless: [Gato GraphQL vs WPGraphQL 2026](https://gatographql.com/comparisons/gatographql-vs-wpgraphql), [SmartWP — Headless WordPress 2026](https://smartwp.com/headless-wordpress/) (źródła wtórne)
- Vercel i Cloudflare: ceny z [`../sanity/stack-technologiczny.md`](../sanity/stack-technologiczny.md) (stan 27.07.2026)
- Starter WP Pirxey i skille `dev-wp-*`: wiedza wewnętrzna Pirxey (potwierdzona)
