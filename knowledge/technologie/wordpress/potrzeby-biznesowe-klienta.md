# Typowe potrzeby biznesowe klienta wobec CMS-a, które może pokryć WordPress

> **Najważniejsza zasada:** WordPress pokrywa niemal każdą potrzebę — pytanie brzmi, **ile wtyczek, własnego kodu i utrzymania** to kosztuje. Najtańsze wdrożenia pokrywają rdzeń własnymi blokami i kilkoma sprawdzonymi wtyczkami; najdroższe powstają, gdy każda potrzeba dostaje osobną wtyczkę.

Stan analizy: **13 września 2026 r.** Dokument uzupełnia [`co-wyroznia.md`](./co-wyroznia.md).

## Jak czytać tę listę

- **WordPress** — pokrywa core i edytor blokowy;
- **WordPress + motyw/bloki** — potrzebny własny motyw lub bloki (ACF, React);
- **WordPress + wtyczka** — potrzebna wtyczka, zwykle płatna;
- **WordPress + integracja** — usługa zewnętrzna;
- **poza WordPressem** — lepiej rozwiązać inną technologią.

## Potrzeby podstawowe — wspólne dla większości klientów

### 1. Marketing publikuje bez oczekiwania na developera

**Pokrycie: WordPress + motyw/bloki.** Edytor blokowy pozwala tworzyć strony z bloków i wzorców. Publikacja jest natychmiastowa w klasycznym motywie.

**Warunek powodzenia:** biblioteka bloków musi pokrywać realne sekcje. Starter Pirxey z blokami ACF i skillami `dev-wp-create-landing-page` wspiera składanie landing pages z istniejących bloków (wiedza wewnętrzna).

**Najniższy koszt:** 10–20 bloków ACF zamiast uniwersalnego page buildera.

### 2. Swoboda marketingu bez psucia design systemu

**Pokrycie: WordPress + motyw/bloki.** `theme.json` ogranicza kolory, typografię i odstępy; bloki ACF mają pola zamiast dowolnych stylów; zablokowane wzorce chronią układ.

**Ryzyko:** page buildery (Elementor, Divi) dają pełną swobodę stylów — szybki start, ale utrata spójności i wydajności.

### 3. Podgląd zmian przed publikacją

**Pokrycie: WordPress.** Edytor pokazuje stronę blisko finalnego wyglądu (edytor jest osadzony w iframe od 7.1); podgląd draftu w motywie. W headless podgląd trzeba zbudować.

### 4. Bezpieczne drafty, publikowanie i wycofywanie zmian

**Pokrycie: WordPress.** Drafty, zaplanowana publikacja, rewizje z przywracaniem.

**Granica:** zmiany opublikowanej strony bez publikowania od razu (draft na żywej stronie) i grupowe release'y wymagają wtyczek; staging całego serwisu zapewnia hosting.

### 5. Współpraca wielu osób nad treścią

**Pokrycie: WordPress (częściowe).** Notatki z wzmiankami na blokach i fragmentach tekstu (7.0/7.1). Brak edycji w czasie rzeczywistym — jednocześnie edytuje jedna osoba.

### 6. Role i rozdzielenie odpowiedzialności

**Pokrycie: WordPress + wtyczka.** Wbudowane role (Administrator, Editor, Author, Contributor). Własne role i wieloetapowe akceptacje przez wtyczki (np. PublishPress, Members).

**Koszt:** brak opłat per użytkownik — dowolna liczba kont.

### 7. Reużywalna i spójna treść

**Pokrycie: WordPress + motyw/bloki.** Zsynchronizowane wzorce (synced patterns), strony opcji ACF, własne typy wpisów i taksonomie.

### 8. Zarządzanie stronami, URL-ami i nawigacją

**Pokrycie: WordPress + wtyczka.** Hierarchia stron, permalinki, menu. Redirecty przez wtyczkę (np. Redirection) lub hosting.

### 9. Zarządzanie assetami

