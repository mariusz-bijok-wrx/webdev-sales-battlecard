# Typowe potrzeby biznesowe klienta wobec CMS-a, które może pokryć Prismic

> **Najważniejsza zasada:** klient rzadko potrzebuje „CMS-a”. Potrzebuje niższego kosztu utrzymania serwisu, krótszego czasu publikacji, mniejszej zależności od developerów, bezpiecznych zmian i możliwości skalowania na kolejne kampanie oraz rynki. Prismic dobrze odpowiada na te potrzeby w serwisach marketingowych opartych na reużywalnych slices, ale część wymagań pokrywa razem z frontendem, a część dopiero przez integrację lub proces organizacyjny.

Stan analizy: **28 lipca 2026 r.** Dokument uzupełnia [`co-wyroznia.md`](./co-wyroznia.md), a warianty implementacji rozwija [`stack-technologiczny.md`](./stack-technologiczny.md). Koncentruje się na potrzebach klienta oraz ich wpływie na koszt.

## Jak czytać tę listę

Każdą potrzebę oznaczono jednym z pięciu poziomów pokrycia:

- **Prismic** — główna odpowiedzialność leży w Visual Page Builderze, repozytorium i usługach platformy;
- **Prismic + frontend** — CMS przechowuje treść i konfigurację, ale zachowanie realizuje aplikacja webowa;
- **Prismic + integracja** — potrzebna jest wyspecjalizowana usługa, np. Crowdin, HubSpot albo platforma eksperymentalna;
- **Prismic + proces migracyjny** — potrzebne są audyt, transformacja danych, import i kontrolowany cutover;
- **poza CMS-em** — Prismic może dostarczać dane, lecz nie powinno być głównym narzędziem do rozwiązania problemu.

Takie rozróżnienie chroni budżet. Najdroższe wdrożenia powstają zwykle wtedy, gdy CMS ma jednocześnie zastąpić system analityczny, CRM, platformę eksperymentalną, DAM, aplikację produktową i dowolny no-code builder.

W Prismic szczególnie ważne są cztery progi kosztowe:

1. **każde repozytorium ma własny plan** — mnożenie repozytoriów dla marek, krajów lub microsite'ów mnoży koszt;
2. **locale są limitowane** — od 2 na Free do 8 na Platinum, a przekroczenie progu może wymusić duży upgrade;
3. **standardowe role zaczynają się od Medium za $150/mies.** — Starter i Small są tanie tylko przy prostym modelu odpowiedzialności;
4. **środowiska developerskie są funkcją wysokich planów** — w Platinum jedno kosztuje obecnie $3 000 rocznie, Enterprise zawiera dwa.

Pełne ceny i ryzyka opisuje [`co-wyroznia.md`](./co-wyroznia.md). Przy każdej potrzebie poniżej wskazano najtańszy sensowny sposób realizacji, a nie najbardziej rozbudowany wariant.

## Potrzeby podstawowe — wspólne dla większości klientów

### 1. Marketing publikuje bez oczekiwania na developera

**Potrzeba biznesowa:** skrócenie czasu od pomysłu do publikacji i odciążenie zespołu technicznego z prostych zmian tekstu, grafik, linków i układu strony.

**Pokrycie: Prismic + frontend.** Visual Page Builder pozwala tworzyć strony z przygotowanych slices, zmieniać ich kolejność, warianty i treść. Publikacja contentu nie wymaga deployu, jeżeli frontend poprawnie obsługuje aktualizację lub rewalidację danych z Content API.

**Warunek powodzenia:** potrzebne komponenty muszą wcześniej istnieć w kodzie. Marketing samodzielnie korzysta z zaprojektowanych możliwości, ale nowa logika, integracja albo zupełnie nowy układ nadal wymaga developmentu.

**Najniższy koszt:** zacząć od 10–20 slices pokrywających większość istniejących i planowanych stron. Warianty powinny odpowiadać decyzjom biznesowym, np. „jasny / ciemny” lub „grafika po lewej / prawej”, zamiast udostępniać surowe parametry CSS.

### 2. Swoboda marketingu bez psucia design systemu

**Potrzeba biznesowa:** szybkie tworzenie landing page'y przy zachowaniu spójności marki, responsywności i dostępności.

**Pokrycie: Prismic + frontend.** Slice definiuje pola i warianty dostępne w Page Builderze, a komponent w kodzie egzekwuje tokeny, layout i zachowanie. Type Builder oraz modele przechowywane lokalnie tworzą kontrakt między edytorem i frontendem.

