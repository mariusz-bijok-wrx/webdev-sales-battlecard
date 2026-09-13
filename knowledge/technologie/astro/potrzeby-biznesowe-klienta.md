# Typowe potrzeby biznesowe klienta, które może pokryć Astro

> **Najważniejsza zasada:** Astro odpowiada za **to, co widzi użytkownik** — szybkość, SEO, wygląd. Za **to, co robi marketing** — edycję, podgląd, role — odpowiada wybrany CMS. Ocena Astro zawsze dotyczy pary: Astro + CMS.

Stan analizy: **13 września 2026 r.**

## Poziomy pokrycia

- **Astro** — framework pokrywa natywnie;
- **Astro + CMS** — zależy od CMS-a (Sanity, Prismic, Strapi);
- **Astro + SSR** — wymaga renderowania na serwerze/edge;
- **Astro + integracja** — usługa zewnętrzna.

## Potrzeby i pokrycie

| # | Potrzeba | Pokrycie | Komentarz |
|---|---|---|---|
| 1 | Marketing publikuje bez developera | **Astro + CMS** | Składanie stron z sekcji zdefiniowanych w CMS; nowa sekcja = developer |
| 2 | Spójny design system | **Astro** | Komponenty w kodzie, warianty w CMS |
| 3 | Podgląd przed publikacją | **Astro + CMS + SSR** | Visual Editing Sanity działa, ale z przeładowaniem strony |
| 4 | Drafty i wycofywanie zmian | **Astro + CMS** | Historia i drafty w CMS-ie |
| 5 | Praca wielu osób | **Astro + CMS** | Zależy od CMS-a |
| 6 | Role | **Astro + CMS** | Zależy od CMS-a |
| 7 | Reużywalna treść | **Astro + CMS** | Model treści w CMS, content layer w Astro |
| 8 | Strony, URL-e, nawigacja | **Astro** | Routing plikowy i dynamiczny; redirecty w konfiguracji lub hostingu |
| 9 | Assety | **Astro + CMS** | Komponent obrazów Astro, CDN obrazów CMS-a |
| 10 | Wydajność i dostępność | **Astro — najmocniejszy obszar** | Minimalny JS, statyczny HTML |
| 11 | Wiele języków | **Astro + CMS** | Routing i18n w Astro, tłumaczenia w CMS |
| 12 | Omnichannel | **CMS** | Treść w headless CMS służy też innym kanałom |
| 13 | SEO i AI visibility | **Astro — bardzo dobre** | Pełna kontrola HTML, sitemap, schema, `llms.txt` |
| 14 | Formularze i CRM | **Astro + integracja** | Embed CRM lub endpoint SSR |
| 15 | Integracje per strona | **Astro + CMS** | Rejestr integracji w kodzie, przełącznik w CMS |
| 16 | Analityka | **Astro + integracja** | GA4/Amplitude; Partytown dla skryptów zewnętrznych |
| 17 | A/B testy | **Astro + integracja / SSR** | Client-side łatwe; server-side wymaga SSR/edge |
| 18 | Personalizacja | **Astro + SSR (warunkowe)** | Mniej naturalna niż w Next.js |
| 19 | Interakcje i animacje | **Astro** | Wyspy React/Vue/Svelte, CSS, GSAP |
| 20 | Wyszukiwanie | **Astro + integracja** | Pagefind (statyczne) lub Algolia |
| 21 | Bezpieczeństwo, SSO | **Astro + CMS** | Mała powierzchnia ataku; SSO w CMS-ie |
| 22 | Historia i audyt | **CMS** | Zależy od planu CMS-a |
| 23 | Przenośność | **Astro — bardzo dobre** | Otwarty kod, dowolny hosting i CMS |
| 24 | AI w pracy nad treścią | **CMS** | Narzędzia AI CMS-a; kod Astro dobrze współpracuje z agentami AI |

## Pytania discovery przed wyceną

1. Jak często marketing będzie potrzebował **nowych typów sekcji** (a nie tylko nowych stron)?
2. Czy potrzebne są personalizacja, logowanie, eksperymenty server-side?
3. Jak ważny jest płynny podgląd na żywo podczas edycji?
4. Który CMS klient już zna lub preferuje?
5. Czy klient ma własnego developera frontendu do utrzymania?

## Źródła

- [Astro 6.0](https://astro.build/blog/astro-6/), [Islands architecture](https://docs.astro.build/en/concepts/islands/)
- Zob. [`co-wyroznia.md`](./co-wyroznia.md)
