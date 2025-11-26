# Kostenschätzung: Drupal Relaunch

::: warning WICHTIG
Diese Kostenschätzung berücksichtigt **BörsenXperts Baseline** (480h Ersparnis).
Ohne Baseline: +CHF 72.000 Zusatzkosten.
:::

## Jahr 1: Gesamtkosten

| Kategorie | Stunden | Rate | Betrag | % |
|-----------|---------|------|--------|---|
| **Entwicklung** | 1.680h | CHF 150 | **CHF 231.400** | 70% |
| **Azure Hosting** | - | - | **CHF 35.400** | 11% |
| **Support & Wartung** | 240h | CHF 150 | **CHF 36.000** | 11% |
| **Monitoring Tools** | - | - | **CHF 3.000** | 1% |
| **Training** | - | - | **CHF 8.000** | 2% |
| **Kontingenz (15%)** | - | - | **CHF 15.000** | 5% |
| **TOTAL JAHR 1** | 1.920h | - | **CHF 328.800** | 100% |

::: danger BUDGET-ÜBERSCHREITUNG
**Projektbudget:** CHF 250.000
**Reale Kosten:** CHF 328.800
**Differenz:** +CHF 78.800 (31,5% über Budget)
:::

## Entwicklungskosten: Detaillierte Aufschlüsselung

### Phase 1: Setup & Architektur (120h)

| Aufgabe | Mit Baseline | Ohne Baseline | Ersparnis |
|---------|--------------|---------------|-----------|
| DDEV Environment Setup | 8h | 16h | 8h |
| Drupal 11 Installation | 8h | 16h | 8h |
| **BörsenXperts Baseline Integration** | **16h** | **0h** | **+16h** |
| Mercury Theme Setup | 20h | 80h | 60h |
| Core Module Configuration | 24h | 60h | 36h |
| CI/CD Pipeline Setup | 16h | 40h | 24h |
| Development Docs | 12h | 24h | 12h |
| Team Onboarding | 16h | 24h | 8h |
| **Subtotal** | **120h** | **260h** | **140h** |

**Kosten:** CHF 18.000 (mit Baseline) vs. CHF 39.000 (ohne)

### Phase 2: Content Architecture (180h)

#### Content Types (23 Types)

| Content Type | Komplexität | Stunden | Felder |
|--------------|-------------|---------|--------|
| Homepage | Hoch | 40h | Hero Carousel, Content Sections |
| Film Program | Hoch | 60h | 20+ Felder, Entity References |
| Film Archive | Hoch | 50h | Search API Integration |
| Film VOD | Mittel | 35h | Video Streaming Integration |
| Person Profile | Mittel | 30h | Referenced by Films |
| News Article | Mittel | 30h | Paragraphs, Media |
| Press Release | Mittel | 25h | Media, Documents |
| Palmarès | Mittel | 25h | Nested Awards |
| Special Awards | Einfach | 15h | Basic Fields |
| Venue | Mittel | 25h | Geolocation, Maps |
| Film Section Page | Mittel | 20h | Landing Pages |
| Jury | Mittel | 20h | Person References |
| Pro/Industry Project | Mittel | 25h | Complex Relations |
| Event | Mittel | 20h | Date Ranges, Locations |
| Partner | Einfach | 10h | Logo, Link |
| Landing Page | Hoch | 40h | Layout Builder |
| Basic Page | Einfach | 20h | Standard Fields |
| **Total** | - | **490h** | **ohne Baseline** |
| **Mit Baseline-Template** | - | **180h** | **310h gespart** |

**Baseline enthält:**
- Content Type Blueprints
- Field Template Library
- Entity Reference Patterns
- Media Integration Patterns

**Kosten:** CHF 27.000 (mit Baseline) vs. CHF 73.500 (ohne)

### Phase 3: Components / Paragraphs (200h)

#### Paragraph Types (35 Components)

