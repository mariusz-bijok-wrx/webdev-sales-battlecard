# Stack technologiczny dla HubSpot CMS

> **Rekomendacja w jednym zdaniu:** dla serwisu marketingowego klienta pracującego w HubSpot CRM najlepszym domyślnym stackiem jest **HubSpot Content Hub Professional + własny motyw (HubL, moduły, CSS/JS) + natywne formularze i smart content**, bez osobnego frontendu i hostingu. Wariant **headless (Next.js + API HubSpot)** ma sens tylko wtedy, gdy strona musi być częścią aplikacji lub istniejącego frontendu, bo traci największą przewagę — edytor wizualny, personalizację i testy działające bez kodu.

Stan analizy: **13 września 2026 r.** Dokument rozwija mapę potrzeb z [`potrzeby-biznesowe-klienta.md`](./potrzeby-biznesowe-klienta.md).

## Najpierw zasada kosztowa: nie odtwarzać tego, za co klient już płaci

HubSpot w cenie abonamentu daje hosting, CDN, WAF, formularze, CRM, personalizację, testy A/B i analitykę. Każda warstwa dokładana obok (osobny hosting frontendu, własny backend formularzy, zewnętrzne narzędzie do testów) to podwójny koszt i utrata integracji z CRM. Najtańszy stack HubSpot to **najmniej technologii poza HubSpot**.

## Rekomendowana architektura bazowa

| Warstwa | Technologia | Odpowiedzialność | Dlaczego jest opłacalna |
|---|---|---|---|
| CMS i hosting | **HubSpot Content Hub Professional** | Strony, blog, landing pages, assety, CDN, SSL, WAF | Zero kosztów serwera i aktualizacji |
| Szablony | **Motyw HubSpot: HubL + HTML** | Szablony stron, drag-and-drop areas, globalne partiale | Natywny edytor wizualny bez budowania preview |
| Komponenty | **Moduły HubSpot** (HubL, CSS, JS); **CMS React** dla interaktywnych komponentów | Sekcje z polami do edycji przez marketing | Marketing składa strony z gotowych modułów |
| Style | **CSS/SCSS w motywie**, tokeny w ustawieniach motywu; Tailwind możliwy w buildzie lokalnym | Spójność marki, responsywność | Ustawienia motywu dostępne dla marketingu bez kodu |
| Dane strukturalne | **HubDB** (Professional+) lub **custom objects** (Enterprise) | Listingi, katalogi, lokalizacje, zespół | Dynamiczne strony bez osobnej bazy |
| Formularze i CRM | **Natywne formularze HubSpot + CRM** | Leady, zgody, workflow | Brak integracji do utrzymania |
| Personalizacja i testy | **Smart content, A/B i adaptive testing** | Warianty treści i CTA | W cenie Professional |
| Lokalny development | **HubSpot CLI** (`hs`), Git, GitHub Actions do wgrywania motywu | Wersjonowanie motywu, code review | Standardowy workflow zespołu |
| Logika serwerowa | **Funkcje serverless HubSpot** | Endpointy dla kalkulatorów, integracji z sekretami | Brak osobnego backendu; wg dokumentacji developerskiej wymagają Enterprise |
| Monitoring | **Code alerts HubSpot** (Professional+), opcjonalnie Sentry dla JS | Błędy szablonów i frontendu | Wbudowane w platformę |

## Tryb natywny czy headless?

### Natywny motyw HubSpot — domyślny wybór

Strony są renderowane i hostowane przez HubSpot. Marketing używa edytora drag-and-drop, smart content i testów A/B bez udziału developera.

**Najlepiej pokrywa:**

- landing pages i kampanie z formularzami;
- personalizację na podstawie danych CRM;
- testy A/B i adaptive testing;
- blog i content marketing z atrybucją leadów;
- klientów bez własnego zespołu DevOps.

**Koszt i ryzyka:**

- developer musi znać **HubL** — mniejszy rynek specjalistów niż React/PHP;
- złożone interakcje wymagają CMS React lub JS w modułach;
- ograniczona kontrola nad serwerem: brak middleware, niestandardowych nagłówków na poziomie edge, wyboru regionu;
- motyw i moduły nie są przenośne poza HubSpot.

### CMS React w HubSpot — komponenty React w motywie

