# Co wyróżnia WordPress jako CMS

> **W skrócie:** WordPress warto wybrać wtedy, gdy klient chce **najniższego kosztu licencji, największego rynku wtyczek i specjalistów oraz pełnej własności kodu i danych**. Najmocniejsze strony to brak opłat licencyjnych, dojrzały edytor blokowy, tysiące gotowych integracji i swoboda hostingu. Ceną jest odpowiedzialność za bezpieczeństwo, aktualizacje i jakość wtyczek — koszt, który nie znika, tylko przenosi się na utrzymanie.

Stan oferty i cen: **13 września 2026 r.** Kwoty są cenami katalogowymi w USD lub EUR, bez podatków i kosztu wdrożenia.

Powiązane: [`potrzeby-biznesowe-klienta.md`](./potrzeby-biznesowe-klienta.md), [`stack-technologiczny.md`](./stack-technologiczny.md).

## Najpierw biznes: ile kosztuje WordPress?

Oprogramowanie jest darmowe (open source, GPL). Budżet tworzą:

1. **wdrożenie** — motyw, bloki, konfiguracja wtyczek, migracja treści;
2. **hosting** — od taniego współdzielonego po zarządzany hosting WordPress lub WordPress VIP;
3. **licencje wtyczek premium** — pola niestandardowe, wielojęzyczność, formularze, SEO, bezpieczeństwo, backup;
4. **utrzymanie i bezpieczeństwo** — regularne aktualizacje core, motywu i wtyczek, testy po aktualizacji, monitoring;
5. **rozwój** — nowe bloki, integracje.

### Typowe koszty katalogowe

| Pozycja | Przykład | Cena |
|---|---|---|
| Core | WordPress | **$0** |
| Pola i bloki | **ACF PRO** | $49/rok (1 strona), $149/rok (10 stron), $249/rok (bez limitu) |
| Wielojęzyczność | **WPML** | €39/rok (Blog, bez tłumaczenia stringów), **€99/rok (CMS, 3 strony produkcyjne)**, €199/rok (Agency) |
| Hosting zarządzany (domyślny u nas) | **WP Engine Essential** | **$420/rok** (1 strona, 25 tys. wizyt), **$780/rok** (3 strony, 75 tys. wizyt), $1560/rok (100 tys. wizyt); 1. rok −20% |
| Hosting zarządzany (alternatywa) | **Kinsta** — pojedyncza strona | od **$35/mies.** (35 tys. wizyt) do **$375/mies.** (750 tys. wizyt); rocznie ok. 17% taniej |
| Hosting enterprise | **WordPress VIP** | wycena indywidualna; SLA 99,95–99,99%, wsparcie 24/7 |

Przykładowy roczny koszt zewnętrzny serwisu firmowego: WP Engine Essential 75 tys. wizyt ($780/rok) + ACF PRO ($49) + WPML CMS (€99 ≈ $110) → **ok. $940/rok**, bez utrzymania i rozwoju (backup i aktualizacje core są w cenie hostingu).

### Gdzie naprawdę powstają oszczędności

- **Brak licencji per użytkownik.** Liczba redaktorów nie zmienia kosztu — duża przewaga przy wielu autorach.
- **Gotowe wtyczki** zamiast developmentu: formularze, SEO, cache, integracje CRM, e-commerce (WooCommerce).
- **Duży rynek specjalistów**, łatwa zmiana agencji.
- **Wewnętrzny starter Pirxey** z blokami ACF i rodziną skilli Claude Code `dev-wp-*` (tworzenie bloków, landing pages, Figma → blok) przyspiesza wdrożenie (wiedza wewnętrzna, potwierdzona).

### Ryzyko kosztowe, które trzeba kontrolować

