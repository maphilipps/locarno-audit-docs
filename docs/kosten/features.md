# Feature-Liste (adesso Calculator)

::: info QUELLE
Diese Feature-Liste stammt aus dem **adesso Calculator 2.01** (Locarno-Festival-Kalkulation.xlsm).
**42 Features** mit einem Gesamtaufwand von **137,5 PT** (Personentage).
*(inkl. F-450 Keycloak: 3,33 PT)*
:::

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

## Alle Features nach Gruppe

### Setup & Infrastruktur (2 Features)

| ID | Title | Beschreibung | Annahmen |
|----|-------|--------------|----------|
| **F-10** | Projekt-Setup & CI/CD | DDEV-Setup, Git-Repository mit Branching-Strategie, CI/CD Pipeline (GitHub Actions), Multi-Environment Setup | Azure Hosting. Standard Drupal-Setup. |
| **F-20** | Hosting-Setup | Einrichtung Platform.sh oder Azure, Multi-Environment Konfiguration, Deployment-Prozesse, SSL | Azure Hosting mit Drupal-Support. |

---

### Content-Modellierung (14 Features)

| ID | Title | Beschreibung | Risiko |
|----|-------|--------------|--------|
| **F-30** | CT: Film | 25+ Felder: Titel (mehrsprachig), Originaltitel, Jahr, Laufzeit, Land, Synopsis, Credits (Referenzen), Trailer, Stills | - |
| **F-40** | CT: Person | Regisseure, Schauspieler, Produzenten, Jury: Name, Biografie, Foto, Filmografie (via Referenzen) | - |
| **F-50** | CT: Film Section & Award | 11 Film-Sektionen (Piazza Grande, Concorso, etc.), 20+ Awards (Pardo d'Oro, etc.) | - |
| **F-60** | CT: Event/Screening & Venue | Events mit Datum, Uhrzeit, Venue, Film-Referenz. Venues mit Adresse, Kapazität, Karte | - |
| **F-70** | CT: News & Press | News/Pressemitteilungen mit Titel, Teaser, Body, Datum, Kategorie, Medien | - |
| **F-80** | CT: Festival Edition & Archiv | 79 Festival-Editionen: Jahr, Motto, Jury, Statistiken, verknüpfte Filme/Awards | - |
| **F-90** | Locarno Pro Content-Types | Open Doors Projects, Industry-Events, ToolBox-Ressourcen | - |
| **F-100** | CT: Tickets & Akkreditierung | Ticket-/Pass-Typen, Akkreditierungskategorien (nur Infoseiten) | - |
| **F-110** | Taxonomien | 7 Vokabulare: Genre, Land, Sprache, Jahr, Rolle, Award-Kategorie, Region | - |
| **F-120** | Paragraph-Types (16 Typen) | Text, Text+Bild, Galerie, Video-Embed, Quote, CTA, Akkordeon, Film-Slider, Person-Grid, etc. | - |
| **F-130** | Media-Types | Image (Focal Point), Remote Video (YouTube/Vimeo), Document (PDF, Press-Kits) | - |

---

### Views & Listings (6 Features)

| ID | Title | Beschreibung | Risiko |
|----|-------|--------------|--------|
| **F-140** | Film-Listings | Film-Hauptlisting mit Exposed Filters (Sektion, Jahr, Land, A-Z), AJAX-Filter | - |
| **F-150** | Programm-Übersicht | Screenings nach Tag/Venue Matrix, Kalender-View, Filter nach Datum/Venue | R-70 |
| **F-160** | Award & Palmarès Listings | Award-Listing pro Jahr, Award-Historie, Gewinner-Verknüpfung | - |
| **F-170** | Personen & Jury Listings | Personen mit Filmografie, Jury-Übersicht pro Jahr, Team-Listing | - |
| **F-180** | News & Content Listings | News mit Pagination, Pressemitteilungen-Archiv, FAQ-Listing | - |
| **F-190** | Open Doors & Pro Listings | Open Doors Projects, Completed Films-Archiv, Venue-Übersicht | - |

---

### Custom Development (5 Features)

| ID | Title | Beschreibung | Risiko |
|----|-------|--------------|--------|
| **F-200** | Film-Credits-System | Bidirektionale Film-Person-Verknüpfung mit Rollen, automatische Filmografie | - |
| **F-210** | Programm-Kalender-Logik | Zeit/Venue-Matrix, Konflikt-Erkennung, Tagesansicht-Generierung | **R-70** |
| **F-220** | Award-Gewinner-Verknüpfung | Film→Award→Jahr Logik, automatische Badge-Anzeige auf Film-Seiten | - |
| **F-230** | Edition-Context | Aktuelle vs. vergangene Festival-Edition, automatische Umschaltung, Archiv-Modus | - |
| **F-240** | Structured Data / Schema.org | Schema.org Markup: Movie, Event, Person, Organization. JSON-LD Generierung | - |

---

### Suche (1 Feature)

| ID | Title | Beschreibung | Risiko |
|----|-------|--------------|--------|
| **F-250** | Search API + Solr | Search API, Solr-Backend, Facetten (Jahr, Sektion, Land, Genre), Autocomplete, Mehrsprachig | **R-60** |

---

### Frontend (9 Features)

| ID | Title | Beschreibung | Risiko |
|----|-------|--------------|--------|
| **F-260** | Theme-Setup & Design-System | Custom Theme (Starterkit/Radix), Design-Tokens, Vite Build, SCSS-Architektur | - |
| **F-270** | Header & Navigation | Mega-Navigation Desktop, Mobile Off-Canvas, Language Switcher, Search, Sticky | - |
| **F-280** | Footer & Globale Elemente | Multi-Column Footer, Newsletter-Signup, Breadcrumb, Cookie-Banner | - |
| **F-290** | Homepage | Hero, News, Featured Films, Countdown, Programm-Teaser, Sponsor-Logos | - |
| **F-300** | Film-Detail-Template | Poster, Trailer, Synopsis, Credits, Screenings, Awards, Related Films, Galerie | - |
| **F-310** | Weitere Detail-Templates | Person, News, Section, Award, Event, Venue (6 Templates) | - |
| **F-320** | Landing Pages | Archiv, Edition, Locarno Pro, Open Doors, Tickets, Akkreditierung, FAQ (9 Templates) | - |
| **F-330** | SDC Komponenten (20+) | Cards, Film-Slider, Hero, Credits-Liste, Award-Badge, Kalender, Filter, Tabs, Modal, etc. | - |
| **F-340** | Responsive & Cross-Browser | Responsive für alle Templates (Mobile, Tablet, Desktop), Cross-Browser-Testing | **R-40** |

---

### Integrationen (4 Features)

| ID | Title | Beschreibung | Risiko |
|----|-------|--------------|--------|
| **F-350** | Ticketing & Akkreditierung Embed | Externes Ticketing via Embed/iFrame, Akkreditierungs-Portal, ggf. API für Verfügbarkeit | **R-30** |
| **F-360** | Video & Maps | YouTube/Vimeo oEmbed, Google Maps für Venues, responsive Einbettung | - |
| **F-370** | Newsletter & Analytics | Newsletter-Signup (Mailchimp/Sendinblue), GA4 mit Consent-Banner (DSGVO/DSG) | - |
| **F-380** | Film-Datenbank-Import | Import aus externer Quelle, Mapping, Validierung. **Hohes Risiko.** | **R-20** |

---

### Mehrsprachigkeit (1 Feature)

| ID | Title | Beschreibung | Risiko |
|----|-------|--------------|--------|
| **F-390** | 4-Sprachen-Setup | DE, EN, IT, FR. Content Translation, Interface Translation, hreflang, TMGMT | - |

---

### Authentication (1 Feature)

| ID | Title | Beschreibung | Aufwand |
|----|-------|--------------|--------:|
| **F-450** | Keycloak oAuth2 Integration | SSO-Integration mit Keycloak, oAuth2 Login, User-Synchronisation, Rollen-Mapping | **3,33 PT** |

---

### SEO & Performance (2 Features)

| ID | Title | Beschreibung | Risiko |
|----|-------|--------------|--------|
| **F-400** | SEO-Komplett-Setup | Metatags, Open Graph, XML-Sitemap, Pathauto, Redirects, Structured Data, robots.txt | **R-50** |
| **F-410** | Performance-Optimierung | Caching-Strategie, CDN, Lazy Loading, Critical CSS, Performance-Monitoring | - |

---

## Risiken-Referenz

| ID | Risiko | Wahrsch. | Impact | Gewichtet |
|----|--------|----------|--------|-----------|
| R-10 | Migration komplexer als erwartet | 60% | 15 PT | **9,0 PT** |
| R-20 | Film-Datenbank-Import-Format unklar | 50% | 10 PT | **5,0 PT** |
| R-30 | Ticketing-API nicht verfügbar | 40% | 5 PT | **2,0 PT** |
| R-40 | Design-Änderungen während Projekt | 50% | 8 PT | **4,0 PT** |
| R-50 | Legacy-URL-Struktur komplex | 50% | 5 PT | **2,5 PT** |
| R-60 | Solr-Hosting nicht verfügbar | 30% | 5 PT | **1,5 PT** |
| R-70 | Programm-Kalender-Komplexität | 40% | 6 PT | **2,4 PT** |
| R-80 | WCAG AA Anforderungen unterschätzt | 40% | 5 PT | **2,0 PT** |
| | **TOTAL Risikopuffer** | | 59 PT | **28,4 PT** |

---

## Mapping: 8 Positionen → Excel-Features

### Position 1: Azure einrichten und aufsetzen

- **F-20:** Hosting-Setup (Azure-spezifisch)
- Inkludiert: App Service, MySQL, Redis, Front Door, Blob Storage, Application Insights
- Staging + Production Environments
- CI/CD mit GitHub Actions

### Position 2: CMS installieren und einrichten

- **F-10:** Projekt-Setup & CI/CD
- **F-390:** 4-Sprachen-Setup (DE, EN, IT, FR)
- Drupal CMS 2.0 Installation
- Modul-Stack Konfiguration

### Position 3: CMS Webpublishing Umsetzung Website

**Content-Types (11):** F-30 bis F-130
- Film, Person, Section, Award, Event, Venue, News, Press, Edition, Pro, Tickets

**Views & Listings (6):** F-140 bis F-190
- Film-Listings, Programm, Awards, Personen, News, Pro

**Custom Development (5):** F-200 bis F-250
- Credits, Kalender, Awards, Edition-Context, Schema.org, Search

**Frontend (9):** F-260 bis F-340
- Theme, Header, Footer, Homepage, Templates, Components, Responsive

### Position 4: APIs anbinden

- **F-350:** Ticketing & Akkreditierung Embed
- **F-360:** Video & Maps (YouTube, Vimeo, Google Maps)
- **F-370:** Newsletter & Analytics (Mailchimp, GA4)
- **F-380:** Film-Datenbank-Import

### Position 5: Registration und Anmelden (Keycloak)

- **F-450:** Keycloak oAuth2 Integration (3,33 PT)
- SSO-Integration mit Keycloak
- oAuth2 Login Flow
- User-Synchronisation
- Rollen-Mapping

### Position 6: Datenintegration bisheriger Website

- **F-380:** Film-Datenbank-Import / Migration
- **P-150:** Datenmigration (28 PT in Project Tasks)
- Magnolia Content Export
- 79 Jahre Archiv-Daten

### Position 7: Dokumentation und Bereitstellen GitHub

Abgedeckt durch **Project Tasks:**
- **P-120:** Erstellung Anwenderhandbuch (2 PT)
- **P-130:** Kundenschulung (2 PT)

### Position 8: Projektleitung, Testing, Bugfix, Performance

Abgedeckt durch **Project Tasks (96 PT):**
- **P-170:** Projektmanagement (40 PT)
- **P-80:** Softwaretest (13,4 PT)
- **P-140:** Fehlerbearb. nach BzA (13,4 PT)
- **P-60/P-70:** Analyse & Entwicklung (107 PT)

---

[→ Kostenschätzung](/kosten/schaetzung)
[→ Budget-Analyse](/kosten/budget)
[→ Offerte](/kosten/offerte)
