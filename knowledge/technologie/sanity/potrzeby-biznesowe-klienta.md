# Typowe potrzeby biznesowe klienta wobec CMS-a, które może pokryć Sanity

> **Najważniejsza zasada:** klient rzadko potrzebuje „CMS-a”. Potrzebuje krótszego czasu publikacji, mniejszej zależności od developerów, spójnej treści, bezpiecznych zmian i możliwości skalowania na kolejne kanały oraz rynki. Sanity może być rdzeniem takiego rozwiązania, ale część potrzeb pokrywa bezpośrednio, część wspólnie z frontendem, a część dopiero przez integrację z wyspecjalizowanym narzędziem.

Stan analizy: **27 lipca 2026 r.** Dokument uzupełnia [`co-wyroznia.md`](./co-wyroznia.md) i koncentruje się na potrzebach klienta, nie na liście funkcji platformy.

## Jak czytać tę listę

Każdą potrzebę oznaczono jednym z czterech poziomów pokrycia:

- **Sanity** — główna odpowiedzialność leży w CMS-ie i Content Lake;
- **Sanity + frontend** — CMS przechowuje model i konfigurację, ale zachowanie realizuje warstwa webowa;
- **Sanity + integracja** — potrzebna jest usługa wyspecjalizowana, np. Crowdin, HubSpot albo narzędzie eksperymentacyjne;
- **poza CMS-em** — Sanity może dostarczać dane, lecz nie powinno być głównym narzędziem do rozwiązania problemu.

Takie rozróżnienie chroni budżet. Najdroższe wdrożenia powstają zwykle wtedy, gdy CMS próbuje zastąpić page builder, system analityczny, CRM, platformę eksperymentalną i aplikację produktową jednocześnie.

## Potrzeby podstawowe — wspólne dla większości klientów

### 1. Marketing publikuje bez oczekiwania na developera

**Potrzeba biznesowa:** skrócenie czasu od pomysłu do publikacji i odciążenie zespołu technicznego z prostych zmian tekstu, grafik, linków i układu strony.

**Pokrycie: Sanity + frontend.** Sanity Studio pozwala tworzyć i edytować dokumenty, a odpowiednio zaprojektowany model strony może składać się z bezpiecznych, reużywalnych sekcji. Publikacja treści nie wymaga deployu aplikacji, jeśli frontend używa rewalidacji, live content albo renderowania na żądanie.

**Warunek powodzenia:** wszystkie potrzebne sekcje muszą mieć implementację we frontendzie. Redaktor może układać i konfigurować istniejące komponenty, ale nie powinien tworzyć dowolnego HTML-a lub kodu produkcyjnego.

**Najniższy koszt:** zacząć od 10–20 najczęściej używanych sekcji pokrywających większość stron, zamiast od uniwersalnego page buildera.

### 2. Swoboda marketingu bez psucia design systemu

**Potrzeba biznesowa:** możliwość szybkiego tworzenia stron przy zachowaniu spójności marki, responsywności i dostępności.

**Pokrycie: Sanity + frontend.** Studio może ograniczać dozwolone warianty sekcji, kolory, rozmiary, kolejność elementów, liczbę CTA czy format assetów. Walidacje mogą blokować brakujące nagłówki, błędne linki lub niedozwolone kombinacje. Frontend odpowiada za responsywne zachowanie i egzekwowanie tokenów design systemu.

**Granica:** Sanity nie sprawi automatycznie, że dowolnie skonfigurowany komponent będzie poprawny na mobile. To odpowiedzialność implementacji, testów i procesu akceptacji komponentu.

**Najniższy koszt:** warianty zamiast surowych ustawień. Pole „układ: standardowy / odwrócony / wyróżniony” jest tańsze i bezpieczniejsze niż kilkanaście pól sterujących CSS-em.

### 3. Podgląd zmian przed publikacją

**Potrzeba biznesowa:** redaktor i interesariusz widzą finalną stronę, zanim zmiana trafi do klientów.

