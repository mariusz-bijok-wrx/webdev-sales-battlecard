# Typowe potrzeby biznesowe klienta wobec CMS-a, które może pokryć HubSpot CMS

> **Najważniejsza zasada:** HubSpot CMS pokrywa najwięcej potrzeb **bez integracji**, gdy strona służy marketingowi i sprzedaży w ekosystemie HubSpot. Im bardziej potrzeba dotyczy danych spoza HubSpot, logiki aplikacyjnej albo wielu kanałów poza stroną, tym szybciej rośnie koszt obejść lub konieczność planu Enterprise.

Stan analizy: **13 września 2026 r.** Dokument uzupełnia [`co-wyroznia.md`](./co-wyroznia.md) i koncentruje się na potrzebach klienta, nie na liście funkcji.

## Jak czytać tę listę

Każdą potrzebę oznaczono poziomem pokrycia:

- **HubSpot** — pokrywa platforma bez dodatkowego developmentu poza konfiguracją;
- **HubSpot + development** — potrzebne są własne moduły, szablony HubL lub CMS React;
- **HubSpot Enterprise** — funkcja istnieje, ale wymaga najwyższego planu;
- **HubSpot + integracja** — potrzebna jest usługa zewnętrzna lub synchronizacja danych;
- **poza HubSpot** — lepiej rozwiązać inną technologią.

## Potrzeby podstawowe — wspólne dla większości klientów

### 1. Marketing publikuje bez oczekiwania na developera

**Pokrycie: HubSpot.** Edytor drag-and-drop pozwala tworzyć strony i landing pages z modułów motywu. Publikacja jest natychmiastowa, bez deployu i bez buildów.

**Warunek powodzenia:** motyw musi zawierać moduły pokrywające realne sekcje. Nowy typ sekcji wymaga developera HubL.

**Najniższy koszt:** gotowy motyw z Marketplace dostosowany do marki na start, własne moduły tylko dla sekcji, których brakuje.

### 2. Swoboda marketingu bez psucia design systemu

**Pokrycie: HubSpot + development.** Moduły mają zdefiniowane pola i style; drag-and-drop areas ograniczają, gdzie i co można wstawić. Ustawienia motywu centralizują kolory i typografię.

**Granica:** edytor pozwala czasem na więcej swobody stylów niż chciałby design system. Ograniczenia trzeba zaprojektować w polach modułów.

### 3. Podgląd zmian przed publikacją

**Pokrycie: HubSpot.** Edytor pokazuje stronę w kontekście, z podglądem desktop/mobile i linkiem podglądu. Content staging (Professional+) pozwala przebudować serwis bez naruszania produkcji.

### 4. Bezpieczne drafty, publikowanie i wycofywanie zmian

**Pokrycie: HubSpot.** Drafty, zaplanowana publikacja, historia wersji stron z przywracaniem. Zatwierdzanie treści przed publikacją w Professional+.

**Granica:** skoordynowana publikacja wielu stron naraz (release) nie jest mechanizmem pierwszej klasy; content staging dotyczy głównie przebudowy serwisu.

### 5. Współpraca wielu osób nad treścią

**Pokrycie: HubSpot.** Komentarze, zadania i przypisania w ramach HubSpot. Każdy edytujący to płatne miejsce.

**Wpływ na koszt:** interesariusze bez edycji nie powinni dostawać płatnych miejsc; sprawdzić dostępne role tylko do podglądu.

### 6. Role i rozdzielenie odpowiedzialności

**Pokrycie: HubSpot / HubSpot Enterprise.** Uprawnienia per narzędzie (blog, strony, landing pages) i zatwierdzanie treści są w Professional. Ograniczanie dostępu per zespół, rynek lub markę (partycjonowanie) oraz SSO — w Enterprise.

### 7. Reużywalna i spójna treść

**Pokrycie: HubSpot + development.** Globalne moduły i partiale (nagłówek, stopka, CTA), HubDB jako tabele danych (Professional+), content embeds do współdzielenia bloków.

**Granica:** HubDB to tabele, a nie pełny model treści z relacjami jak w headless CMS.

### 8. Zarządzanie stronami, URL-ami i nawigacją

**Pokrycie: HubSpot.** Slugi, menu nawigacji, rejestr przekierowań URL i domeny zarządzane w panelu, bez udziału developera.

