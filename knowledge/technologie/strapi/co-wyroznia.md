# Co wyróżnia Strapi jako headless CMS

> **W skrócie:** Strapi warto wybrać wtedy, gdy firma chce zachować kontrolę nad kodem, danymi i miejscem uruchomienia CMS-a, a jednocześnie potrzebuje gotowego panelu redakcyjnego i API. Największą przewagą jest możliwość wyboru między zarządzanym Strapi Cloud a self-hostingiem tej samej aplikacji. Największym ryzykiem biznesowym jest błędne założenie, że „open source” oznacza brak kosztów: przy self-hostingu koszt przenosi się na infrastrukturę i operacje, a w Cloud hosting oraz płatne funkcje CMS są rozliczane osobno.

Stan oferty i cen: **29 lipca 2026 r.** Wszystkie kwoty są cenami katalogowymi w USD, bez podatków, kosztu frontendu, wdrożenia i migracji.

Powiązane: [`potrzeby-biznesowe-klienta.md`](./potrzeby-biznesowe-klienta.md).

## Najpierw biznes: ile kosztuje Strapi?

Koszt Strapi składa się z dwóch niezależnych warstw:

1. **planu CMS** — Community, Growth albo Enterprise; decyduje o funkcjach redakcyjnych, governance i wsparciu;
2. **hostingu** — Strapi Cloud albo infrastruktury utrzymywanej przez klienta lub partnera.

Do tego dochodzą koszty wspólne dla obu wariantów: model treści, frontend, integracje, migracja, testy, szkolenia oraz późniejszy rozwój. Dlatego dwóch ofert nie należy porównywać wyłącznie jako „$35 za Cloud” i „$0 za self-hosted”.

### Licencja funkcji CMS

| Plan CMS | Cena katalogowa | Dla kogo | Najważniejsze możliwości i ograniczenia |
|---|---:|---|---|
| **Community** | **$0** | PoC, mały lub średni zespół bez zaawansowanego workflow | Open source na licencji MIT; RBAC, Draft & Publish, i18n, Media Library, REST/GraphQL, webhooks, import/eksport/transfer; brak Live Preview, Releases i historii treści |
| **Growth** | **$45/mies.** za 3 miejsca | Zespół marketingowy potrzebujący podglądu i planowanych publikacji | Live Preview, Releases, 30 dni historii treści, podstawowe wsparcie; kolejne miejsce **$15/mies.**; SSO jako osobny dodatek |
| **Enterprise** | **wycena indywidualna** | Organizacje z formalnym approval flow, audytem, SSO i wymaganiami wsparcia | Review Workflows, Audit Logs, SSO, dłuższa historia, wsparcie na warunkach umowy; opcjonalna licencja offline i premium support |

