# Co wyróżnia Webflow

> **W skrócie:** Webflow warto wybrać wtedy, gdy liczy się **szybkość wizualnego budowania dopracowanej strony marketingowej i samodzielność zespołu design/marketing** bez utrzymywania serwera. Najmocniejsze strony to wizualny Designer generujący czysty HTML/CSS, animacje (GSAP), zarządzany hosting i niski próg wejścia cenowego dla pojedynczej strony. Ceną są limity CMS (20 tys. elementów w Premium), rosnący koszt miejsc i dodatków oraz silny lock-in — CMS i interakcje nie wychodzą z Webflow w użytecznej formie.

Stan oferty i cen: **13 września 2026 r.** Kwoty w USD, bez podatków. **13 maja 2026 r. Webflow zmienił plany**: CMS i Business zastąpił jeden plan Premium, dodał plan Team i kredyty AI. Klienci na starych planach zachowują ceny do odnowienia po 29 czerwca 2026 r. (wg źródła wtórnego).

Powiązane: [`potrzeby-biznesowe-klienta.md`](./potrzeby-biznesowe-klienta.md), [`stack-technologiczny.md`](./stack-technologiczny.md).

## Najpierw biznes: ile kosztuje Webflow?

Webflow rozlicza dwa wymiary jednocześnie:

1. **Site plan** — per strona: hosting, CMS, limity ruchu i funkcji;
2. **Workspace plan i miejsca** — per zespół: staging, eksport kodu, role, liczba osób edytujących;
3. **dodatki** — Localize (języki), Optimize (A/B, personalizacja), Analyze (analityka), dodatkowy transfer;
4. **wdrożenie** — projekt, budowa w Designerze, struktura CMS, integracje;
5. **utrzymanie** — rozwój komponentów; brak kosztów serwera.

### Site plans

| Plan | Cena (rocznie / miesięcznie) | Najważniejsze limity i funkcje |
|---|---:|---|
| **Starter** | $0 | Domena webflow.io, 2 strony statyczne, 50 elementów CMS, 1 GB transferu |
| **Basic** | **$15 / $25 za mies.** | Własna domena, 300 stron statycznych, 10 GB transferu, **bez CMS** |
| **Premium** | **$25 / $39 za mies.** | 300 stron statycznych, **20 tys. elementów CMS, 40 kolekcji**, 50 GB transferu (rozszerzalne do 2,5 TB za dopłatą $30–1460/mies.), code components, wyszukiwarka, zaplanowana publikacja, CMS API 120 req/min |
| **Team** | **$2500/mies.**, umowa roczna | Premium + Localize (2 języki), 100 kolekcji, 500 stron statycznych, do 30 TB transferu, 5 pełnych + 5 ograniczonych miejsc + do 100 darmowych, publikacja pojedynczych stron, workflow publikacji, page branching, log aktywności, AEO agents, CMS API 600 req/min, SLA hostingu 99,0% |
| **Enterprise** | wycena indywidualna | Team + własne role, granularne uprawnienia do stron i kolekcji, design approvals, SSO, SCIM, audit logs API, SLA hostingu 99,99% |

### Workspace plans i miejsca

| Pozycja | Cena (rocznie) | Co daje |
|---|---:|---|
| **Starter Workspace** | $0 | 1 pełne miejsce, 2 strony staging |
| **Core** | **$19/mies.** | 10 stron staging, custom code, **eksport kodu**, Shared Libraries |
| **Growth** | **$49/mies.** | Nielimitowany staging, role per strona, uprawnienia do publikacji, redirecty 301 na staging |
| **Pełne miejsce** (design, admin) | **$39/mies./os.** | Projektowanie stron, ustawienia |
| **Ograniczone miejsce** (treść, budowa stron z komponentów) | **$15/mies./os.** | Edycja treści i page building z zatwierdzonych bloków |
| **Darmowe miejsce** | $0 | Przegląd i komentarze |

### Dodatki