**Pokrycie: WordPress + integracja.** Biblioteka mediów z miniaturami i alt textem; optymalizacja obrazów i CDN zapewnia hosting lub wtyczka.

### 10. Wydajność, dostępność i responsywność

**Pokrycie: WordPress + motyw + hosting.** Wydajność zależy od motywu, liczby wtyczek, cache i hostingu. Zarządzany hosting (WP Engine — u nas domyślnie, Kinsta, VIP) zapewnia cache i CDN.

**Najniższy koszt:** lekki własny motyw, ograniczona liczba wtyczek, cache po stronie hostingu.

## Potrzeby wzrostu i skalowania

### 11. Wiele języków i rynków

**Pokrycie: WordPress + wtyczka.** WPML (€99/rok CMS), Polylang lub MultilingualPress. Integracja z TMS/Crowdin przez wtyczki lub API.

**Wpływ na koszt:** wtyczki wielojęzyczne zwiększają złożoność bazy i czasem obniżają wydajność. Wybrać przed migracją treści.

### 12. Omnichannel i wiele serwisów

**Pokrycie: WordPress Multisite lub headless.** Multisite obsługuje wiele stron w jednej instalacji. Omnichannel przez REST API lub WPGraphQL.

**Granica:** model treści WordPressa (wpisy, strony, meta) jest mniej elastyczny niż w headless CMS; bloki są zapisane jako HTML z komentarzami, trudniejsze do użycia poza webem.

### 13. SEO i widoczność w wyszukiwarkach oraz systemach AI

**Pokrycie: WordPress + wtyczka.** Yoast SEO, Rank Math lub SEOPress: metadane, sitemap, schema, breadcrumbs. Klasyczny render PHP daje indeksowalny HTML.

### 14. Formularze, lead generation i CRM

**Pokrycie: WordPress + wtyczka/integracja.** Gravity Forms, WPForms lub embed HubSpot/GetResponse. Oficjalna wtyczka HubSpot dla WordPressa.

**Ryzyko:** dane zgłoszeń przechowywane w bazie WordPressa — ustalić retencję i RODO.

### 15. Integracje zarządzane per strona

**Pokrycie: WordPress + motyw/bloki.** Pola ACF do włączania integracji per strona; Google Tag Manager.

### 16. Analityka i kontrola jakości danych

**Pokrycie: integracja.** GA4, GTM, Matomo lub inna platforma przez wtyczkę lub motyw.

### 17. Eksperymenty A/B

**Pokrycie: integracja.** VWO, Optimizely, Amplitude lub wtyczki A/B. Brak natywnego mechanizmu.

### 18. Personalizacja i dynamiczne ścieżki użytkownika

**Pokrycie: WordPress + integracja (warunkowe).** Możliwa przez PHP, wtyczki lub zewnętrzne narzędzia, ale cache stron utrudnia personalizację serwerową.

### 19. Interaktywne komponenty, animacje i embedy

**Pokrycie: WordPress + motyw/bloki.** Bloki z JS, Interactivity API, GSAP lub React w wybranych blokach.

### 20. Wyszukiwanie i filtrowanie treści

**Pokrycie: WordPress + wtyczka.** Wbudowane wyszukiwanie jest podstawowe; SearchWP, FacetWP, ElasticPress lub Algolia dla lepszej jakości.

## Potrzeby organizacji dojrzałej lub regulowanej

### 21. Bezpieczeństwo, SSO i compliance

**Pokrycie: WordPress + hosting + wtyczka.** SSO przez wtyczki SAML/OIDC; WAF i hardening przez hosting; WordPress VIP dla wymagań enterprise (SLA do 99,99%).

**Ryzyko:** 91% podatności w ekosystemie dotyczy wtyczek (Patchstack, 2026) — każda wtyczka to decyzja bezpieczeństwa.

### 22. Historia, audyt i odzyskiwanie

**Pokrycie: WordPress + hosting + wtyczka.** Rewizje treści; backup i przywracanie przez hosting; log aktywności przez wtyczkę (np. WP Activity Log).

### 23. Przenośność i ograniczenie vendor lock-in