Dodatek SSO do Growth kosztuje obecnie **$150/mies. plus $50/mies. za miejsce**. Aktualne funkcje i warunki publikuje [cennik Strapi CMS](https://strapi.io/pricing-cms).

Community nie ogranicza liczbą wpisów, requestów API, content types, locale ani ról na poziomie licencji CMS. Nie oznacza to jednak darmowej, nieograniczonej produkcji: zużycie nadal obciąża limity Strapi Cloud albo zasoby własnej infrastruktury.

### Strapi Cloud — hosting jest osobnym rachunkiem

Strapi Cloud jest zarządzanym PaaS dla aplikacji Strapi, a nie abonamentem zawierającym wszystkie płatne funkcje CMS. Plan Cloud zapewnia hosting aplikacji, bazy i assetów; Growth lub Enterprise dokupuje się osobno, jeśli potrzebne są ich funkcje.

| Plan Cloud | Cena miesięczna | Limity bazowe | Istotne cechy operacyjne |
|---|---:|---|---|
| **Starter** | **$35/projekt** | 100 tys. requestów API; 50 GB assetów; 50 GB transferu assetów | 1 środowisko; aplikacja usypiana przy braku ruchu; brak zarządzanych backupów i CRON |
| **Pro** | **$90/projekt** | 1 mln requestów API; 250 GB assetów; 500 GB transferu assetów | 1 środowisko; always-on; cotygodniowe i ręczne backupy; CRON; dodatkowe środowisko $60/mies. |
| **Business** | **$450/projekt** | 10 mln requestów API; 1 TB assetów; 1 TB transferu assetów | 2 środowiska; codzienne backupy; 99,9% SLA; dodatkowe środowisko $300/mies. |

Płatne nadwyżki wynoszą obecnie **$1,50 za 25 tys. requestów API**, **$0,60 za 1 GB assetów** i **$30 za 100 GB transferu assetów**. Szczegóły oraz wariant roczny zawiera [cennik Strapi Cloud](https://strapi.io/pricing-cloud). Zasady rozliczeń potwierdzają, że [Cloud obejmuje hosting, a nie płatne funkcje CMS](https://support.strapi.io/articles/3581379360-understanding-strapi-cloud-usage-and-billing).

Przykładowe miesięczne minima przed podatkiem, frontendem i wdrożeniem:

| Wariant | Minimalny koszt katalogowy | Co obejmuje |
|---|---:|---|
| **Cloud Starter + Community** | **$35** | Najtańsza produkcyjna instancja Cloud bez Live Preview, Releases i historii treści |
| **Cloud Starter + Growth** | **$80** | Hosting oraz 3 miejsca CMS z Live Preview, Releases i historią treści |
| **Cloud Pro + Growth** | **$135** | Jak wyżej, ale z always-on, backupami, CRON i większymi limitami |
| **Cloud Business + Growth** | **$495** | Dwa środowiska, codzienne backupy i SLA, ale nadal bez funkcji Enterprise |
| **Self-hosted + Community** | **$0 licencji** | CMS bez opłaty; cała infrastruktura i odpowiedzialność operacyjna po stronie klienta |
| **Self-hosted + Growth** | **od $45** | Płatne funkcje redakcyjne; do tego pełny koszt własnego hostingu |

### Self-hosted — brak licencji nie oznacza braku kosztu

Community można uruchomić bez opłaty licencyjnej na własnym VPS-ie, w AWS, Azure, GCP, Kubernetesie, data center albo sieci izolowanej. Firma wybiera PostgreSQL, MySQL lub MariaDB, storage assetów, CDN, pocztę i pozostałe elementy infrastruktury. Jest to realna przewaga, gdy organizacja już ma platform team, kontrakty chmurowe i standardy operacyjne.

W modelu 12-miesięcznego TCO self-hosted trzeba jednak policzyć:

- compute dla aplikacji i osobne zasoby dla środowisk preview/staging;
- zarządzaną bazę danych, storage obiektowy, CDN, transfer i e-mail;
- backupy bazy i assetów, retencję, szyfrowanie oraz regularne testy odtworzenia;
- monitoring, logi, alerty, zarządzanie sekretami i certyfikatami;
- aktualizacje Strapi, Node.js, bazy, systemu operacyjnego i pluginów;
- skalowanie, wysoką dostępność, ochronę przed DDoS i procedury awaryjne;
- czas DevOps/SRE, obsługę incydentów i dyżury, jeśli CMS jest krytyczny;
- audyty bezpieczeństwa, compliance oraz dokumentację operacyjną.

Mała instancja może mieć niski rachunek infrastrukturalny, ale nawet kilka godzin specjalisty miesięcznie potrafi kosztować więcej niż Strapi Cloud Pro. Z drugiej strony przy dużej skali, istniejącej platformie i przewidywalnym obciążeniu self-hosted może być tańszy oraz dawać lepszą kontrolę niż kolejne progi Cloud.

### Gdzie naprawdę powstają oszczędności

Największa oszczędność Strapi nie wynika z zerowej ceny Community, lecz z możliwości użycia jednego modelu treści i API w wielu kanałach oraz z niewymuszania jednego dostawcy infrastruktury. Ten sam projekt może zostać rozwinięty, przeniesiony albo uruchomiony w innym środowisku bez przepisywania całego CMS-a.

Komponenty i Dynamic Zones pozwalają zbudować kontrolowany page builder: marketing składa stronę z zatwierdzonych sekcji, a frontend zachowuje spójność design systemu. Dobrze zaprojektowany model ogranicza drobne zadania developerskie, błędy publikacyjne i duplikowanie treści między stronami.

Oszczędność nie jest automatyczna. Strapi udostępnia narzędzia do modelowania i rozszerzania, ale nie dostarcza gotowego modelu strony, biblioteki sekcji ani integracji dopasowanych do klienta. Zbyt ogólne Dynamic Zones utrudnią governance, a zbyt sztywny model ponownie uzależni marketing od developerów.

### Główne ryzyka kosztowe

**Podwójny abonament w Cloud.** Cloud Pro za $90 nie odblokowuje Live Preview, Releases ani historii. Dla tych funkcji trzeba dodać co najmniej Growth.

**Pozornie darmowy self-hosting.** Licencja Community ma koszt $0, ale klient przejmuje backup, bezpieczeństwo, aktualizacje, monitoring, skalowanie i dostępność.

**Środowiska.** Bezpieczny proces zwykle potrzebuje co najmniej development, preview/staging i production. W Cloud dodatkowe środowiska są istotną pozycją cennika; self-hosted mnoży zasoby i pracę operacyjną.

**Miejsca CMS.** Po przejściu na Growth każdy aktywny użytkownik panelu zużywa miejsce niezależnie od roli. Interesariusze, tłumacze i osoby zatwierdzające powinni być policzeni przed zakupem.

**Assety i transfer.** Duże wideo, animacje i ciężkie biblioteki multimediów szybko zwiększają transfer. Wideo produkcyjne zwykle lepiej obsługiwać przez wyspecjalizowaną platformę niż bezpośrednio z Media Library.

**Customizacja i pluginy.** Własny backend jest przewagą Strapi, ale każda modyfikacja zwiększa zakres testów aktualizacji. Plugin społecznościowy trzeba ocenić pod kątem utrzymania, kompatybilności i bezpieczeństwa.

## Strapi Cloud czy self-hosted?

| Kryterium biznesowe | Strapi Cloud | Self-hosted |
|---|---|---|
| **Szybkość startu** | Bardzo wysoka; platforma dostarcza bazę, deployment, CDN i e-mail | Zależy od gotowości platformy klienta |
| **Przewidywalność kosztu** | Wysoka do momentu wejścia w nadwyżki lub dodatkowe środowiska | Wysoka przy dojrzałej platformie; niska bez policzenia pracy operacyjnej |
| **Kontrola danych i sieci** | Ograniczona do możliwości i regionów usługi | Pełna kontrola nad regionem, siecią, bazą, retencją i dostępem |
| **Backup i odtwarzanie** | Zarządzane od Pro; częstotliwość zależy od planu | Pełna odpowiedzialność klienta, ale też dowolna polityka |
| **Skalowanie i utrzymanie** | Większość infrastruktury przejmuje Strapi | Klient projektuje, monitoruje i utrzymuje całość |
| **Customizacja aplikacji** | Duża, ale w granicach platformy Cloud | Największa; dowolne usługi, providery i topologia |
| **Compliance i izolacja** | Wystarczające dla części organizacji; wymaga weryfikacji warunków | Najlepsze dla wymogów on-prem, isolated network i własnych kontroli |
| **Ryzyko zależności od dostawcy** | Wyższe operacyjnie, choć kod i dane można przenosić | Niższe wobec hostingu; nadal pozostaje zależność od Strapi i pluginów |
| **Kompetencje potrzebne po starcie** | Głównie development i obserwacja limitów | Development plus DevOps/SRE, bezpieczeństwo i baza danych |

**Praktyczna reguła:** Strapi Cloud kupuje czas i zmniejsza odpowiedzialność operacyjną. Self-hosted kupuje kontrolę, ale wymaga istniejących kompetencji. Nie należy wybierać self-hostingu tylko dlatego, że Community ma licencję $0.

## Co Strapi robi inaczej

### 1. CMS jest aplikacją, którą firma może posiadać i rozwijać

Strapi jest aplikacją Node.js z kodem projektu, schematami, konfiguracją i rozszerzeniami. W przeciwieństwie do zamkniętego SaaS klient może przejrzeć kod, dodać kontrolery, serwisy, polityki, middleware i pluginy oraz wybrać miejsce uruchomienia. Oficjalny opis [self-hostingu Strapi](https://strapi.io/hosting) podkreśla możliwość użycia własnej bazy i infrastruktury.

Biznesowo ogranicza to zależność od jednego hostingu i pozwala dopasować backend do nietypowej domeny. Ceną jest utrzymywanie aplikacji, a nie tylko konfigurowanie usługi.

### 2. Model treści łączy strukturę danych z kontrolowanym page buildingiem

Strapi rozróżnia collection types, single types i reużywalne components. Dynamic Zone może zawierać zatwierdzony zestaw różnych komponentów, dzięki czemu redaktor układa stronę bez edycji HTML lub CSS. [Content-Type Builder](https://docs.strapi.io/cms/features/content-type-builder) pozwala wizualnie definiować pola, relacje, komponenty i walidacje.

Ważne ograniczenie: Content-Type Builder działa tylko w środowisku development. Zmiana schematu jest zmianą aplikacji i powinna przejść przez kod, testy oraz deployment. Marketing może tworzyć strony z istniejących sekcji, ale dodanie nowego rodzaju sekcji nadal zwykle wymaga developera.

### 3. Podstawy redakcyjne są bezpłatne, za dojrzały workflow się płaci

Community zawiera Draft & Publish, role i granularne uprawnienia, i18n, Media Library oraz standardowy Preview po skonfigurowaniu frontendu. **Live Preview** wymaga Growth lub Enterprise; dokumentacja rozróżnia [bezpłatny Preview i płatny Live Preview](https://docs.strapi.io/cms/features/preview).

Growth dodaje Releases, czyli grupowanie wielu zmian oraz wspólne publikowanie, wycofywanie i harmonogram. Formalne wieloetapowe Review Workflows oraz Audit Logs są funkcjami Enterprise. To sensowny podział produktowy, ale wymagania governance mogą być większym czynnikiem ceny niż ruch strony.

### 4. API i backend można dopasować do wielu kanałów

Strapi automatycznie generuje REST API, a GraphQL jest dostępny przez oficjalny plugin. API tokens, webhooks i backendowe rozszerzenia pozwalają zasilać stronę, aplikację mobilną, portal, e-commerce albo wewnętrzne narzędzie z jednego źródła treści.

Frontend pozostaje osobnym produktem. Strapi nie gwarantuje sam z siebie SEO, responsywności, dostępności, personalizacji ani szybkości strony — zależą one od modelu treści, frameworka, cache, hostingu i implementacji komponentów.

### 5. Lokalizacja jest bezpłatna, ale workflow tłumaczeń trzeba zaprojektować

i18n jest funkcją Community i pozwala lokalizować całe content types oraz wybrane pola. Komponenty i Dynamic Zones mogą różnić się między locale, co wspiera realne różnice rynkowe. Dokumentacja [Internationalization](https://docs.strapi.io/cms/features/internationalization) wskazuje jednak, że treść edytuje i publikuje się po jednym locale naraz.

Integracja z Crowdin lub innym TMS-em nie jest pełnym procesem biznesowym „z pudełka”. Trzeba ustalić źródło prawdy, mapowanie pól, statusy, obsługę relacji i slugów, retry, konflikt zmian oraz publikację wielu języków.

### 6. Kod i dane są przenośne, lecz nie całkowicie neutralne

Strapi oferuje bezpłatne, CLI-owe eksporty, importy i transfer pomiędzy instancjami. Eksport może zawierać konfigurację, encje, relacje, schematy i assety w szyfrowanym oraz skompresowanym archiwum. Transfer bezpośredni zakłada zgodność schematów. Szczegóły opisuje [Data Management](https://docs.strapi.io/cms/features/data-management).

Ułatwia to przejście pomiędzy środowiskami oraz między Cloud i self-hosted. Nie usuwa jednak zależności od Strapi: komponenty, Dynamic Zones, pluginy, własny backend i kontrakt API nadal trzeba przepisać przy zmianie CMS-a.

## Migracja z innego CMS-a

Migracja do Strapi nie jest pojedynczym importem bazy. Natywne import/export/transfer najlepiej obsługują instancje Strapi o zgodnym schemacie; dane z WordPressa, Drupal, Contentful, Sanity lub własnego CMS-a zwykle wymagają osobnego procesu ETL przez API albo skrypt migracyjny.

Bezpieczny zakres migracji obejmuje:

1. **inwentaryzację** typów treści, pól, relacji, języków, assetów, użytkowników, URL-i i integracji;
2. **mapowanie do modelu docelowego**, które rozdziela dane domenowe od sekcji strony i eliminuje zbędne dziedzictwo starego CMS-a;
3. **migrację próbną** na pełnej lub reprezentatywnej kopii, razem z raportem rekordów pominiętych i błędnych;
4. **transfer assetów i relacji** z zachowaniem alt textów, metadanych, locale, referencji i kolejności komponentów;
5. **mapę redirectów**, aby zachować SEO po zmianie slugów i struktur URL;
6. **walidację biznesową i techniczną**: liczby rekordów, wymagane pola, duplikaty, linki, rendery stron, SEO oraz uprawnienia;
7. **delta migration i cutover**, czyli przeniesienie zmian powstałych po próbie, krótkie okno zamrożenia oraz plan wycofania;
8. **archiwum i rollback**, zanim stary system zostanie wyłączony.

Największy koszt migracji zależy nie od liczby rekordów, lecz od jakości starego modelu, liczby wyjątków, relacji, języków, formatów rich text i zmian URL. Dlatego wycenę należy poprzedzić technicznym discovery oraz migracją próbną, zamiast mnożyć rekordy przez jedną stawkę.

Wybór hostingu nie zmienia zasad mapowania treści. Strapi Cloud upraszcza przygotowanie środowiska docelowego; self-hosted daje większą kontrolę nad połączeniami sieciowymi, dużymi transferami i oknem cutover. W obu przypadkach skrypt migracyjny powinien być powtarzalny, wersjonowany i generować raport.

## Jak Strapi odpowiada na typowe potrzeby klienta

| Potrzeba | Odpowiedź Strapi | Na co uważać |
|---|---|---|
| **Niski koszt wejścia** | Community bez opłaty licencyjnej; Cloud Starter od $35 | TCO obejmuje hosting, frontend, wdrożenie, migrację i utrzymanie |
| **Edycja bez developera** | Content Manager, komponenty i Dynamic Zones | Nowe typy i komponenty wymagają zmiany schematu w development |
| **Bezpieczny page builder** | Lista dozwolonych komponentów, walidacje i uprawnienia | UX redakcyjny i biblioteka sekcji są częścią wdrożenia |
| **Draft, preview i publikacja** | Draft & Publish i Preview w Community; Live Preview oraz Releases w Growth | Frontend preview trzeba skonfigurować; approval flow wymaga Enterprise |
| **Role i bezpieczeństwo zmian** | Granularny RBAC bezpłatnie | SSO, Review Workflows i Audit Logs zwiększają koszt licencji |
| **Wiele języków** | i18n bez limitu locale na poziomie licencji | Publikacja działa per locale; TMS i redirecty wymagają integracji |
| **Wiele kanałów** | REST, GraphQL, webhooks i rozszerzalny backend | Kontrakt API i cache trzeba zaprojektować pod konsumentów |
| **Integracje** | Pluginy, providery oraz własne kontrolery i serwisy | Każdy plugin zwiększa ryzyko aktualizacji i utrzymania |
| **Wydajność i skala** | Cloud z rosnącymi limitami albo dowolna architektura self-hosted | Strapi jest runtime'em Node.js; baza, cache, CDN i zapytania wymagają obserwacji |
| **Backup i ciągłość działania** | Cloud Pro/Business mają zarządzane backupy; self-hosted daje pełną kontrolę | Starter nie ma zarządzanych backupów; self-hosted wymaga testów odtworzenia |
| **Migracja z obecnego CMS-a** | Otwarte API, własny kod i narzędzia data management | Zewnętrzny format trzeba zmapować; migracja nie jest automatyczna |
| **Ograniczenie vendor lock-in** | Kod, baza i assety mogą działać poza Strapi Cloud | Model, pluginy i API pozostają specyficzne dla Strapi |

## Kiedy wybrać Strapi Cloud

Cloud jest zwykle lepszym wyborem, gdy:

- firma chce szybko uruchomić projekt i nie ma dedykowanego zespołu platformowego;
- koszt czasu DevOps jest większy niż różnica w abonamencie;
- standardowy model deploymentu, bazy, CDN i backupów spełnia wymagania;
- ważna jest jedna odpowiedzialność za hosting Strapi i oficjalne wsparcie;
- obciążenie mieści się w przewidywalnych limitach, a dodatkowe środowiska zostały uwzględnione w budżecie.

Dla krytycznej strony biznesowej rozsądnym punktem wyjścia jest zwykle **Cloud Pro**, nie Starter: always-on, ręczne i cotygodniowe backupy oraz CRON zmniejszają ryzyko operacyjne. Growth należy dodać tylko wtedy, gdy Live Preview, Releases lub historia treści rzeczywiście uzasadniają $45 miesięcznie i koszt miejsc.

## Kiedy wybrać self-hosted

Self-hosted ma mocniejsze uzasadnienie, gdy:

- klient ma już dojrzałą platformę, monitoring, backupy, on-call i standardy bezpieczeństwa;
- dane muszą pozostać w konkretnym regionie, koncie chmurowym, data center albo sieci izolowanej;
- potrzebna jest nietypowa topologia, własny provider, private networking lub ścisła integracja z systemami wewnętrznymi;
- skala i profil ruchu sprawiają, że własna infrastruktura jest ekonomiczniejsza od limitów Cloud;
- organizacja akceptuje odpowiedzialność za aktualizacje, incydenty, dostępność i disaster recovery;
- wymagana jest możliwość zmiany dostawcy hostingu bez zmiany CMS-a.

Self-hosted Community jest szczególnie atrakcyjny dla prostego workflow i silnego zespołu technicznego. Jeżeli organizacja potrzebuje SSO, audytu i formalnych akceptacji, koszt Enterprise nadal wystąpi niezależnie od własnej infrastruktury.

## Kiedy lepiej rozważyć inne rozwiązanie

Strapi może nie być optymalnym wyborem, gdy:

- klient oczekuje gotowej strony, motywu i page buildera bez budowy frontendu;
- marketing ma samodzielnie tworzyć zupełnie nowe typy sekcji produkcyjnych bez procesu developerskiego;
- organizacja nie chce utrzymywać aplikacji ani płacić za zarządzany hosting;
- wymagane jest rozbudowane approval flow, SSO i audyt, ale budżet zakłada wyłącznie Community;
- nie ma właściciela aktualizacji kodu i pluginów po zakończeniu wdrożenia;
- główną potrzebą jest prosta strona aktualizowana sporadycznie, dla której headless CMS i osobny frontend zwiększają złożoność bez proporcjonalnej wartości.

## Rekomendacja decyzyjna

Najlepszy argument za Strapi brzmi: **firma może zacząć od otwartego CMS-a, zachować kod i dane oraz świadomie wybrać, czy płaci dostawcy za operacje, czy realizuje je na własnej platformie**.

Dla klienta biznesowego decyzję warto podjąć w czterech krokach:

1. **Policzyć dwa rachunki osobno:** plan CMS wynikający z workflow oraz hosting wynikający z ruchu, assetów, środowisk i poziomu dostępności.
2. **Porównać 12-miesięczny TCO:** abonament Cloud przeciw infrastrukturze, pracy DevOps, backupom, monitoringowi, aktualizacjom i ryzyku incydentów self-hosted.
3. **Zrobić proof of concept na rzeczywistym use case:** złożona strona z Dynamic Zones, preview, rolami, jednym locale i reprezentatywną integracją.
4. **Wykonać migrację próbną przed wiążącą wyceną:** na rzeczywistych danych, assetach, relacjach i URL-ach, z raportem jakości oraz zmierzonym czasem cutover.

Jeżeli priorytetem jest szybki start i mała odpowiedzialność operacyjna, rekomendowanym punktem odniesienia jest **Strapi Cloud Pro + Community albo Growth zależnie od workflow**. Jeżeli klient ma dojrzałą platformę i twarde wymagania dotyczące danych lub sieci, należy wycenić **self-hosted Community/Growth/Enterprise** razem z pełnym kosztem operacji. Ostateczna decyzja powinna wynikać z TCO i ryzyka, a nie z samej ceny licencji.

## Źródła

- [Strapi — CMS Pricing](https://strapi.io/pricing-cms)
- [Strapi — Cloud Pricing](https://strapi.io/pricing-cloud)
- [Understanding Strapi Cloud usage and billing](https://support.strapi.io/articles/3581379360-understanding-strapi-cloud-usage-and-billing)
- [Self-host Strapi](https://strapi.io/hosting)
- [Strapi 5 Documentation](https://docs.strapi.io/)
- [Content-Type Builder](https://docs.strapi.io/cms/features/content-type-builder)
- [Preview](https://docs.strapi.io/cms/features/preview)
- [Releases](https://docs.strapi.io/cms/features/releases)
- [Role-Based Access Control](https://docs.strapi.io/cms/features/rbac)
- [Internationalization](https://docs.strapi.io/cms/features/internationalization)
- [Data Management](https://docs.strapi.io/cms/features/data-management)
