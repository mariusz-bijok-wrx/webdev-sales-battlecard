# Stack technologiczny dla Webflow

> **Rekomendacja w jednym zdaniu:** dla serwisu marketingowego najlepszym domyślnym stackiem jest **Webflow Premium + Workspace Core/Growth + biblioteka komponentów i zmiennych + natywne formularze z integracją CRM**, a kod (code components przez DevLink, Webflow Cloud) dokładać tylko dla elementów, których nie da się zbudować wizualnie. **Webflow jako headless CMS dla Next.js** rzadko się opłaca — traci się Designer, a zostają limity CMS i abonament.

Stan analizy: **13 września 2026 r.** Dokument rozwija mapę potrzeb z [`potrzeby-biznesowe-klienta.md`](./potrzeby-biznesowe-klienta.md).

## Najpierw zasada kosztowa: budować wizualnie, kodować wyjątki

Przewagą Webflow jest to, że projektant i marketing pracują bez frontendu w kodzie. Każda warstwa kodu obok (custom code, code components, aplikacja w Webflow Cloud, zewnętrzny frontend) przywraca koszt developera, review i utrzymania. Najtańszy stack Webflow to **maksimum w Designerze i CMS, minimum kodu z jasno opisanym właścicielem**.

## Rekomendowana architektura bazowa

| Warstwa | Technologia | Odpowiedzialność | Dlaczego jest opłacalna |
|---|---|---|---|
| Design i frontend | **Webflow Designer** | Layout, style, responsywność, interakcje | Brak kodowania frontendu stron marketingowych |
| Design system | **Komponenty z właściwościami, zmienne, Shared Libraries** | Spójność marki, reużywalne sekcje | Marketing składa strony z zatwierdzonych bloków |
| Konwencja klas | **Client-First (Finsweet)** lub inna ustalona konwencja | Czytelna struktura klas | Łatwiejsze przekazanie projektu innej osobie |
| Treść | **Webflow CMS** (kolekcje, referencje) | Blog, case studies, zespół, oferty pracy | Szablony kolekcji generują strony automatycznie |
| Hosting | **Webflow Hosting** (CDN, SSL, DDoS, backupy) | Serwowanie strony | Zero utrzymania serwera |
| Animacje | **Interakcje GSAP w Webflow** | Scroll, hover, sekwencje | Bez ręcznego JS |
| Komponenty w kodzie | **Code components React przez DevLink** (Premium) | Kalkulatory, konfiguratory, widżety z logiką | Marketing konfiguruje propsy na canvasie |
| Aplikacje | **Webflow Cloud** — Next.js lub Astro pod domeną strony | Logowanie, dashboard, formularze z logiką serwerową | Jedna domena i jeden dostawca; SQLite/KV/storage obiektowy |
| Formularze i CRM | **Formularze Webflow + integracja** (aplikacja HubSpot/Salesforce, Zapier/Make) lub embed formularza CRM | Leady | CRM pozostaje właścicielem danych |
| Języki | **Localize Essential/Advanced** | Wersje językowe, `hreflang`, URL-e | Natywnie w Designerze i CMS |
| Analityka i testy | **GA4/GTM** lub **Analyze**; **Optimize** dla A/B i personalizacji | Pomiar i eksperymenty | Wybrać jedno źródło prawdy dla analityki |
| Filtry i wyszukiwanie | **Wyszukiwarka Webflow**; **Finsweet Attributes** dla filtrów i paginacji list | Listingi z filtrami | Bez własnego JS |
| Automatyzacja treści | **CMS API**, **MCP Webflow**, Make/Zapier | Import, synchronizacja, AI workflow | API 120 req/min w Premium, 600 w Team |

## Webflow natywnie czy headless?

### Webflow natywnie — domyślny wybór

**Najlepiej pokrywa:**

- strony marketingowe i produktowe SaaS;
- serwisy z mocnym designem i animacjami;
- landing pages kampanii budowane przez marketing;
- blog i case studies do kilku tysięcy elementów;
- zespoły bez developera frontendu.