**Pokrycie: WordPress — najlepszy w tym porównaniu.** Otwarty kod, pełny dostęp do bazy, eksport XML, dowolny hosting.

**Granica:** motyw, bloki ACF i konfiguracja wtyczek są związane z WordPressem; migracja do innego CMS-a nadal wymaga przebudowy.

### 24. AI-assisted content operations

**Pokrycie: WordPress + integracja.** Abilities API i WP AI Client w 7.0; wtyczki AI; w Pirxey skille Claude Code tworzące drafty landing pages przez MCP (wiedza wewnętrzna).

## Zakres typowego pełnego serwisu SaaS

| Grupa wymagań | Pokrycie WordPress (klasyczny) | Komentarz |
|---|---|---|
| Ownership marketingu i strony | **bardzo dobre** | Edytor blokowy, własne bloki |
| Page building i komponenty | **bardzo dobre** | ACF Blocks lub bloki React |
| Mobile i wysokie rozdzielczości | **dobre** | Zależy od motywu |
| Template pages i preview | **dobre** | Podgląd natywnie; staging przez hosting |
| Lokalizacja i Crowdin | **dobre** | WPML/Polylang + integracja |
| Formularze i thank-you pages | **dobre** | Wtyczki lub embed HubSpot |
| Nawigacja i breadcrumbs | **bardzo dobre** | Menu natywne, breadcrumbs z wtyczki SEO |
| Custom code, motion, embedy | **dobre** | PHP, JS, Interactivity API |
| Integracje per strona | **dobre** | Pola ACF, GTM |
| Personalizacja | **warunkowe** | Konflikt z cache; zewnętrzne narzędzia |
| Eksperymenty, analityka, SEO, AI visibility | **dobre** | Integracje; SEO przez wtyczki |
| Workflow AI | **dobre** | Abilities API, MCP |
| Bezpieczeństwo i role | **warunkowe** | Zależy od hostingu, utrzymania i wtyczek |
| Publikowanie, środowiska, wiele języków | **dobre** | Staging hostingu; brak edycji real-time |

## Priorytetyzacja wdrożenia pod najniższy koszt

### Etap 1 — rdzeń o najwyższym zwrocie

- lekki motyw i 10–20 bloków ACF;
- strony, blog, menu, redirecty, SEO;
- formularze podpięte do CRM;
- zarządzany hosting z backupem i stagingiem;
- abonament utrzymaniowy.

### Etap 2 — skalowanie operacji

- wielojęzyczność;
- workflow akceptacji;
- lepsze wyszukiwanie;
- testy A/B przez zewnętrzne narzędzie.

### Etap 3 — funkcje wymagające dowodu wartości

- headless frontend;
- personalizacja;
- Multisite;
- WordPress VIP.

## Pytania discovery przed wyceną

1. Kto będzie odpowiadał za aktualizacje, backup i incydenty bezpieczeństwa?
2. Czy klient ma już hosting lub politykę hostingu (region, chmura, VIP)?
3. Ile wtyczek jest dziś w użyciu i które są krytyczne?
4. Ile języków i czy rynki publikują niezależnie?
5. Czy potrzebna jest współpraca w czasie rzeczywistym w edytorze?
6. Czy potrzebne są SSO, audyt i formalne akceptacje?
7. Czy strona ma zostać klasyczna, czy musi zasilać inne kanały (headless)?

## Źródła

- [WordPress 7.0](https://wordpress.org/news/2026/05/armstrong/), [WordPress 7.1](https://wordpress.org/news/2026/08/mary-lou/)
- [ACF PRO](https://www.advancedcustomfields.com/pro/), [WPML pricing](https://wpml.org/purchase/)
- [WP Engine plans](https://wpengine.com/plans/), [Kinsta pricing](https://kinsta.com/pricing/), [WordPress VIP pricing](https://wpvip.com/pricing/)
- [Patchstack — State of WordPress Security in 2026](https://patchstack.com/whitepaper/state-of-wordpress-security-in-2026/)