| Kategorie | Anzahl | Stunden | Beispiele |
|-----------|--------|---------|-----------|
| **Hero Components** | 3 | 30h | Hero Carousel, Hero Video, Hero Static |
| **Content Sections** | 8 | 60h | Text, Image-Text, Two-Column, Three-Column |
| **Media Components** | 5 | 40h | Image Gallery, Video Embed, Slider |
| **Film Components** | 4 | 40h | Film Card, Film List, Screening Info |
| **Interactive** | 4 | 30h | Accordion, Tabs, Modal, Lightbox |
| **CTA & Buttons** | 3 | 20h | CTA Block, Button Group, Banner |
| **Lists & Cards** | 5 | 40h | News Teaser, Event Card, Person Card |
| **Special** | 3 | 30h | Quote Block, Social Links, Contact Form |
| **Total** | **35** | **290h** | **ohne Baseline** |
| **Mit Baseline-Components** | **35** | **200h** | **90h gespart** |

**Baseline enthält:**
- Paragraph Type Blueprints (20 häufige Types)
- Tailwind CSS Components
- Storybook Stories für alle Components
- Accessibility-Tests (WCAG 2.1 AA)

**Kosten:** CHF 30.000 (mit Baseline) vs. CHF 43.500 (ohne)

### Phase 4: Theme & Design (240h)

| Aufgabe | Mit Baseline | Ohne Baseline | Ersparnis |
|---------|--------------|---------------|-----------|
| **Mercury Theme (Baseline)** | **0h** | **120h** | **120h** |
| Custom Design Anpassungen | 80h | 80h | 0h |
| Responsive Breakpoints | 40h | 60h | 20h |
| Component Styling | 60h | 100h | 40h |
| Animation & Interactions | 30h | 50h | 20h |
| Performance Optimization | 20h | 40h | 20h |
| Cross-browser Testing | 10h | 20h | 10h |
| **Subtotal** | **240h** | **470h** | **230h** |

**Baseline Mercury Theme:**
- ✅ Tailwind CSS 3 Integration
- ✅ Responsive Grid System
- ✅ Component Library
- ✅ Typography System
- ✅ Color Scheme Management
- ✅ Icon Library (Heroicons)

**Kosten:** CHF 36.000 (mit Baseline) vs. CHF 70.500 (ohne)

### Phase 5: Migration (320h)

| Aufgabe | Stunden | Details |
|---------|---------|---------|
| Magnolia Content Export | 60h | JCR XML + CSV Exports |
| Data Mapping & Transformation | 80h | Field-Mapping, Cleaning |
| Drupal Migrate Plugin Dev | 100h | Source + Process Plugins |
| Film Archive Migration (10k+) | 40h | Batch Processing, Search API |
| Media Assets Migration | 30h | Download, Upload to Azure Blob |
| URL Redirects | 20h | 2.000+ Redirects |
| Validation & Fixes | 40h | Content Integrity Checks |
| **Total** | **370h** | - |
| **Mit Baseline Migrate Templates** | **320h** | **50h gespart** |

**Baseline Migrate-Vorlagen:**
- CSV/XML Source Plugin Templates
- Media Migration Patterns
- Taxonomy Migration Templates
- URL Redirect Generator

**Kosten:** CHF 48.000

### Phase 6: Testing (200h)

| Test-Kategorie | Stunden | Tools |
|----------------|---------|-------|
| Unit Tests (PHPUnit) | 50h | PHPUnit |
| Integration Tests | 40h | PHPUnit, Behat |
| E2E Tests (Playwright) | 50h | Playwright MCP |
| Accessibility Tests | 30h | Axe-core, WAVE |
| Performance Tests | 20h | k6, JMeter |
| Cross-browser Testing | 10h | BrowserStack |
| **Total** | **200h** | - |

**Baseline Testing-Framework:**
- ✅ PHPUnit Test Suites
- ✅ Playwright Test Templates
- ✅ CI/CD Test Integration
- ✅ Accessibility Test Library

**Kosten:** CHF 30.000

### Phase 7: Deployment & Go-Live (80h)

| Aufgabe | Stunden | Details |
|---------|---------|---------|
| Azure Infrastructure Setup | 20h | App Service, Database, Redis |
| Staging Deployment | 10h | Full Migration on Staging |
| Beta Launch | 20h | 10% Traffic Test |
| Production Cutover | 10h | DNS Switch, Validation |
| Post-Launch Monitoring | 20h | First Week Support |
| **Total** | **80h** | - |

**Kosten:** CHF 12.000

### Phase 8: Training & Handover (50h)