**Granica:** Prismic nie zweryfikuje automatycznie każdej kombinacji pod kątem mobile, kontrastu, długości tekstu czy działania animacji. Zakres walidacji modelu jest mniejszy niż pełny test działającego komponentu.

**Najniższy koszt:** ograniczona lista wariantów, jasne nazwy pól, krótkie instrukcje oraz przetestowane wartości domyślne. Nie tworzyć jednego „uniwersalnego slice'a” z dziesiątkami przełączników.

### 3. Podgląd zmian przed publikacją

**Potrzeba biznesowa:** redaktor i interesariusz widzą finalną stronę, zanim zmiana trafi do klientów.

**Pokrycie: Prismic + frontend.** Prismic obsługuje live preview poszczególnych slices, pełny preview serwisu z draftami i shareable previews. Oficjalne SDK upraszczają konfigurację dla Next.js, Nuxt i SvelteKit.

**Granica:** preview wymaga osobnej trasy symulatora oraz poprawnej obsługi sesji draftów, routingu i locale. Dla Astro integracja jest bardziej własna niż w trzech pierwszoplanowych frameworkach, co podnosi koszt developmentu.

**Najniższy koszt:** preview oparte na tych samych komponentach i aplikacji co produkcja. Osobne, ręcznie synchronizowane „demo środowisko” zwykle zwiększa koszt i ryzyko różnic.

### 4. Bezpieczne drafty, publikowanie i wycofywanie zmian

**Potrzeba biznesowa:** produkcja nie może zostać uszkodzona przez niekompletną lub przypadkową zmianę.

**Pokrycie: Prismic.** Drafty oddzielają pracę od opublikowanej treści. Releases grupują do 200 stron, pozwalają je wspólnie podejrzeć i opublikować natychmiast albo w zaplanowanym czasie. Drafty, scheduling, releases i historia są zawarte we wszystkich planach.

**Granica:** wieloetapowy approval flow, np. autor → legal → country owner → publisher, nie jest automatycznie gotowym workflow. Może wymagać ról, zewnętrznego systemu zadań lub procesu organizacyjnego. Usunięcie release'u może wycofać jego zmiany lub zarchiwizować nowe strony, dlatego zespół potrzebuje jasnej instrukcji.

**Najniższy koszt:** prosty proces draft → preview → release → publish. Rozbudowywać go dopiero po zidentyfikowaniu realnych błędów i wymaganych akceptacji.

### 5. Współpraca wielu osób nad treścią

**Potrzeba biznesowa:** kilka osób tworzy i publikuje treść bez chaosu w plikach, mailach i ręcznych listach stron.

**Pokrycie: Prismic + proces zespołu.** Repozytorium zapewnia wspólną listę treści, filtry po autorze, tagi, spaces, drafty i releases. Spaces mogą oddzielić np. marketing produktu, blog i treści prawne.

**Granica:** nie należy zakładać, że Prismic zastąpi narzędzie do komentarzy, zadań i pełnego workflow akceptacji. Jeśli zespół potrzebuje formalnych handoffów, terminu, osoby odpowiedzialnej i dowodu zatwierdzenia, może zachować Jira, Asanę lub inne narzędzie pracy.

**Najniższy koszt:** jeden właściciel dokumentu lub release'u, spójna konwencja tags/spaces i proces akceptacji opisany zanim powstanie integracja.

### 6. Role i rozdzielenie odpowiedzialności

**Potrzeba biznesowa:** autor może pisać, publisher publikować, a ustawienia techniczne pozostają dostępne administratorom.

**Pokrycie: Prismic.** Od planu Medium dostępne są standardowe role Writer, Publisher i Administrator. Custom roles per space lub locale są dodatkiem Enterprise.

**Wpływ na koszt:** role są częstszą przyczyną przejścia ze Small za $25 na Medium za $150 niż ruch lub liczba dokumentów. Własna macierz uprawnień może przenieść projekt do Enterprise.

**Najniższy koszt:** sprawdzić, czy trzy standardowe role pokrywają rzeczywiste ryzyko. Custom roles kupować wtedy, gdy ograniczenie dostępu do konkretnej marki, przestrzeni lub rynku ma uzasadnienie prawne albo organizacyjne.

### 7. Reużywalna i spójna treść

