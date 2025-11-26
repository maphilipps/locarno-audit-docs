# Kostenschätzung: Drupal Relaunch

::: info QUELLE
Diese Kostenschätzung basiert auf dem **adesso Calculator 2.01** (Locarno-Festival-Kalkulation.xlsm).
Alle Werte in EUR. Umrechnung CHF: ×1,05
:::

## Projekt-Zusammenfassung (adesso Calculator)

| Position | Aufwand (PT) | Kosten (€) | Preis (€) |
|----------|-------------:|----------:|---------:|
| **Features** | 137,5 | 106.147 | 110.000 |
| **Project Tasks** | 96,0 | 53.600 | 76.800 |
| **Risikopuffer** | 28,4 | 14.200 | 22.720 |
| **TOTAL** | **261,9 PT** | **173.947 €** | **209.520 €** |

::: tip UMRECHNUNG
**EUR 209.520** ≈ **CHF 219.996** (Kurs 1,05)
:::

::: info HINWEIS
Inkl. **F-450 Keycloak oAuth2** mit 3,33 PT (nachträglich hinzugefügt)
:::

## Aufwand nach Rolle

| Rolle | Seniority | Aufwand (PT) | Kosten (€) |
|-------|-----------|-------------:|----------:|
| Developer | Middle | 108,5 | 97.710 |
| Project Manager | Senior | 43,0 | 21.500 |
| Requirement Engineer | Middle | 39,5 | 19.733 |
| Sonstige Rollen | Mixed | 33,4 | 16.700 |
| Test Engineer | Middle | 17,7 | 8.850 |
| Software Architect | Senior | 10,8 | 5.383 |
| DevOps Engineer | Middle | 5,6 | 2.800 |
| Test Manager | Senior | 3,4 | 1.700 |
| **TOTAL** | | **261,9 PT** | **173.947 €** |

## Projektdauer

| Parameter | Wert |
|-----------|------|
| **Projektlänge** | 20 Wochen |
| **Team-Größe (Ø)** | 3,1 FTE |
| **Anzahl Features** | 42 |
| **Anzahl Risiken** | 8 |

---

## Risiko-Analyse (aus adesso Calculator)

| ID | Risiko | Wahrsch. | Impact (PT) | Gewichtet |
|-----|--------|----------|-------------|-----------|
| R-10 | Migration komplexer als erwartet | 60% | 15 | **9,0 PT** |
| R-20 | Film-Datenbank-Import-Format unklar | 50% | 10 | **5,0 PT** |
| R-40 | Design-Änderungen während Projekt | 50% | 8 | **4,0 PT** |
| R-50 | Legacy-URL-Struktur komplex | 50% | 5 | **2,5 PT** |
| R-70 | Programm-Kalender-Komplexität | 40% | 6 | **2,4 PT** |
| R-30 | Ticketing-API nicht verfügbar | 40% | 5 | **2,0 PT** |
| R-80 | WCAG AA Anforderungen unterschätzt | 40% | 5 | **2,0 PT** |
| R-60 | Solr-Hosting nicht verfügbar | 30% | 5 | **1,5 PT** |
| | **TOTAL Risikopuffer** | | **59 PT** | **28,4 PT** |

::: warning HÖCHSTES RISIKO
**R-10: Migration komplexer als erwartet** (9 PT gewichtet)
- 79 Jahre Archiv-Daten
- Undokumentierte Datenstrukturen
- Qualitätsprobleme in historischen Daten
:::

---

## Feature-Aufwand nach Kategorie

| Kategorie | Anzahl Features | Beschreibung |
|-----------|---------------:|--------------|
| **Content-Modellierung** | 14 | Content-Types, Taxonomien, Paragraphs, Media |
| **Frontend** | 9 | Theme, Templates, SDC-Komponenten, Responsive |
| **Views & Listings** | 6 | Film-, Programm-, Award-, News-Listings |
| **Custom Development** | 5 | Film-Credits, Kalender, Schema.org |
| **Setup & Infrastruktur** | 2 | Projekt-Setup, Hosting |
| **Integrationen** | 3 | Ticketing, Video/Maps, Newsletter |
| **Authentication** | 1 | Keycloak oAuth2 SSO (F-450) |
| **SEO** | 2 | SEO-Setup, Performance |
| **Total** | **42 Features** | |

::: details Feature-Gruppen (aus Excel)
- **Setup & Infrastruktur:** F-10, F-20
- **Content-Modellierung:** F-30 bis F-130
- **Views & Listings:** F-140 bis F-190
- **Custom Development:** F-200 bis F-240
- **Suche:** F-250
- **Frontend:** F-260 bis F-340
- **Integrationen:** F-350 bis F-380
- **Mehrsprachigkeit:** F-390
- **SEO:** F-400, F-410
- **Authentication:** F-450 (Keycloak oAuth2)
:::

---

## Project Tasks (aus adesso Calculator)

| ID | Task-Gruppe | Task | Aufwand (PT) |
|----|-------------|------|-------------:|
| P-170 | Übergreifend | Projektmanagement | 40 |
| P-150 | Implementierung | Datenmigration | 28 |
| P-60 | Implementierung | Analyse & Software Design | 26,8 |
| P-70 | Implementierung | Software-Entwicklung | 80,5 |
| P-80 | Implementierung | Softwaretest | 13,4 |
| P-140 | Implementierung | Fehlerbearb. nach BzA | 13,4 |
| P-10 bis P-50 | Initialisierung | Setup, Kick-off, Konzepte | 9 |
| P-90 bis P-130 | Implementierung | Testautomatisierung, Doku, Schulung | 8 |
| P-180 bis P-220 | Übergreifend | Test/Architektur/DevOps/Meetings | 11 |
| | | **TOTAL Project Tasks** | **96 PT** |

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