| Aufgabe | Stunden | Teilnehmer |
|---------|---------|------------|
| Admin Training | 15h | 5 Admins |
| Editor Training | 20h | 10 Editors |
| Developer Handover | 10h | 2 Devs |
| Documentation | 5h | All |
| **Total** | **50h** | - |

**Kosten:** CHF 7.500

---

## Entwicklung: Zusammenfassung

| Phase | Mit Baseline | Ohne Baseline | Ersparnis |
|-------|--------------|---------------|-----------|
| Setup & Architektur | 120h | 260h | 140h |
| Content Types | 180h | 490h | 310h |
| Components | 200h | 290h | 90h |
| Theme & Design | 240h | 470h | 230h |
| Migration | 320h | 370h | 50h |
| Testing | 200h | 200h | 0h |
| Deployment | 80h | 80h | 0h |
| Training | 50h | 50h | 0h |
| **TOTAL ENTWICKLUNG** | **1.390h** | **2.210h** | **820h** |
| **+ Projektmanagement (21%)** | **290h** | **450h** | **160h** |
| **GRAND TOTAL** | **1.680h** | **2.660h** | **980h** |

**Entwicklungskosten @ CHF 150/h:**
- **Mit Baseline:** CHF 231.400
- **Ohne Baseline:** CHF 399.000
- **Ersparnis:** **CHF 167.600**

::: tip BASELINE-VORTEIL
Die BörsenXperts Baseline spart **980 Stunden** = **CHF 147.000**.
Baseline-Lizenz-Kosten: **CHF 75.000**
**Netto-Ersparnis: CHF 72.000**
:::

## Azure Hosting-Kosten (Jahr 1)

### Production Environment

| Service | SKU | Kosten/Monat | Jahr 1 |
|---------|-----|--------------|--------|
| **App Service** (Linux) | P2v3 (2 Instances) | CHF 1.200 | CHF 14.400 |
| **Database** (MySQL) | General Purpose 4 vCores | CHF 800 | CHF 9.600 |
| **Redis Cache** | Standard C1 | CHF 240 | CHF 2.880 |
| **Blob Storage** | Hot Tier (200 GB) | CHF 40 | CHF 480 |
| **CDN** | Standard Microsoft | CHF 120 | CHF 1.440 |
| **Application Insights** | Included | CHF 50 | CHF 600 |
| **Subtotal Production** | - | **CHF 2.450** | **CHF 29.400** |

### Staging Environment

| Service | SKU | Kosten/Monat | Jahr 1 |
|---------|-----|--------------|--------|
| App Service | P1v3 (1 Instance) | CHF 300 | CHF 3.600 |
| Database | Shared | CHF 150 | CHF 1.800 |
| Redis Cache | Shared | CHF 50 | CHF 600 |
| **Subtotal Staging** | - | **CHF 500** | **CHF 6.000** |

**Total Azure (Jahr 1):** CHF 35.400

::: details Reserved Instances Optimierung
Durch Reserved Instances (3-Jahres-Commitment):
- App Service: -30% = CHF 4.320 Ersparnis
- Database: -40% = CHF 3.840 Ersparnis
- **Total RI Savings:** CHF 8.160/Jahr

**Optimierte Kosten:** CHF 27.240/Jahr
:::

## Support & Wartung (240h/Jahr)

| Leistung | Stunden/Monat | Stunden/Jahr | Kosten |
|----------|---------------|--------------|--------|
| **Hotfix & Bugfixes** | 8h | 96h | CHF 14.400 |
| **Security Updates** | 4h | 48h | CHF 7.200 |
| **Content Support** | 4h | 48h | CHF 7.200 |
| **Performance Monitoring** | 2h | 24h | CHF 3.600 |
| **Backup & Disaster Recovery** | 2h | 24h | CHF 3.600 |
| **TOTAL** | **20h** | **240h** | **CHF 36.000** |

## Monitoring & Tools (Jahr 1)

| Tool | Zweck | Kosten/Jahr |
|------|-------|-------------|
| **New Relic APM** | Performance Monitoring | CHF 1.200 |
| **Blackfire** | PHP Profiling | CHF 600 |
| **Sentry** | Error Tracking | CHF 600 |
| **Uptime Robot** | Uptime Monitoring | CHF 0 |
| **Google Analytics 4** | Web Analytics | CHF 0 |
| **Hotjar** | User Behavior | CHF 600 |
| **TOTAL** | - | **CHF 3.000** |