**Potrzeba biznesowa:** dane autora, produkt, komunikat prawny lub element nawigacji powinny być aktualizowane w jednym miejscu.

**Pokrycie: Prismic.** Custom types i Content Relationships pozwalają współdzielić dokumenty, a slices standaryzują sposób prezentacji sekcji na wielu stronach.

**Ryzyko:** Prismic jest mocno zoptymalizowany pod strony i slices. Bardzo złożony graf treści współdzielony przez wiele produktów może być trudniejszy do modelowania i pobierania niż w CMS-ie o bardziej data-first charakterze.

**Najniższy koszt:** współdzielić tylko treści mające własny cykl życia i wiele miejsc użycia. Nie zamieniać każdego zdania w osobny dokument ani każdej sekcji w globalną referencję.

### 8. Zarządzanie stronami, URL-ami i nawigacją

**Potrzeba biznesowa:** marketing tworzy strony, ustala UID, linkowanie wewnętrzne i elementy nawigacji.

**Pokrycie: Prismic + frontend.** Page types przechowują strony, UID-y i relacje, a Route Resolver mapuje dokumenty na URL-e. Link fields pozwalają wybierać istniejące dokumenty zamiast wpisywać adres ręcznie. Frontend generuje hierarchię, breadcrumbs i właściwe zachowanie tras.

**Granica:** Prismic nie jest serwerem redirectów. CMS może przechowywać mapę stary URL → nowy cel, ale regułę 301 wykonuje framework, hosting albo CDN. Hierarchiczny routing wymaga świadomego modelu; sam UID nie tworzy drzewa strony.

**Najniższy koszt:** jeden komponent linku, centralny rejestr nawigacji i redirectów oraz automatyczny test linków do stron zarchiwizowanych lub nieopublikowanych.

### 9. Zarządzanie assetami

**Potrzeba biznesowa:** redaktor znajduje obrazy i pliki, kontroluje alt text, crop, prawa i użycie materiału.

**Pokrycie: Prismic + frontend.** Media Library obsługuje wyszukiwanie, tagowanie, filtrowanie, tytuł, alt text, copyright i prywatne notatki. Obrazy są serwowane przez imgix z kompresją, formatowaniem, cropem i responsywnymi rozmiarami.

**Granica:** jest to biblioteka mediów CMS-a, a nie pełny DAM z cyklem praw licencyjnych, zaawansowanymi approvalami i dystrybucją dla wielu systemów. Globalna zmiana metadanych assetu nie musi automatycznie aktualizować już zapisanych pól we wszystkich dokumentach; alt text dla locale często trzeba utrzymać przy użyciu obrazu.

**Najniższy koszt:** zacząć od Media Library, wspólnej taksonomii tagów i wymaganych pól dostępności. Osobny DAM wdrażać dopiero przy realnym problemie licencji, wolumenu lub wielu kanałów.

### 10. Wydajność, dostępność i responsywność

**Potrzeba biznesowa:** strona działa szybko i poprawnie na telefonach, dużych ekranach oraz dla osób korzystających z technologii asystujących.

**Pokrycie: głównie poza CMS-em.** Prismic dostarcza Content API, CDN i optymalizację obrazów. Modele mogą wymagać alt textu i ograniczać wybór wariantów, ale Core Web Vitals, semantyczny HTML, CSS, focus management, responsive i ilość JavaScriptu należą do frontendu.

**Najniższy koszt:** komponenty testowane przed dodaniem do biblioteki slices, statyczne lub cache'owane renderowanie treści, obrazy z poprawnym `srcset` i automatyczne testy accessibility dla kluczowych stron.

## Potrzeby wzrostu i skalowania

### 11. Wiele języków i rynków

**Potrzeba biznesowa:** jedna platforma obsługuje treści globalne i lokalne, różne slugi, terminy publikacji oraz wyjątki rynkowe.

**Pokrycie: Prismic + frontend + opcjonalna integracja.** Prismic tworzy powiązane dokumenty per locale, pozwala kopiować strony pojedynczo lub grupowo i publikować je niezależnie. Frontend odpowiada za routing, `hreflang`, canonicale i redirecty językowe. Crowdin lub inny TMS może obsłużyć tłumaczenia, pamięć tłumaczeniową, glossary i LQA.