- **Bezpieczeństwo wtyczek.** Według raportu Patchstack w 2025 r. odkryto **11 334 podatności** w ekosystemie WordPress (+42% r/r); **91% dotyczyło wtyczek**, tylko 6 — core (wszystkie niskiego ryzyka). 46% podatności nie miało łatki w chwili ujawnienia, a mediana czasu do pierwszej próby wykorzystania wynosiła ok. 5 godzin. [State of WordPress Security in 2026](https://patchstack.com/whitepaper/state-of-wordpress-security-in-2026/).
- **Koszt aktualizacji.** Każda wtyczka to zależność; aktualizacje mogą zepsuć stronę bez testów na stagingu.
- **Dług techniczny page builderów.** Elementor, Divi i podobne dają swobodę, ale utrudniają wydajność, spójność design systemu i migrację.
- **Spór WP Engine vs Automattic.** Od 2024 r. trwa spór prawny, w którym m.in. repozytorium ACF zostało przejęte przez WordPress.org i zastąpione forkiem Secure Custom Fields; nakaz sądowy przywrócił WP Engine kontrolę nad ACF. Proces trwa, rozprawa spodziewana na przełomie 2026/2027 (źródła wtórne — pewność średnia). Dla klienta: ryzyko dotyczy ekosystemu i dostawców, nie działania core WordPress.

**Rekomendacja kosztowa:** licencja jest tania, ale w wycenie trzeba jawnie ująć **abonament utrzymaniowy** (aktualizacje, backup, monitoring bezpieczeństwa). Bez niego niski koszt WordPressa jest pozorny.

## Co WordPress robi inaczej

### 1. Własność i swoboda hostingu

Kod i baza danych należą do klienta. Można hostować wszędzie: od taniego hostingu po chmurę, zarządzany hosting lub WordPress VIP. Migracja do innego hostingu nie wymaga zmiany CMS-a.

### 2. Edytor blokowy (Gutenberg) jako page builder

Marketing składa strony z bloków. Bloki mogą być natywne, z wtyczek lub własne (ACF Blocks albo bloki React). WordPress 7.0 (20 maja 2026) dodał m.in. notatki z wzmiankami na blokach, nowy wygląd panelu i Abilities API dla automatyzacji i AI. WordPress 7.1 (19 sierpnia 2026) rozszerzył notatki na fragmenty tekstu i dodał bloki Tabs i Playlist.

**Uwaga:** zapowiadana współpraca w czasie rzeczywistym (wiele osób edytuje jednocześnie) **nie weszła do 7.0**; według źródeł wtórnych przesunięto ją najwcześniej na 2027 r.

### 3. Największy ekosystem rozszerzeń

Dziesiątki tysięcy wtyczek i motywów. Większość typowych potrzeb (formularze, SEO, wielojęzyczność, członkostwa, e-commerce) ma gotowe rozwiązanie. Jakość bywa bardzo różna — dobór i ograniczenie liczby wtyczek to kluczowa kompetencja wdrożeniowca.

### 4. Tryb klasyczny lub headless

WordPress może renderować stronę (motyw PHP) albo być headless CMS-em przez REST API lub WPGraphQL dla frontendu Next.js/Astro. Headless zwiększa koszt i usuwa część zalet (podgląd, wtyczki wpływające na frontend).

### 5. Odpowiedzialność za utrzymanie leży po stronie klienta lub agencji

W odróżnieniu od HubSpot i Webflow, nikt nie aktualizuje platformy za klienta, chyba że kupi zarządzany hosting z aktualizacjami lub umowę serwisową.

## Jak WordPress odpowiada na typowe potrzeby klienta

| Potrzeba | Odpowiedź WordPress | Na co uważać |
|---|---|---|
| **Prosta edycja bez developera** | Edytor blokowy, własne bloki ACF, wzorce bloków | Źle zaprojektowane bloki lub page builder psują spójność |
| **Szybkie publikowanie kampanii** | Wzorce stron, duplikacja, zaplanowana publikacja | Zaawansowane release'y wymagają wtyczek |
| **Praca wielu osób** | Role, notatki na blokach (7.0+) | Brak edycji w czasie rzeczywistym; blokada edycji dokumentu |
| **Role i akceptacje** | Wbudowane role; workflow akceptacji przez wtyczki (np. PublishPress) | Każda wtyczka workflow to dodatkowe utrzymanie |
| **Wiele języków** | WPML, Polylang, MultilingualPress | Licencje i wpływ na wydajność; wybór przed migracją |
| **Wiele serwisów** | WordPress Multisite | Wspólne wtyczki i aktualizacje dla wszystkich stron |
| **Wydajność** | Cache, CDN, zarządzany hosting | Wydajność zależy od motywu, wtyczek i hostingu |
| **Integracje** | Wtyczki, REST API, WPGraphQL, hooki PHP | Wtyczki integracyjne niskiej jakości to ryzyko bezpieczeństwa |
| **Bezpieczeństwo** | Aktualizacje, WAF hostingu, wtyczki bezpieczeństwa | 91% podatności w wtyczkach — potrzebny proces utrzymania |
| **Przenośność** | Otwarty kod, eksport XML, pełny dostęp do bazy | Motyw i bloki ACF są związane z WordPressem |

## Kiedy WordPress jest szczególnie dobrym wyborem

- budżet licencyjny jest ograniczony, a redaktorów jest wielu;
- klient chce **pełnej własności** kodu i danych oraz swobody wyboru hostingu;
- serwis to strona firmowa, blog, portal treści lub WooCommerce;
- potrzebne są gotowe wtyczki do typowych funkcji;
- klient ma lub kupi **umowę utrzymaniową**;
- zespół delivery ma starter WordPress i doświadczenie w blokach ACF.

## Kiedy lepiej rozważyć inne rozwiązanie

- klient **nie chce ani nie zapłaci za utrzymanie** i aktualizacje — lepszy SaaS (Webflow, HubSpot);
- treść ma zasilać wiele kanałów i aplikacji — lepszy headless CMS;
- wymagana jest **współpraca w czasie rzeczywistym** w edytorze;
- organizacja ma surowe wymagania bezpieczeństwa bez budżetu na WordPress VIP lub hardening;
- strona ma być w pełni zintegrowana z HubSpot CRM i personalizacją CRM — lepszy HubSpot CMS.

## Rekomendacja decyzyjna

Najlepszy argument za WordPressem: **najniższy koszt licencji i największa swoboda przy dojrzałym edytorze i ogromnym ekosystemie — pod warunkiem, że utrzymanie jest zaplanowane i opłacone**.

1. **Policzyć TCO na 3 lata** z hostingiem, licencjami wtyczek i abonamentem utrzymaniowym.
2. **Ograniczyć liczbę wtyczek** do sprawdzonych i wypisać je w ofercie.
3. **Ustalić, kto odpowiada za aktualizacje i incydenty bezpieczeństwa** — klient, agencja czy hosting.

## Źródła

- [WordPress 7.0 „Armstrong”](https://wordpress.org/news/2026/05/armstrong/) (20.05.2026), [WordPress 7.1 „Mary Lou”](https://wordpress.org/news/2026/08/mary-lou/) (19.08.2026)
- [ACF PRO pricing](https://www.advancedcustomfields.com/pro/)
- [WPML pricing](https://wpml.org/purchase/)
- [WP Engine plans](https://wpengine.com/plans/), [Kinsta pricing](https://kinsta.com/pricing/)
- [WordPress VIP pricing](https://wpvip.com/pricing/)
- [Patchstack — State of WordPress Security in 2026](https://patchstack.com/whitepaper/state-of-wordpress-security-in-2026/)
- Spór WP Engine vs Automattic: [Search Engine Journal](https://www.searchenginejournal.com/wp-engine-vs-automattic-rulings-preserve-wp-engines-lawsuit/555928/), [WP Engine](https://wpengine.com/blog/ensuring-stability-and-security/) (źródła wtórne / strony sporu)
- Real-time collaboration usunięte z 7.0: [Briteweb](https://briteweb.com/insights/wordpress-7/) (źródło wtórne)