## Training & Onboarding (CHF 8.000)

| Training | Teilnehmer | Dauer | Kosten |
|----------|------------|-------|--------|
| Admin Training | 5 Admins | 3 Tage | CHF 3.000 |
| Editor Training | 10 Editors | 3 Tage | CHF 4.000 |
| Video Tutorials | Alle | - | CHF 1.000 |
| **TOTAL** | 15 Personen | - | **CHF 8.000** |

## Kontingenz (15%)

Reserviert für unvorhergesehene Kosten:
- Scope Creep
- Technische Herausforderungen
- Zusätzliche Testing-Zyklen
- Performance-Optimierungen

**Betrag:** CHF 15.000 (wird nur bei Bedarf verwendet)

---

## Budget-Optionen

### Option A: Vollständiges Budget (EMPFOHLEN)

```
Jahr 1: CHF 328.800
Jahr 2-5: CHF 85.200/Jahr

5-Jahres TCO: CHF 669.638
```

**Vorteile:**
- ✅ Alle 23 Content Types
- ✅ Alle 35 Components
- ✅ Volles Film-Archiv (10.000+)
- ✅ Keine Kompromisse
- ✅ Realistisches Budget

**Finanzierung:**
- Budget-Erhöhung auf CHF 330.000
- Oder: CHF 78.800 aus Reserve-Budget

### Option B: Phasen-Ansatz (Budget-konform)

#### Phase 1 (Jahr 1): CHF 250.000

**Umfang:**
- 15 von 23 Content Types (Core Types)
- 25 von 35 Components (Essential)
- 1.700 Seiten (ohne komplexes Film-Archiv)
- Basis-Search (ohne Solr)

**Reduktionen:**
- ❌ Kein VOD Content Type
- ❌ Kein Pro/Industry Content Type
- ❌ Film-Archiv nur Basic (ohne Faceted Search)
- ❌ Weniger Paragraph-Varianten

#### Phase 2 (Jahr 2): CHF 80.000

**Umfang:**
- 8 restliche Content Types
- 10 restliche Components
- Film-Archiv-Vollausbau mit Solr
- Advanced Features

**Vorteile Phasen-Ansatz:**
- ✅ Passt ins CHF 250k Budget
- ✅ Schrittweise Einführung
- ✅ Learning aus Phase 1

**Nachteile:**
- ⚠️ Zwei Deployment-Zyklen
- ⚠️ Einige Features verzögert
- ⚠️ Möglicherweise höhere Gesamt-Kosten (+10%)

---

## Kostenvergleich: Drupal vs. Alternativen

| CMS | Jahr 1 | Jahr 2-5 | 5-Jahres TCO |
|-----|--------|----------|--------------|
| **Drupal 11** | CHF 328.800 | CHF 340.838 | **CHF 669.638** |
| **Umbraco** | CHF 303.500 | CHF 363.782 | **CHF 667.282** |
| **Magnolia** | CHF 432.570 | CHF 431.425 | **CHF 863.995** |

**Drupal ist 2% teurer als Umbraco, aber:**
- ✅ Bessere Multilingual-Unterstützung
- ✅ Größere Developer-Community
- ✅ Kein .NET Lock-in
- ✅ BörsenXperts Baseline-Vorteil

**Drupal ist 29% günstiger als Magnolia:**
- Keine CHF 345k Lizenzkosten
- Günstigere Hosting-Kosten
- Keine Vendor Lock-in

---

## Empfehlung

### Für Budget CHF 330.000: Option A (Vollumfang)

**Begründung:**
- Realistische Kostenschätzung
- Keine Kompromisse bei Features
- Beste User Experience
- Zukunftssicher

### Für Budget CHF 250.000: Option B (Phasen)

**Begründung:**
- Budget-konform
- Core Features in Phase 1
- Lernkurve nutzen
- Risiko-Minimierung

---

[→ Budget-Analyse Details](/kosten/budget)
[→ ROI & TCO Berechnung](/kosten/roi)
[→ CMS-Vergleich](/cms-vergleich/)
