# Technologie webowe, które warto łączyć z Prismic

> **Rekomendacja w jednym zdaniu:** dla szerokiego zakresu nowoczesnego serwisu SaaS najbezpieczniejszym domyślnym połączeniem jest **Prismic Medium + Next.js + TypeScript**, ale **Nuxt** może być równie dobry i tańszy dla zespołu Vue, **SvelteKit** jest wartościowym lekkim wariantem dla zespołu znającego Svelte, a **Astro** daje najniższy koszt dla prostego content-first website pod warunkiem zaakceptowania większego kosztu własnej integracji z Prismic i ograniczenia funkcji dynamicznych.

Stan analizy: **28 lipca 2026 r.** Dokument rozwija mapę potrzeb z [`potrzeby-biznesowe-klienta.md`](./potrzeby-biznesowe-klienta.md), uzupełnia [`co-wyroznia.md`](./co-wyroznia.md) i ocenia warianty względem referencyjnego zakresu pełnego serwisu SaaS (14 grup wymagań opisanych w `potrzeby-biznesowe-klienta.md`).

## Najpierw zasada kosztowa: najtańszy jest stack znany zespołowi, który pokrywa zakres bez obejść

Prismic powinien odpowiadać za modele, treść, assety, drafty, preview i konfigurację stron. Frontend odpowiada za routing, rendering, responsive, SEO, accessibility, formularze, analitykę i interakcje. Każda dodatkowa usługa albo framework oznacza:

- integrację, aktualizacje i monitoring;
- kolejny model cache, routingu i deployu;
- wpływ na security, privacy i consent;
- wiedzę potrzebną do utrzymania rozwiązania;
- ryzyko niespójności preview i produkcji;
- koszt rekrutacji lub wdrożenia kolejnego developera.

Koszt developmentu należy oceniać co najmniej w pięciu wymiarach:

1. **kompetencje obecnego zespołu** — zmiana React na Vue lub Svelte tylko dla teoretycznie mniejszego bundle'a rzadko się zwraca;
2. **dojrzałość integracji Prismic** — first-party SDK, preview i generowane typy oszczędzają dni pracy oraz przyszłe debugowanie;
3. **profil strony** — statyczny content-first website ma inne potrzeby niż serwis z personalizacją, formularzami i danymi produktu;
4. **hosting i runtime** — niski rachunek ma znaczenie dopiero po uwzględnieniu adapterów, buildów, observability i pracy utrzymaniowej;
5. **koszt zmiany za dwa lata** — popularny i dobrze udokumentowany stack łatwiej przejąć, zaktualizować i rozwijać.

**Reguła TCO:** różnica $20–100 miesięcznie w hostingu jest mniejsza niż koszt jednego dodatkowego dnia developmentu. Framework z droższym runtime'em może być tańszy w całości, jeśli usuwa custom preview, ręczną rewalidację i nietypowe adaptery.

## Aktualny fundament Prismica: Type Builder + CLI, nie Slice Machine

Nowe wdrożenie powinno używać **Type Buildera w chmurze i lokalnego Prismic CLI**. Ten zestaw zastępuje Slice Machine jako rekomendowany workflow:

- Type Builder służy do wizualnego modelowania page types, custom types i slices;
- modele pozostają dostępne lokalnie i mogą być wersjonowane w Git;
- CLI synchronizuje modele, generuje typy TypeScript i tworzy pliki komponentów;
- slice simulator wspiera development preview;
- Prismic MCP może tworzyć testową treść i drafty bez ręcznego wypełniania każdego pola;
- Slice Machine nadal działa w istniejących projektach, ale nie będzie dalej rozwijany.

