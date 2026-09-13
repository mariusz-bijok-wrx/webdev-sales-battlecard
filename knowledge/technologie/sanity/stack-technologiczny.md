# Technologie webowe, które warto łączyć z Sanity

> **Rekomendacja w jednym zdaniu:** dla szerokiego zakresu nowoczesnego serwisu SaaS najlepszym domyślnym połączeniem jest **Sanity + Next.js + TypeScript**, natomiast **Sanity + Astro** jest bardziej ekonomicznym wyborem dla serwisów głównie treściowych, w których szybkość, prostota i niski koszt hostingu są ważniejsze niż rozbudowana personalizacja oraz logika aplikacyjna.

Stan analizy: **27 lipca 2026 r.** Dokument rozwija mapę potrzeb z [`potrzeby-biznesowe-klienta.md`](./potrzeby-biznesowe-klienta.md) i ocenia warianty względem referencyjnego zakresu pełnego serwisu SaaS (14 grup wymagań opisanych w `potrzeby-biznesowe-klienta.md`).

## Najpierw zasada kosztowa: najmniejszy stack, który pokrywa realny zakres

Sanity powinno być systemem rekordowym dla treści, konfiguracji redakcyjnej i relacji między dokumentami. Nie warto dokładać technologii tylko dlatego, że jest popularna. Każda nowa usługa oznacza:

- kolejną umowę i abonament;
- integrację, monitoring i procedurę awarii;
- dodatkowy model uprawnień oraz sekretów;
- wpływ na performance, privacy i consent;
- wiedzę, którą zespół musi utrzymywać;
- potencjalną niespójność danych.

Ekonomiczny stack nie ma najmniejszej liczby narzędzi za wszelką cenę. Ma **najmniejszą liczbę narzędzi, które jasno rozdzielają odpowiedzialności i eliminują kosztowny custom development**.

## Rekomendowana architektura bazowa

| Warstwa | Rekomendowana technologia | Odpowiedzialność | Dlaczego jest opłacalna |
|---|---|---|---|
| Treść i CMS | **Sanity Content Lake + Studio** | Modele treści, strony, komponentowa konfiguracja, assety, drafty, role, preview | Jedno źródło treści dla wielu stron i kanałów; niski koszt wejścia |
| Frontend | **Next.js lub Astro** | Routing, rendering, SEO, responsywność, interakcje, integracje | Oba mają oficjalne ścieżki integracji z Sanity; wybór zależy od dynamiki serwisu |
| Język | **TypeScript** | Kontrakty między schematem, zapytaniami i komponentami | Wykrywa kosztowne błędy integracji przed publikacją |
| UI | **React + własny design system** dla Next.js; w Astro komponenty Astro z wyspami React tam, gdzie są potrzebne | Reużywalne, responsywne sekcje i interakcje | Jeden zestaw komponentów chroni markę i ogranicza pracę redakcyjną |
| Style | **CSS Modules albo Tailwind CSS** | Tokeny, warianty i responsywność | Oba podejścia są tanie w utrzymaniu; wybór powinien wynikać z kompetencji zespołu |
| Dokumentacja UI | **Storybook** przy większej bibliotece komponentów | Katalog wariantów, testowanie i akceptacja sekcji | Opłaca się, gdy komponentów jest wiele lub pracuje nad nimi kilka zespołów |
| Hosting | **Vercel** dla najprostszego Next.js; **Cloudflare Workers/static assets** dla niższego kosztu infrastruktury; Astro dobrze pasuje do obu | CDN, compute, preview deployments, SSL | Można zoptymalizować koszt względem czasu zespołu i wymagań runtime |
| Testy | **Vitest + Playwright + axe/Lighthouse CI** | Logika, ścieżki publikacji, responsive, accessibility i performance | Automatyzacja chroni autonomię marketingu bez ręcznego QA każdej strony |
| Monitoring | **Sentry** lub istniejące APM klienta | Błędy frontendu i integracji | Nie warto budować własnej obserwowalności |

Nie każda pozycja musi wejść do pierwszego wydania. Storybook, Sentry i rozbudowany CI uzasadnia skala projektu, ale TypeScript, test najważniejszej ścieżki i monitoring błędów produkcyjnych zwykle zwracają się szybko.

## Next.js czy Astro?

### Next.js — największe pokrycie use case'ów jednym frameworkiem

Next.js jest pełnym frameworkiem React do aplikacji webowych. Oprócz statycznego generowania oferuje rendering serwerowy, Route Handlers, Server Actions, cache i rewalidację, redirecty, warstwę requestową oraz bogaty ekosystem React.

