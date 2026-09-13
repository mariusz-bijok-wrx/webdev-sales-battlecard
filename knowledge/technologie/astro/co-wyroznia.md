# Co wyróżnia Astro

> **W skrócie:** Astro warto wybrać wtedy, gdy strona jest **treściowa i marketingowa**, a priorytetem są wydajność, SEO i niski koszt hostingu. Najmocniejsze strony to domyślnie statyczny HTML z minimalnym JavaScriptem, bardzo tani hosting i swoboda wyboru CMS-a. Ceną jest to, że Astro to framework, a nie CMS — marketing potrzebuje osobnego CMS-a, a każda nowa sekcja i funkcja dynamiczna wymaga developera.

Stan analizy: **13 września 2026 r.** Kwoty w USD, bez podatków.

Powiązane: [`potrzeby-biznesowe-klienta.md`](./potrzeby-biznesowe-klienta.md), [`stack-technologiczny.md`](./stack-technologiczny.md).

## Najpierw biznes: ile kosztuje Astro?

Astro jest darmowy (open source, MIT). Budżet tworzą:

1. **wdrożenie** — frontend w kodzie, komponenty, integracja z CMS-em;
2. **CMS** — Astro nie ma panelu dla marketingu; do wyboru headless CMS z `knowledge/technologie/`;
3. **hosting** — statyczny hosting lub Workers;
4. **utrzymanie** — aktualizacje frameworka i zależności, rozwój sekcji.

### Typowy koszt zewnętrzny

| Pozycja | Wariant | Cena |
|---|---|---|
| Framework | Astro | **$0** |
| Hosting | **Cloudflare Workers** — statyczne assety bezpłatne i bez limitu; Workers Paid przy SSR | **$0** lub **$5/mies.** (10 mln requestów) |
| Hosting alternatywny | Vercel Pro | $20/mies. za miejsce |
| CMS — przykład | **Sanity Growth** | $15/miejsce/mies. (Free na start) |
| CMS — przykład | **Prismic Small** | $25/mies. (7 użytkowników, 4 języki) |
| CMS — przykład | **Strapi Cloud Pro + Growth** | $135/mies. |

Przykład: Astro + Sanity Growth (3 redaktorów) + Cloudflare Workers Paid → **$45 + $5 = $50/mies., ok. $600/rok**. Ceny CMS i hostingu według plików w `knowledge/technologie/` (stan lipiec 2026).

### Gdzie naprawdę powstają oszczędności

- **Hosting prawie za darmo** — statyczne strony nie zużywają compute; skoki ruchu nie podnoszą rachunku.
- **Performance „z pudełka”** — HTML bez zbędnego JS; łatwiej osiągnąć wysokie Core Web Vitals niż w WordPressie z wtyczkami czy Webflow z interakcjami.
- **Brak licencji frameworka i brak lock-in platformy** — kod należy do klienta, CMS i hosting można wymienić.
- **Mała powierzchnia ataku** — brak serwera aplikacyjnego i wtyczek PHP.

### Ryzyko kosztowe, które trzeba kontrolować

- **Każda zmiana poza treścią wymaga developera** — nowy typ sekcji, formularz z logiką, integracja.
- **Dwa systemy** — framework i CMS mają osobne aktualizacje i koszty.
- **Brak doświadczenia w portfolio** — `db.csv` nie zawiera projektów Astro (stan 13.09.2026); pierwsze wdrożenia niosą ryzyko estymacji.
- **Funkcje dynamiczne** (personalizacja, logowanie, eksperymenty server-side) wymagają SSR lub osobnych usług — mniej naturalne niż w Next.js.

**Rekomendacja kosztowa:** najniższe TCO dla serwisu content-first z headless CMS-em. Nie wybierać Astro tylko dla taniego hostingu, jeśli zakres jest mocno dynamiczny — różnica zostanie wydana na obejścia.

## Co Astro robi inaczej

1. **Islands architecture** — strona to statyczny HTML, a JavaScript ładuje się tylko dla wybranych interaktywnych „wysp” (React, Vue, Svelte). [Dokumentacja](https://docs.astro.build/en/concepts/islands/).
2. **Content layer** — jedno API do treści z plików Markdown, CMS-ów i API. **Live Content Collections** (stabilne od Astro 6, marzec 2026) pobierają treść w chwili żądania — zmiana w CMS jest widoczna bez przebudowy strony.
3. **Framework, nie platforma** — hosting na Cloudflare, Vercel, Netlify lub statycznie gdziekolwiek.
4. **Cloudflare jako właściciel** — od 16 stycznia 2026 zespół Astro jest częścią Cloudflare; framework pozostaje MIT, z deklaracją wspierania wszystkich platform hostingowych. Astro 6 uruchamia serwer developerski na runtime Workers.

## Jak Astro odpowiada na typowe potrzeby klienta

| Potrzeba | Odpowiedź Astro | Na co uważać |
|---|---|---|
| **Edycja bez developera** | Przez headless CMS | Zależy od wybranego CMS-a i jakości modelu sekcji |
| **Wydajność i SEO** | Statyczny HTML, minimalny JS, wbudowane API fontów i obrazów | Ciężkie wyspy React niwelują przewagę |
| **Wiele języków** | Routing i18n wbudowany | Treść tłumaczona w CMS-ie |
| **Personalizacja i A/B** | Przez SSR/edge lub narzędzia client-side | Mniej dojrzałe niż w Next.js |
| **Formularze** | Embed HubSpot/GetResponse lub endpoint serwerowy | Endpoint wymaga SSR |
| **Podgląd zmian** | Visual Editing zależnie od CMS-a (np. Sanity) | Podgląd mniej płynny niż w Next.js (przeładowanie strony) |
| **Przenośność** | Otwarty kod, dowolny hosting i CMS | Migracja komponentów przy zmianie frameworka |

## Kiedy Astro jest szczególnie dobrym wyborem

- serwis marketingowy, blog, dokumentacja, landing pages;
- wydajność i SEO/AEO są kluczowe;
- klient chce **najniższego rachunku za hosting** i braku lock-in;
- zakres dynamiczny jest ograniczony;
- design ma własny, dopracowany system komponentów.

## Kiedy lepiej rozważyć inne rozwiązanie

- marketing chce budować strony wizualnie bez developera — **Webflow**;
- strona jest sklepem — **Shopify**;
- dużo logiki aplikacyjnej, personalizacji, logowania — **Next.js + headless CMS**;
- klient potrzebuje CRM, personalizacji i testów w jednym systemie — **HubSpot**;
- klient nie ma budżetu na developera przy każdej nowej sekcji — **WordPress** lub **Webflow**.

## Źródła

- [Astro 6.0](https://astro.build/blog/astro-6/) (marzec 2026)
- [The Astro Technology Company joins Cloudflare](https://astro.build/blog/joining-cloudflare/) (16.01.2026)
- [Astro — Islands architecture](https://docs.astro.build/en/concepts/islands/)
- Ceny Sanity, Prismic, Strapi, Vercel i Cloudflare: [`../sanity/`](../sanity/co-wyroznia.md), [`../prismic/`](../prismic/co-wyroznia.md), [`../strapi/`](../strapi/stack-technologiczny.md)
- `db.csv` — brak projektów Astro