**Wpływ na koszt:** locale są twardym limitem planu: Free 2, Starter 3, Small 4, Medium 5, Platinum 8, Enterprise indywidualnie. Piąty język może więc zmienić licencję z $25 na $150 miesięcznie, a szósty z $150 na $675. Do tego dochodzi duplikowanie i ręczne utrzymywanie zmian między wersjami.

**Najniższy koszt:** potwierdzić liczbę rynków przed wyborem planu, ustalić język bazowy i moment odłączenia tłumaczenia od źródła. Integrację TMS wdrożyć po stabilizacji modeli. Wbudowane tłumaczenie AI jest obecnie beta i dostępne na żądanie, więc nie powinno być jedyną podstawą procesu.

### 12. Omnichannel i wiele serwisów

**Potrzeba biznesowa:** treść zasila główny serwis, aplikację, help center, kolejne marki lub microsites.

**Pokrycie: Prismic.** Content API, GraphQL i webhooks pozwalają wielu konsumentom korzystać z repozytorium. Custom types nadają się do współdzielonych danych, a slices do stron webowych.

**Granica kosztowa:** plan jest naliczany per repozytorium. Osobne repo dla każdej marki lub kraju zwiększa koszt licencji, synchronizacji modeli, komponentów, preview i release'ów. Jeden wspólny repo może z kolei utrudniać uprawnienia i niezależność zespołów.

**Najniższy koszt:** jeden repo dla jednego spójnego obszaru odpowiedzialności i wspólna biblioteka slices. Kolejne repozytorium tworzyć dopiero, gdy niezależny zespół, marka, bezpieczeństwo lub cykl release'ów uzasadniają osobny lifecycle.

### 13. SEO i widoczność w wyszukiwarkach oraz systemach AI

**Potrzeba biznesowa:** marketing kontroluje tytuły, opisy, canonicale, indeksowanie i structured data, a treść może być poprawnie interpretowana przez wyszukiwarki i crawlery AI.

**Pokrycie: Prismic + frontend.** CMS przechowuje metadane, relacje i semantyczne dane produktu, kategorii czy autora. Frontend generuje HTML, JSON-LD, sitemapę, `robots.txt`, canonicale, `hreflang` oraz odpowiedzi HTTP.

**Granica:** pole „SEO” nie gwarantuje widoczności. Potrzebne są poprawny rendering, architektura informacji, linkowanie, wydajność, jakość treści i monitoring. „AI-ready” strona nie wynika z osobnego pliku lub checkboxa, lecz z czytelnego HTML-u, danych strukturalnych i jednoznacznej treści.

**Najniższy koszt:** wspólny model SEO z sensownymi defaultami, automatyczna walidacja braków oraz JSON-LD generowany z danych domenowych zamiast ręcznie wklejanego JSON-u.

### 14. Formularze, lead generation i CRM

**Potrzeba biznesowa:** marketer wybiera formularz, ustawia CTA i thank-you page, a lead trafia do HubSpot, GetResponse lub innego CRM-u.

**Pokrycie: Prismic + integracja + frontend.** Prismic może przechowywać identyfikator formularza, wariant prezentacji, tekst zgód, thank-you page i zdarzenia analityczne. Frontend osadza formularz albo bezpiecznie wysyła dane do dostawcy. CRM pozostaje właścicielem leadów.

**Granica:** dane osobowe nie powinny trafiać do dokumentów Prismic. CMS nie zastępuje backendu do walidacji, consent, antyspamu, retry i audytu.

**Najniższy koszt:** użyć formularzy już działających u klienta i jednego slice'a będącego kontrolowanym adapterem. Własny backend formularzy budować dopiero, gdy embed nie spełnia wymagań UX, bezpieczeństwa lub niezawodności.

### 15. Integracje zarządzane per strona

**Potrzeba biznesowa:** marketing włącza LiveChat, demo, tracking albo narzędzie kampanii tylko na wybranych stronach.

**Pokrycie: Prismic + frontend.** Dokument może zawierać listę zatwierdzonych integracji i bezpieczną konfigurację. Frontend ładuje odpowiedni adapter oraz respektuje consent.

**Ryzyko:** dowolne pole na JavaScript omija review, zwiększa powierzchnię ataku, pogarsza wydajność i może naruszyć politykę prywatności.

**Najniższy koszt:** rejestr integracji w kodzie i prosty wybór w CMS-ie. Nowy dostawca przechodzi jednorazowy review techniczny, a późniejsze włączanie na stronach nie wymaga deployu.

