# Stack technologiczny dla Astro

> **Rekomendacja w jednym zdaniu:** dla serwisu content-first najlepszym domyślnym stackiem jest **Astro 6 + TypeScript + headless CMS (Sanity Growth domyślnie) + Cloudflare Workers**, z wyspami React tylko dla interaktywnych elementów. Gdy zakres zawiera dużo personalizacji, logowania i logiki serwerowej, lepszy jest **Next.js + ten sam CMS**.

Stan analizy: **13 września 2026 r.**

## Rekomendowana architektura bazowa

| Warstwa | Technologia | Odpowiedzialność | Dlaczego opłacalna |
|---|---|---|---|
| Framework | **Astro 6** | Routing, rendering, SEO, obrazy, fonty | Minimalny JS, darmowy |
| Język | **TypeScript** | Typy treści i komponentów | Mniej błędów integracji z CMS |
| Treść | **Sanity Growth** (domyślnie); Prismic lub Strapi zależnie od klienta | Model treści, edycja, podgląd, role | Oficjalne integracje z Astro |
| Pobieranie treści | **Content layer** — build-time collections; **Live Content Collections** dla treści zmieniających się często | Treść w HTML | Publikacja bez przebudowy przy live collections |
| Komponenty | **Komponenty Astro**, wyspy **React** tylko dla interakcji | Sekcje strony | Mniej JS niż pełny React |
| Style | **Tailwind CSS lub CSS Modules** | Tokeny, responsywność | Zgodnie z kompetencjami zespołu |
| Hosting | **Cloudflare Workers** (static assets + SSR tam, gdzie potrzebny) | CDN, SSR, edge | Statyka bezpłatna; Paid $5/mies. |
| Formularze | **Embed HubSpot/GetResponse** lub endpoint SSR | Leady | CRM właścicielem danych |
| Wyszukiwanie | **Pagefind** (statyczny indeks) | Wyszukiwarka treści | Bez usługi zewnętrznej |
| Jakość | **Vitest, Playwright, axe, Lighthouse CI** | Testy regresji | Utrzymanie wysokiego performance |

## Statyka czy SSR?

| Tryb | Kiedy | Koszt |
|---|---|---|
| **Statyczny (build)** | Treść zmienia się kilka razy dziennie lub rzadziej; publikacja przez webhook → build | Najniższy; build przy każdej publikacji |
| **Hybrydowy** | Większość stron statyczna, podgląd, formularze i wybrane strony renderowane na żądanie | Niski; rekomendowany domyślnie |
| **Live Content Collections** | Treść musi być widoczna natychmiast po publikacji | Requesty do CMS przy wizytach — kontrolować cache |

## Astro czy Next.js z tym samym CMS-em?

| Kryterium | Astro | Next.js |
|---|---|---|
| Performance „z pudełka” | **bardzo dobre** | dobre, wymaga dyscypliny |
| Hosting | **$0–5/mies.** | Vercel Pro od $20/mies. za miejsce |
| Podgląd na żywo w CMS | dobry (przeładowanie) | **bardzo dobry** (live) |
| Personalizacja, auth, logika serwerowa | warunkowe | **bardzo dobre** |
| Rynek developerów | mniejszy | **największy** |
| Doświadczenie w portfolio (`db.csv`) | **brak projektów** | 10+ projektów headless / Next.js |

## Porównanie pod kątem typowego zakresu

| Obszar | Astro + headless CMS | Komentarz |
|---|---|---|
| Implementation cost | **średni** | Frontend w kodzie + model CMS; brak godzin w `db.csv` |
| Technical SEO | **bardzo dobre** | Pełna kontrola HTML |
| Hosting | **najniższy** | Statyka bezpłatna |
| Performance | **bardzo dobre** | Minimalny JS |
| Content management | **zależy od CMS-a** | Sanity/Prismic dobre; nowe sekcje wymagają developera |
| API connection | **dobre** | Integracje w kodzie; SSR dla sekretów |
| Design development | **bardzo dobre** | Pełna swoboda w kodzie |
| Admin panel usability | **zależy od CMS-a** | Panel CMS-a, nie Astro |

## Czego nie budować w pierwszej wersji

- pełnej aplikacji React w wyspach — to sygnał, że lepszy jest Next.js;
- dwóch frameworków dla jednego serwisu;
- własnego CMS-a opartego o pliki Markdown dla marketingu;
- personalizacji server-side bez potwierdzonej potrzeby.

## Warianty wdrożenia

- **A — content-first, najniższe TCO:** Astro + Sanity Growth + Cloudflare Workers.
- **B — mały serwis, jeden redaktor:** Astro + Sanity Free lub Prismic Starter + hosting statyczny.
- **C — self-hosted CMS:** Astro + Strapi (Cloud lub self-hosted) + Cloudflare.
- **D — osobny blog/dokumentacja** obok głównego serwisu w Next.js.

## Źródła

- [Astro 6.0](https://astro.build/blog/astro-6/), [Astro joins Cloudflare](https://astro.build/blog/joining-cloudflare/)
- [Astro on Cloudflare Workers](https://developers.cloudflare.com/workers/framework-guides/web-apps/astro/), [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/)
- Analizy Astro jako frontendu: [`../sanity/stack-technologiczny.md`](../sanity/stack-technologiczny.md), [`../prismic/stack-technologiczny.md`](../prismic/stack-technologiczny.md), [`../strapi/stack-technologiczny.md`](../strapi/stack-technologiczny.md)