| Dodatek | Cena (rocznie) | Zakres |
|---|---:|---|
| **Localize Essential** | **$9/mies. za język** (do 3 języków) | Tłumaczenie AI (10 tys. słów/język/mies.), CMS i strony statyczne, SEO per język |
| **Localize Advanced** | **$29/mies. za język** (do 10 języków) | + lokalizacja assetów i URL-i, automatyczne przekierowanie użytkownika, 50 tys. słów/język/mies. |
| **Optimize** | od **$299/mies.** (25 tys. odsłon; $379 miesięcznie); przy 500 tys. odsłon $1499/mies. (cena przy rozliczeniu miesięcznym) | A/B testy, personalizacja, AI Optimize, do 5 równoległych testów |
| **Analyze** | od **$9/mies.** (2 tys. sesji; $12 miesięcznie); przy 500 tys. sesji $299/mies. (cena przy rozliczeniu miesięcznym) | Analityka ruchu, kliknięć i widoczności w AI |

**Przykład:** strona Premium ($25) + Workspace Core ($19) + 2 pełne miejsca (1 w cenie planu + 1 × $39) + 3 ograniczone miejsca (3 × $15) + Localize Advanced dla 3 języków (3 × $29) → ok. **$215/mies., $2580/rok** bez Optimize. Z Optimize dla 50 tys. odsłon (ok. $499/mies. — cena roczna do potwierdzenia) → ok. **$8600/rok**.

### Gdzie naprawdę powstają oszczędności

- **Brak utrzymania serwera** i aktualizacji — hosting na CDN z ochroną DDoS i backupami.
- **Designer zamiast frontendu kodowanego ręcznie** dla stron marketingowych: szybkie iteracje designu bez developera.
- **Ograniczone miejsca za $15** dla marketingu zamiast pełnych licencji.
- **Wbudowane SEO/AEO, formularze, wyszukiwarka i animacje** bez wtyczek.

### Ryzyko kosztowe, które trzeba kontrolować

- **Limity CMS.** Premium: 20 tys. elementów i 40 kolekcji. Duży blog, katalog lub wiele języków szybko wymaga planu Team ($2500/mies.) lub Enterprise.
- **Transfer.** Dwa kolejne miesiące ponad limit powodują **automatyczne podniesienie planu**.
- **Dodatki mnożą rachunek:** języki są rozliczane per język, Optimize per odsłony.
- **Duża przepaść Premium → Team.** Workflow publikacji, page branching, log aktywności i wyższe limity API są dopiero w planie za $2500/mies.
- **Zmiany cennika.** Webflow zmieniał plany w 2023 i 2026 r.; w wieloletnim TCO zaplanować rezerwę.

**Rekomendacja kosztowa:** Webflow jest bardzo konkurencyjny dla serwisu marketingowego do kilku tysięcy elementów CMS i małego zespołu. Przy dużym wolumenie treści, wielu językach i wymaganiach governance koszt skokowo rośnie — liczyć wariant Team/Enterprise od razu.

## Co Webflow robi inaczej

### 1. Wizualny Designer generujący produkcyjny kod

Designer odwzorowuje model CSS (box model, flex, grid, klasy, zmienne) w interfejsie wizualnym. Wynikiem jest semantyczny HTML i CSS hostowany przez Webflow. Projektant z wiedzą o webie buduje stronę bez developera frontendu.

### 2. Rozdzielenie ról: design, page building, treść

Pełne miejsca projektują komponenty i szablony; ograniczone miejsca (marketing) budują strony z zatwierdzonych komponentów i edytują treść; darmowe miejsca komentują. To model zbliżony do headless CMS z biblioteką sekcji, ale bez kodowania frontendu.

### 3. Interakcje i animacje bez kodu

Interakcje z GSAP na osi czasu — złożone animacje scroll i hover bez biblioteki JS pisanej ręcznie. Mocna przewaga dla stron brandowych i SaaS.

### 4. Kod tam, gdzie wizualny builder nie wystarcza

- **Code components (DevLink):** komponenty React z repozytorium importowane do Designera; marketing ustawia ich propsy i łączy z CMS.
- **Webflow Cloud:** hostowanie aplikacji Next.js i Astro pod domeną strony (np. `/app`) z bazami SQLite, KV i storage obiektowym; limity requestów i CPU per plan, dopłaty po przekroczeniu.
- **Custom code** w stronach i CMS (plan Workspace Core+).

### 5. SEO i AEO wbudowane w platformę

Metadane, canonicale, sitemap, schema, `robots.txt` i `llms.txt`, redirecty 301, audyty SEO/AEO z AI; w Team agenci AEO.

### 6. Silny lock-in