### 16. Analityka i kontrola jakości danych

**Potrzeba biznesowa:** zespół mierzy konwersję i przed publikacją wie, czy komponent emituje właściwe zdarzenia.

**Pokrycie: Prismic + frontend + integracja.** Slice może przechowywać zatwierdzony klucz eventu lub cel biznesowy. Frontend emituje zdarzenie, a Amplitude, GA lub inna platforma je przechowuje i analizuje.

**Granica:** Prismic nie waliduje rzeczywistego zdarzenia w przeglądarce. Preview treści nie zastępuje testu warstwy danych.

**Najniższy koszt:** centralny słownik zdarzeń, automatyczne testy kluczowych CTA i brak dowolnych nazw wpisywanych przez redaktora.

### 17. Eksperymenty A/B

**Potrzeba biznesowa:** marketing testuje komunikaty, sekcje, CTA lub całe URL-e i ocenia wpływ na wynik.

**Pokrycie: Prismic + integracja + frontend.** CMS może przechowywać warianty treści albo identyfikatory eksperymentu. Alokacja użytkownika, targeting, exposure event i statystyka powinny należeć do VWO, Amplitude Experiment lub innej platformy.

**Granica:** dwa slices z różną treścią nie tworzą poprawnego testu bez wiarygodnego przydziału i pomiaru. Dynamiczne warianty komplikują preview, cache i SEO.

**Najniższy koszt:** wykorzystać narzędzie już opłacane przez klienta. Zacząć od testów URL lub jednego jawnego slotu, zamiast modelować eksperyment w każdym slice.

### 18. Personalizacja i dynamiczne ścieżki użytkownika

**Potrzeba biznesowa:** treść, CTA lub oferta zależy od kampanii, segmentu, rynku, zachowania albo danych firmograficznych.

**Pokrycie: Prismic + frontend + integracja.** Prismic może przechowywać zatwierdzone warianty i identyfikatory reguł. Rozpoznawanie użytkownika, ewaluacja, consent i ochrona prywatności należą do frontendu, CDP, feature flags lub platformy personalizacyjnej.

**Ryzyko:** liczba kombinacji rośnie szybko, utrudnia QA i pomiar, a renderowanie per request może zwiększyć koszt hostingu.

**Najniższy koszt:** personalizować jeden obszar o wysokiej wartości, np. hero lub CTA na podstawie źródła kampanii. Rozszerzać dopiero po zmierzeniu wyniku.

### 19. Interaktywne komponenty, animacje i embedy

**Potrzeba biznesowa:** nowoczesny serwis SaaS potrzebuje interaktywnego hero, sliderów, kalkulatorów, demonstracji produktu, Lottie, SVG lub wideo.

**Pokrycie: Prismic + frontend.** CMS przechowuje treść, assety i bezpieczne parametry, a komponent implementuje interakcję. Type Builder i CLI pomagają utrzymać model oraz wygenerowane typy; AI może przyspieszyć kodowanie.

**Granica:** AI ani Page Builder nie zdejmują odpowiedzialności za performance, mobile, accessibility i bezpieczeństwo. Dowolny custom code wprowadzany przez redaktora jest drogim i ryzykownym wyjątkiem.

**Najniższy koszt:** wspólne, lazy-loadowane komponenty; CSS i natywne API przed ciężką biblioteką; dozwolone embedy zamiast surowego skryptu.

### 20. Wyszukiwanie i filtrowanie treści

**Potrzeba biznesowa:** użytkownik znajduje artykuł, template, produkt lub dokument po frazie, kategorii i atrybutach.

**Pokrycie: Prismic + frontend; czasem integracja.** Content API wystarcza do listingów, filtrów i prostych zapytań. Zaawansowany full-text search, tolerancja literówek, ranking, facety i duża skala mogą wymagać Algolii, Typesense lub innego indeksu aktualizowanego webhookami.

**Najniższy koszt:** zacząć od filtrowania po jawnych polach i kategoriach. Zewnętrzny silnik wdrożyć dopiero po zdefiniowaniu jakości wyszukiwania, wolumenu i częstotliwości aktualizacji.

## Potrzeby organizacji dojrzałej lub regulowanej

### 21. Bezpieczeństwo, SSO i compliance

**Potrzeba biznesowa:** kontrola dostępu, centralne odbieranie uprawnień, prywatne API, ślad zmian, SLA i zgodność z politykami organizacji.