Integracja z Sanity jest szczególnie dojrzała. Oficjalny pakiet [`next-sanity`](https://www.sanity.io/docs/nextjs/introduction) łączy klienta, cache Next.js, Draft Mode, Visual Editing, Live Content API, webhooki, Portable Text i opcjonalne osadzenie Studio. Live Content może aktualizować opublikowane strony bez pełnego deployu, a edytor dostaje płynny preview.

**Najlepiej pokrywa:**

- personalizację na request lub na edge;
- dynamiczne ścieżki użytkownika i segmentację;
- formularze wymagające bezpiecznej logiki serwerowej;
- integracje, które potrzebują Route Handlers;
- A/B testing i feature flags po stronie serwera lub klienta;
- interaktywne komponenty React oraz doświadczenia zbliżone do aplikacji;
- hybrydowe strony łączące marketing i fragmenty danych produktowych;
- rozbudowane preview oraz aktualizacje w czasie rzeczywistym.

**Koszt i ryzyka:**

- więcej zachowań domyślnie może działać dynamicznie, więc architektura cache wymaga dyscypliny;
- React i hydratacja ułatwiają przypadkowe wysłanie zbyt dużej ilości JavaScriptu;
- nowe mechanizmy cache zmieniały się między wersjami Next.js, dlatego wersje `next`, `next-sanity` i sposób Live Content trzeba aktualizować razem;
- Vercel daje najprostszy deployment, ale koszt zależy od miejsc zespołu oraz zużycia compute, obrazów i transferu;
- alternatywny hosting przez adapter zwiększa zakres testów kompatybilności.

### Next.js ze statycznym eksportem — niższy hosting kosztem runtime'u

Next.js może działać bez serwera Node.js i bez funkcji edge. Ustawienie `output: 'export'` powoduje, że `next build` generuje katalog statycznych plików HTML, CSS, JavaScript i pozostałych assetów. Taki katalog można hostować na zwykłym CDN-ie lub hostingu statycznym.

To ważne rozróżnienie: **statyczne renderowanie strony w Next.js nie jest tym samym co statyczny eksport całej aplikacji**.

- Przy zwykłym wdrożeniu Next.js większość stron może być pre-renderowana i tanio serwowana z cache, ale runtime nadal istnieje dla preview, ISR, formularzy, personalizacji i wybranych tras dynamicznych.
- Przy `output: 'export'` runtime nie istnieje w ogóle. Każda funkcja wymagająca obsługi requestu przez Next.js musi zostać usunięta, przeniesiona do przeglądarki albo zrealizowana przez osobną usługę.

Pełną listę aktualnych ograniczeń utrzymuje dokumentacja [Static Exports](https://nextjs.org/docs/app/guides/static-exports).

#### Co statyczny eksport nadal daje

**Treść Sanity renderowaną do HTML podczas builda.** Server Components mogą pobrać opublikowaną treść z Content Lake w trakcie `next build`. Użytkownik otrzymuje gotowy, indeksowalny HTML bez wykonywania zapytania do Sanity podczas każdego wejścia.

**Dynamiczne ścieżki znane podczas builda.** Strony takie jak `[locale]/[slug]` działają, jeżeli `generateStaticParams()` zwróci wszystkie obsługiwane kombinacje. Można więc wygenerować strony produktowe, landing pages, wpisy, template'y i wersje językowe istniejące w chwili budowania aplikacji.

**Interaktywność po stronie klienta.** Client Components, React, animacje, slidery, kalkulatory, analityka oraz embedowane formularze nadal działają w przeglądarce. Statyczny eksport nie oznacza strony pozbawionej JavaScriptu.

**Client-side data fetching.** Komponent może po załadowaniu strony pobierać dane bezpośrednio z publicznego API Sanity albo innej usługi. Jest to użyteczne dla danych często zmieniających się, ale pogarsza początkowe SEO i UX dla zawartości, która nie znalazła się w wygenerowanym HTML-u. Prywatnego tokenu Sanity nie wolno umieszczać w kodzie przeglądarki.

**Statyczne Route Handlers.** Handler `GET`, którego wynik można obliczyć podczas builda i który nie zależy od obiektu `Request`, może wygenerować plik. Nadaje się np. do statycznego feedu lub manifestu, ale nie staje się endpointem wykonywanym na żądanie.

**Tani i prosty hosting.** Nie ma kosztu compute per request, cold startów ani potrzeby utrzymywania adaptera runtime. Statyczne pliki łatwo cache'ować globalnie, a skok ruchu nie zwiększa liczby wykonań funkcji.

**Małą powierzchnię ataku.** Brak serwera aplikacyjnego usuwa część klas błędów i ogranicza liczbę sekretów potrzebnych w środowisku produkcyjnym. Sekrety używane do pobrania danych podczas builda pozostają w CI, a nie w runtime strony.

#### Jakich możliwości statyczny eksport pozbawia

| Możliwość | Skutek `output: 'export'` | Typowe obejście |
|---|---|---|
| **Publikacja bez pełnego builda** | Brak ISR i rewalidacji tagiem lub ścieżką; HTML nie zmieni się po publikacji w Sanity | Webhook Sanity uruchamiający nowy build i deployment |
| **Nowa strona dostępna natychmiast** | Slug nieuwzględniony przez `generateStaticParams()` nie istnieje i zwykle zwróci 404 | Pełny rebuild po utworzeniu strony |
| **Draft Mode i standardowe Visual Editing** | Draft Mode wymaga runtime'u i nie jest wspierany w static export | Osobna dynamiczna aplikacja preview albo rezygnacja z pełnego preview draftów |
| **Live Content API w standardowym modelu Next.js** | Brak serwera, który może odświeżyć wyrenderowaną stronę i cache | Rebuild; ewentualnie client-side fetching dla wybranych danych |
| **Personalizacja na request** | Brak dostępu do cookies, nagłówków, geolokalizacji i sesji podczas renderowania | Personalizacja w przeglądarce lub zewnętrzna warstwa edge przed hostingiem |
| **Server Actions** | Nie są obsługiwane | Zewnętrzny formularz albo osobny endpoint serverless |
| **Dynamiczne Route Handlers** | Handler zależny od `Request`, cookies lub sekretów nie może działać | Osobny Worker/function/API |
| **Redirecty, rewrites i headers Next.js** | Konfiguracja `next.config` nie wykonuje ich automatycznie | Reguły hostingu/CDN, np. plik redirectów lub edge function |
| **Proxy/middleware** | Brak runtime'u przechwytującego request | Konfiguracja CDN albo osobna warstwa edge |
| **Domyślny Image Optimizer Next.js** | Nie jest dostępny | Sanity Image CDN, własny loader albo `unoptimized` |
| **Autoryzowane strony i dane prywatne** | Nie można sprawdzić sesji na serwerze podczas requestu | Osobna aplikacja dynamiczna; client-only auth nie chroni statycznego HTML-u |
| **Intercepting Routes** | Nie są obsługiwane | Zwykła nawigacja lub architektura bez tego wzorca |

#### Wpływ na Sanity i pracę marketingu

Największą oszczędnością jest hosting, ale największą stratą — natychmiastowy cykl publikacji. Po zmianie w Sanity treść w wygenerowanym HTML-u pozostaje stara do kolejnego builda. Webhook może automatycznie uruchomić deployment, lecz czas publikacji zależy wtedy od długości całego builda oraz kolejki CI.

Koszt builda rośnie wraz z liczbą stron i języków. Przykładowo 2 tys. stron w 10 wersjach językowych może oznaczać dziesiątki tysięcy tras generowanych przy każdej zmianie. Oszczędność kilku dolarów na runtime może zostać zamieniona w długi feedback loop, większe zużycie CI i trudniejszą pracę redaktorów.

Pełne Visual Editing Sanity jest szczególnie problematyczne. Standardowa integracja Next.js korzysta z Draft Mode i runtime'u do bezpiecznego pobierania draftów. Przy czystym eksporcie nie należy przenosić prywatnego tokenu do przeglądarki. Można utrzymywać osobną dynamiczną instancję preview, ale wtedy powstają dwa tryby wdrożenia i dodatkowy koszt utrzymania. Często taniej jest zachować minimalny runtime w głównej aplikacji.

#### Kiedy statyczny eksport ma sens

- mały lub średni serwis marketingowy aktualizowany kilka razy w tygodniu, a nie wiele razy dziennie;
- kampanijny microsite o zamkniętym zestawie stron;
- blog, dokumentacja lub katalog, dla którego rebuild trwa krótko;
- wszystkie formularze korzystają z zewnętrznego dostawcy;
- brak personalizacji serwerowej, autoryzacji i danych zależnych od requestu;
- klient akceptuje publikację przez automatyczny rebuild;
- priorytetem są prosty hosting, odporność na skoki ruchu i minimalny koszt infrastruktury.

#### Kiedy lepiej zachować runtime Next.js

- marketing oczekuje płynnego Visual Editing i wiarygodnego preview draftów;
- nowe strony muszą być dostępne natychmiast po publikacji;
- serwis ma wiele stron i locale, przez co pełne buildy są długie;
- potrzebne są ISR, Live Content, personalizacja, eksperymenty server-side lub locale detection;
- formularze wymagają sekretów, walidacji serwerowej, antyspamu albo integracji z kilkoma systemami;
- część stron łączy treść CMS z aktualnymi danymi aplikacji lub cennika;
- hosting ma wykonywać redirecty, nagłówki bezpieczeństwa i logikę edge zdefiniowaną w aplikacji.

#### Ocena dla pełnego zakresu referencyjnego

Dla pełnego zakresu referencyjnego **czysty static export nie jest rekomendowany**. Pokryłby strony, SEO, lokalizowane HTML-e, design system, animacje klienckie i embedy, ale osłabiłby kluczowe cele: natychmiastowe publikowanie, rozbudowane preview, personalizację, testy po stronie serwera, bezpieczne formularze i hybrydowe strony cenowe.

Lepszym kompromisem jest zwykłe wdrożenie Next.js z **domyślnie statycznie renderowanymi stronami i minimalnym runtime'em tylko tam, gdzie wnosi wartość**. Dzięki temu publiczny ruch nadal może być obsługiwany głównie z cache, a klient nie rezygnuje z ISR, Draft Mode, Visual Editing i wybranych funkcji serwerowych. `output: 'export'` warto traktować jako świadomą optymalizację dla ograniczonego zakresu, a nie domyślny sposób obniżania kosztu każdego projektu Sanity.

### Astro — najniższy koszt dla content-first website

Astro projektowano dla serwisów bogatych w treść. Domyślnie generuje HTML, a JavaScript trafia do przeglądarki tylko dla wybranych „wysp” interaktywności. Komponent slidera, kalkulatora lub formularza może używać React, podczas gdy reszta strony pozostaje statyczna. [Dokumentacja Astro](https://docs.astro.build/en/concepts/islands/) opisuje ten model jako static HTML z małymi, opcjonalnymi wyspami JavaScriptu.

Sanity ma [oficjalną integrację z Astro](https://www.sanity.io/plugins/sanity-astro) oraz wsparcie Visual Editing. Istotna różnica: Astro nie ma bezpośredniego odpowiednika Next.js Live Content API; standardowy preview po zmianie pola przeładowuje stronę, żeby pobrać najnowszą treść. Nadal jest użyteczny, ale mniej płynny przy rozbudowanym page buildingu.

**Najlepiej pokrywa:**

- strony marketingowe, landing pages, blog, help center i dokumentację;
- SEO i AEO oparte na indeksowalnym HTML-u;
- serwisy z dużą liczbą statycznych stron;
- szybkie strony z niewielką liczbą interakcji;
- kampanijne microsites;
- bardzo tani hosting statycznych assetów;
- używanie React tylko tam, gdzie daje wartość.

**Koszt i ryzyka:**

- personalizacja na request wymaga przejścia z czystej statyki do SSR lub logiki edge;
- wiele interaktywnych wysp może z czasem odtworzyć złożoność aplikacji React, ale w mniej spójnym modelu;
- zaawansowane formularze i integracje serwerowe są możliwe, lecz mniej naturalne dla zespołu wyspecjalizowanego w Next.js;
- live preview jest mniej płynny;
- rynek specjalistów i liczba gotowych wzorców enterprise są mniejsze niż dla Next.js.

## Porównanie pod kątem referencyjnego zakresu wymagań

Ocena jest jakościowa: **bardzo dobre** oznacza pokrycie naturalnymi mechanizmami frameworka; **dobre** — pokrycie bez istotnego ryzyka, ale z dodatkową implementacją; **warunkowe** — rozwiązanie możliwe, lecz zmienia prosty model architektury lub wymaga usługi zewnętrznej.

| Grupa wymagań | Sanity + Next.js | Sanity + Astro | Komentarz kosztowy |
|---|---|---|---|
| Ownership marketingu i strony | **bardzo dobre** | **bardzo dobre** | Koszt zależy głównie od jakości modelu sekcji, nie frameworka |
| Routing, URL-e i redirecty | **bardzo dobre** | **dobre** | Oba obsługują routing; Next.js ma szersze wzorce dynamiczne i middleware/proxy |
| Page building i komponenty | **bardzo dobre** | **bardzo dobre** | Oba mogą renderować ten sam model Sanity; Next.js ma płynniejszy live preview |
| Mobile i wysokie rozdzielczości | **bardzo dobre** | **bardzo dobre** | Odpowiada design system i CSS, nie CMS ani framework sam w sobie |
| Template pages i listingi | **bardzo dobre** | **bardzo dobre** | Astro ma przewagę kosztową dla statycznych katalogów |
| Crowdin i lokalizacja | **dobre** | **dobre** | Główny koszt to model treści, workflow tłumaczeń i routing językowy |
| HubSpot/GetResponse forms | **bardzo dobre** | **dobre** | Embedy są równie proste; własna warstwa serwerowa jest naturalniejsza w Next.js |
| Nawigacja i breadcrumbs | **bardzo dobre** | **bardzo dobre** | W obu generowane z ustrukturyzowanych danych Sanity |
| Motion, embedy, custom components | **bardzo dobre** | **dobre** | React ma największy ekosystem; Astro ogranicza JS przez islands |
| Integracje włączane per strona | **bardzo dobre** | **dobre** | Oba mogą lazy-loadować adaptery; Next.js lepiej znosi rosnącą dynamikę |
| Personalizacja i visitor journeys | **bardzo dobre** | **warunkowe** | To najmocniejszy argument za Next.js w pełnym zakresie referencyjnym |
| A/B testing i analytics | **bardzo dobre** | **dobre** | Client-side działa w obu; server/edge experiments są prostsze w Next.js |
| SEO, structured data i LLM readiness | **bardzo dobre** | **bardzo dobre** | Astro łatwiej utrzymuje minimalny JS; oba generują poprawny HTML |
| AI-assisted workflows | **dobre** | **dobre** | Workflow działa przez Sanity API; frontend ma drugorzędne znaczenie |
| Security, role i auth | **bardzo dobre** | **dobre** | Role CMS zapewnia Sanity; zaawansowana logika requestów jest dojrzalsza w Next.js |
| Draft, preview, staging, production | **bardzo dobre** | **dobre** | Astro Visual Editing przeładowuje stronę po zmianie; Next.js ma Live Content API |

### Ocena dla pełnego zakresu referencyjnego

Przy zachowaniu wszystkich wymagań z zakresu referencyjnego **Next.js jest sensowniejszym wyborem**. Decydują nie zwykłe strony marketingowe, bo te oba frameworki obsłużą dobrze, lecz suma potrzeb dynamicznych:

- personalizacja sekcji i CTA na podstawie sygnałów użytkownika;
- page-level VWO/Amplitude i przyszłe feature flags;
- interaktywne hero oraz komponenty generowane lub rozwijane w React;
- formularze i integracje wymagające bezpiecznej logiki serwerowej;
- hybrydowe strony cenowe łączące CMS z warstwą produktu;
- płynne Visual Editing dla autonomicznego marketingu;
- pozostawienie miejsca na przyszłe agentowe i programatyczne workflow.

Astro byłoby lepsze kosztowo, gdyby zakres pierwszej fazy ograniczyć do treści, lokalizacji, SEO, formularzy embedowanych i kilku izolowanych interakcji. W takim wariancie personalizację oraz złożone testy można świadomie odłożyć. Nie warto jednak wybierać Astro wyłącznie dla niższego rachunku hostingowego, jeśli różnica zostanie wielokrotnie wydana na customową obsługę funkcji dynamicznych.

## Czy łączyć Next.js i Astro z jednym Sanity?

Technicznie Sanity może zasilać oba. Biznesowo ma to sens, gdy są to **oddzielne produkty o innym profilu**, np.:

- główna platforma marketingowa w Next.js;
- dokumentacja, blog lub centrum pomocy w Astro;
- szybkie, izolowane microsites kampanijne w Astro.

Nie rekomenduje się dwóch frameworków dla jednego spójnego serwisu na początku. Powstają wtedy dwa systemy routingu, dwa preview, dwa zestawy komponentów, dwa pipeline'y wdrożeniowe, podwójne testy integracji oraz większe ryzyko różnic SEO i analityki. Koszt zespołu zwykle przewyższa oszczędność infrastruktury.

**Reguła:** jeden frontend na jeden spójny obszar odpowiedzialności. Drugi framework dopiero wtedy, gdy niezależność produktu, zespołu lub profilu wydajności uzasadnia osobny lifecycle.

## Rekomendowany stack dla pełnego serwisu SaaS

### Rdzeń

1. **Sanity Growth** dla produkcyjnego serwisu zespołowego — Free do proof of conceptu.
2. **Next.js App Router + TypeScript**, w wersjach oficjalnie wspieranych przez bieżący `next-sanity`.
3. **`next-sanity`**, Sanity TypeGen i typowane zapytania GROQ.
4. **React** dla biblioteki sekcji i interaktywnych komponentów.
5. **CSS Modules lub Tailwind CSS** według istniejących kompetencji; bez wprowadzania obu jako równorzędnych standardów.
6. **Storybook** dla komponentów zaakceptowanych do użycia przez marketing, jeżeli biblioteka ma rosnąć.

### Content operations

- Visual Editing i Draft Mode;
- live preview oraz rewalidacja bez pełnego deployu;
- schema validation i asynchroniczne testy linków/slugów;
- typy `page`, `pageSection`, `navigation`, `redirect`, `formReference`, `integrationConfig` i modele domenowe;
- lokalizacja dokumentowa albo polowa — jedna strategia bazowa;
- Crowdin przez API/webhooks po ustabilizowaniu schematów;
- regularny eksport datasetu jako część backupu.

### Design system i page building

- sekcje implementowane w kodzie, konfigurowane w Sanity;
- ograniczona lista wariantów chroniąca design system;
- komponenty responsywne z defaultów, bez ręcznego sterowania CSS-em przez marketing;
- preview desktop/mobile oraz automatyczne testy dostępności;
- `unknown section` fallback, aby błąd pojedynczego dokumentu nie wyłączał całej strony;
- walidacja referencji, CTA, alt textów i wymaganych eventów.

### Formularze i CRM

Najtańsza kolejność:

1. referencja do istniejącego formularza HubSpot/GetResponse w Sanity;
2. bezpieczny adapter frontendu i zarządzany thank-you page;
3. wspólne mapowanie eventów analitycznych;
4. dopiero później własny Route Handler, jeśli embedy nie spełniają wymagań walidacji, antyspamu, consent albo UX.

CMS nie powinien przechowywać leadów. Pozostają w systemie CRM/marketing automation.

### Analityka, eksperymenty i personalizacja

- wykorzystać **Amplitude lub VWO już obecne u klienta**, zamiast budować własny silnik;
- Sanity przechowuje tylko bezpieczne warianty treści, identyfikatory eksperymentu i zatwierdzoną konfigurację;
- SDK odpowiada za alokację wariantu oraz exposure events;
- event taxonomy żyje w kodzie lub wspólnym rejestrze, a redaktor wybiera event z listy;
- personalizację zacząć od sygnałów o wysokiej wartości i małym ryzyku cache, np. locale i campaign source;
- ciężkie SDK ładować po zgodzie i tylko na stronach, na których są potrzebne.

Amplitude ma osobne mechanizmy dla analytics, feature experiments i web experiments; aktualne opcje przedstawia [Browser Unified SDK](https://amplitude.com/docs/sdks/analytics/browser/browser-unified-sdk). Włączenie wszystkich modułów jednym skryptem może zwiększyć bundle i zakres przetwarzania danych, więc należy aktywować tylko zakupione oraz używane funkcje.

### Motion i interaktywność

Najtańsza kolejność implementacji:

1. CSS transitions, animations i natywne View Transitions;
2. mały komponent React dla konkretnej interakcji;
3. Motion albo podobna biblioteka, gdy animacje stanowią system;
4. Lottie dla istniejących animacji JSON;
5. GSAP tylko dla złożonych sekwencji, parallax i scroll choreography uzasadnionych projektem.

Sanity przechowuje parametry, tekst, asset i dozwolony wariant. Nie przechowuje dowolnego kodu animacji wpisywanego przez redaktora.

### Testy i jakość

- **Vitest** — mappery sekcji, helpery SEO, routing i walidacje;
- **Playwright** — publikacja, preview, formularze, linki, locale i kluczowe ścieżki;
- **axe** — automatyczne wykrywanie podstawowych błędów dostępności;
- **Lighthouse CI** — budżety performance dla reprezentatywnych template'ów;
- visual regression dla biblioteki sekcji, jeśli liczba wariantów i tempo zmian to uzasadniają;
- test konfiguracji analytics przed publikacją zamiast ręcznego sprawdzania każdego eventu.

## Hosting: najniższy rachunek czy najniższy całkowity koszt?

### Next.js na Vercel

To wariant o najmniejszym ryzyku integracyjnym. Preview deployments, cache, funkcje i mechanizmy Next.js są dostępne bez adaptera. Vercel Pro kosztuje obecnie **$20/mies. za platformę z jednym miejscem wdrażającym i $20 kredytu infrastrukturalnego**; dodatkowe płatne miejsca kosztują po $20/mies. Dochodzi zużycie ponad limity i opcjonalne dodatki. Aktualne zasady opisuje [Vercel Pro Plan](https://vercel.com/docs/plans/pro-plan).

**Wybierać, gdy:** czas developmentu, niezawodny DX i minimalne ryzyko są ważniejsze niż najniższy możliwy rachunek infrastrukturalny.

### Next.js na Cloudflare Workers

Cloudflare wdraża Next.js przez adapter OpenNext. Według aktualnej dokumentacji obsługuje App Router, Route Handlers, Server Components, SSG, SSR, ISR, Server Actions i większość kluczowych funkcji, ale nie jest runtime'em macierzystym Next.js. [Lista zgodności](https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/) powinna być sprawdzana przy aktualizacji frameworka.

Workers Paid ma obecnie minimalną opłatę **$5/mies.**, zawiera 10 mln requestów i 30 mln ms CPU, a statyczne assety są bezpłatne i nielimitowane. Platforma nie dolicza egressu dla Workers. Szczegóły są w [cenniku Workers](https://developers.cloudflare.com/workers/platform/pricing/).

**Wybierać, gdy:** zespół akceptuje adapter i testy kompatybilności, a skala lub polityka infrastrukturalna daje realną oszczędność.

### Astro na hostingu statycznym lub Workers

Astro domyślnie pre-renderuje strony, więc statyczny wariant może być bardzo tani i odporny na skoki ruchu. Jeśli potrzebne są personalizacja, sesja albo request-time logic, wybrane strony mogą działać on-demand. Cloudflare pozwala serwować czyste static assets bez adaptera, a przy SSR użyć [adaptera Astro dla Workers](https://developers.cloudflare.com/workers/framework-guides/web-apps/astro/).

**Wybierać, gdy:** większość stron jest publiczna i taka sama dla użytkowników, a aktualizacja może następować przez webhook uruchamiający build albo kontrolowane renderowanie on-demand.

### Reguła TCO

Różnica $15–100 miesięcznie w hostingu jest mała wobec kilku dodatkowych dni pracy developera. Tańszy runtime wygrywa dopiero wtedy, gdy:

- jest znany zespołowi;
- pokrywa potrzebne funkcje bez obejść;
- ma monitoring i kontrolę kosztów;
- nie komplikuje preview, rewalidacji i deployu;
- oszczędność powtarza się przez wystarczająco długi czas lub przy dużej skali.

## Technologie opcjonalne — dodawać dopiero po spełnieniu warunku

| Technologia / kategoria | Dodaj, gdy | Nie dodawaj, gdy |
|---|---|---|
| **Crowdin** | Jest wiele locale, formalny proces tłumaczeń i obecny zespół localization | Tłumaczenia są sporadyczne lub dotyczą dwóch prostych wersji |
| **Amplitude/VWO Experiment** | Istnieje ruch, hipotezy, owner i proces analizy | „A/B testing” jest tylko pozycją na roadmapie bez metodologii |
| **Algolia/Typesense** | GROQ nie zapewnia potrzebnej jakości full-text, facetingu lub skali | Potrzebne są jedynie listingi i filtry po znanych polach |
| **Sentry** | Serwis ma krytyczne formularze, integracje lub wiele dynamicznych ścieżek | Istniejące APM klienta już pokrywa frontend |
| **Storybook** | Biblioteka sekcji jest współdzielona i rozwijana regularnie | Projekt ma kilka prostych, stabilnych komponentów |
| **Motion/GSAP** | Wiele komponentów używa wspólnego systemu motion albo złożonej choreografii | Wystarczą pojedyncze przejścia CSS |
| **Feature flag service** | Potrzebne są kontrolowane rollouty i server-side experiments | Flagi byłyby używane tylko jako permanentna konfiguracja treści |
| **Własny backend** | Potrzebna jest agregacja danych, sekrety, kolejki lub niezawodny workflow | Sanity, frontend i istniejące SaaS-y pokrywają przypadek |
| **Dodatkowy DAM** | Prawa, workflow assetów i wiele marek przekraczają możliwości Sanity | Potrzebne jest zwykłe przechowywanie obrazów i plików |

## Czego nie budować w pierwszej wersji

- uniwersalnego edytora dowolnego layoutu;
- pola do wklejania dowolnego JavaScriptu;
- własnego systemu A/B testingu;
- własnej platformy formularzowej, jeśli HubSpot/GetResponse działa;
- osobnej bazy na konfigurację, którą może przechowywać Sanity;
- zewnętrznego wyszukiwania bez wymagań wykraczających poza GROQ;
- dwóch równoległych frameworków frontendowych dla tych samych stron;
- mikrofrontendów bez niezależnych zespołów i cykli wdrożeniowych;
- AI publikującego bez draftu, walidacji i akceptacji człowieka;
- personalizacji każdej sekcji od pierwszego wydania.

Każdy z tych elementów może kiedyś być uzasadniony. Żaden nie jest warunkiem rozpoczęcia autonomicznej pracy marketingu.

## Rekomendowane warianty wdrożenia

### Wariant A — maksymalne pokrycie use case'ów

**Sanity Growth + Next.js + TypeScript + React + Vercel**

Najlepszy dla zakresu podobnego do referencyjnego. Minimalizuje ryzyko funkcjonalne i czas integracji Visual Editing, personalizacji, formularzy oraz eksperymentów. Koszt infrastruktury jest wyższy niż wariant czysto statyczny, ale jeden spójny stack ogranicza koszt developmentu.

### Wariant B — kosztowo zoptymalizowany pełny stack

**Sanity Growth + Next.js + TypeScript + Cloudflare Workers**

Ma sens dla zespołu znającego Cloudflare i gotowego utrzymywać OpenNext. Przed decyzją potrzebny jest spike obejmujący Draft Mode, Visual Editing, cache/revalidation, image optimization, redirects i używane SDK marketingowe.

### Wariant C — najniższy koszt content-first

**Sanity Growth + Astro + TypeScript + hosting statyczny/Cloudflare + wyspy React**

Najlepszy dla serwisów publicznych, SEO-heavy, z ograniczoną personalizacją. Zapewnia szybki HTML, mało JavaScriptu i tani hosting. Należy zaakceptować mniej płynne Visual Editing oraz ostrożnie kontrolować wzrost liczby interaktywnych wysp.

### Wariant D — proof of concept

**Sanity Free + ten sam docelowy framework + hosting free tier**

PoC powinien sprawdzić pełny pion funkcjonalny: model strony, 3–5 sekcji, preview, jeden formularz, jeden locale dodatkowy, SEO i pomiar eventu. Nie należy tworzyć prototypu w innym frameworku niż planowany produkcyjnie — pozorna oszczędność kończy się ponowną implementacją.

## Ostateczna rekomendacja dla pełnego zakresu referencyjnego

1. Wybrać **Sanity Growth + Next.js + TypeScript** jako jeden rdzeń serwisu.
2. Zacząć od hostingu minimalizującego ryzyko zespołu: Vercel, jeżeli liczy się szybkość realizacji; Cloudflare po spike'u, jeżeli priorytetem jest długoterminowy koszt infrastruktury.
3. Zbudować zamkniętą bibliotekę reużywalnych sekcji z Visual Editing i responsywnymi defaultami.
4. HubSpot/GetResponse, Crowdin oraz istniejące VWO/Amplitude integrować jako systemy wyspecjalizowane — nie odtwarzać ich funkcji w Sanity.
5. W pierwszej fazie zapewnić gotowość na personalizację i AI w modelu danych, ale nie budować pełnych silników bez potwierdzonych scenariuszy.
6. Astro rozważyć dla osobnego help center, dokumentacji lub microsites, nie jako drugi frontend tych samych stron.

Takie podejście pokrywa pełny kierunek biznesowy dokumentu, a jednocześnie utrzymuje koszt pod kontrolą przez etapowanie funkcji najbardziej zmiennych i najdroższych.

## Źródła

- Sanity: [Sanity and Next.js](https://www.sanity.io/docs/nextjs/introduction), [Visual Editing with Next.js App Router](https://www.sanity.io/docs/nextjs/visual-editing-with-next-js-app-router)
- Sanity: [Visual Editing](https://www.sanity.io/docs/visual-editing), [official Astro integration](https://www.sanity.io/plugins/sanity-astro)
- Astro: [Islands architecture](https://docs.astro.build/en/concepts/islands/), [Sanity & Astro](https://docs.astro.build/en/guides/cms/sanity/)
- Next.js: [App Router documentation](https://nextjs.org/docs/app), [Static Exports](https://nextjs.org/docs/app/guides/static-exports), [Caching](https://nextjs.org/docs/app/guides/caching), [Metadata and OG images](https://nextjs.org/docs/app/getting-started/metadata-and-og-images)
- Cloudflare: [Next.js on Workers](https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/), [Astro on Workers](https://developers.cloudflare.com/workers/framework-guides/web-apps/astro/), [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/)
- Vercel: [Pro Plan](https://vercel.com/docs/plans/pro-plan), [Pricing](https://vercel.com/pricing)
- Amplitude: [Browser Unified SDK](https://amplitude.com/docs/sdks/analytics/browser/browser-unified-sdk), [Experiment overview](https://amplitude.com/docs/feature-experiment/overview)