**Pokrycie: Sanity + frontend.** Drafty, Presentation Tool i Visual Editing pozwalają oglądać nieopublikowaną treść w kontekście strony, przechodzić z elementu podglądu do właściwego pola oraz obserwować zmiany. Zakres i płynność podglądu zależą od wybranego frameworka; [Visual Editing](https://www.sanity.io/docs/visual-editing) ma oficjalne integracje m.in. z Next.js i Astro.

**Najniższy koszt:** jeden chroniony preview oparty na tej samej aplikacji i komponentach co produkcja, zamiast osobnego środowiska odtwarzającego stronę.

### 4. Bezpieczne drafty, publikowanie i wycofywanie zmian

**Potrzeba biznesowa:** produkcja nie może zostać uszkodzona przez niekompletną lub przypadkową zmianę.

**Pokrycie: Sanity.** Draft oddziela pracę od treści opublikowanej. Historia dokumentu wspiera porównanie i przywracanie wersji. Growth udostępnia zaplanowane publikowanie pojedynczych draftów; rozbudowane Content Releases wielu dokumentów są funkcją określonych planów Enterprise. Szczegóły opisują [Scheduled Drafts](https://www.sanity.io/docs/studio/scheduled-drafts) i [Content Releases](https://www.sanity.io/docs/studio/content-releases).

**Granica:** klasyczny wieloetapowy approval flow, np. marketing → legal → country owner → publish, może wymagać własnych akcji, zadań, integracji albo funkcji Enterprise.

**Najniższy koszt:** użyć gotowych ról i prostego procesu draft → preview → publish, zanim powstanie własny silnik workflow.

### 5. Współpraca wielu osób nad treścią

**Potrzeba biznesowa:** eliminacja plików „final-v7”, blokowania dokumentów i uzgodnień rozproszonych po e-mailu lub komunikatorze.

**Pokrycie: Sanity.** Studio jest środowiskiem współdzielonym w czasie rzeczywistym. Growth dodaje komentarze, wzmianki i zadania. Viewerzy są bezpłatni, więc interesariusze mogą przeglądać i komentować bez zwiększania liczby płatnych miejsc.

**Najniższy koszt:** płatne role przydzielać osobom rzeczywiście tworzącym lub publikującym treść; pozostałym dać Viewer.

### 6. Role i rozdzielenie odpowiedzialności

**Potrzeba biznesowa:** marketer może zmieniać treść, ale nie tokeny, datasety i ustawienia techniczne; autor może pisać, lecz nie zawsze publikować.

**Pokrycie: Sanity.** Growth udostępnia gotowe role Administrator, Editor, Developer, Contributor i Viewer. Contributor może tworzyć drafty bez prawa publikacji. Własne role i granularne reguły dostępu są funkcją Enterprise. Aktualny model opisuje dokumentacja [Roles](https://www.sanity.io/docs/user-guides/roles).

**Najniższy koszt:** najpierw dopasować proces do pięciu gotowych ról Growth. Przechodzenie do Enterprise wyłącznie z powodu „idealnej” macierzy uprawnień powinno mieć uzasadnienie ryzykiem lub compliance.

### 7. Reużywalna i spójna treść

**Potrzeba biznesowa:** nazwa produktu, cennik, dane autora, komunikat prawny lub opis funkcji powinny być aktualizowane w jednym miejscu.

**Pokrycie: Sanity.** Ustrukturyzowane dokumenty i referencje pozwalają współdzielić dane między stronami oraz kanałami. GROQ umożliwia pobieranie powiązanych danych w formie potrzebnej frontendowi.

**Ryzyko:** nadmierna reużywalność może utrudnić redakcję. Nie każdy fragment tekstu musi być osobnym dokumentem.

**Najniższy koszt:** osobno modelować treści mające własny cykl życia, właściciela albo wiele miejsc użycia; pozostałe trzymać lokalnie w dokumencie strony.

### 8. Zarządzanie stronami, URL-ami i nawigacją

**Potrzeba biznesowa:** marketing tworzy strony, ustala slug, hierarchię, linkowanie wewnętrzne i elementy nawigacji.

**Pokrycie: Sanity + frontend.** Sanity może przechowywać strony, slugi, relacje parent/child, nawigacje i breadcrumbs. Własne inputy mogą pozwalać wybierać istniejącą stronę zamiast wklejać URL. Frontend buduje trasę, generuje breadcrumbs oraz rozstrzyga zachowanie brakujących i nieopublikowanych dokumentów.

**Granica:** redirect jest zachowaniem serwera lub CDN-u. Sanity może być źródłem reguł, ale egzekwuje je frontend albo platforma hostingowa.

**Najniższy koszt:** jeden typ linku wewnętrznego oparty na referencji i jeden rejestr redirectów z walidacją konfliktów.

### 9. Zarządzanie assetami

**Potrzeba biznesowa:** redaktor wybiera obrazy i pliki, kontroluje alt text, crop, proporcje oraz użycie materiału.

**Pokrycie: Sanity + frontend.** Sanity przechowuje assety i metadane, udostępnia Asset CDN oraz transformacje obrazów. Schemat może wymagać alternatywnego tekstu, określać hotspot i ograniczać typ pliku. Frontend dobiera format, rozmiar i sposób lazy loadingu.

**Granica:** zaawansowany DAM z prawami licencyjnymi, kampaniami, akceptacją assetów i biblioteką wielu marek może wymagać Media Library lub zewnętrznego DAM-u.

**Najniższy koszt:** nie wdrażać osobnego DAM-u, dopóki proces zarządzania prawami i liczbą assetów rzeczywiście go nie wymaga.

### 10. Wydajność, dostępność i responsywność

**Potrzeba biznesowa:** strona działa szybko, stabilnie i poprawnie na telefonach, dużych ekranach oraz dla osób korzystających z technologii asystujących.

**Pokrycie: głównie poza CMS-em.** Sanity dostarcza Content Lake, API CDN i Asset CDN. Schemat może wymagać danych potrzebnych dostępności, ale Core Web Vitals, HTML, CSS, responsywność, focus management i semantyka należą do frontendu.

**Najniższy koszt:** pre-renderować treść, ograniczyć JavaScript, stosować komponenty z przetestowanym zachowaniem oraz blokować publikację komponentu bez testów mobile i accessibility.

## Potrzeby wzrostu i skalowania

### 11. Wiele języków i rynków

**Potrzeba biznesowa:** jedna platforma obsługuje treści globalne i lokalne, różne slugi, terminy publikacji oraz wyjątki rynkowe.

**Pokrycie: Sanity + frontend + opcjonalna integracja.** Sanity obsługuje lokalizację na poziomie pól lub całych dokumentów i nie nalicza opłat za liczbę locale. Frontend odpowiada za routing językowy, `hreflang`, canonicale, mapę URL-i i redirecty. Crowdin lub inny TMS może obsłużyć właściwy proces tłumaczeń. Modele opisuje [Localization](https://www.sanity.io/docs/studio/localization).

**Wpływ na koszt:** lokalizacja dokumentowa mnoży liczbę dokumentów i może przyspieszyć dojście do limitu planu. Lokalizacja pól utrzymuje mniej dokumentów, ale komplikuje formularze i publikację niezależnych rynków.

**Najniższy koszt:** wybrać jeden model bazowy na podstawie realnego procesu; nie mieszać obu bez konkretnego powodu. Automatyzację z TMS wdrożyć po ustabilizowaniu schematów.

### 12. Omnichannel i wiele serwisów

**Potrzeba biznesowa:** ta sama treść zasila stronę marketingową, aplikację, centrum pomocy, ekrany produktu albo kolejne marki.

**Pokrycie: Sanity.** Ustrukturyzowana treść nie jest związana z jednym szablonem. API, klienty i webhooks umożliwiają wielu konsumentom korzystanie z Content Lake.

**Granica:** jeden globalny dataset nie zawsze jest najlepszy. Różne wymogi prawne, zespoły i cykle wdrożeń mogą wymagać podziału — a dodatkowe datasety w Growth są kosztowne.

**Najniższy koszt:** współdzielić tylko dane rzeczywiście wspólne i zacząć od jednego datasetu produkcyjnego plus prostego modelu środowisk.

### 13. SEO i widoczność w wyszukiwarkach oraz systemach AI

**Potrzeba biznesowa:** marketing kontroluje tytuły, opisy, canonicale, indeksowanie, structured data i linkowanie; treść może być prawidłowo interpretowana przez wyszukiwarki oraz crawlery AI.

**Pokrycie: Sanity + frontend.** CMS przechowuje metadane, relacje i semantyczne dane produktu, kategorii czy autora. Frontend generuje poprawny HTML, JSON-LD, sitemapę, `robots.txt`, canonicale i `hreflang`.

**Granica:** sam checkbox „SEO” w Studio nie gwarantuje widoczności. Potrzebne są jakość treści, indeksowalny rendering, wydajność, autorytet domeny oraz monitoring.

**Najniższy koszt:** centralny obiekt SEO ze zdrowymi defaultami i wyjątkami tylko tam, gdzie są potrzebne; structured data generować z właściwych modeli treści, nie z osobnego pola JSON.

### 14. Formularze, lead generation i CRM

**Potrzeba biznesowa:** marketer wybiera formularz, ustawia CTA i thank-you page, a lead trafia do HubSpot, GetResponse lub innego CRM-u.

**Pokrycie: Sanity + integracja + frontend.** Sanity może przechowywać identyfikator formularza, wariant prezentacji, zgody, thank-you page oraz wymagane zdarzenia analityczne. Frontend renderuje formularz lub bezpiecznie wysyła dane do dostawcy. CRM pozostaje właścicielem danych leadowych.

**Granica:** dane osobowe i zgłoszenia nie powinny trafiać do zwykłych dokumentów Sanity tylko dlatego, że CMS jest dostępny.

**Najniższy koszt:** użyć istniejących formularzy HubSpot/GetResponse i lekkiej konfiguracji w CMS-ie. Własny backend formularzy budować dopiero, gdy wymagane są wspólna walidacja, routing, antyspam lub niezawodna obsługa błędów poza możliwościami embedów.

### 15. Integracje zarządzane per strona

**Potrzeba biznesowa:** marketing włącza LiveChat, demo, tracking lub narzędzie kampanii tylko na wybranych stronach.

**Pokrycie: Sanity + frontend.** Dokument strony może zawierać listę dozwolonych integracji i ich bezpieczną konfigurację. Frontend warunkowo ładuje zatwierdzone moduły po spełnieniu warunków zgody.

**Ryzyko:** dowolne pole na JavaScript tworzy zagrożenie bezpieczeństwa, prywatności, wydajności i stabilności.

**Najniższy koszt:** rejestr integracji implementowanych w kodzie oraz prosty przełącznik w CMS-ie. Nowa integracja przechodzi jednorazowy review developerski, ale jej późniejsze włączanie per strona nie wymaga deployu.

### 16. Analityka i kontrola jakości danych

**Potrzeba biznesowa:** zespół mierzy konwersję i przed publikacją wie, czy komponent wyemituje właściwe zdarzenia.

**Pokrycie: Sanity + frontend + integracja.** Schemat komponentu może oferować zatwierdzony `event key`, a preview może pokazywać planowane eventy. Frontend emituje zdarzenie; Amplitude, GA lub inna platforma je przechowuje i analizuje.

**Najniższy koszt:** centralny, wersjonowany słownik eventów i automatyczne testy najważniejszych ścieżek. Nie pozwalać redaktorom wpisywać dowolnych nazw zdarzeń.

### 17. Eksperymenty A/B

**Potrzeba biznesowa:** marketing testuje komunikaty, sekcje, CTA lub całe URL-e i ocenia wpływ na wynik.

**Pokrycie: Sanity + integracja + frontend.** Sanity może przechowywać warianty treści albo identyfikatory eksperymentów. Losowanie wariantu, targeting, exposure event i statystyka powinny należeć do VWO, Amplitude Experiment lub innej platformy eksperymentalnej.

**Granica:** Sanity nie jest samodzielnym silnikiem eksperymentów. Publikowanie dwóch wersji treści bez poprawnej alokacji i ekspozycji nie tworzy wiarygodnego testu A/B.

**Najniższy koszt:** wykorzystać narzędzie analityczne już kupione przez klienta. Zacząć od testów URL lub kilku jawnych slotów wariantowych, zamiast budować uniwersalną warstwę eksperymentów w każdej sekcji.

### 18. Personalizacja i dynamiczne ścieżki użytkownika

**Potrzeba biznesowa:** treść, CTA lub oferta zależy od kampanii, segmentu, rynku, zachowania albo danych firmograficznych.

**Pokrycie: Sanity + frontend + integracja.** Sanity jest dobrym repozytorium wariantów oraz reguł opisanych w języku biznesowym. Rozpoznawanie użytkownika, ewaluacja reguł i ochrona prywatności należą do warstwy personalizacji, feature flags, CDP lub frontendu.

**Ryzyko:** liczba wariantów rośnie wykładniczo, preview staje się trudny, cache mniej skuteczny, a pomiar wyników niejednoznaczny.

**Najniższy koszt:** personalizować najpierw jeden lub dwa obszary o wysokiej wartości, np. hero i CTA na podstawie kampanii. Nie budować od razu osobnej wersji całej strony dla każdego segmentu.

### 19. Interaktywne komponenty, animacje i embedy

**Potrzeba biznesowa:** nowoczesny serwis SaaS potrzebuje interaktywnego hero, sliderów, kalkulatorów, demonstracji produktu, Lottie, SVG lub wideo.

**Pokrycie: Sanity + frontend.** CMS przechowuje treść, assety i bezpieczne parametry komponentu. Kod interakcji żyje we frontendzie. Zewnętrzne embedy powinny pochodzić z listy dozwolonych dostawców.

**Granica:** AI może przyspieszyć napisanie komponentu, ale nie zmienia wymagań review, wydajności, responsywności, dostępności i bezpieczeństwa.

**Najniższy koszt:** CSS i natywne API przeglądarki przed biblioteką; wspólne, testowane komponenty przed custom code per strona; lazy loading dla ciężkich interakcji.

### 20. Wyszukiwanie i filtrowanie treści

**Potrzeba biznesowa:** użytkownik znajduje artykuł, template, produkt lub dokument po frazie, kategorii i atrybutach.

**Pokrycie: Sanity + frontend; czasem integracja.** GROQ wystarcza do prostych listingów i filtrów. Zaawansowane full-text search, literówki, ranking behawioralny, facety oraz duża skala mogą wymagać Algolii, Typesense lub innego indeksu aktualizowanego webhookami.

**Najniższy koszt:** zacząć od filtrowania i wyszukiwania dostępnego w aktualnym zbiorze. Osobny silnik wdrożyć dopiero po zdefiniowaniu wymagań jakościowych i skali.

## Potrzeby organizacji dojrzałej lub regulowanej

### 21. Bezpieczeństwo, SSO i compliance

**Potrzeba biznesowa:** kontrola dostępu, centralne odbieranie uprawnień, prywatne dane, ślad zmian, SLA i zgodność z politykami organizacji.

**Pokrycie: Sanity + cała architektura.** Growth udostępnia prywatne datasety i gotowe role. SAML SSO, własne role, user attributes, dedykowane wsparcie i SLA znajdują się w Enterprise lub dodatkach. Bezpieczeństwo skryptów, formularzy, tokenów, preview i pipeline'u wdrożeniowego pozostaje odpowiedzialnością całego rozwiązania.

**Najniższy koszt:** wymagania compliance spisać przed wyceną. Nie kupować Enterprise „na wszelki wypadek”, ale też nie projektować obejść dla obowiązkowego SSO lub granularnych uprawnień.

### 22. Historia, audyt i odzyskiwanie

**Potrzeba biznesowa:** wiadomo kto i kiedy zmienił treść, można porównać wersje i odtworzyć poprzedni stan.

**Pokrycie: Sanity.** Studio i History API udostępniają rewizje dokumentów; zakres retencji zależy od planu. Eksport datasetu pozwala wykonywać niezależne kopie treści i assetów.

**Granica:** historia CMS-a nie zastępuje pełnej polityki backupu, disaster recovery ani audytu pozostałych systemów.

**Najniższy koszt:** ustalić wymagany RPO, RTO i czas retencji, a następnie automatyzować regularny eksport zamiast zakładać, że nieograniczona historia jest częścią każdego planu.

### 23. Przenośność i ograniczenie vendor lock-in

**Potrzeba biznesowa:** firma zachowuje dostęp do własnej treści i może zmienić frontend lub dostawcę.

**Pokrycie: Sanity.** Dataset można wyeksportować z dokumentami i assetami przez [`sanity datasets export`](https://www.sanity.io/docs/cli-reference/cli-datasets). Oddzielenie treści od prezentacji ułatwia wymianę frontendu.

**Granica:** GROQ, schematy, Studio, workflow i integracje są specyficzne dla Sanity. Eksport danych ogranicza lock-in danych, ale nie eliminuje kosztu migracji rozwiązania.

### 24. AI-assisted content operations

**Potrzeba biznesowa:** przyspieszenie tworzenia, tłumaczenia, audytu i masowej aktualizacji treści oraz programatyczne przygotowywanie draftów.

**Pokrycie: Sanity + integracja.** Content Agent, AI Assist i Agent Actions mogą pracować na ustrukturyzowanych dokumentach. API pozwala także tworzyć drafty przez zewnętrzny workflow. Najbezpieczniejszy model to AI przygotowujące propozycję, którą zatwierdza człowiek.

**Granica:** automatyczne generowanie stron bez walidacji może szybko zwiększyć liczbę dokumentów, koszty AI, duplikację i ryzyko SEO.

**Najniższy koszt:** najpierw deterministyczne operacje — duplikacja strony, wypełnienie znanych pól, walidacja i draft. Agenta z szeroką autonomią wdrażać dopiero po zebraniu powtarzalnych przypadków użycia.

## Wnioski z referencyjnego zakresu pełnego serwisu SaaS

Referencyjny zakres obejmuje 14 grup wymagań dla nowoczesnego serwisu SaaS. Są one reprezentatywne dla dojrzałych klientów marketingowych:

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

Sanity jest bardzo dobrym rdzeniem dla tego zakresu, ale **nie pokrywa samodzielnie żadnej z grup dotyczących zachowania finalnej strony**. Najpełniej odpowiada za ownership treści, komponentową konfigurację stron, preview, role, drafty, lokalizowane dokumenty i źródło konfiguracji integracji. Frontend odpowiada za routing, responsywność, SEO, interakcje i wydajność. Crowdin, HubSpot/GetResponse, VWO/Amplitude i podobne usługi zachowują własne specjalizacje.

Najważniejszy wniosek kosztowy z tego zakresu: wymaganie „Marketing może robić wszystko bez developera” należy rozumieć jako **marketing samodzielnie korzysta z wcześniej zaprojektowanych możliwości**, a nie „marketing tworzy dowolną logikę i kod bez procesu technicznego”. Pierwsza interpretacja daje szybki i stabilny system; druga prowadzi do kosztownego, trudnego do zabezpieczenia page buildera.

## Priorytetyzacja wdrożenia pod najniższy koszt

### Etap 1 — rdzeń o najwyższym zwrocie

- modele stron i najczęstszych sekcji;
- linki, nawigacja, slugi i podstawowe redirecty;
- draft, preview, Visual Editing i publikacja;
- SEO, obrazy, responsywność oraz dostępność komponentów;
- podstawowe role Growth;
- formularze oparte na istniejącej platformie klienta;
- analityka dla kluczowych CTA;
- jedna bazowa strategia lokalizacji.

### Etap 2 — skalowanie operacji

- Crowdin i automatyzacja tłumaczeń;
- większa biblioteka sekcji i template'ów;
- komentarze, zadania i dopracowane walidacje;
- rejestr integracji per strona;
- automatyczne testy linków, eventów, mobile i accessibility;
- proste eksperymenty URL lub komponentów.

### Etap 3 — funkcje wymagające dowodu wartości

- wielowymiarowa personalizacja;
- własne approval flow;
- zewnętrzny silnik wyszukiwania;
- szerokie AI content operations;
- arbitrary custom code;
- złożone Content Releases i funkcje Enterprise;
- dodatkowe datasety lub osobny DAM.

## Pytania discovery przed wyceną

1. Które zmiany dziś najczęściej czekają na developera i ile trwa oczekiwanie?
2. Jakie 10–20 sekcji pokrywa większość istniejących i planowanych stron?
3. Kto może tworzyć, akceptować i publikować treść?
4. Które dane są współdzielone między stronami, kanałami lub rynkami?
5. Ile języków istnieje dziś, kto tłumaczy i czy rynki publikują niezależnie?
6. Które integracje są obowiązkowe, a które tylko potencjalne?
7. Czy personalizacja i A/B testing mają zdefiniowane hipotezy, ruch i właściciela analizy?
8. Jakie dane osobowe przechodzą przez serwis i gdzie powinny być przechowywane?
9. Jakie są wymagania SSO, SLA, retencji, audytu i środowisk?
10. Które funkcje muszą być w pierwszym wydaniu, aby zmienić wynik biznesowy?

Odpowiedzi na te pytania zwykle obniżają koszt bardziej niż wybór pojedynczej biblioteki. Pozwalają zbudować prosty rdzeń i dodawać tylko te możliwości, których wartość klient potrafi wykorzystać.

## Źródła

- Sanity: [Studio](https://www.sanity.io/docs/studio), [Visual Editing](https://www.sanity.io/docs/visual-editing), [Localization](https://www.sanity.io/docs/studio/localization)
- Sanity: [Roles](https://www.sanity.io/docs/user-guides/roles), [Scheduled Drafts](https://www.sanity.io/docs/studio/scheduled-drafts), [Content Releases](https://www.sanity.io/docs/studio/content-releases)
- Sanity: [Plans and payments](https://www.sanity.io/docs/platform-management/plans-and-payments), [Pricing](https://www.sanity.io/pricing?lang=en)
- Sanity: [API CDN](https://www.sanity.io/docs/content-lake/api-cdn), [Datasets CLI](https://www.sanity.io/docs/cli-reference/cli-datasets)