HubSpot pozwala budować moduły w React i renderować je na stronach HubSpot (projekty CMS React zarządzane przez CLI). Daje zespołowi React znajome narzędzia bez rezygnacji z edytora i hostingu HubSpot.

**Uwaga:** projekty z endpointami API korzystają z funkcji serverless, które wg dokumentacji developerskiej wymagają **Content Hub Enterprise**. Platforma developerska HubSpot zmienia się dynamicznie (wersjonowanie projektów, deprecjacja Projects v2025.1 na 1 sierpnia 2026) — przed wyceną sprawdzić aktualną wersję platformy.

### Headless: Next.js + API HubSpot

HubSpot może udostępniać treść bloga, stron i tabel HubDB przez API, a formularze przez Forms API. Frontend Next.js/Astro renderuje stronę na Vercel lub Cloudflare.

**Kiedy ma sens:**

- strona marketingowa jest częścią istniejącej aplikacji Next.js;
- zespół klienta nie chce HubL, a HubSpot jest wymagany ze względu na CRM;
- potrzebna jest logika serwerowa i edge, której HubSpot nie oferuje.

**Czego pozbawia:**

| Możliwość | Skutek headless | Typowe obejście |
|---|---|---|
| **Edytor drag-and-drop** | Marketing edytuje dane, nie widzi strony | Własny preview — duży koszt |
| **Smart content** | Personalizacja HubSpot nie działa na zewnętrznym frontendzie | Własna logika na danych CRM przez API |
| **A/B i adaptive testing** | Nie działają poza stronami HubSpot | Zewnętrzne narzędzie eksperymentów |
| **Hosting w cenie** | Trzeba płacić i utrzymywać drugi hosting | Vercel/Cloudflare |
| **Raporty stron** | Analityka stron HubSpot ograniczona do tracking code | Tracking code HubSpot + GA4 |

**Rekomendacja:** headless na HubSpot zwykle łączy koszt abonamentu HubSpot z kosztem headless CMS-a, bez zalet żadnego z nich. Jeśli klient potrzebuje headless, lepiej porównać Sanity/Strapi/Prismic + integrację formularzy HubSpot.

## Hybryda: HubSpot jako CRM, inny CMS dla strony

Najczęstsza alternatywa: **Sanity/Prismic/Strapi/WordPress/Webflow + formularze i tracking HubSpot**. Leady nadal trafiają do CRM, tracking code śledzi wizyty, ale:

- smart content i testy HubSpot nie działają na stronach spoza HubSpot;
- raporty atrybucji stron są mniej szczegółowe;
- formularze embed lub Forms API trzeba utrzymywać;
- klient płaci za Marketing Hub (CRM i automatyzacje) zamiast Content Hub.

Wybrać hybrydę, gdy strona wymaga możliwości, których HubSpot CMS nie ma (omnichannel, aplikacja, wysoka elastyczność modelu treści), a personalizacja CRM na stronie nie jest krytyczna.

## Porównanie pod kątem typowego pełnego zakresu serwisu SaaS

| Grupa wymagań | HubSpot natywnie | HubSpot headless | Komentarz kosztowy |
|---|---|---|---|
| Ownership marketingu i strony | **bardzo dobre** | **warunkowe** | Natywnie brak kosztu preview |
| Routing, URL-e i redirecty | **dobre** | **bardzo dobre** | Natywnie redirecty w panelu; brak middleware |
| Page building i komponenty | **dobre** | **dobre** | HubL lub React; headless wymaga własnego edytora |
| Template pages i listingi | **bardzo dobre** | **dobre** | HubDB i dynamiczne strony |
| Lokalizacja i Crowdin | **dobre** | **dobre** | Crowdin przez integrację |
| Formularze i thank-you pages | **bardzo dobre** | **dobre** | Natywne formularze bez integracji |
| Motion, embedy, custom components | **dobre** | **bardzo dobre** | Headless daje pełny ekosystem React |
| Personalizacja | **bardzo dobre** | **słabe** | Smart content działa tylko natywnie |
| A/B testing i analytics | **bardzo dobre** | **warunkowe** | Testy HubSpot tylko natywnie |
| SEO i LLM readiness | **dobre** | **bardzo dobre** | Headless daje pełną kontrolę HTML |
| Security, role i auth | **warunkowe** | **warunkowe** | SSO i partycjonowanie tylko Enterprise |
| Draft, preview, staging | **dobre** | **warunkowe** | Natywnie podgląd i content staging |