### 9. Zarządzanie assetami

**Pokrycie: HubSpot.** Menedżer plików z CDN, automatyczna optymalizacja obrazów, hosting wideo (limity per plan: 150 filmów Professional, 500 Enterprise).

**Granica:** brak zaawansowanego DAM z prawami licencyjnymi.

### 10. Wydajność, dostępność i responsywność

**Pokrycie: HubSpot + development.** Hosting z CDN i alertami kodu (Professional+). Jakość HTML, dostępność i Core Web Vitals zależą od motywu i modułów.

**Ryzyko:** skrypty HubSpot (tracking, formularze, chat) dokładają JavaScript; trzeba to uwzględnić w budżecie performance.

## Potrzeby wzrostu i skalowania

### 11. Wiele języków i rynków

**Pokrycie: HubSpot.** Warianty językowe stron, landing pages i blogów są powiązane ze sobą; tłumaczenie AI treści. Limity języków zależą od planu (katalog produktu: Starter do 50, Professional/Enterprise bez limitu — do potwierdzenia przy zakupie).

**Granica:** każdy język to osobna strona do utrzymania; integracja z TMS (np. Crowdin) wymaga API lub aplikacji z Marketplace.

### 12. Omnichannel i wiele serwisów

**Pokrycie: HubSpot Enterprise / poza HubSpot.** Multisite (domena główna + 9 dodatkowych) jest w Enterprise. Zasilanie aplikacji mobilnej lub produktu treścią z HubSpot przez API jest możliwe, ale to nie jest główny scenariusz platformy.

### 13. SEO i widoczność w wyszukiwarkach oraz systemach AI

**Pokrycie: HubSpot.** Metadane, canonicale, sitemap, rekomendacje SEO i audyt (Professional+), integracja z Google Search Console.

**Granica:** structured data i `llms.txt` wymagają ręcznej konfiguracji w szablonach.

### 14. Formularze, lead generation i CRM

**Pokrycie: HubSpot — najmocniejszy obszar.** Formularze natywne, progresywne pola, zgody, CTA, chat, zapisy do CRM, workflow po zgłoszeniu (zaawansowane automatyzacje w Marketing Hub).

**Najniższy koszt:** nie budować żadnej warstwy formularzy — to przewaga, za którą klient płaci w abonamencie.

### 15. Integracje zarządzane per strona

**Pokrycie: HubSpot.** Kod w nagłówku/stopce per strona lub szablon, aplikacje z Marketplace.

**Ryzyko:** dowolny kod wklejany przez marketing w nagłówek strony — ustalić zasady i kto zatwierdza.

### 16. Analityka i kontrola jakości danych

**Pokrycie: HubSpot.** Analityka ruchu, źródeł, konwersji i atrybucji przychodu w jednym miejscu. GA4 i inne narzędzia można dodać obok.

### 17. Eksperymenty A/B

**Pokrycie: HubSpot (Professional+).** A/B testing i adaptive testing stron i landing pages.

**Granica:** testy per strona; testy wielu elementów w wielu miejscach lub server-side eksperymenty wymagają zewnętrznego narzędzia.

### 18. Personalizacja i dynamiczne ścieżki użytkownika

**Pokrycie: HubSpot (Professional+).** Smart content na podstawie kraju, urządzenia, źródła, języka, listy lub etapu lejka kontaktu z CRM.

**Granica:** dane spoza HubSpot trzeba najpierw zsynchronizować do CRM.

### 19. Interaktywne komponenty, animacje i embedy

**Pokrycie: HubSpot + development.** Moduły z własnym JS/CSS; CMS React dla komponentów React.

**Granica:** logika wymagająca serwera (kalkulator z sekretem API, własne endpointy) wymaga funkcji serverless — dla CMS wg dokumentacji developerskiej Enterprise.

### 20. Wyszukiwanie i filtrowanie treści

**Pokrycie: HubSpot + development.** Wbudowana wyszukiwarka stron i blogów; listingi z HubDB.

**Granica:** zaawansowane facety i duże katalogi — zewnętrzny silnik wyszukiwania.

## Potrzeby organizacji dojrzałej lub regulowanej

### 21. Bezpieczeństwo, SSO i compliance

**Pokrycie: HubSpot / HubSpot Enterprise.** Zarządzany hosting z WAF, SSL i monitoringiem; SSO, logi aktywności i sandboxy w Enterprise.