Eksport kodu (Workspace Core+) daje statyczny HTML/CSS/JS, ale **bez treści CMS i stron dynamicznych**. Dane CMS można pobrać przez API lub CSV, jednak interakcje, komponenty, szablony kolekcji i logika lokalizacji nie przenoszą się do innego systemu.

## Jak Webflow odpowiada na typowe potrzeby klienta

| Potrzeba | Odpowiedź Webflow | Na co uważać |
|---|---|---|
| **Prosta edycja bez developera** | Edycja na stronie, page building z komponentów dla ograniczonych miejsc | Nowy komponent wymaga osoby z pełnym miejscem |
| **Dopracowany design i animacje** | Designer + interakcje GSAP | Wymaga projektanta znającego Webflow |
| **Praca wielu osób** | Współpraca w czasie rzeczywistym, komentarze | Każdy edytujący to płatne miejsce |
| **Role i akceptacje** | Role per strona (Growth), workflow publikacji (Team), granularne uprawnienia i approvals (Enterprise) | Governance skokowo droższe |
| **Wiele języków** | Localize Essential/Advanced | Rozliczanie per język; zaawansowane funkcje od Advanced |
| **Duży wolumen treści** | CMS z kolekcjami i referencjami | 20 tys. elementów w Premium; limity pól (100 pól, 20 referencji na kolekcję w Team) |
| **A/B i personalizacja** | Optimize | Od $299/mies., rozliczane per odsłony |
| **Integracje** | Custom code, Apps Marketplace, CMS API, Webflow Cloud | Logika serwerowa przez Webflow Cloud lub zewnętrzne usługi |
| **Bezpieczeństwo** | Zarządzany hosting, 2FA; SSO i SCIM tylko Enterprise | Brak kontroli nad serwerem |
| **Przenośność** | Eksport HTML/CSS, API i CSV dla CMS | Eksport bez CMS i dynamicznych stron |

## Kiedy Webflow jest szczególnie dobrym wyborem

- serwis marketingowy lub produktowy z **mocnym designem i animacjami**;
- zespół design/marketing chce **iterować bez developera**;
- klient nie chce utrzymywać hostingu ani aktualizacji;
- treści jest umiarkowanie dużo (poniżej ok. 20 tys. elementów CMS);
- szybkie wdrożenie jest ważniejsze niż pełna kontrola nad kodem.

## Kiedy lepiej rozważyć inne rozwiązanie

- duży wolumen treści, katalog lub wiele języków przy budżecie poniżej planu Team;
- treść ma zasilać wiele kanałów (aplikację, produkt) — lepszy headless CMS;
- wymagana jest złożona logika aplikacyjna lub dostęp do danych użytkownika;
- klient wymaga **niskiego vendor lock-in**;
- wymagane są SSO i granularne uprawnienia, a budżet nie obejmuje Enterprise;
- klient jest w HubSpot i chce personalizacji na danych CRM — lepszy HubSpot CMS.

## Rekomendacja decyzyjna

Najlepszy argument za Webflow: **zespół marketingu i designu dostaje szybkie, wizualne narzędzie do budowania dopracowanych stron, a klient nie utrzymuje serwera ani frontendu w kodzie**.

1. **Policzyć wolumen treści i języków** — czy mieści się w Premium, czy od razu Team/Enterprise.
2. **Policzyć miejsca** — pełne dla design, ograniczone dla marketingu.
3. **Ocenić akceptację lock-in** — co klient zrobi, jeśli za 3–5 lat zmieni platformę.

## Źródła

- [Webflow — Plans & pricing](https://webflow.com/pricing) (stan 13.09.2026)
- [Webflow Blog — Simplified plans and updated pricing 2026](https://webflow.com/blog/simplified-plans-and-updated-pricing-2026)
- [Webflow Help Center — Updated pricing and simplified plans for May 2026](https://help.webflow.com/hc/en-us/articles/51059955082387-Updated-pricing-and-simplified-plans-for-May-2026)
- [Memberstack — New Webflow pricing in 2026](https://www.memberstack.com/blog/new-webflow-pricing-in-2026-what-every-plan-costs-and-how-to-choose) (źródło wtórne; daty dla starych planów)
- [Webflow Cloud — developer docs](https://developers.webflow.com/webflow-cloud/intro)
- [Code components](https://developers.webflow.com/code-components/introduction), [DevLink](https://webflow.com/feature/devlink)
