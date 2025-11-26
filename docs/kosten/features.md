# Feature-Liste

## Übersicht

::: tip KALKULATION
Die vollständige Feature-Liste mit Aufwandsschätzungen befindet sich im **adesso Calculator**:

📊 **[Locarno-Festival-Kalkulation.xlsm](https://o365adessogroup.sharepoint.com/:x:/r/sites/Drupal/Shared%20Documents/General/Akquisen/Locarno%20Filmfestival/Locarno-Festival-Kalkulation.xlsm?d=wdda7cd93b37f46fb8233d671e1f1110e&csf=1&web=1&e=K6r1UQ)**

**Inhalt:**
- 42 Features (F-10 bis F-450)
- Aufwand pro Feature in PT
- Rollen-Zuordnung
- Risiko-Bewertung
:::

---

## Zusammenfassung nach 8 Kern-Positionen

| # | Position | Features | Bemerkung |
|---|----------|----------|-----------|
| 1 | Azure einrichten und aufsetzen | F-20 (Hosting) | Inkl. in Setup |
| 2 | CMS installieren und einrichten | F-10, F-390 | Setup + i18n |
| 3 | CMS Webpublishing Umsetzung Website | F-30 bis F-340 | 32 Features |
| 4 | APIs anbinden (Ticketing, Fiona, Sony VOD) | F-350 bis F-380 | 4 Features |
| 5 | Registration und Anmelden (Keycloak) | F-450 | 3,33 PT |
| 6 | Datenintegration bisheriger Website | F-380 | Migration |
| 7 | Dokumentation und Bereitstellen GitHub | *(Project Tasks)* | P-120, P-130 |
| 8 | Projektleitung, Testing, Bugfix, Performance | *(Project Tasks)* | 96 PT |

---

## Feature-Kategorien

| Kategorie | Features | Beschreibung |
|-----------|----------|--------------|
| **Setup & Infrastruktur** | F-10, F-20 | Projekt-Setup, Azure Hosting |
| **Content-Modellierung** | F-30 bis F-130 | 14 Content-Types, Taxonomien, Paragraphs |
| **Views & Listings** | F-140 bis F-190 | Film-, Programm-, Award-Listings |
| **Custom Development** | F-200 bis F-240 | Credits-System, Kalender, Schema.org |
| **Suche** | F-250 | Search API + Solr |
| **Frontend** | F-260 bis F-340 | Theme, Templates, SDC-Komponenten |
| **Integrationen** | F-350 bis F-380 | Ticketing, Video, Newsletter, Import |
| **Mehrsprachigkeit** | F-390 | 4-Sprachen-Setup (DE, EN, IT, FR) |
| **SEO & Performance** | F-400, F-410 | SEO-Setup, Caching |
| **Authentication** | F-450 | Keycloak oAuth2 SSO |

---

## Risiken

| ID | Risiko | Wahrsch. | Impact |
|----|--------|----------|--------|
| R-10 | Migration komplexer als erwartet | 60% | Hoch |
| R-20 | Film-Datenbank-Import-Format unklar | 50% | Hoch |
| R-30 | Ticketing-API nicht verfügbar | 40% | Mittel |
| R-40 | Design-Änderungen während Projekt | 50% | Mittel |
| R-50 | Legacy-URL-Struktur komplex | 50% | Mittel |
| R-60 | Solr-Hosting nicht verfügbar | 30% | Mittel |
| R-70 | Programm-Kalender-Komplexität | 40% | Mittel |
| R-80 | WCAG AA Anforderungen unterschätzt | 40% | Mittel |

::: warning HÖCHSTES RISIKO
**R-10: Migration komplexer als erwartet**
- 79 Jahre Archiv-Daten
- Undokumentierte Datenstrukturen
- Qualitätsprobleme in historischen Daten
:::

---

## Position-zu-Feature Mapping

### Position 1: Azure einrichten und aufsetzen

- **F-20:** Hosting-Setup (Azure-spezifisch)
- App Service, MySQL, Redis, Front Door, Blob Storage
- Staging + Production Environments

### Position 2: CMS installieren und einrichten

- **F-10:** Projekt-Setup & CI/CD
- **F-390:** 4-Sprachen-Setup (DE, EN, IT, FR)
- Drupal CMS 2.0 Installation

### Position 3: CMS Webpublishing Umsetzung Website

- **Content-Types:** F-30 bis F-130
- **Views & Listings:** F-140 bis F-190
- **Custom Development:** F-200 bis F-250
- **Frontend:** F-260 bis F-340

### Position 4: APIs anbinden

- **F-350:** Ticketing & Akkreditierung Embed
- **F-360:** Video & Maps
- **F-370:** Newsletter & Analytics
- **F-380:** Film-Datenbank-Import

### Position 5: Registration und Anmelden (Keycloak)

- **F-450:** Keycloak oAuth2 Integration
- SSO-Integration, oAuth2 Login, User-Sync

### Position 6: Datenintegration bisheriger Website

- **F-380:** Film-Datenbank-Import / Migration
- **P-150:** Datenmigration (Project Task)
- 79 Jahre Archiv-Daten

### Position 7: Dokumentation und GitHub

- **P-120:** Anwenderhandbuch
- **P-130:** Kundenschulung

### Position 8: Projektleitung, Testing, Bugfix

- **P-170:** Projektmanagement
- **P-80:** Softwaretest
- **P-140:** Fehlerbearbeitung

---

[→ Kostenschätzung](/kosten/schaetzung)
[→ Budget-Analyse](/kosten/budget)