## Hosting i koszty infrastruktury

W trybie natywnym **koszt hostingu jest zerowy poza abonamentem** — CDN, SSL, WAF i skalowanie pod ruch są w cenie. Nie ma opłat za transfer ani za skoki ruchu. To istotna różnica wobec WordPressa (hosting zarządzany) i headless CMS-ów (osobny hosting frontendu).

W trybie headless dochodzi hosting frontendu: Vercel Pro od $20/mies. za miejsce lub Cloudflare Workers od $5/mies. (ceny z analizy Sanity, 27.07.2026).

## Technologie opcjonalne — dodawać dopiero po spełnieniu warunku

| Technologia | Dodaj, gdy | Nie dodawaj, gdy |
|---|---|---|
| **Marketing Hub Professional** | Potrzebne są workflow, lead scoring, e-mail marketing | Klient potrzebuje tylko formularzy i CRM |
| **Content Hub Enterprise** | Multisite, SSO, partycjonowanie, serverless są krytyczne | Wystarczają funkcje Professional |
| **CMS React** | Zespół zna React i buduje interaktywne moduły | Moduły są proste i statyczne |
| **Zewnętrzny TMS (Crowdin)** | Wiele języków i proces tłumaczeń | Tłumaczenia AI HubSpot wystarczają |
| **GA4 obok analityki HubSpot** | Marketing ma istniejące raporty GA | Raporty HubSpot pokrywają potrzeby |
| **Headless frontend** | Strona jest częścią aplikacji | Strona jest marketingowa |

## Czego nie budować w pierwszej wersji

- własnego backendu formularzy — HubSpot Forms to przewaga platformy;
- zewnętrznego narzędzia A/B, jeśli Professional pokrywa testy stron;
- headless frontendu „na przyszłość”;
- dziesiątek wariantów smart content bez hipotez i ruchu;
- własnych funkcji serverless, dopóki nie ma planu Enterprise;
- osobnej bazy danych dla listingów, które mieszczą się w HubDB.

## Rekomendowane warianty wdrożenia

### Wariant A — najniższe TCO dla marketingu B2B

**Content Hub Professional + motyw HubL + natywne formularze + smart content**

Najlepszy, gdy klient ma HubSpot CRM. Brak hostingu, integracji i narzędzi zewnętrznych.

### Wariant B — wiele marek, rynków i zespołów

**Content Hub Enterprise + multisite + partycjonowanie + SSO**

Dla organizacji z kilkoma domenami i zespołami regionalnymi. Kosztowny, ale zastępuje kilka instalacji CMS.

### Wariant C — zespół React

**Content Hub Professional/Enterprise + CMS React + HubSpot CLI + GitHub Actions**

Dla klienta z zespołem React, który chce zostać przy edytorze HubSpot. Wymaga weryfikacji dojrzałości CMS React i planu dla funkcji serverless.

### Wariant D — hybryda

**Inny CMS dla strony + HubSpot Marketing Hub/CRM + formularze embed**

Gdy strona wymaga możliwości spoza HubSpot. Porównać z pełnym HubSpot CMS pod kątem utraty personalizacji i testów.

## Źródła

- HubSpot: [Content Hub pricing](https://www.hubspot.com/pricing/content), [Product & Services Catalog](https://legal.hubspot.com/hubspot-product-and-services-catalog)
- HubSpot developers: [CMS overview](https://developers.hubspot.com/docs/cms/start-building/introduction/overview), [React on HubSpot](https://developers.hubspot.com/react-on-hubspot)
- HubSpot developers: [Navigating Serverless Functions on the New Developer Platform](https://developers.hubspot.com/blog/navigating-serverless-functions-on-hubspots-new-developer-platform), [Projects v2025.1 deprecation](https://developers.hubspot.com/changelog/upcoming-deprecation-hubspot-projects-v2025-1-aug-1-2026)
- Vercel i Cloudflare: ceny przyjęte z [`../sanity/stack-technologiczny.md`](../sanity/stack-technologiczny.md) (stan 27.07.2026)