**Pokrycie: Prismic + cała architektura.** Platforma obsługuje prywatne API i tokeny. Enterprise dodaje SSO, backupy, restoring capabilities, InfoSec/legal review, SLA, custom roles i wsparcie premium. Bezpieczeństwo formularzy, zewnętrznych skryptów, sekretów, preview i pipeline'u wdrożeniowego pozostaje odpowiedzialnością rozwiązania.

**Wpływ na koszt:** obowiązkowe SSO lub SLA od razu kieruje projekt do wyceny Enterprise, niezależnie od ruchu. Obejścia dla wymogu bezpieczeństwa zwykle kosztują więcej i zwiększają ryzyko.

**Najniższy koszt:** spisać wymagania compliance przed wyborem planu i architektury. Nie kupować Enterprise „na wszelki wypadek”, ale też nie projektować fikcyjnego SSO poza CMS-em.

### 22. Historia, audyt i odzyskiwanie

**Potrzeba biznesowa:** wiadomo, co zmieniono, można obejrzeć poprzednie wersje i odtworzyć serwis po błędzie albo awarii.

**Pokrycie: Prismic, częściowo Enterprise.** Pełna historia rewizji jest wymieniona we wszystkich planach. Enterprise dodaje backupy oraz restoring capabilities na poziomie usługi.

**Granica:** historia dokumentu nie jest pełną polityką disaster recovery. Eksport przez Document API nie obejmuje automatycznie draftów, archiwów ani nieużywanych assetów, a odtworzenie modeli, kodu i konfiguracji wymaga własnego repozytorium oraz procesu.

**Najniższy koszt:** modele i kod wersjonować w Git, cyklicznie eksportować opublikowane dane oraz określić wymagane RPO/RTO. Enterprise uzasadniać potrzebą gwarantowanego restore, nie samym słowem „backup”.

### 23. Przenośność i ograniczenie vendor lock-in

**Potrzeba biznesowa:** firma zachowuje dostęp do treści i może zmienić frontend lub dostawcę.

**Pokrycie: Prismic + własny proces eksportu.** Opublikowane dokumenty można pobrać przez Document API, assety przez ich adresy, a modele przechowywać w repozytorium kodu. Oddzielenie treści od frontendu ułatwia redesign.

**Granica:** slices, modele, linki, locale, workflow preview i komponenty pozostają specyficzne dla Prismic. Publiczny eksport nie jest kompletnym snapshotem wszystkich stanów. Lock-in danych można ograniczyć, ale migracja rozwiązania nadal wymaga transformacji.

**Najniższy koszt:** utrzymywać modele w kodzie, dokumentować mapowanie typów, testować eksport przed sytuacją awaryjną i unikać kodowania znaczenia biznesowego wyłącznie w nazwach technicznych slices.

### 24. AI-assisted development i content operations

**Potrzeba biznesowa:** przyspieszenie modelowania, implementacji komponentów, tworzenia stron, tłumaczeń i masowych zmian treści.

**Pokrycie: Prismic + AI + review człowieka.** Prismic CLI jest projektowany do pracy z agentami kodującymi i obsługuje setup, modele, typy oraz lokalny preview. Oficjalny Prismic MCP pozwala agentom wyszukiwać, czytać i tworzyć treść, przesyłać assety oraz zarządzać releases. Type Builder daje wizualną kontrolę modeli.

**Bezpieczna granica:** operacje tworzą drafty do weryfikacji; Migration API nie publikuje programatycznie. To ogranicza pełną autonomię, ale chroni produkcję. AI nie zastępuje review designu, faktów, SEO, accessibility, tłumaczeń ani praw do assetów.

**Wpływ na koszt:** część funkcji AI jest beta, dostępna na żądanie lub sprzedawana jako osobny AI landing page builder. Do ROI trzeba doliczyć koszt modelu, agenta i review. Nie zakładać procentowej oszczędności bez pilota.

**Najniższy koszt:** zacząć od deterministycznych zadań — scaffolding slice'a, generowanie typów, duplikacja strony, uzupełnienie znanych pól i masowa zmiana przygotowana jako draft. Mierzyć pełny czas razem z poprawkami.

### 25. Migracja z istniejącego CMS-a

**Potrzeba biznesowa:** klient chce zmienić CMS bez utraty treści, SEO, assetów, linków, locale i ciągłości publikowania.

