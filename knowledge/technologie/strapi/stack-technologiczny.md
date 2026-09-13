# Technologie webowe, które warto łączyć ze Strapi

> **Rekomendacja w jednym zdaniu:** dla szerokiego zakresu nowoczesnego serwisu SaaS najlepszym domyślnym połączeniem jest **Strapi Cloud Pro + CMS Growth + Next.js + TypeScript**, natomiast **Strapi + Astro** jest bardziej ekonomicznym wyborem dla serwisów głównie treściowych; self-hosted warto wybrać wtedy, gdy klient ma już dojrzałą platformę i może przejąć operacje bez tworzenia nowego zespołu lub procesu.

Stan analizy i cen: **29 lipca 2026 r.** Dokument rozwija [`potrzeby-biznesowe-klienta.md`](./potrzeby-biznesowe-klienta.md), uzupełnia porównanie kosztów w [`co-wyroznia.md`](./co-wyroznia.md) i ocenia warianty względem referencyjnego zakresu pełnego serwisu SaaS (14 grup wymagań opisanych w `potrzeby-biznesowe-klienta.md`).

Wszystkie kwoty są cenami katalogowymi w USD, bez podatków, kosztu wdrożenia, dodatkowych miejsc, środowisk i zużycia ponad limity.

## Najpierw zasada kosztowa: dwa hostingi i najmniejszy potrzebny stack

Architektura Strapi ma dwie niezależne warstwy, które łatwo błędnie połączyć w jednym haśle „hosting strony”:

1. **backend CMS** — aplikacja Strapi, baza danych, assety i panel administratora, uruchomione w Strapi Cloud albo self-hosted;
2. **frontend** — publiczna strona w Next.js lub Astro, uruchomiona niezależnie na Vercel, Cloudflare albo hostingu statycznym.

Zakup Strapi Cloud nie hostuje frontendu. Z kolei Vercel lub Cloudflare dla strony nie zastępują hostingu długotrwale działającej aplikacji Strapi, bazy i storage assetów.

Każda dodatkowa technologia oznacza:

- kolejny abonament albo zasób infrastrukturalny;
- osobny deployment, monitoring i procedurę awarii;
- dodatkowe sekrety, role i zależności bezpieczeństwa;
- wpływ na performance, privacy i consent;
- aktualizacje oraz wiedzę, którą zespół musi utrzymywać;
- kolejne miejsce, w którym może rozjechać się kontrakt danych.

Ekonomiczny stack nie ma najmniejszej liczby narzędzi za wszelką cenę. Ma **najmniejszą liczbę narzędzi, które jasno rozdzielają odpowiedzialności i eliminują droższy custom development**.

## Rekomendowana architektura bazowa

| Warstwa | Rekomendowana technologia | Odpowiedzialność | Dlaczego jest opłacalna |
|---|---|---|---|
| CMS | **Strapi 5 Community lub Growth** | Content types, komponenty, Dynamic Zones, drafty, role, i18n, API i integracje backendowe | Open-source'owy rdzeń bez limitu treści na poziomie licencji; płatne funkcje tylko dla potrzebnego workflow |
| Hosting CMS | **Strapi Cloud Pro** albo **self-hosted na istniejącej platformie** | Runtime Node.js, baza, storage, backup, logi i dostępność | Cloud minimalizuje operacje; self-hosted wykorzystuje kontrolę i kompetencje klienta |
| Baza | **PostgreSQL** | Treść, relacje, konfiguracja i metadane Strapi | Najbezpieczniejszy domyślny wybór produkcyjny; szerokie wsparcie zarządzanych usług i narzędzi backupu |
| Assety | **storage Strapi Cloud** albo **S3-compatible storage + CDN** w self-hosted | Obrazy i pliki | Oddziela pliki od dysku instancji i pozwala skalować backend bez utraty assetów |
| Frontend | **Next.js lub Astro** | Routing, rendering, SEO, responsywność, integracje i zachowanie strony | Next.js pokrywa szeroką dynamikę; Astro obniża koszt dla content-first |
| Język | **TypeScript** w CMS-ie i frontendzie | Kontrakty modeli, API, komponentów i integracji | Wykrywa kosztowne błędy przed publikacją i ułatwia bezpieczne migracje schematu |
| API | **REST domyślnie; GraphQL warunkowo** | Pobieranie opublikowanej treści i draftów | REST nie wymaga dodatkowego pluginu; GraphQL opłaca się przy wielu złożonych konsumentach |
| UI | **React** dla Next.js; **komponenty Astro + wyspy React** dla Astro | Biblioteka sekcji, formularze i interakcje | Jeden design system ogranicza swobodę do bezpiecznych wariantów |
| Style | **jeden standard istniejący u klienta** | Tokeny, warianty i responsywność | Wprowadzanie drugiego systemu CSS zwykle nie daje zwrotu |
| Testy | **testy jednostkowe + Playwright + accessibility/performance CI** | Mappery API, preview, publikacja, formularze, locale i jakość strony | Automatyzacja chroni autonomię marketingu bez ręcznego QA każdej strony |
| Monitoring | **istniejące APM klienta lub Sentry** | Błędy CMS-a, frontendu i integracji | Jedna obserwowalność jest tańsza niż osobne dashboardy bez właściciela |