**Koszt i ryzyka:**

- limity CMS (20 tys. elementów, 40 kolekcji w Premium);
- publikacja całej strony w self-serve (pojedyncze strony od Team);
- lock-in Designera, interakcji i CMS;
- brak kontroli nad serwerem i edge (nagłówki bezpieczeństwa od Team).

### Webflow + Webflow Cloud — strona i aplikacja pod jedną domeną

Webflow Cloud hostuje aplikacje **Next.js i Astro** z repozytorium GitHub, montowane pod ścieżką domeny strony (np. `example.com/app`) lub jako osobna aplikacja. Dostępne są bazy SQLite, magazyn klucz–wartość i storage obiektowy.

**Limity (stan 13.09.2026):**

| Zasób | Starter/Basic | Premium | Nadwyżka |
|---|---|---|---|
| Liczba aplikacji | 5 | 15 | — |
| Requesty | 1 mln/mies. | 2 mln/mies. | $2 za 1 mln |
| CPU | 15 min | 30 min | $2 za 5 h CPU |
| SQLite storage | 100 MB | 200 MB | $2 za 500 MB |

Transfer aplikacji jest wspólny z limitem transferu strony. Webflow informuje o nadwyżkach z co najmniej 30-dniowym wyprzedzeniem.

**Kiedy ma sens:** mała aplikacja lub formularz z logiką serwerową, który ma żyć pod domeną marketingową, bez osobnego hostingu. **Kiedy nie:** główna aplikacja produktu — lepiej dedykowana infrastruktura.

### Webflow jako headless CMS dla Next.js

CMS API i Content Delivery API pozwalają pobierać treść do zewnętrznego frontendu.

**Czego pozbawia:**

| Możliwość | Skutek headless | Typowe obejście |
|---|---|---|
| **Designer i interakcje** | Nie działają na zewnętrznym frontendzie | Kodowanie frontendu od nowa |
| **Page building przez marketing** | Marketing edytuje tylko dane CMS | Własny model sekcji |
| **Hosting w cenie** | Drugi hosting | Vercel/Cloudflare |
| **Localize, Optimize, Analyze** | Działają na stronach Webflow | Zewnętrzne narzędzia |

**Rekomendacja:** jeżeli frontend ma być w Next.js, porównać Sanity/Prismic/Strapi zamiast Webflow jako headless — mają bogatszy model treści, lepszy preview dla frontendu w kodzie i nie ograniczają liczby elementów w ten sam sposób.

## Porównanie pod kątem typowego pełnego zakresu serwisu SaaS

| Grupa wymagań | Webflow natywnie | Webflow + Cloud/DevLink | Komentarz kosztowy |
|---|---|---|---|
| Ownership marketingu i strony | **bardzo dobre** | **bardzo dobre** | Code components konfigurowalne na canvasie |
| Routing, URL-e i redirecty | **dobre** | **dobre** | Redirecty 301; brak middleware dla stron Webflow |
| Page building i komponenty | **bardzo dobre** | **bardzo dobre** | DevLink dla komponentów React |
| Template pages i listingi | **dobre** | **dobre** | Limity CMS decydują o planie |
| Lokalizacja i Crowdin | **dobre** | **dobre** | Localize per język + integracja TMS |
| Formularze i thank-you pages | **dobre** | **bardzo dobre** | Cloud dla formularzy z logiką serwerową |
| Motion, embedy, custom components | **bardzo dobre** | **bardzo dobre** | GSAP natywnie |
| Personalizacja | **warunkowe** | **warunkowe** | Optimize — osobny koszt |
| A/B testing i analytics | **dobre** | **dobre** | Optimize lub zewnętrzne narzędzie |
| SEO i LLM readiness | **bardzo dobre** | **bardzo dobre** | SEO/AEO wbudowane |
| Security, role i auth | **warunkowe** | **warunkowe** | SSO/role granularne w Enterprise |
| Draft, preview, staging | **dobre** | **dobre** | Branch staging i workflow publikacji od Team |

## Hosting i koszty infrastruktury