**Granica:** dane leadów i kontaktów są przechowywane w HubSpot — potwierdzić z działem prawnym region danych i umowy powierzenia.

### 22. Historia, audyt i odzyskiwanie

**Pokrycie: HubSpot.** Historia wersji stron; logi aktywności w Enterprise.

### 23. Przenośność i ograniczenie vendor lock-in

**Pokrycie: słabe.** Treść można wyeksportować, ale motyw HubL, moduły, HubDB, smart content i raporty nie przenoszą się. To świadomy kompromis za wygodę i integrację z CRM.

### 24. AI-assisted content operations

**Pokrycie: HubSpot.** Generowanie treści, Content Remix, brand voice, tłumaczenia AI — rozliczane kredytami HubSpot.

## Zakres typowego pełnego serwisu SaaS

Dla porównania z Sanity, Strapi i Prismic ta sama lista 14 grup wymagań:

| Grupa wymagań | Pokrycie HubSpot | Komentarz |
|---|---|---|
| Ownership marketingu i strony | **bardzo dobre** | Marketing tworzy strony bez developera |
| Page building i komponenty | **dobre** | Moduły HubL; nowe sekcje wymagają developera |
| Mobile i wysokie rozdzielczości | **dobre** | Zależy od jakości motywu |
| Template pages i preview | **bardzo dobre** | Szablony i podgląd natywnie |
| Lokalizacja i Crowdin | **dobre** | Warianty językowe natywnie; Crowdin przez integrację |
| Formularze i thank-you pages | **bardzo dobre** | Natywne formularze HubSpot — brak integracji |
| Nawigacja i breadcrumbs | **dobre** | Menu natywne; breadcrumbs w szablonie |
| Custom code, motion, embedy | **warunkowe** | Możliwe w modułach; logika serwerowa wymaga Enterprise |
| Integracje per strona | **dobre** | Kod per strona, Marketplace |
| Personalizacja | **bardzo dobre** | Smart content na danych CRM (Professional+) |
| Eksperymenty, analityka, SEO, AI visibility | **bardzo dobre** | A/B, adaptive testing, atrybucja w cenie |
| Workflow AI | **dobre** | Wbudowane AI rozliczane kredytami |
| Bezpieczeństwo i role | **warunkowe** | Partycjonowanie i SSO tylko Enterprise |
| Publikowanie, środowiska, wiele języków | **dobre** | Brak osobnych środowisk dev/stage/prod jak w kodzie; sandbox w Enterprise |

## Priorytetyzacja wdrożenia pod najniższy koszt

### Etap 1 — rdzeń o najwyższym zwrocie

- motyw z 10–20 modułami;
- strony, blog, nawigacja, redirecty;
- formularze i CTA podpięte do CRM;
- SEO i podstawowa analityka.

### Etap 2 — skalowanie operacji

- wersje językowe;
- HubDB i dynamiczne strony;
- testy A/B najważniejszych landing pages;
- zatwierdzanie treści.

### Etap 3 — funkcje wymagające dowodu wartości

- smart content dla segmentów;
- multisite i partycjonowanie (Enterprise);
- funkcje serverless i CMS React.

## Pytania discovery przed wyceną

1. Czy klient używa HubSpot CRM lub Marketing Hub? Jeśli nie — czy planuje migrację CRM?
2. Ile osób będzie edytować stronę (płatne miejsca)?
3. Ile domen, marek i rynków ma obsłużyć jeden system?
4. Czy potrzebne są SSO, partycjonowanie zespołów lub logi audytowe (Enterprise)?
5. Czy strona musi łączyć się z danymi produktu lub systemami spoza HubSpot?
6. Czy treść ma zasilać kanały inne niż strona www?
7. Jak ważna jest możliwość zmiany dostawcy w ciągu 3–5 lat?

## Źródła

- [HubSpot — Content Hub pricing](https://www.hubspot.com/pricing/content)
- [HubSpot Product & Services Catalog](https://legal.hubspot.com/hubspot-product-and-services-catalog)
- [HubSpot CMS overview](https://developers.hubspot.com/docs/cms/start-building/introduction/overview)
- [Navigating Serverless Functions on HubSpot's New Developer Platform](https://developers.hubspot.com/blog/navigating-serverless-functions-on-hubspots-new-developer-platform)