Nie każda pozycja musi wejść do pierwszego wydania. Osobny katalog komponentów, rozbudowane visual regression i zewnętrzne wyszukiwanie uzasadnia skala projektu, ale TypeScript, monitoring produkcji, test preview oraz test formularza zwracają się szybko.

## Minimalne koszty katalogowe wariantów

| Wariant | Minimum miesięczne | Co obejmuje | Czego nie obejmuje |
|---|---:|---|---|
| **PoC: Cloud Starter + Community** | **$35 + frontend** | Jedno środowisko CMS, standardowy Preview, podstawowy model i API | Backupów Cloud, always-on, Live Preview, Releases i historii |
| **Managed production: Cloud Pro + Community + Vercel Pro** | **$110** | Zarządzany CMS z backupami i dynamiczny frontend Next.js | Płatnego workflow CMS, dodatkowego środowiska i nadwyżek |
| **Rekomendowany full scope: Cloud Pro + Growth + Vercel Pro** | **$155** | Hosting CMS, 3 miejsca Growth, Live Preview, Releases, historia i frontend | Dodatkowego środowiska CMS, kolejnych miejsc, SSO i Enterprise |
| **Full scope + dodatkowe środowisko Cloud** | **$215** | Jak wyżej plus drugie środowisko CMS w Cloud Pro | Dalszych środowisk, nadwyżek i funkcji Enterprise |
| **Business + Growth + Vercel Pro** | **$515** | Dwa środowiska CMS, codzienne backupy, 99,9% SLA i płatny workflow | Enterprise CMS, kolejnych miejsc oraz zużycia ponad limity |
| **Self-hosted Growth + Vercel Pro** | **$65 + infrastruktura CMS** | Licencja Growth i frontend | Bazy, compute, storage, CDN, backupów, monitoringu i pracy operacyjnej |
| **Self-hosted Community + Cloudflare Workers** | **od $5 + infrastruktura CMS** | Najniższy katalogowy koszt płatnego frontendu | Całego TCO CMS oraz płatnych funkcji redakcyjnych |