Hosting jest częścią Site planu: CDN, SSL, ochrona DDoS, backupy. Koszt zależy od transferu:

- Premium zawiera **50 GB/mies.** (według Webflow zwykle 5–25 tys. odsłon); więcej za dopłatą, np. 100 GB +$30/mies., 500 GB +$260/mies., 1 TB +$560/mies. (ceny przy rozliczeniu miesięcznym);
- Team do 30 TB/mies.;
- **dwa kolejne miesiące ponad limit powodują automatyczne podniesienie planu** — przy kampaniach i dużym ruchu ustawić monitoring.

Dostępność hostingu: Premium bez SLA; Team 99,0%; Enterprise 99,99%.

## Technologie opcjonalne — dodawać dopiero po spełnieniu warunku

| Technologia | Dodaj, gdy | Nie dodawaj, gdy |
|---|---|---|
| **Localize** | Więcej niż jeden język | Serwis jednojęzyczny |
| **Optimize** | Ruch min. kilkadziesiąt tys. odsłon, hipotezy i właściciel analizy | „A/B” tylko na roadmapie |
| **Analyze** | Marketing nie ma GA4 lub chce danych o ruchu z AI | GA4/Amplitude już pokrywa potrzeby |
| **Code components (DevLink)** | Interakcja wymaga logiki React | Da się zbudować interakcją GSAP |
| **Webflow Cloud** | Mała aplikacja pod domeną strony | Główna aplikacja produktu |
| **Finsweet Attributes** | Filtry, paginacja, sortowanie list CMS | Proste listingi |
| **Make/Zapier** | Integracje formularzy i CMS bez natywnej aplikacji | Istnieje natywna aplikacja Webflow |
| **Plan Team** | Workflow publikacji, branching, log aktywności, >40 kolekcji | Mały zespół i proste publikowanie |

## Czego nie budować w pierwszej wersji

- headless frontendu na Webflow CMS;
- custom code zamiast natywnych interakcji i komponentów;
- własnych filtrów w JS, jeżeli wystarczą atrybuty Finsweet;
- aplikacji produktowej w Webflow Cloud;
- personalizacji przed ustaleniem ruchu i hipotez;
- struktury CMS bez planu limitów elementów na 2–3 lata.

## Rekomendowane warianty wdrożenia

### Wariant A — najniższe TCO dla serwisu marketingowego

**Premium + Workspace Core + 1–2 pełne miejsca + ograniczone miejsca dla marketingu + formularze z integracją CRM**

Najlepszy dla serwisu SaaS lub firmowego do kilku tysięcy elementów CMS.

### Wariant B — wiele rynków

**Wariant A + Localize Advanced + integracja TMS**

Dla 3–10 języków z lokalizowanymi URL-ami. Uwzględnić, że wersje językowe zwiększają wolumen pracy nad treścią.

### Wariant C — marketing + lekka aplikacja

**Premium + code components (DevLink) + Webflow Cloud (Next.js/Astro)**

Dla kalkulatorów, konfiguratorów i małych aplikacji pod domeną strony. Przed decyzją spike: limity requestów i CPU, logowanie, dostęp do danych CMS z aplikacji.

### Wariant D — organizacja z governance

**Team lub Enterprise + Localize + Optimize + SSO (Enterprise)**

Dla zespołów potrzebujących workflow publikacji, logów, granularnych uprawnień i SLA. Porównywać z headless CMS przy tym poziomie budżetu.

## Źródła

- [Webflow — Plans & pricing](https://webflow.com/pricing) (stan 13.09.2026; limity Webflow Cloud, dodatków i transferu)
- [Webflow Blog — Simplified plans and updated pricing 2026](https://webflow.com/blog/simplified-plans-and-updated-pricing-2026)
- [Webflow Cloud — developer docs](https://developers.webflow.com/webflow-cloud/intro)
- [Code components](https://developers.webflow.com/code-components/introduction), [DevLink](https://webflow.com/feature/devlink), [DevLink overview](https://help.webflow.com/hc/en-us/articles/33961378995219-DevLink-overview)