**Pokrycie: Prismic + proces migracyjny.** Migration API jest dostępne we wszystkich planach. `@prismicio/migrate` wspiera m.in. konwersję HTML-u do Rich Text, tworzenie assetów i relacji. Zaimportowane dokumenty trafiają jako drafty do Migration Release, gdzie można je sprawdzić przed ręczną publikacją.

**Główny koszt:** nie jest nim licencja ani liczba rekordów, lecz audyt, docelowy model, mapowanie starych bloków na slices, transformacja HTML-u, assety, relacje, locale, redirecty 301, QA i cutover. Migracja musi zwykle objąć także frontend albo jego części.

**Orientacyjny nakład techniczny:** prosta migracja **5–15 osobodni**, typowy wielojęzyczny serwis marketingowy **20–60 osobodni**, złożona migracja wielu źródeł **60–150+ osobodni**. Są to heurystyki do wstępnego budżetu, nie ceny Prismica. Założenia i sposób estymacji opisuje sekcja [„Ile kosztuje migracja z innego CMS-a?”](./co-wyroznia.md#ile-kosztuje-migracja-z-innego-cms-a).

**Najniższy koszt:** zrobić discovery i próbny import 20–50 reprezentatywnych dokumentów, zmierzyć automatyczną konwersję oraz ręczne poprawki, a dopiero później wycenić całość. Nie kopiować modelu 1:1, jeśli utrwala on problemy starego CMS-a.

## Wnioski z referencyjnego zakresu pełnego serwisu SaaS

Referencyjny zakres obejmuje 14 grup wymagań dla nowoczesnego serwisu SaaS:

1. ownership marketingu, routing i zakres stron;
2. page building oraz reużywalne komponenty;
3. mobile i wysokie rozdzielczości;
4. strony i preview template'ów;
5. lokalizacja oraz Crowdin;
6. formularze HubSpot/GetResponse i thank-you pages;
7. nawigacja oraz breadcrumbs;
8. custom code, motion i embedy;
9. integracje per strona;
10. personalizacja;
11. eksperymenty, analityka, SEO i widoczność dla AI;
12. workflow wspierane przez AI;
13. bezpieczeństwo i role;
14. publikowanie, środowiska i wiele języków.

Prismic dobrze pasuje do centralnego celu dokumentu: marketing buduje i publikuje strony z zatwierdzonych sekcji bez oczekiwania na deploy. Slices, variants, Visual Page Builder, preview i Releases odpowiadają bezpośrednio na ownership, szybkość kampanii i bezpieczne guardrails.

Nie pokrywa jednak samodzielnie żadnej grupy dotyczącej zachowania finalnej strony. Frontend odpowiada za routing, responsive, SEO, AEO, interakcje, wydajność, analitykę i personalizację. Crowdin, HubSpot/GetResponse, VWO/Amplitude i narzędzia consent zachowują własne odpowiedzialności.

Najważniejsze konsekwencje kosztowe dla pełnego zakresu referencyjnego:

- **role** wymagają co najmniej Medium, jeżeli autorzy nie mogą samodzielnie publikować;
- **liczba języków** może szybko wymusić Platinum albo Enterprise;
- **oddzielne staging/content environments** nie są tanią funkcją bazowego planu;
- **Next.js, Nuxt i SvelteKit** mają bardziej gotowe ścieżki preview niż Astro;
- **personalizacja, A/B testing i custom code** są kosztami frontendu i integracji, nie funkcjami uzyskanymi przez zakup CMS-a;
- **AI** może przyspieszyć budowę i content operations, lecz potrzebuje mierzonego pilota oraz human review;
- **migracja obecnego CMS MVP** powinna zostać wyceniona po próbnym imporcie, a nie na podstawie liczby stron.

Wymaganie „Marketing może robić wszystko bez developera” należy rozumieć jako: **marketing samodzielnie korzysta z wcześniej zaprojektowanych i przetestowanych możliwości**. Nie powinno oznaczać dowolnego kodu, dowolnej integracji i tworzenia nowej logiki bez review. Pierwszy wariant jest przewidywalnym systemem; drugi próbą zbudowania kosztownej platformy no-code wewnątrz CMS-a.

## Priorytetyzacja wdrożenia pod najniższy koszt

### Etap 0 — discovery i migracja reprezentatywnej próbki

- inwentaryzacja obecnych typów, stron, locale, assetów, linków i redirectów;
- wybór 20–50 dokumentów obejmujących typowe oraz najtrudniejsze przypadki;
- docelowe modele i slices w Type Builderze;
- powtarzalny import do Migration Release;
- pomiar ręcznych poprawek, QA i strategii cutover;
- potwierdzenie planu na podstawie użytkowników, ról, locale i środowisk.

### Etap 1 — rdzeń o najwyższym zwrocie

- page types oraz 10–20 najczęstszych slices i wariantów;
- linki, nawigacja, UID-y i podstawowe redirecty;
- drafty, full-website preview, Releases i publikacja;
- SEO, obrazy, responsive oraz accessibility komponentów;
- formularze oparte na istniejącej platformie klienta;
- analityka kluczowych CTA;
- jedna strategia locale i jasna odpowiedzialność za publikację.

### Etap 2 — skalowanie operacji

- integracja Crowdin lub innego TMS;
- większa biblioteka slices oraz template'ów;
- spaces, tags i standardowe role od Medium;
- rejestr integracji per strona;
- automatyczne testy linków, eventów, mobile i accessibility;
- proste eksperymenty URL lub wybranych slotów;
- cykliczny eksport opublikowanej treści.

### Etap 3 — funkcje wymagające dowodu wartości

- wielowymiarowa personalizacja;
- custom roles i SSO;
- pełny zewnętrzny silnik wyszukiwania;
- szerokie AI content operations i osobno wyceniany landing page builder;
- arbitrary custom code;
- wiele repozytoriów lub środowisk;
- Enterprise backup/restore i osobny DAM.

## Pytania discovery przed wyceną

1. Które zmiany dziś najczęściej czekają na developera i ile trwa oczekiwanie?
2. Jakie 10–20 sekcji pokrywa większość istniejących i planowanych stron?
3. Kto może tworzyć, akceptować i publikować treść — czy potrzebne są role od planu Medium?
4. Ile repozytoriów naprawdę wymaga osobnego lifecycle, a ile serwisów może współdzielić repo i bibliotekę slices?
5. Ile locale istnieje dziś i za dwa lata, kto tłumaczy oraz czy rynki publikują niezależnie?
6. Czy wymagane są osobne content environments, a jeśli tak, do jakich zmian i testów?
7. Które integracje są obowiązkowe, a które tylko potencjalne?
8. Czy personalizacja i A/B testing mają zdefiniowane hipotezy, ruch i właściciela analizy?
9. Jakie dane osobowe przechodzą przez serwis i gdzie powinny być przechowywane?
10. Jakie są wymagania SSO, SLA, backupu, restore, retencji i audytu?
11. Co znajduje się w obecnym CMS-ie: liczba typów, dokumentów, locale, assetów, relacji i niestandardowych bloków?
12. Czy stary system daje kompletny eksport i czy można wprowadzić content freeze podczas cutover?
13. Które stare URL-e mają ruch lub backlinki i muszą otrzymać redirect 301?
14. Które funkcje pierwszego wydania zmienią wynik biznesowy, a które można odłożyć do zmierzenia wartości?

Odpowiedzi na te pytania zwykle obniżają koszt bardziej niż wybór pojedynczej biblioteki. Pozwalają dobrać właściwy plan, ograniczyć migrację do wartościowej treści i zbudować rdzeń, który marketing rzeczywiście wykorzysta.

## Źródła

- Prismic: [Pricing](https://prismic.io/pricing), [Visual Page Builder](https://prismic.io/docs/guides/page-builder), [Organize content](https://prismic.io/docs/guides/bulk-actions)
- Prismic: [Type Builder](https://prismic.io/docs/type-builder), [CLI](https://prismic.io/docs/cli), [Frameworks](https://prismic.io/docs/frameworks)
- Prismic: [Preview](https://prismic.io/docs/preview), [User roles](https://prismic.io/features/user-roles), [Spaces](https://prismic.io/updates/spaces)
- Prismic: [Localization](https://prismic.io/features/localization), [Image field and optimization](https://prismic.io/docs/fields/image), [Media Library](https://prismic.io/updates/new-media-library)
- Prismic: [Migration](https://prismic.io/docs/migration), [Migration API](https://prismic.io/docs/migration-api-technical-reference), [API limits](https://prismic.io/docs/api)
- Prismic: [MCP](https://prismic.io/docs/mcp), [AI features](https://prismic.io/features/ai), [Security](https://prismic.io/legal/security)