Vercel Pro kosztuje obecnie **$20/mies.**, zawiera jedno miejsce developerskie oraz $20 kredytu zużycia; kolejne miejsca developerskie kosztują $20/mies. Workers Paid ma bazową opłatę **$5/mies.**, obejmuje 10 mln requestów i 30 mln ms CPU, a requesty do statycznych assetów są bezpłatne i nielimitowane. Szczegóły zmieniają się niezależnie od Strapi, dlatego model 12-miesięczny powinien używać aktualnych cenników [Vercel](https://vercel.com/pricing) i [Cloudflare Workers](https://developers.cloudflare.com/workers/platform/pricing/).

Podane minima służą do porównania architektury, nie do wyceny projektu. Największymi brakującymi pozycjami są implementacja i migracja, a w self-hosted również czas DevOps/SRE.

## Hosting CMS: Strapi Cloud czy self-hosted?

### Strapi Cloud — najmniejszy koszt organizacyjny

Cloud uruchamia własną aplikację Strapi jako zarządzany PaaS. Baza, deployment, storage assetów, CDN i podstawowa obserwowalność są częścią planu hostingowego. Kod projektu nadal znajduje się w repozytorium i może zawierać własne rozszerzenia.

**Najlepiej pokrywa:**

- szybki start bez budowania osobnej platformy CMS;
- mały lub średni zespół bez stałego DevOps dla projektu;
- przewidywalny profil ruchu i assetów;
- standardowy deployment z Git i kilka kontrolowanych środowisk;
- potrzebę oficjalnego wsparcia oraz jednej odpowiedzialności za hosting Strapi.

**Koszt i ryzyka:**

- hosting i funkcje CMS są osobnymi rachunkami;
- Pro zawiera jedno środowisko, a kolejne kosztuje $60/mies.;
- limity API, storage i transferu generują nadwyżki;
- plan musi pokrywać wymagany backup, retencję i SLA;
- nietypowe wymagania sieciowe lub infrastrukturalne mogą wykraczać poza platformę;
- frontend nadal wymaga osobnego hostingu i monitoringu.

**Rekomendacja:** Starter dla PoC; Pro jako punkt wyjścia dla krytycznego serwisu; Business dopiero wtedy, gdy dzienne backupy, dwa środowiska i 99,9% SLA są wymaganiem, a nie oczekiwaniem „na przyszłość”.

### Self-hosted — kontrola opłacalna przy gotowej platformie

Self-hosted pozwala uruchomić Strapi w koncie chmurowym, data center lub sieci klienta. Produkcyjna architektura powinna traktować aplikację jako oddzielny backend Node.js z trwałą bazą i zewnętrznym storage assetów, nie jako część deploymentu frontendu.

Minimalny zakres operacyjny obejmuje:

- uruchomienie i skalowanie procesu Strapi;
- PostgreSQL z backupem, monitoringiem i planem odtworzenia;
- S3-compatible storage, CDN oraz kopie assetów;
- reverse proxy, TLS, domeny, health checks i ochronę sieciową;
- zarządzanie sekretami, tokenami, e-mailem i uprawnieniami;
- logi, metryki, alerty i reagowanie na incydenty;
- aktualizacje Strapi, Node.js, bazy i pluginów;
- bezpieczny deployment zmian schematu oraz rollback;
- osobne środowiska i procedurę synchronizacji danych;
- okresowe testy disaster recovery.

**Najlepiej pokrywa:** wymagania data residency, private networking, on-prem, izolację, własne klucze, niestandardowe providery i organizacje z istniejącym platform teamem.

**Koszt i ryzyka:** niska cena compute nie obejmuje pracy ludzi. Własna infrastruktura jest ekonomiczna wtedy, gdy Strapi korzysta z istniejących standardów, a nie tworzy jednorazowy wyjątek utrzymywany przez autora projektu.

### Czego nie łączyć

Nie należy próbować uruchamiać całego Strapi jako Route Handlera Next.js albo funkcji frontendu. CMS ma własny panel, backend, pluginy, proces build/start, połączenia z bazą i lifecycle. Frontend oraz CMS powinny mieć oddzielne deploymenty, domeny, sekrety i skalowanie.

Można trzymać oba projekty w monorepo, jeśli zespół tego potrzebuje, ale monorepo nie oznacza wspólnego runtime'u. W małym zespole osobne repozytoria bywają tańsze operacyjnie, bo uprawnienia i pipeline'y są prostsze.

## REST, Strapi Client czy GraphQL?

### REST — rekomendowany punkt wyjścia

Strapi automatycznie generuje REST API dla content types. Dla pojedynczej strony marketingowej jest to zwykle najtańsza opcja: nie wymaga dodatkowego pluginu, łatwo ją cache'ować, debugować i wywoływać podczas builda lub renderowania.

Trzeba jednak świadomie zarządzać `populate`, filtrami, polami, locale i statusem draft/published. Jeden współdzielony moduł zapytań powinien budować wymagane parametry i mapować odpowiedzi na komponenty. Unika się dzięki temu zarówno brakujących relacji, jak i kosztownego pobierania całego grafu danych.

### Oficjalny Strapi Client — wygoda, nie obowiązek

[Strapi Client](https://docs.strapi.io/cms/api/client) upraszcza typowe operacje JavaScript/TypeScript. Warto go rozważyć, gdy kilka aplikacji wykonuje podobny CRUD albo zespół chce jeden interfejs do API.

Dla server-rendered frontendu zwykły `fetch` może pozostać prostszy, ponieważ bezpośrednio współpracuje z mechanizmem cache i rewalidacji frameworka. Nie należy dodawać klienta tylko po to, aby opakować jedno lub dwa odczyty.

### GraphQL — dopiero przy konkretnej korzyści

GraphQL jest oficjalnym pluginem Strapi. Ma sens, gdy wiele ekranów potrzebuje różnych kształtów danych, zespół ma dojrzałe narzędzia GraphQL albo kontrakt jest współdzielony przez kilka złożonych produktów.

Kosztem są dodatkowy plugin, schemat, zapytania, ochrona przed drogimi operacjami, obserwowalność i testowanie. Dla jednego serwisu marketingowego REST z kontrolowanym `populate` jest zwykle tańszy.

## Next.js czy Astro?

### Next.js — największe pokrycie pełnego zakresu

Next.js App Router łączy statyczne generowanie, ISR, rendering na żądanie, Route Handlers, Server Actions, Draft Mode, redirecty, warstwę requestową i ekosystem React.

Strapi konfiguruje Preview przez handler zwracający URL frontendu. Dokumentacja [Strapi Preview](https://docs.strapi.io/cms/features/preview) pokazuje integrację z Next.js Draft Mode. Publikacja może uruchomić webhook do chronionego Route Handlera, który wywołuje rewalidację tagu lub ścieżki. Dzięki temu większość publicznego ruchu korzysta z cache, a zmiana treści nie wymaga pełnego deployu.

**Najlepiej pokrywa:**

- natychmiastową publikację i selektywną rewalidację;
- bezpieczny Preview draftów oraz Live Preview Growth;
- personalizację, feature flags i eksperymenty per request;
- formularze wymagające sekretów, walidacji serwerowej i antyspamu;
- hybrydowe strony cenowe łączące CMS z danymi produktu;
- interaktywne komponenty React i rozbudowane visitor journeys;
- redirecty i logikę locale zależną od requestu;
- jeden spójny stack dla marketingu oraz części aplikacyjnej.

**Koszt i ryzyka:**

- cache, drafty i rewalidacja wymagają świadomej architektury;
- łatwo wysłać zbyt dużo JavaScriptu przez nadmierną liczbę Client Components;
- dynamiczne ścieżki zwiększają compute i powierzchnię monitoringu;
- Vercel minimalizuje ryzyko zgodności, ale rozlicza miejsca i użycie;
- Cloudflare wymaga adaptera OpenNext oraz testów po aktualizacji Next.js;
- frontend nie powinien przekazywać prywatnego tokenu Strapi do przeglądarki.

### Next.js ze statycznym eksportem — tani frontend kosztem publikacji

`output: 'export'` generuje HTML, CSS i JavaScript bez runtime'u Node.js. Strona może pobrać opublikowaną treść ze Strapi podczas builda i działać na dowolnym hostingu statycznym.

| Możliwość | Skutek statycznego eksportu | Typowe obejście |
|---|---|---|
| Publikacja treści | HTML pozostaje stary do kolejnego builda | Webhook Strapi uruchamia pełny build i deployment |
| Nowa strona | Nie istnieje, dopóki build nie wygeneruje jej sluga | Automatyczny rebuild po publikacji |
| Draft Mode i bezpieczny Preview | Brak runtime'u do pobrania draftu z sekretem | Osobna dynamiczna aplikacja preview |
| Live Preview | Czysty static export nie ma bezpiecznej trasy draftów | Dynamiczne preview albo rezygnacja z Live Preview |
| Personalizacja na request | Brak cookies, nagłówków i sesji podczas renderowania | Client-side lub zewnętrzna warstwa edge |
| Formularze z sekretami | Brak Server Actions i dynamicznych Route Handlers | Zewnętrzny formularz lub osobny endpoint |
| Redirecty i headers Next.js | Nie wykonują się w runtime | Reguły hostingu/CDN |
| Domyślna optymalizacja obrazów | Brak serwera Image Optimizer | Zewnętrzny image CDN/loader albo przygotowane warianty |

Największą oszczędnością jest tani hosting, ale największą stratą — pętla publikacji. Koszt builda rośnie z liczbą stron i locale. Jeżeli każda poprawka uruchamia długi build, rachunek CI i czas redaktora mogą przewyższyć oszczędność runtime'u.

Statyczny eksport ma sens dla małego bloga, dokumentacji, microsite'u lub katalogu aktualizowanego rzadko. Nie jest rekomendowany dla pełnego zakresu referencyjnego, który wymaga płynnego preview, personalizacji, testów, formularzy i stron hybrydowych. Aktualne ograniczenia utrzymuje dokumentacja [Next.js Static Exports](https://nextjs.org/docs/app/guides/static-exports).

### Astro — najniższy koszt dla content-first

Astro domyślnie generuje statyczny HTML i dodaje JavaScript tylko do wybranych „wysp” interaktywności. Może też renderować wybrane strony na żądanie po dodaniu adaptera. [Islands architecture](https://docs.astro.build/en/concepts/islands/) dobrze pasuje do stron marketingowych, dokumentacji, blogów i katalogów.

Strapi integruje się przez REST, GraphQL albo klienta, tak samo jak z innymi frontendami. Standardowy Preview może wskazywać trasę Astro, ale bezpieczne drafty i Live Preview wymagają dynamicznej trasy lub osobnego środowiska. Ten pion trzeba sprawdzić w PoC, zwłaszcza jeżeli płynność redakcji jest kryterium wyboru Growth.

**Najlepiej pokrywa:**

- publiczne strony marketingowe i landing pages;
- blog, help center, dokumentację i katalog template'ów;
- SEO/AEO oparte na indeksowalnym HTML-u;
- bardzo małą ilość JavaScriptu na stronie;
- tani hosting statyczny i odporność na skoki ruchu;
- kilka izolowanych interakcji React bez hydratacji całej strony.

**Koszt i ryzyka:**

- natychmiastowa publikacja statycznych stron wymaga build hooka;
- dynamiczny Preview wymaga adaptera i runtime'u;
- personalizacja server-side zmienia prosty model statyczny w aplikację SSR;
- wiele wysp React może odtworzyć złożoność aplikacji w mniej spójnym modelu;
- zaawansowane formularze i integracje są możliwe, ale Next.js ma szerszy ekosystem gotowych wzorców;
- rosnący zakres dynamiczny może zniwelować początkową przewagę kosztową.

## Porównanie pod kątem referencyjnego zakresu wymagań

Ocena jest jakościowa: **bardzo dobre** oznacza naturalne pokrycie mechanizmami stacku; **dobre** — dodatkową, przewidywalną implementację; **warunkowe** — możliwość wymagającą zmiany prostego modelu albo usługi zewnętrznej.

| Grupa wymagań | Strapi + Next.js | Strapi + Astro | Komentarz kosztowy |
|---|---|---|---|
| Ownership marketingu i strony | **bardzo dobre** | **bardzo dobre** | Zależy głównie od Dynamic Zones i jakości biblioteki sekcji |
| Routing, URL-e i redirecty | **bardzo dobre** | **dobre** | Next.js naturalniej obsługuje logikę per request |
| Page building i komponenty | **bardzo dobre** | **bardzo dobre** | Ten sam model Strapi; różni się implementacja frontendu |
| Mobile i wysokie rozdzielczości | **bardzo dobre** | **bardzo dobre** | Odpowiada design system i CSS, nie CMS |
| Template pages i listingi | **bardzo dobre** | **bardzo dobre** | Astro ma przewagę dla statycznych katalogów |
| Crowdin i lokalizacja | **dobre** | **dobre** | Koszt leży w workflow tłumaczeń i routingu locale |
| HubSpot/GetResponse forms | **bardzo dobre** | **dobre** | Embedy są proste w obu; własny backend naturalniejszy w Next.js |
| Nawigacja i breadcrumbs | **bardzo dobre** | **bardzo dobre** | Generowane z relacji oraz slugów Strapi |
| Motion, embedy i custom components | **bardzo dobre** | **dobre** | React pokrywa szeroki zakres; Astro ogranicza JS przez islands |
| Integracje per strona | **bardzo dobre** | **dobre** | Oba mogą lazy-loadować adaptery; Next lepiej znosi rosnącą dynamikę |
| Personalizacja i visitor journeys | **bardzo dobre** | **warunkowe** | Najmocniejszy argument za Next.js w pełnym zakresie |
| A/B testing i analytics | **bardzo dobre** | **dobre** | Client-side działa w obu; server/edge łatwiejsze w Next.js |
| SEO, structured data i LLM readiness | **bardzo dobre** | **bardzo dobre** | Astro łatwiej utrzymuje minimalny JS; oba generują poprawny HTML |
| AI-assisted workflows | **dobre** | **dobre** | Workflow działa przez Strapi API; frontend jest drugorzędny |
| Security i auth frontendu | **bardzo dobre** | **dobre** | Role CMS zapewnia Strapi; runtime Next.js ma więcej gotowych wzorców |
| Draft, Preview i Live Preview | **bardzo dobre** | **dobre/warunkowe** | Next.js Draft Mode jest udokumentowany przez Strapi; Astro wymaga PoC |

### Ocena dla pełnego zakresu referencyjnego

Przy zachowaniu całego zakresu **Next.js jest sensowniejszym wyborem**. Nie decydują zwykłe strony marketingowe, bo oba frameworki obsłużą je dobrze, lecz suma potrzeb dynamicznych:

- personalizacja sekcji i CTA na podstawie sygnałów użytkownika;
- VWO/Amplitude i przyszłe feature flags per strona;
- interaktywne hero i komponenty React;
- formularze oraz integracje wymagające bezpiecznej logiki serwerowej;
- hybrydowe strony cenowe łączące CMS z warstwą produktu;
- Draft Mode, Live Preview i selektywna rewalidacja;
- pozostawienie miejsca na przyszłe programatyczne workflow.

Astro jest lepsze kosztowo, gdy pierwsza faza ogranicza się do treści, lokalizacji, SEO, formularzy embedowanych i kilku izolowanych interakcji. Nie warto wybierać Astro wyłącznie dla niższego rachunku hostingowego, jeśli różnica zostanie wydana na customową obsługę rosnącego runtime'u.

## Czy łączyć Next.js i Astro z jednym Strapi?

Technicznie Strapi może zasilać oba. Biznesowo ma to sens, gdy są to oddzielne produkty o innym profilu:

- główna platforma marketingowa w Next.js;
- dokumentacja, blog lub help center w Astro;
- izolowane microsites kampanijne w Astro.

Nie rekomenduje się dwóch frameworków dla jednego spójnego serwisu na początku. Powstają dwa routingi, dwa preview, dwa mappery Dynamic Zones, dwa zestawy testów i dwa pipeline'y wdrożeniowe. Oszczędność hostingu zwykle nie pokrywa kosztu zespołu.

**Reguła:** jeden frontend na jeden spójny obszar odpowiedzialności. Drugi framework dopiero wtedy, gdy niezależność produktu, zespołu lub profilu wydajności uzasadnia osobny lifecycle.

## Rekomendowany stack dla pełnego serwisu SaaS

### Rdzeń

1. **Strapi Cloud Pro + CMS Growth** jako bazowy wariant zarządzany; Community do PoC albo prostszego workflow.
2. **Next.js App Router + TypeScript** jako frontend pełnego zakresu.
3. **REST API przez server-side `fetch`** jako domyślny kontrakt; GraphQL lub Strapi Client dopiero po wykazaniu korzyści.
4. **PostgreSQL** oraz zewnętrzny storage assetów w self-hosted; zasoby zarządzane przez plan w Cloud.
5. **React** dla zamkniętej biblioteki sekcji i interaktywnych komponentów.
6. **Jeden istniejący standard stylowania** oraz katalog komponentów, jeśli biblioteka jest rozwijana przez kilka zespołów.

### Content operations

- content types `page`, `navigation`, `redirect`, `formReference`, `integrationConfig` oraz modele domenowe;
- Dynamic Zone z ograniczoną listą sekcji implementowanych we frontendzie;
- Draft & Publish oraz Preview skonfigurowane dla właściwych typów;
- Live Preview i Releases w Growth, jeśli wynikają z procesu redakcyjnego;
- minimalny RBAC i osobne tokeny read-only, preview, webhook oraz migracyjne;
- jedna strategia lokalizacji oraz Crowdin po ustabilizowaniu schematów;
- webhook podpisany sekretem, który rewaliduje wyłącznie zmienione strony;
- regularny eksport i test odtworzenia niezależnie od historii treści.

### Kontrakt API i typy

- generować typy Strapi dla kodu backendu przez oficjalne narzędzia TypeScript;
- we frontendzie utrzymywać jawne typy widoków i mapper API → komponent;
- nie przekazywać surowej odpowiedzi Strapi przez całą aplikację;
- centralizować `populate`, fields, locale, status i obsługę paginacji;
- wersjonować zmiany schematu razem z kodem;
- posiadać fallback dla nieznanego komponentu Dynamic Zone, aby jeden błędny wpis nie wyłączał całej strony;
- testować zgodność modeli na CI przed deploymentem CMS-a i frontendu.

### Design system i page building

- sekcje implementowane w kodzie, konfigurowane w Strapi;
- ograniczona lista wariantów chroniąca design system;
- komponenty responsywne z bezpiecznymi defaultami;
- żadnego pola na arbitrary CSS lub JavaScript;
- Preview desktop/mobile i automatyczne testy dostępności;
- walidacja CTA, linków, alt textów i wymaganych eventów;
- migracja starego layoutu do komponentów docelowych, a nie odtwarzanie HTML-a źródłowego 1:1.

### Formularze i CRM

Najtańsza kolejność:

1. referencja do istniejącego formularza HubSpot/GetResponse w Strapi;
2. adapter frontendu i zarządzany thank-you page;
3. wspólne mapowanie eventów analitycznych;
4. własny Route Handler dopiero wtedy, gdy embedy nie spełniają wymagań walidacji, antyspamu, consent lub UX.

CMS nie powinien przechowywać leadów. Pozostają w systemie CRM lub marketing automation.

### Analityka, eksperymenty i personalizacja

- wykorzystać VWO lub Amplitude już obecne u klienta;
- Strapi przechowuje tylko zatwierdzone warianty, identyfikatory i bezpieczną konfigurację;
- SDK odpowiada za alokację wariantu i exposure events;
- event taxonomy żyje w kodzie lub wersjonowanym rejestrze;
- personalizację zacząć od sygnałów o wysokiej wartości, np. locale i campaign source;
- ciężkie SDK ładować po zgodzie i tylko na stronach, na których są potrzebne;
- nie wykonywać per-user personalizacji w publicznym API Strapi.

### Migracja z innego CMS-a

- inwentaryzacja content types, pól, relacji, locale, assetów, URL-i i integracji;
- jawna mapa źródło → docelowy model Strapi;
- skrypt ETL uruchamiany poza frontendem, idempotentny i generujący raport;
- migracja assetów do docelowego providera przed finalnym cutover;
- zachowanie relacji, alt textów, statusów i kolejności Dynamic Zones;
- mapa redirectów oraz testy SEO przed zmianą DNS/routingu;
- migracja próbna, delta migration, krótkie okno zamrożenia i rollback;
- backup celu przed każdym destrukcyjnym importem;
- natywne `export`, `import` i `transfer` tylko dla zgodnych instancji Strapi.

### Testy i jakość

- testy jednostkowe mapperów sekcji, helperów SEO i reguł routingu;
- Playwright dla Preview, publikacji, formularzy, locale i najważniejszych ścieżek;
- automatyczne testy podstawowej dostępności;
- budżety performance dla reprezentatywnych template'ów;
- visual regression, jeśli liczba wariantów i tempo zmian to uzasadniają;
- test eventów analytics przed publikacją;
- smoke test CMS API oraz frontendu po każdym deploymencie;
- test odtworzenia bazy i assetów, nie tylko sprawdzenie obecności backupu.

## Hosting frontendu: najniższy rachunek czy najniższy TCO?

### Next.js na Vercel

To wariant o najmniejszym ryzyku integracyjnym. Next.js działa bez adaptera, a platforma zapewnia preview deployments, cache, ISR, funkcje, image optimization i rollback. Pro kosztuje obecnie **$20/mies.**, zawiera $20 kredytu zużycia i jedno miejsce developerskie; kolejne miejsca kosztują $20/mies.

**Wybierać, gdy:** szybkość wdrożenia, sprawdzony Draft Mode, rewalidacja i minimalne ryzyko zespołu są ważniejsze niż najniższy możliwy rachunek infrastrukturalny.

**Uważać na:** compute, transfer, obrazki, buildy, dodatkowe miejsca i płatne dodatki. Cache zmniejsza użycie funkcji, ale nie usuwa wszystkich pozycji rachunku.

### Next.js na Cloudflare Workers

Cloudflare wdraża Next.js przez [adapter OpenNext](https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/). Aktualnie obsługuje App Router, Server Components, SSG, SSR, ISR, Server Actions, streaming i większość funkcji, ale nie jest runtime'em macierzystym Next.js.

Workers Paid kosztuje bazowo **$5/mies.**, obejmuje 10 mln requestów i 30 mln ms CPU; requesty do statycznych assetów są bezpłatne i nielimitowane. Jest to atrakcyjny model dla publicznej strony z wysokim udziałem cache.

**Wybierać, gdy:** zespół zna Cloudflare, chce obniżyć powtarzalny koszt i akceptuje spike oraz testy zgodności po aktualizacji frameworka.

**Spike powinien objąć:** Draft Mode Strapi, Live Preview, webhook revalidation, image optimization, redirecty, locale, używane SDK marketingowe oraz maksymalny czas/CPU najcięższych tras.

### Astro na hostingu statycznym lub Workers

Astro domyślnie pre-renderuje strony, więc statyczny wariant może być bardzo tani. Czyste assety można wdrożyć bez adaptera; on-demand rendering wymaga adaptera, np. [Astro dla Cloudflare Workers](https://developers.cloudflare.com/workers/framework-guides/web-apps/astro/).

**Wybierać, gdy:** większość stron jest publiczna, wspólna dla użytkowników i może aktualizować się przez build hook. Jeżeli potrzebne są drafty, sesja lub personalizacja, należy policzyć runtime oraz utrzymanie dynamicznych tras.

### Reguła TCO

Różnica kilkunastu lub kilkudziesięciu dolarów miesięcznie jest mała wobec kilku dodatkowych dni developmentu. Tańszy frontend wygrywa wtedy, gdy:

- runtime jest znany zespołowi;
- pokrywa Preview, rewalidację i formularze bez obejść;
- ma monitoring i kontrolę kosztów;
- nie komplikuje migracji ani codziennej pracy marketingu;
- oszczędność powtarza się przez wystarczająco długi okres lub dużą skalę.

## Technologie opcjonalne — dodawać dopiero po spełnieniu warunku

| Technologia / kategoria | Dodaj, gdy | Nie dodawaj, gdy |
|---|---|---|
| **GraphQL** | Kilku konsumentów potrzebuje różnych, złożonych kształtów danych | Jeden frontend dobrze obsługuje REST |
| **Strapi Client** | Wiele aplikacji powtarza te same operacje CRUD | Server-side `fetch` i cache frameworka są prostsze |
| **Crowdin** | Istnieje wiele locale i formalny proces tłumaczeń | Tłumaczenia są sporadyczne lub schemat nadal się zmienia |
| **VWO/Amplitude Experiment** | Jest ruch, hipoteza, owner i proces analizy | A/B testing jest tylko pozycją na roadmapie |
| **Algolia/Typesense** | API Strapi nie zapewnia wymaganej jakości full-text, facetingu lub skali | Wystarczą filtry po ustrukturyzowanych polach |
| **Sentry / dodatkowe APM** | Istniejące narzędzia nie pokrywają błędów CMS-a i frontendu | Klient ma już wspólną obserwowalność |
| **Katalog komponentów** | Biblioteka sekcji jest współdzielona i rozwijana regularnie | Projekt ma kilka stabilnych komponentów |
| **Biblioteka motion** | Wiele sekcji używa jednego systemu animacji | Wystarczą przejścia CSS |
| **Feature flag service** | Potrzebne są rollouty i server-side experiments | Flagi byłyby trwałą konfiguracją treści |
| **Osobny backend/BFF** | Potrzebna jest agregacja wielu systemów, kolejki lub inny lifecycle niż frontend | Strapi, Route Handlers i istniejące SaaS-y pokrywają przypadek |
| **Dodatkowy DAM** | Prawa, workflow assetów i wiele marek przekraczają Media Library | Potrzebne jest zwykłe przechowywanie obrazów i plików |
| **Redis/cache przy Strapi** | Pomiary pokazują problem wymagający współdzielonego cache lub koordynacji | CDN i cache frontendu już usuwają obciążenie |

## Czego nie budować w pierwszej wersji

- uniwersalnego edytora dowolnego layoutu;
- pola do wklejania arbitrary JavaScriptu lub CSS-u;
- własnego systemu A/B testingu;
- własnej platformy formularzowej, jeśli HubSpot/GetResponse działa;
- drugiego backendu bez odpowiedzialności wykraczającej poza Strapi i frontend;
- GraphQL tylko dlatego, że projekt jest headless;
- zewnętrznego wyszukiwania bez wymagań wykraczających poza filtry Strapi;
- dwóch frameworków frontendowych dla tych samych stron;
- mikrofrontendów bez niezależnych zespołów i lifecycle;
- Redis, kolejki lub Kubernetes „na przyszłość” bez pomiarów;
- AI publikującego bez draftu, walidacji i akceptacji człowieka;
- self-hostingu bez właściciela aktualizacji, backupu i incydentów.

Każdy z tych elementów może kiedyś być uzasadniony. Żaden nie jest warunkiem rozpoczęcia autonomicznej pracy marketingu.

## Rekomendowane warianty wdrożenia

### Wariant A — maksymalne pokrycie use case'ów

**Strapi Cloud Pro + CMS Growth + Next.js + TypeScript + Vercel Pro**

Najlepszy dla zakresu podobnego do referencyjnego. Minimalizuje ryzyko operacyjne CMS-a i czas implementacji Draft Mode, Live Preview, rewalidacji, formularzy, personalizacji oraz eksperymentów. Minimum katalogowe to **$155/mies.**, a z drugim środowiskiem CMS — **$215/mies.**, przed dodatkowymi miejscami i użyciem.

### Wariant B — zarządzany CMS bez płatnego workflow

**Strapi Cloud Pro + Community + Next.js + TypeScript + Vercel Pro**

Kosztuje katalogowo od **$110/mies.** i zachowuje zarządzane backupy oraz dynamiczny frontend. Ma sens, jeśli standardowy Preview, Draft & Publish i RBAC wystarczają, a Live Preview, Releases i Content History nie mają jeszcze uzasadnienia biznesowego.

### Wariant C — kosztowo zoptymalizowany pełny stack

**Strapi Cloud Pro + Growth + Next.js + TypeScript + Cloudflare Workers**

Obniża minimum frontendu do bazowego planu Workers, ale wymaga spike'u OpenNext. Jest opłacalny dla zespołu znającego Cloudflare i gotowego utrzymywać testy kompatybilności.

### Wariant D — self-hosted z pełną kontrolą

**Strapi Growth self-hosted + PostgreSQL + object storage/CDN + Next.js + TypeScript**

Ma sens przy obowiązkowym regionie danych, private network lub gotowej platformie klienta. Licencja i Vercel zaczynają się od **$65/mies.**, lecz rzeczywisty koszt wyznaczają infrastruktura, środowiska, backup, monitoring, aktualizacje i dyżury. Bez gotowej platformy wariant zwykle nie jest tańszy od Cloud Pro.

### Wariant E — najniższy koszt content-first

**Strapi Community + Astro + TypeScript + hosting statyczny**

Najlepszy dla bloga, dokumentacji, katalogu albo prostego serwisu marketingowego. Frontend może kosztować symbolicznie, ale CMS nadal wymaga Cloud Starter/Pro albo self-hostingu. Publikacja odbywa się przez build hook, a dynamiczny Preview trzeba zaprojektować osobno.

### Wariant F — proof of concept

**Strapi Cloud Starter + Community + docelowy framework**

PoC powinien sprawdzić pełny pion: model strony, 3–5 sekcji Dynamic Zone, Preview, jeden formularz, dodatkowy locale, SEO, webhook publikacji i próbny import. Nie należy prototypować w innym frameworku niż planowany produkcyjnie — pozorna oszczędność kończy się ponowną implementacją.

## Ostateczna rekomendacja dla pełnego zakresu referencyjnego

1. Wybrać **Strapi Cloud Pro + CMS Growth + Next.js + TypeScript** jako bazowy wariant decyzyjny.
2. Rozpocząć od Vercel Pro, jeśli priorytetem są czas realizacji i najmniejsze ryzyko; Cloudflare rozważyć po spike'u, jeśli powtarzalny koszt frontendu ma znaczenie.
3. Utrzymać CMS i frontend jako dwa osobne deploymenty z niezależnymi sekretami, monitoringiem i skalowaniem.
4. Użyć REST i server-side `fetch` jako domyślnej integracji; GraphQL lub Strapi Client dodać dopiero dla konkretnego przypadku.
5. Zbudować zamkniętą bibliotekę sekcji Dynamic Zone z bezpiecznymi wariantami, Preview i responsywnymi defaultami.
6. HubSpot/GetResponse, Crowdin i VWO/Amplitude integrować jako systemy wyspecjalizowane, nie odtwarzać ich funkcji w Strapi.
7. Przed finalną wyceną wykonać migrację próbną wraz z assetami, relacjami, locale, raportem i redirectami.
8. Self-hosted wybrać tylko po potwierdzeniu platform ownera, RPO/RTO, kosztu środowisk oraz odpowiedzialności za aktualizacje i incydenty.
9. Astro pozostawić dla osobnego help center, dokumentacji lub microsites albo dla świadomie ograniczonego wariantu content-first.

To podejście pokrywa pełny kierunek biznesowy, a koszt utrzymuje pod kontrolą przez trzy decyzje podejmowane osobno: plan funkcji CMS, hosting backendu oraz runtime frontendu.

## Źródła

- Strapi: [CMS Pricing](https://strapi.io/pricing-cms), [Cloud Pricing](https://strapi.io/pricing-cloud), [Self-hosting](https://strapi.io/hosting)
- Strapi: [Deployment](https://docs.strapi.io/cms/deployment), [Preview](https://docs.strapi.io/cms/features/preview), [Webhooks](https://docs.strapi.io/cms/backend-customization/webhooks)
- Strapi: [REST API](https://docs.strapi.io/cms/api/rest), [GraphQL API](https://docs.strapi.io/cms/api/graphql), [Strapi Client](https://docs.strapi.io/cms/api/client)
- Strapi: [TypeScript](https://docs.strapi.io/cms/typescript), [Data Management](https://docs.strapi.io/cms/features/data-management), [Media Library](https://docs.strapi.io/cms/features/media-library)
- Next.js: [App Router](https://nextjs.org/docs/app), [Draft Mode](https://nextjs.org/docs/app/guides/draft-mode), [ISR](https://nextjs.org/docs/app/guides/incremental-static-regeneration), [Static Exports](https://nextjs.org/docs/app/guides/static-exports)
- Astro: [Islands architecture](https://docs.astro.build/en/concepts/islands/), [On-demand rendering](https://docs.astro.build/en/guides/on-demand-rendering/), [Strapi guide](https://docs.astro.build/en/guides/cms/strapi/)
- Cloudflare: [Next.js on Workers](https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/), [Astro on Workers](https://developers.cloudflare.com/workers/framework-guides/web-apps/astro/), [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/)
- Vercel: [Next.js](https://vercel.com/docs/frameworks/full-stack/nextjs), [Pricing](https://vercel.com/pricing), [Pro plan](https://vercel.com/docs/plans/pro-plan)