To wpływa na koszt stacku. Nie należy wybierać frameworka na podstawie starego adaptera Slice Machine ani zaczynać nowego repo od `@slicemachine/init`. Punktem odniesienia są aktualne komendy Prismic CLI i bieżące SDK frameworkowe. Kierunek platformy opisują [Type Builder](https://prismic.io/docs/type-builder) oraz [ogłoszenie workflow Type Builder + CLI](https://prismic.io/blog/how-building-with-prismic-is-changing).

## Rekomendowana architektura bazowa

| Warstwa | Rekomendowana technologia | Odpowiedzialność | Uzasadnienie kosztowe |
|---|---|---|---|
| Treść | **Prismic** | Modele, strony, slices, assety, locale, drafty, Releases i preview | Gotowy Page Builder zamiast budowy własnego CMS-a |
| Modeling | **Type Builder + Prismic CLI** | Modele, synchronizacja, scaffolding komponentów i typy | Aktualny, agent-ready workflow bez utrzymywania lokalnej aplikacji Slice Machine |
| Frontend | **Jeden z: Next.js, Nuxt, SvelteKit, Astro** | Routing, HTML, SEO, responsive, interakcje i integracje | Wybór według zakresu oraz kompetencji, nie trendu |
| Język | **TypeScript** | Kontrakt między modelami, API i komponentami | Wykrywa rozbieżności przed publikacją i wspiera agentów kodujących |
| UI | **React, Vue, Svelte albo Astro components** | Biblioteka slices i design system | Jeden spójny system komponentów obniża koszt kolejnych kampanii |
| Style | **istniejący standard zespołu: CSS Modules, scoped CSS lub Tailwind** | Tokeny, warianty i responsive | Migracja stylowania bez potrzeby zwiększa zakres i ryzyko |
| Dokumentacja UI | **Storybook albo Histoire**, jeśli biblioteka jest duża | Katalog wariantów, testy i akceptacja slices | Opłacalne przy wielu komponentach lub zespołach; zbędne w małym PoC |
| Testy | **Vitest + Playwright + axe/Lighthouse CI** | Mappery, preview, routing, formularze, accessibility i performance | Chroni autonomię marketingu bez ręcznego QA każdej strony |
| Hosting | **Vercel albo Cloudflare Workers/static assets** | CDN, compute, preview deployments i SSL | Vercel minimalizuje ryzyko Next.js; Cloudflare obniża koszt wielu wariantów |
| Monitoring | **Sentry lub istniejące APM klienta** | Błędy renderowania, integracji i formularzy | Własna observability rzadko jest opłacalna |

Nie każda pozycja musi wejść do pierwszej wersji. TypeScript, test kluczowej ścieżki publikacji i monitoring błędów produkcyjnych zwykle zwracają się szybko. Storybook, pełne visual regression i rozbudowane APM powinny wynikać ze skali biblioteki oraz krytyczności serwisu.

## Poziom oficjalnego wsparcia Prismic

| Framework | Oficjalna ścieżka Prismic | Główne pakiety | Preview i wygenerowane typy | Wpływ na koszt developmentu |
|---|---|---|---|---|
| **Next.js** | **pełna, first-party** | `@prismicio/client`, `@prismicio/react`, `@prismicio/next` | Live slice preview, full-website preview, toolbar, TypeScript | Najniższe ryzyko dla React i najwięcej gotowych wzorców |
| **Nuxt 4** | **pełna, first-party** | `@prismicio/client`, `@prismicio/vue`, `@nuxtjs/prismic` | Live/full preview, auto-importy, TypeScript | Bardzo niski koszt dla zespołu Vue; mniej boilerplate'u przez moduł Nuxt |
| **SvelteKit** | **pełna, first-party** | `@prismicio/client`, `@prismicio/svelte` | Live/full preview, simulator i TypeScript | Mało kodu i JS; koszt zależy od dostępności kompetencji Svelte |
| **Astro** | **ogólny klient, bez równorzędnej ścieżki w katalogu frameworków** | `@prismicio/client` + własne komponenty/integracja | Typy są możliwe, ale preview i mapowanie slices wymagają więcej własnej pracy | Najniższy koszt prostego frontendu, wyższy koszt integracji Prismic i utrzymania |

Oficjalny katalog [Frameworks](https://prismic.io/docs/frameworks) wymienia Next.js, Nuxt i SvelteKit. Astro może pobierać dane z Content API, używać TypeScript i renderować slices, ale nie należy zakładać pełnej parytetowej integracji. W szczególności repozytoria tworzone historycznie jako „Other” mogą wymagać dodatkowej pracy przy nowym Type Builderze.

## Porównanie frameworków pod kątem kosztu developmentu

Ocena jest jakościowa i zakłada zespół z podobnym poziomem znajomości każdego frameworka. W realnym projekcie znajomość technologii może zmienić wynik o całą kategorię.

| Kryterium | Next.js | Nuxt 4 | SvelteKit | Astro |
|---|---|---|---|---|
| Pierwsze wdrożenie Prismic | **niskie** | **niskie** | **niskie** | **średnie/wysokie** |
| Live i full preview | **niskie ryzyko** | **niskie ryzyko** | **niskie ryzyko** | **własna integracja** |
| Prosty content-first frontend | **średni narzut** | **średni narzut** | **niski narzut** | **najniższy narzut** |
| Funkcje full-stack | **bardzo szerokie** | **bardzo szerokie** | **szerokie** | **dobre, ale nie główny profil** |
| Personalizacja request-time | **naturalna** | **naturalna** | **naturalna** | **możliwa po przejściu na runtime** |
| Minimalizacja JS | **wymaga dyscypliny** | **wymaga dyscypliny** | **dobra** | **najlepsza domyślnie** |
| Hosting statyczny | **możliwy z dużymi ograniczeniami** | **dobry przez generate** | **dobry przez adapter-static/prerender** | **naturalny wariant domyślny** |
| Przenośność między hostingami | **średnia** | **wysoka przez Nitro** | **wysoka przez adaptery** | **wysoka przez adaptery/statykę** |
| Rynek i ciągłość utrzymania | **najniższe ryzyko** | **niskie przy ekosystemie Vue** | **zależne od rynku i zespołu** | **dobre dla content, słabsze dla złożonych aplikacji** |
| Koszt pełnego zakresu referencyjnego | **niski/średni** | **niski/średni** | **średni** | **średni/wysoki** |

„Niski koszt” nie oznacza małej liczby linii kodu. Oznacza najmniej niewiadomych w preview, cache, rewalidacji, integracjach, testowaniu i późniejszym przejęciu projektu.

## Next.js — domyślny wybór dla szerokiego zakresu i zespołu React

Next.js 16 App Router oferuje Server Components, statyczne renderowanie, ISR, Draft Mode, Route Handlers, Server Actions, redirecty i request-time rendering. Oficjalna integracja Prismic wspiera wszystkie funkcje CMS-a, Type Builder/CLI, wygenerowane typy, live preview slices i pełny preview draftów.

**Najlepiej pokrywa:**

- personalizację po cookies, kampanii, locale lub sygnałach serwerowych;
- bezpieczne formularze i integracje wymagające sekretów;
- hybrydowe strony cenowe łączące CMS z danymi produktu;
- server-side A/B testing i feature flags;
- złożone komponenty React i duży istniejący design system;
- natychmiastową rewalidację treści po webhooku;
- szeroki zakres przyszłych funkcji bez zmiany frameworka.

**Koszt i ryzyka:**

- wiele sposobów cache i renderowania zwiększa koszt decyzji architektonicznych;
- łatwo wysłać za dużo JavaScriptu przez nadmierne Client Components;
- Vercel jest najprostszym runtime'em, ale adapter do innej platformy wymaga testów zgodności;
- aktualizacje Next.js, React i `@prismicio/next` trzeba planować razem;
- elastyczność full-stack może zachęcać do budowy funkcji, które powinny pozostać w SaaS klienta.

**Rekomendacja:** domyślnie statycznie renderować publiczne strony i używać runtime'u tylko dla Draft Mode, rewalidacji, formularzy, personalizacji oraz tras wymagających świeżych danych. To zachowuje większość oszczędności statycznego HTML-u bez utraty najważniejszych workflow marketingu.

### Next.js ze statycznym eksportem

`output: 'export'` generuje pliki HTML, CSS i JavaScript bez runtime'u Next.js. Hosting jest prosty i tani, ale nie działa ISR, Draft Mode, Server Actions, request-dependent Route Handlers, cookies, headers, redirecty/rewrites z konfiguracji, proxy ani domyślny Image Optimizer.

W kontekście Prismic oznacza to:

- treść i znane ścieżki mogą zostać wygenerowane podczas builda;
- publikacja wymaga pełnego builda uruchamianego webhookiem;
- nowe UID-y nie istnieją do kolejnego deploymentu;
- standardowy pełny preview draftów wymaga osobnej dynamicznej aplikacji albo innego obejścia;
- czas publikacji rośnie wraz z liczbą stron × locale;
- dynamiczne formularze i personalizacja przechodzą do zewnętrznych usług albo przeglądarki.

**Ma sens dla:** zamkniętego microsite'u, niewielkiego bloga, dokumentacji albo serwisu aktualizowanego rzadko. **Nie jest rekomendowany dla pełnego zakresu referencyjnego**, bo oszczędność runtime'u obniża autonomię marketingu i komplikuje preview.

Aktualne ograniczenia utrzymuje dokumentacja [Next.js Static Exports](https://nextjs.org/docs/app/guides/static-exports).

## Nuxt 4 — równorzędny ekonomicznie wybór dla zespołu Vue

Nuxt 4 korzysta z Vue i serwera Nitro. `routeRules` pozwalają mieszać prerendering, SSR, cache, SWR/ISR, client-only i redirecty w jednej aplikacji. Nitro zapewnia API routes oraz deployment na Node, serverless i edge. Moduł `@nuxtjs/prismic` auto-importuje klienta, komponenty i composables, a Prismic oficjalnie wspiera Type Builder/CLI, typy i preview.

**Najlepiej pokrywa:**

- pełny serwis marketingowy organizacji mającej design system Vue;
- statyczne strony z wybranymi trasami SSR lub SWR;
- formularze i integracje przez Nitro server routes;
- personalizację oraz redirecty sterowane per route;
- hosting poza jedną platformą dzięki presetom Nitro;
- zespół, który szybciej dostarcza w Vue niż w React.

**Koszt i ryzyka:**

- dla zespołu React wprowadza drugi ekosystem, bibliotekę komponentów i model mentalny;
- część usług marketingowych publikuje przykłady najpierw dla React/Next, co może wymagać adaptacji;
- zachowanie `isr` i `swr` zależy od platformy docelowej, więc test na lokalnym Node nie wystarcza;
- migracja Nuxt 3 → 4 i duże wersje `@nuxtjs/prismic` mogą wymagać jednorazowych zmian;
- auto-importy skracają kod, ale mogą utrudnić onboarding osobie spoza ekosystemu Nuxt.

**Rekomendacja:** jeżeli klient ma Vue/Nuxt w produkcie lub zespole, Nuxt nie jest „drugim wyborem”. Może mieć niższy TCO niż Next.js, ponieważ zachowuje kompetencje, design system i pipeline. Dla pełnego zakresu referencyjnego pokrywa prawie ten sam profil funkcjonalny.

### Nuxt jako statyczny serwis

`nuxt generate` tworzy statyczną wersję, ale traci hybrid rendering z `routeRules`. Tak jak w innych SSG, publikacja z Prismic wymaga builda i deploymentu, a funkcje zależne od requestu muszą działać osobno. Dla małego content site jest to tani wariant; dla pełnego preview, formularzy i personalizacji lepiej zachować Nitro runtime z prerenderingiem wybranych tras.

## SvelteKit — lekki pełny stack dla zespołu znającego Svelte

SvelteKit domyślnie renderuje pierwszy request po stronie serwera i przejmuje kolejne nawigacje w przeglądarce. Każda trasa może kontrolować `prerender`, `ssr` i `csr`. Server load functions, form actions i `+server` endpoints pokrywają bezpieczną logikę, a adaptery pozwalają wdrażać aplikację na Node, Vercel, Netlify, Cloudflare lub jako statyczne pliki. Prismic oferuje first-party `@prismicio/svelte`, live slice preview, full preview i typy.

**Najlepiej pokrywa:**

- szybkie serwisy marketingowe z umiarkowaną interaktywnością;
- zespół, który już używa Svelte w produkcie lub design systemie;
- projekty chcące ograniczyć boilerplate i runtime JavaScript;
- hybrydę stron prerenderowanych z wybranymi endpointami i actions;
- hosting na Cloudflare Workers bez dodatkowego adaptera pośredniego klasy OpenNext.

**Koszt i ryzyka:**

- mniejsza dostępność developerów i gotowych integracji może zwiększyć koszt utrzymania w niektórych organizacjach;
- biblioteka komponentów React/Vue nie jest bezpośrednio reużywalna;
- zaawansowane marketing SDK czasem wymagają własnych wrapperów;
- prerenderowane strony aktualizują się dopiero po buildzie, jeśli nie zachowa się SSR dla tras contentowych;
- mniejsza liczba wzorców enterprise oznacza większą odpowiedzialność architekta przy nietypowych wymaganiach.

**Rekomendacja:** SvelteKit jest ekonomiczny, gdy kompetencja istnieje już w zespole lub projekt ma długoterminowego ownera Svelte. Wybieranie go wyłącznie dla mniejszego bundle'a nie uzasadnia kosztu organizacyjnej zmiany technologii.

## Astro — najniższy koszt content-first, ale najwyższa luka integracyjna z Prismic

Astro domyślnie renderuje komponenty do HTML i usuwa ich JavaScript. Interaktywność włącza się tylko dla wysp przez `client:*`; wybrane fragmenty mogą działać jako server islands. Serwis może być całkowicie statyczny albo używać on-demand rendering przez adapter. Astro pozwala osadzać komponenty React, Vue i Svelte.

**Najlepiej pokrywa:**

- blog, dokumentację, help center, newsroom i publiczne landing pages;
- serwisy z małą liczbą interakcji i wysokim priorytetem performance;
- statyczny hosting odporny na skoki ruchu;
- projekt, który chce użyć istniejącego komponentu React tylko w pojedynczych wyspach;
- microsites o ograniczonym lifecycle.

**Koszt i ryzyka:**

- Prismic nie wymienia Astro jako pełnej ścieżki obok Next.js, Nuxt i SvelteKit;
- mapping slices, komponenty pól, live simulator i full preview wymagają własnej integracji oraz testów;
- repozytorium „Other” może wymagać dodatkowej pracy z Type Builderem;
- przejście od statycznego serwisu do personalizacji i logiki request-time wymaga adaptera oraz nowego modelu cache;
- mieszanie wielu UI frameworków w wyspach zwiększa bundle i utrzymanie;
- oszczędność runtime'u może zostać skonsumowana przez kilka dni customowego preview.

**Rekomendacja:** Astro wybierać, gdy zakres naprawdę jest content-first i zespół akceptuje własną warstwę Prismic. Przed decyzją wykonać spike obejmujący Type Builder, synchronizację modeli, wygenerowane typy, `SliceZone`-like mapper, live slice preview, full preview draftu i publikację nowego UID-u.

## Porównanie pod kątem referencyjnego zakresu wymagań

Ocena: **bardzo dobre** — naturalne pokrycie frameworkiem i oficjalną integracją; **dobre** — pokrycie z typową implementacją; **warunkowe** — możliwe, ale zmienia prosty model lub wymaga istotnej pracy własnej.

| Grupa wymagań | Prismic + Next.js | Prismic + Nuxt | Prismic + SvelteKit | Prismic + Astro |
|---|---|---|---|---|
| Ownership marketingu | **bardzo dobre** | **bardzo dobre** | **bardzo dobre** | **dobre** |
| Routing, URL-e i redirecty | **bardzo dobre** | **bardzo dobre** | **bardzo dobre** | **dobre** |
| Page building i slices | **bardzo dobre** | **bardzo dobre** | **bardzo dobre** | **warunkowe** |
| Mobile i wysokie rozdzielczości | **bardzo dobre** | **bardzo dobre** | **bardzo dobre** | **bardzo dobre** |
| Template pages i listingi | **bardzo dobre** | **bardzo dobre** | **bardzo dobre** | **bardzo dobre** |
| Crowdin i locale | **dobre** | **dobre** | **dobre** | **dobre** |
| HubSpot/GetResponse | **bardzo dobre** | **bardzo dobre** | **bardzo dobre** | **dobre** |
| Nawigacja i breadcrumbs | **bardzo dobre** | **bardzo dobre** | **bardzo dobre** | **bardzo dobre** |
| Motion, embedy i custom UI | **bardzo dobre** | **bardzo dobre** | **dobre** | **dobre** |
| Integracje per strona | **bardzo dobre** | **bardzo dobre** | **dobre** | **dobre** |
| Personalizacja i visitor journeys | **bardzo dobre** | **bardzo dobre** | **bardzo dobre** | **warunkowe** |
| A/B testing i analytics | **bardzo dobre** | **bardzo dobre** | **dobre** | **dobre** |
| SEO, structured data i AI visibility | **bardzo dobre** | **bardzo dobre** | **bardzo dobre** | **bardzo dobre** |
| AI-assisted development | **bardzo dobre** | **bardzo dobre** | **dobre** | **warunkowe** |
| Security i request-time controls | **bardzo dobre** | **bardzo dobre** | **bardzo dobre** | **dobre** |
| Draft, preview i production | **bardzo dobre** | **bardzo dobre** | **bardzo dobre** | **warunkowe** |

Mobile, SEO i dostępność są podobne we wszystkich frameworkach, jeśli implementacja jest dobra. Różnicę TCO tworzą głównie preview Prismica, dynamika request-time, dostępność gotowych SDK i kompetencje zespołu.

### Ocena dla pełnego zakresu referencyjnego

1. **Next.js** jest najbezpieczniejszym defaultem przy braku dodatkowego kontekstu.
2. **Nuxt** jest równorzędną rekomendacją, jeśli klient ma Vue/Nuxt i może reużyć komponenty lub kompetencje.
3. **SvelteKit** pokrywa zakres technicznie, ale wymaga potwierdzenia długoterminowego ownershipu i dostępności zespołu.
4. **Astro** jest rekomendowane dopiero po ograniczeniu personalizacji, server-side experiments, złożonych formularzy i oczekiwań wobec gotowego preview Prismica.

Nie należy wybierać Next.js wyłącznie dlatego, że jest popularny, ani Astro wyłącznie dlatego, że generuje mniej JavaScriptu. W pełnym zakresie referencyjnym suma wymagań dynamicznych i redakcyjnych jest ważniejsza niż wynik prostego benchmarku strony.

## Czy łączyć kilka frameworków z jednym Prismic?

Technicznie Content API może zasilać wiele frontendów. Biznesowo ma to sens, gdy produkty są rzeczywiście niezależne:

- główna strona w Next.js lub Nuxt;
- dokumentacja albo help center w Astro;
- osobna aplikacja produktowa w SvelteKit;
- izolowane microsites z własnym zespołem i cyklem życia.

Nie rekomenduje się kilku frameworków dla jednego spójnego serwisu na początku. Powstają wtedy różne mapowania slices, preview, routing, biblioteki UI, pipeline'y, analytics i testy. Koszt zespołu prawie zawsze przewyższa oszczędność hostingu.

**Reguła:** jeden frontend i jeden system komponentów na jeden spójny obszar odpowiedzialności. Kolejny framework dopiero wtedy, gdy niezależność produktu lub zespołu jest mierzalną korzyścią.

## Rekomendowany stack dla pełnego serwisu SaaS

### Rdzeń

1. **Prismic Medium** jako punkt wyjścia, jeżeli autor i publisher muszą mieć różne role; Small tylko dla prostego zespołu bez rozdzielenia odpowiedzialności.
2. **Type Builder + Prismic CLI**, bez rozpoczynania nowego projektu w Slice Machine.
3. **Next.js 16 App Router + TypeScript** albo **Nuxt 4 + TypeScript**, zależnie od istniejącej kompetencji.
4. Odpowiedni first-party SDK Prismic i wygenerowane typy.
5. Jeden design system i jeden standard stylowania znany zespołowi.
6. Storybook/Histoire dopiero, gdy biblioteka slices jest współdzielona lub regularnie rozwijana.

### Content operations

- live slice preview i full-website preview;
- Releases i scheduling;
- webhook do precyzyjnej rewalidacji lub builda;
- modele `page`, `navigation`, `redirect`, `formReference`, `integrationConfig` i domenowe custom types;
- jawna strategia locale, URL-i, canonicali oraz `hreflang`;
- test nieznanego slice'a, aby pojedynczy błąd modelu nie wyłączył całej strony;
- cykliczny eksport opublikowanych dokumentów i modele wersjonowane w Git;
- migration scripts zachowane przynajmniej do zakończenia cutover i odbioru.

### Design system i page building

- slices implementowane w kodzie, wybierane i konfigurowane w Prismic;
- warianty zamiast surowych ustawień layoutu;
- responsive i accessibility jako cecha komponentu, nie zadanie redaktora;
- dozwolone zakresy długości, fallbacki i bezpieczne defaulty;
- testy representative content: pusty, krótki, długi, różne locale i brak assetu;
- agent może wygenerować scaffolding, ale review obejmuje finalny HTML, performance i zachowanie.

### Formularze i CRM

Najtańsza kolejność:

1. identyfikator istniejącego formularza HubSpot/GetResponse w Prismic;
2. jeden adapter UI i zarządzany thank-you page;
3. wspólne eventy analityczne oraz consent;
4. własny server endpoint dopiero przy wymaganiach walidacji, antyspamu, retry albo złożonego routingu.

CMS nie przechowuje leadów ani sekretów integracji.

### Analityka, eksperymenty i personalizacja

- wykorzystać VWO/Amplitude obecne u klienta;
- Prismic przechowuje zatwierdzone warianty i identyfikatory, nie silnik statystyczny;
- event taxonomy pozostaje w kodzie albo wersjonowanym rejestrze;
- SDK ładować po zgodzie i tylko na potrzebnych stronach;
- zacząć od locale, campaign source i jednego slotu personalizacji;
- server-side allocation wdrażać tylko, jeśli poprawia pomiar lub UX względem tańszego wariantu klientowego.

### AI-ready development

- zainstalować oficjalny skill Prismic dla używanego agenta;
- CLI używać do setupu, modeli, typów i scaffoldu;
- MCP używać do testowej treści, duplikacji i masowych draftów;
- w CI sprawdzać, czy wygenerowane typy odpowiadają modelom;
- agentowi przekazać reguły design systemu, accessibility i testów;
- wymagać human review przed publikacją i nie wkładać prywatnych tokenów do przeglądarki.

Największą przewagę ma framework z first-party ścieżką Prismic. W Astro agent może napisać brakujący glue code szybciej, ale organizacja nadal staje się jego właścicielem.

### Testy i jakość

- **Vitest** — mappery slices, routing, SEO i transformacje danych;
- **Playwright** — preview, publikacja, formularze, locale, redirecty i kluczowe CTA;
- **axe** — podstawowe błędy accessibility;
- **Lighthouse CI** — budżety performance dla reprezentatywnych template'ów;
- visual regression, jeśli wariantów jest wiele lub zespół często zmienia design system;
- test webhooks/revalidation, aby publikacja nie pozostawiała starej treści w cache.

## Hosting: koszt rachunku a koszt utrzymania

### Next.js na Vercel

To wariant o najmniejszym ryzyku kompatybilności dla Next.js. Pro kosztuje obecnie **$20/mies. za platformę**, zawiera jedno miejsce wdrażające i $20 kredytu infrastrukturalnego. Dodatkowe płatne miejsca kosztują $20/mies.; Viewerzy są bezpłatni. W cenie są m.in. 1 TB Fast Data Transfer i 10 mln Edge Requests przed naliczaniem dalszego użycia zgodnie z planem. Szczegóły opisuje [Vercel Pro Plan](https://vercel.com/docs/plans/pro-plan).

**Wybierać, gdy:** czas zespołu, preview deployments i minimalne ryzyko Next.js mają większą wartość niż najniższy rachunek.

### Wszystkie warianty na Cloudflare Workers

Cloudflare ma oficjalne ścieżki dla Next.js przez OpenNext, Nuxt przez preset Nitro, SvelteKit przez `@sveltejs/adapter-cloudflare` i Astro przez `@astrojs/cloudflare`. Workers Paid kosztuje minimum **$5/mies.**, obejmuje 10 mln requestów i 30 mln ms CPU; egress nie jest dodatkowo płatny. Requesty do statycznych assetów są bezpłatne i nielimitowane. Aktualne zasady publikuje [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/).

**Ryzyko:** Next.js działa przez adapter OpenNext i runtime `workerd`, więc przy aktualizacji trzeba sprawdzić [macierz wspieranych funkcji](https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/). Nuxt, SvelteKit i Astro także wymagają testu używanych bibliotek pod runtime'em Workers.

**Wybierać, gdy:** zespół zna Cloudflare, potrafi diagnozować adapter/runtime i realnie skorzysta z niższego kosztu oraz braku egressu.

### Hosting statyczny

Astro, prerenderowany SvelteKit i `nuxt generate` mogą działać jako same assety. Jest to najtańszy i najprostszy wariant infrastrukturalny, ale treść zmienia się dopiero po buildzie. Dla Prismic trzeba policzyć czas builda, kolejkę CI, liczbę stron × locale i wpływ na marketing.

Nie warto oszczędzać $5–20 miesięcznie kosztem kilku minut oczekiwania na każdą publikację, utraty preview albo dodatkowej dynamicznej aplikacji tylko dla redaktorów.

## Technologie opcjonalne — dodawać dopiero po spełnieniu warunku

| Technologia | Dodaj, gdy | Nie dodawaj, gdy |
|---|---|---|
| **Crowdin** | Jest wiele locale, formalny workflow, glossary i zespół localization | Są dwa proste języki i sporadyczne tłumaczenia |
| **VWO/Amplitude Experiment** | Istnieje ruch, hipoteza, owner i proces analizy | A/B testing jest tylko pozycją na roadmapie |
| **Algolia/Typesense** | Content API nie daje potrzebnego full-text, rankingów lub facetów | Wystarczą listingi i filtry po znanych polach |
| **Sentry** | Serwis ma krytyczne formularze, integracje i dynamiczne ścieżki | Istniejące APM klienta już pokrywa frontend |
| **Storybook/Histoire** | Biblioteka slices jest duża, współdzielona i często zmieniana | Projekt ma kilka stabilnych komponentów |
| **Motion/GSAP** | Istnieje system motion lub złożona choreografia scroll | Wystarczą CSS transitions i pojedyncze animacje |
| **Feature flags** | Potrzebne są rollouty i server-side experiments | Flagi byłyby permanentną konfiguracją treści |
| **Własny backend** | Potrzebne są sekrety, kolejki, agregacja lub niezawodny workflow | Framework i istniejące SaaS-y pokrywają przypadek |
| **DAM** | Prawa, akceptacje, wiele marek i kanałów przekraczają Media Library | Potrzebna jest zwykła biblioteka obrazów i plików |

## Czego nie budować w pierwszej wersji

- uniwersalnego edytora dowolnego layoutu;
- pola do wklejania dowolnego JavaScriptu;
- własnego systemu A/B testingu;
- własnej platformy formularzy, jeśli HubSpot/GetResponse spełnia wymagania;
- drugiego frontendu tylko dla innego frameworka;
- mikrofrontendów bez niezależnych zespołów i cykli wdrożeniowych;
- zewnętrznego search bez wymagań wykraczających poza API i filtry;
- personalizacji każdego slice'a od pierwszego wydania;
- AI publikującego bez draftu, walidacji i akceptacji;
- nowego projektu w Slice Machine;
- statycznego eksportu tylko dlatego, że hosting runtime kosztuje kilka dolarów.

## Rekomendowane warianty wdrożenia

### Wariant A — najmniejsze ryzyko pełnego zakresu

**Prismic Medium + Next.js 16 + TypeScript + React + Vercel**

Najlepszy default dla pełnego zakresu referencyjnego i zespołu React. Minimalizuje pracę nad preview, formularzami, personalizacją i dynamicznymi integracjami. Koszt hostingu jest wyższy niż czysta statyka, ale niski wobec kosztu developmentu.

### Wariant B — pełny zakres dla organizacji Vue

**Prismic Medium + Nuxt 4 + TypeScript + Vue + Vercel/Cloudflare**

Równorzędny funkcjonalnie wariant, często najtańszy dla firmy używającej Vue. `@nuxtjs/prismic` ogranicza boilerplate, a Nitro ułatwia hybrydowe renderowanie i przenoszenie hostingu.

### Wariant C — lekki full-stack

**Prismic Medium + SvelteKit + TypeScript + Cloudflare Workers**

Dobry dla zespołu Svelte, umiarkowanej personalizacji i potrzeby niskiego JS. Nie wybierać bez potwierdzonego ownera utrzymania oraz dostępności kompetencji.

### Wariant D — najniższy koszt content-first

**Prismic Small/Medium + Astro + TypeScript + Cloudflare static assets/Workers**

Najlepszy dla bloga, help center, dokumentacji lub uproszczonej strony marketingowej. Wymaga spike'u integracji Type Buildera i preview. Small wystarcza tylko, gdy zespół nie potrzebuje rozdzielenia writer/publisher.

### Wariant E — proof of concept

**Prismic Free + docelowy framework + bezpłatny hosting**

PoC powinien sprawdzić pełny pion: Type Builder, 3–5 slices, wygenerowane typy, live i full preview, dodatkowe locale, formularz, SEO, webhook oraz pomiar eventu. Nie prototypować w innym frameworku niż planowany produkcyjnie.

## Ostateczna rekomendacja dla pełnego zakresu referencyjnego

1. Wybrać **Next.js**, jeśli organizacja nie ma silnej preferencji frameworkowej, albo **Nuxt**, jeśli istnieje kompetencja i design system Vue.
2. Użyć **Prismic Medium**, ponieważ pełny zakres zakłada bezpieczne rozdzielenie tworzenia i publikowania treści.
3. Rozpocząć na Type Builderze i Prismic CLI; nie budować nowego workflow na Slice Machine.
4. Zachować runtime dla preview, rewalidacji, formularzy i personalizacji; publiczne strony renderować statycznie lub cache'ować tam, gdzie to możliwe.
5. HubSpot/GetResponse, Crowdin, VWO i Amplitude integrować jako systemy wyspecjalizowane.
6. Najpierw zbudować ograniczoną bibliotekę slices oraz pełny cykl draft → preview → Release → publish.
7. SvelteKit wybrać tylko z potwierdzonym ownershipem zespołu; Astro po ograniczeniu zakresu lub dla osobnego content produktu.
8. Hosting wybrać po spike'u kluczowych funkcji, nie na podstawie samej ceny bazowej.
9. AI używać do modeli, scaffoldu i draftów, ale utrzymać testy oraz human review.
10. Migrację wycenić na reprezentatywnej próbce, zanim zostanie zamknięty budżet frontendu i content operations.

Taki wariant maksymalizuje autonomię marketingu bez budowy własnego page buildera, a koszt kontroluje przez jeden frontend, first-party integrację, statyczne renderowanie tam, gdzie ma sens, i etapowanie funkcji o niepotwierdzonej wartości.

## Źródła

- Prismic: [Frameworks](https://prismic.io/docs/frameworks), [Next.js](https://prismic.io/docs/nextjs), [Nuxt](https://prismic.io/docs/nuxt), [SvelteKit](https://prismic.io/docs/sveltekit)
- Prismic: [Type Builder](https://prismic.io/docs/type-builder), [CLI](https://prismic.io/docs/cli), [Preview](https://prismic.io/features/preview)
- Prismic: [2026 JavaScript packages](https://prismic.io/updates/developer-experience), [Prismic MCP](https://prismic.io/docs/mcp)
- Next.js: [App Router](https://nextjs.org/docs/app), [Draft Mode](https://nextjs.org/docs/app/guides/draft-mode), [ISR](https://nextjs.org/docs/app/guides/incremental-static-regeneration), [Static Exports](https://nextjs.org/docs/app/guides/static-exports)
- Nuxt: [Rendering modes and route rules](https://nuxt.com/docs/4.x/guide/concepts/rendering), [Nitro server engine](https://nuxt.com/docs/4.x/guide/concepts/server-engine)
- SvelteKit: [Page options and prerendering](https://svelte.dev/docs/kit/page-options), [Adapters](https://svelte.dev/docs/kit/adapters)
- Astro: [Islands architecture](https://docs.astro.build/en/concepts/islands/), [On-demand rendering](https://docs.astro.build/en/guides/on-demand-rendering/), [Server islands](https://docs.astro.build/en/guides/server-islands/)
- Cloudflare: [Automatic framework configuration](https://developers.cloudflare.com/workers/framework-guides/automatic-configuration/), [Next.js](https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/), [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/)
- Vercel: [Pro Plan](https://vercel.com/docs/plans/pro-plan), [Pricing](https://vercel.com/docs/pricing)
