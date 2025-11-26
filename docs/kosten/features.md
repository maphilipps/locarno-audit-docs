# Feature-Liste für adesso Calculator

::: info EXCEL-IMPORT
Diese Feature-Liste ist für den Import in den **adesso Calculator 2.01** formatiert.
Spalten entsprechen dem Features-Sheet.
:::

## Übersicht nach 8 Kern-Positionen

| # | Position | Features | PT |
|---|----------|----------|-----|
| 1 | Azure einrichten und aufsetzen | 1 | 13 |
| 2 | CMS installieren und einrichten | 3 | 12 |
| 3 | CMS Webpublishing Umsetzung Website | 32 | 170 |
| 4 | APIs anbinden (Ticketing, Fiona, Sony VOD) | 5 | 32 |
| 5 | Registration und Anmelden (Keycloak oAuth2) | 1 | 8 |
| 6 | Datenintegration bisheriger Website | 1 | 10 |
| 7 | Dokumentation und Bereitstellen GitHub | - | (Project Tasks) |
| 8 | Projektleitung, Testing, Bugfix, Performance | - | (Project Tasks) |
| **TOTAL** | | **43** | **245 PT** |

---

## 1. Azure einrichten und aufsetzen

### F-420: Azure Infrastructure Setup

| Feld | Wert |
|------|------|
| **ID** | F-420 |
| **Feature group** | 1. Azure Infrastructure |
| **Feature sub group** | - |
| **Feature title** | Azure Infrastructure Setup |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Azure Switzerland North Setup: High Availability Konfiguration mit App Service Plan Premium v3, Azure Database for MySQL Flexible Server, Azure Front Door mit WAF (Web Application Firewall), Anti-DDoS Protection Standard, Azure Blob Storage für Medien, Application Insights Monitoring, Auto-Scaling für 5000 req/min Peak, Staging + Production Environments, CI/CD Pipeline mit GitHub Actions |
| **Assumptions** | Azure Subscription wird vom Kunden bereitgestellt. Zugang zu Azure Portal vor Projektstart. Switzerland North Region verfügbar. |
| **Risks** | R-AZURE |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 2 |
| Development | 6 |
| Test | 3 |
| Bugfix | 2 |
| **Total** | **13** |

---

## 2. CMS installieren und einrichten

### F-10: Projekt-Setup & CI/CD

| Feld | Wert |
|------|------|
| **ID** | F-10 |
| **Feature group** | 2. CMS Setup |
| **Feature sub group** | - |
| **Feature title** | Projekt-Setup & CI/CD |
| **Sub feature title** | - |
| **(Sub-)Feature description** | DDEV-Setup, Projekt-Init, Git-Repository mit Branch-Strategie, GitHub Actions CI/CD Pipeline, Linting, Testing, Deployment Workflows |
| **Assumptions** | Platform.sh oder vergleichbares Managed Hosting. Standard Git-Workflow. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 1 |
| Development | 2 |
| Test | 1 |
| Bugfix | 0 |
| **Total** | **4** |

---

### F-20: Drupal CMS Installation

| Feld | Wert |
|------|------|
| **ID** | F-20 |
| **Feature group** | 2. CMS Setup |
| **Feature sub group** | - |
| **Feature title** | Drupal CMS Installation |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Drupal CMS 2.0 Installation mit 22 Recipes (SEO, Accessibility, Forms, AI), Modul-Stack Konfiguration, Admin UI Anpassungen (Gin Theme, Coffee), Media Library Setup |
| **Assumptions** | Managed Hosting mit Drupal-Support. Keine komplexe Custom-Konfiguration. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 0 |
| Development | 1 |
| Test | 0 |
| Bugfix | 0 |
| **Total** | **1** |

---

### F-390: 4-Sprachen-Setup

| Feld | Wert |
|------|------|
| **ID** | F-390 |
| **Feature group** | 2. CMS Setup |
| **Feature sub group** | Mehrsprachigkeit |
| **Feature title** | 4-Sprachen-Setup |
| **Sub feature title** | DE, EN, IT, FR |
| **(Sub-)Feature description** | Drupal-Mehrsprachigkeit für DE, EN, IT, FR. Content Translation, Interface Translation, Language Switcher, hreflang Tags, URL-Präfixe pro Sprache |
| **Assumptions** | Übersetzungen werden vom Kunden geliefert. Standard-Übersetzungs-Workflow. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 2 |
| Development | 3 |
| Test | 1 |
| Bugfix | 1 |
| **Total** | **7** |

---

## 3. CMS Webpublishing Umsetzung Website

### 3.1 Content Types

#### F-30: CT: Film

| Feld | Wert |
|------|------|
| **ID** | F-30 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Content Types |
| **Feature title** | CT: Film |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Komplexer Content-Type mit 25+ Feldern: Titel (mehrsprachig), Synopsis, Technische Daten (Länge, Format, Land, Jahr), Cast/Crew-Referenzen, Trailer-Embed, Poster/Stills, Sektion-Zuordnung, Award-Verknüpfungen, VOD-Link |
| **Assumptions** | Film-Daten werden strukturiert geliefert. Keine automatische Verknüpfung mit externen Datenbanken (IMDB etc.). |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 2 |
| Development | 3 |
| Test | 1 |
| Bugfix | 1 |
| **Total** | **7** |

---

#### F-40: CT: Person

| Feld | Wert |
|------|------|
| **ID** | F-40 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Content Types |
| **Feature title** | CT: Person |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Content-Type für Regisseure, Schauspieler, Produzenten etc. mit Biografie, Foto, Filmografie (bidirektionale Referenz zu Filmen) |
| **Assumptions** | Keine automatische Verknüpfung mit externen Datenbanken. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 0 |
| Development | 1 |
| Test | 0 |
| Bugfix | 0 |
| **Total** | **1** |

---

#### F-50: CT: Film Section & Award

| Feld | Wert |
|------|------|
| **ID** | F-50 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Content Types |
| **Feature title** | CT: Film Section & Award |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Content-Types für die 11 Film-Sektionen (Piazza Grande, Concorso, Cineasti del presente, etc.) und Award-Kategorien (Pardo d'oro, etc.) |
| **Assumptions** | Statische Strukturen, die sich selten ändern. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 1 |
| Development | 2 |
| Test | 1 |
| Bugfix | 0 |
| **Total** | **4** |

---

#### F-60: CT: Event/Screening & Venue

| Feld | Wert |
|------|------|
| **ID** | F-60 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Content Types |
| **Feature title** | CT: Event/Screening & Venue |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Event-Content-Type mit Datum, Uhrzeit, Venue, Film-Referenz, Ticketing-Link. Venue-Content-Type mit Adresse, Kapazität, Geolocation, Maps-Integration |
| **Assumptions** | Screening-Daten werden manuell oder via Fiona Import gepflegt. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 1 |
| Development | 2 |
| Test | 1 |
| Bugfix | 0 |
| **Total** | **4** |

---

#### F-70: CT: News & Press

| Feld | Wert |
|------|------|
| **ID** | F-70 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Content Types |
| **Feature title** | CT: News & Press |
| **Sub feature title** | - |
| **(Sub-)Feature description** | News/Pressemitteilungs-Content-Type mit Titel, Teaser, Body (Paragraphs), Kategorien, Medien, Publish-Date |
| **Assumptions** | Standard-News-Funktionalität ohne komplexe Workflows. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 0 |
| Development | 1 |
| Test | 0 |
| Bugfix | 0 |
| **Total** | **1** |

---

#### F-80: CT: Festival Edition & Archiv

| Feld | Wert |
|------|------|
| **ID** | F-80 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Content Types |
| **Feature title** | CT: Festival Edition & Archiv |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Content-Type für 79 Festival-Editionen: Jahr, Datum, Thema, Jury, Palmarès-Referenz, Statistiken, historische Daten |
| **Assumptions** | Historische Daten werden migriert. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 0 |
| Development | 1 |
| Test | 0 |
| Bugfix | 0 |
| **Total** | **1** |

---

#### F-90: CT: Locarno Pro

| Feld | Wert |
|------|------|
| **ID** | F-90 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Content Types |
| **Feature title** | CT: Locarno Pro Content-Types |
| **Sub feature title** | Open Doors, Industry |
| **(Sub-)Feature description** | Content-Types für Open Doors Projects, Open Doors Completed Films, Industry Events, Co-Production Opportunities |
| **Assumptions** | Basis-Funktionalität ohne komplexe Interaktionen. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 1 |
| Development | 2 |
| Test | 1 |
| Bugfix | 0 |
| **Total** | **4** |

---

#### F-100: CT: Tickets & Akkreditierung

| Feld | Wert |
|------|------|
| **ID** | F-100 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Content Types |
| **Feature title** | CT: Tickets & Akkreditierung |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Content-Types für Ticket-/Pass-Typen und Akkreditierungs-Kategorien (Informationsseiten) |
| **Assumptions** | Nur Informationsseiten, keine Buchungslogik. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 0 |
| Development | 1 |
| Test | 0 |
| Bugfix | 0 |
| **Total** | **1** |

---

#### F-110: Taxonomien

| Feld | Wert |
|------|------|
| **ID** | F-110 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Content Types |
| **Feature title** | Taxonomien |
| **Sub feature title** | 7 Vokabulare |
| **(Sub-)Feature description** | 7 Taxonomie-Vokabulare: Genre, Land, Sprache, Jahr, News-Kategorie, Award-Typ, Person-Rolle |
| **Assumptions** | Vorbefüllt mit Standard-Werten. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 0 |
| Development | 1 |
| Test | 0 |
| Bugfix | 0 |
| **Total** | **1** |

---

### 3.2 Paragraph Types / Components

#### F-120: Paragraph-Types (16 Typen)

| Feld | Wert |
|------|------|
| **ID** | F-120 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Paragraphs |
| **Feature title** | Paragraph-Types (16 Typen) |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Text, Text+Bild, Bild/Galerie, Video-Embed, Quote, CTA, Accordion, Tabs, Feature-Box, Film-Teaser-Liste, Person-Grid, Event-Liste, Download-Liste, Social-Embed, Maps, Newsletter-Signup |
| **Assumptions** | Design liegt vor, keine komplexen Animationen. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 2 |
| Development | 4 |
| Test | 1 |
| Bugfix | 1 |
| **Total** | **8** |

---

#### F-130: Media-Types

| Feld | Wert |
|------|------|
| **ID** | F-130 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Media |
| **Feature title** | Media-Types |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Konfiguration der Media-Types: Image (mit Focal Point), Remote Video (YouTube/Vimeo), Document (PDF), Audio |
| **Assumptions** | Standard Drupal Media-Handling. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 0 |
| Development | 1 |
| Test | 0 |
| Bugfix | 0 |
| **Total** | **1** |

---

### 3.3 Views & Listings

#### F-140: Film-Listings

| Feld | Wert |
|------|------|
| **ID** | F-140 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Views & Listings |
| **Feature title** | Film-Listings |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Film-Hauptlisting mit Exposed Filters (Sektion, Jahr, Land, Genre), AJAX-Pagination, Card-Darstellung |
| **Assumptions** | Standard Views-Funktionalität, AJAX-Filter. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 1 |
| Development | 2 |
| Test | 1 |
| Bugfix | 0 |
| **Total** | **4** |

---

#### F-150: Programm-Übersicht

| Feld | Wert |
|------|------|
| **ID** | F-150 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Views & Listings |
| **Feature title** | Programm-Übersicht |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Screenings nach Tag/Venue Matrix-Darstellung, Kalender-View, Tagesansicht, Wochenansicht |
| **Assumptions** | Komplexe View mit Custom-Gruppierung. |
| **Risks** | R-70 |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 1 |
| Development | 2 |
| Test | 1 |
| Bugfix | 0 |
| **Total** | **4** |

---

#### F-160: Award & Palmarès Listings

| Feld | Wert |
|------|------|
| **ID** | F-160 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Views & Listings |
| **Feature title** | Award & Palmarès Listings |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Award-Listing pro Jahr (Palmarès), Award-Historie pro Kategorie, Gewinner-Anzeige auf Film-/Person-Seiten |
| **Assumptions** | Daten sind strukturiert verfügbar. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 1 |
| Development | 2 |
| Test | 1 |
| Bugfix | 0 |
| **Total** | **4** |

---

#### F-170: Personen & Jury Listings

| Feld | Wert |
|------|------|
| **ID** | F-170 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Views & Listings |
| **Feature title** | Personen & Jury Listings |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Personen-Listing mit Filmografie, Jury-Übersicht pro Jahr und Sektion |
| **Assumptions** | Standard Views mit Referenz-Auflösung. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 0 |
| Development | 1 |
| Test | 0 |
| Bugfix | 0 |
| **Total** | **1** |

---

#### F-180: News & Content Listings

| Feld | Wert |
|------|------|
| **ID** | F-180 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Views & Listings |
| **Feature title** | News & Content Listings |
| **Sub feature title** | - |
| **(Sub-)Feature description** | News-Listing mit Pagination, Pressemitteilungen-Archiv, Content-Übersichten |
| **Assumptions** | Standard Views-Funktionalität. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 1 |
| Development | 2 |
| Test | 1 |
| Bugfix | 0 |
| **Total** | **4** |

---

#### F-190: Open Doors & Pro Listings

| Feld | Wert |
|------|------|
| **ID** | F-190 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Views & Listings |
| **Feature title** | Open Doors & Pro Listings |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Open Doors Projects-Listing, Completed Films-Archiv, Industry Events, Pro-Bereich Übersichten |
| **Assumptions** | Ähnliche Struktur wie andere Listings. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 1 |
| Development | 2 |
| Test | 1 |
| Bugfix | 0 |
| **Total** | **4** |

---

### 3.4 Custom Development

#### F-200: Film-Credits-System

| Feld | Wert |
|------|------|
| **ID** | F-200 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Custom Development |
| **Feature title** | Film-Credits-System |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Custom-Modul für bidirektionale Film-Person-Verknüpfung mit Rollen (Regie, Cast, Produktion etc.), sortierbare Credits-Liste |
| **Assumptions** | Entity Reference mit Custom Field Formatter. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 2 |
| Development | 4 |
| Test | 1 |
| Bugfix | 1 |
| **Total** | **8** |

---

#### F-210: Programm-Kalender-Logik

| Feld | Wert |
|------|------|
| **ID** | F-210 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Custom Development |
| **Feature title** | Programm-Kalender-Logik |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Custom-Modul für Zeit/Venue-Matrix, Konflikt-Erkennung bei Überschneidungen, Tages-/Wochen-Aggregation |
| **Assumptions** | Keine Echtzeit-Verfügbarkeit, nur Anzeige. |
| **Risks** | R-70 |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 2 |
| Development | 4 |
| Test | 1 |
| Bugfix | 1 |
| **Total** | **8** |

---

#### F-220: Award-Gewinner-Verknüpfung

| Feld | Wert |
|------|------|
| **ID** | F-220 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Custom Development |
| **Feature title** | Award-Gewinner-Verknüpfung |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Logik für Film→Award→Jahr Verknüpfung, automatische Badge-Anzeige auf Film-Seiten |
| **Assumptions** | Entity Reference basiert. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 1 |
| Development | 2 |
| Test | 1 |
| Bugfix | 0 |
| **Total** | **4** |

---

#### F-230: Edition-Context

| Feld | Wert |
|------|------|
| **ID** | F-230 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Custom Development |
| **Feature title** | Edition-Context |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Modul für aktuelle vs. vergangene Festival-Edition Handling, automatische Content-Filterung nach Edition |
| **Assumptions** | Konfigurierbar via Admin-UI. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 1 |
| Development | 2 |
| Test | 1 |
| Bugfix | 0 |
| **Total** | **4** |

---

#### F-240: Structured Data / Schema.org

| Feld | Wert |
|------|------|
| **ID** | F-240 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Custom Development |
| **Feature title** | Structured Data / Schema.org |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Custom-Modul für Schema.org Markup: Movie, Event, Person, Organization, VideoObject JSON-LD |
| **Assumptions** | Basierend auf Content-Type-Feldern. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 1 |
| Development | 2 |
| Test | 1 |
| Bugfix | 0 |
| **Total** | **4** |

---

#### F-250: Search API + Solr

| Feld | Wert |
|------|------|
| **ID** | F-250 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Suche |
| **Feature title** | Search API + Solr |
| **Sub feature title** | Enterprise Search |
| **(Sub-)Feature description** | Search API Konfiguration, Solr-Backend auf Azure, Indexierung aller Content-Types, Faceted Search (Jahr, Genre, Sektion, Land), Multilingual Search, Autocomplete, Boosting für Relevanz |
| **Assumptions** | Solr-Server verfügbar (Managed Hosting oder dedizierter Service). |
| **Risks** | R-60 |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 2 |
| Development | 5 |
| Test | 2 |
| Bugfix | 1 |
| **Total** | **10** |

---

### 3.5 Frontend / Theme

#### F-260: Theme-Setup & Design-System

| Feld | Wert |
|------|------|
| **ID** | F-260 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Frontend |
| **Feature title** | Theme-Setup & Design-System |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Custom Theme auf Basis von Starterkit/Radix, Design-System Implementation, Tailwind CSS Setup, Typography, Color Scheme, Icon Library |
| **Assumptions** | Design-System und Styleguide werden aus Figma geliefert. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 2 |
| Development | 3 |
| Test | 1 |
| Bugfix | 1 |
| **Total** | **7** |

---

#### F-270: Header & Navigation

| Feld | Wert |
|------|------|
| **ID** | F-270 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Frontend |
| **Feature title** | Header & Navigation |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Mega-Navigation Desktop mit Film-Sektionen, Mobile Off-Canvas Navigation, Language Switcher, Search Toggle, User Menu (Login/Logout) |
| **Assumptions** | Komplexe Navigation mit mehreren Ebenen. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 2 |
| Development | 3 |
| Test | 1 |
| Bugfix | 1 |
| **Total** | **7** |

---

#### F-280: Footer & Globale Elemente

| Feld | Wert |
|------|------|
| **ID** | F-280 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Frontend |
| **Feature title** | Footer & Globale Elemente |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Multi-Column Footer mit Newsletter-Signup, Breadcrumbs, Back-to-Top, Cookie Banner, Social Icons, Partner-Logos |
| **Assumptions** | Standard-Komplexität. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 1 |
| Development | 2 |
| Test | 1 |
| Bugfix | 0 |
| **Total** | **4** |

---

#### F-290: Homepage

| Feld | Wert |
|------|------|
| **ID** | F-290 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Frontend |
| **Feature title** | Homepage |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Homepage-Template mit Hero, aktuelle News, Featured Films, Programm-Highlights, Partner-Slider, Events-Teaser |
| **Assumptions** | Layout Builder oder Custom-Template. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 2 |
| Development | 3 |
| Test | 1 |
| Bugfix | 1 |
| **Total** | **7** |

---

#### F-300: Film-Detail-Template

| Feld | Wert |
|------|------|
| **ID** | F-300 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Frontend |
| **Feature title** | Film-Detail-Template |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Komplexes Template mit Poster, Trailer, Synopsis, Credits, Technische Daten, Screenings, Awards, Related Films |
| **Assumptions** | Wichtigste Seite, hoher Detailgrad. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 2 |
| Development | 3 |
| Test | 1 |
| Bugfix | 1 |
| **Total** | **7** |

---

#### F-310: Weitere Detail-Templates

| Feld | Wert |
|------|------|
| **ID** | F-310 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Frontend |
| **Feature title** | Weitere Detail-Templates |
| **Sub feature title** | Person, News, Section, Award |
| **(Sub-)Feature description** | Person-Detail, News-Detail, Section-Übersicht, Award-Detail, Event-Detail Templates |
| **Assumptions** | Mittlere Komplexität pro Template. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 2 |
| Development | 4 |
| Test | 1 |
| Bugfix | 1 |
| **Total** | **8** |

---

#### F-320: Landing Pages

| Feld | Wert |
|------|------|
| **ID** | F-320 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Frontend |
| **Feature title** | Landing Pages |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Archiv-Landing, Edition-Übersicht, Locarno Pro Landing, Tickets/Akkreditierung Landing, About-Seiten |
| **Assumptions** | Modularer Aufbau mit Paragraphs. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 2 |
| Development | 5 |
| Test | 2 |
| Bugfix | 1 |
| **Total** | **10** |

---

#### F-330: SDC Komponenten (20+)

| Feld | Wert |
|------|------|
| **ID** | F-330 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Frontend |
| **Feature title** | SDC Komponenten (20+) |
| **Sub feature title** | Single Directory Components |
| **(Sub-)Feature description** | Card/Teaser (Film, Person, News), Film-Slider, Hero Variants, Section Headers, Badges, Buttons, Form Elements, Modal, Tabs, Accordion |
| **Assumptions** | Single Directory Components mit Twig/CSS/JS. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 5 |
| Development | 10 |
| Test | 3 |
| Bugfix | 2 |
| **Total** | **20** |

---

#### F-340: Responsive & Cross-Browser

| Feld | Wert |
|------|------|
| **ID** | F-340 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Frontend |
| **Feature title** | Responsive & Cross-Browser |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Responsive Anpassungen für alle Templates und Komponenten (Mobile, Tablet, Desktop), Cross-Browser Testing (Chrome, Firefox, Safari, Edge) |
| **Assumptions** | Komplexe Site mit vielen Komponenten. |
| **Risks** | R-40 |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 4 |
| Development | 8 |
| Test | 2 |
| Bugfix | 2 |
| **Total** | **16** |

---

### 3.6 SEO & Performance

#### F-400: SEO-Komplett-Setup

| Feld | Wert |
|------|------|
| **ID** | F-400 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | SEO |
| **Feature title** | SEO-Komplett-Setup |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Metatags, Open Graph, XML-Sitemap (mehrsprachig), Robots.txt, Canonical URLs, hreflang, Legacy-URL Redirects (2.000+) |
| **Assumptions** | Legacy-URLs werden dokumentiert geliefert. |
| **Risks** | R-50 |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 2 |
| Development | 4 |
| Test | 1 |
| Bugfix | 1 |
| **Total** | **8** |

---

#### F-410: Performance-Optimierung

| Feld | Wert |
|------|------|
| **ID** | F-410 |
| **Feature group** | 3. CMS Webpublishing |
| **Feature sub group** | Performance |
| **Feature title** | Performance-Optimierung |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Caching-Strategie (Varnish, Redis, CDN), Lazy Loading für Bilder/Videos, Critical CSS, Asset-Aggregation, WebP-Konvertierung |
| **Assumptions** | Hosting unterstützt Caching/CDN. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 1 |
| Development | 2 |
| Test | 1 |
| Bugfix | 0 |
| **Total** | **4** |

---

## 4. APIs anbinden (Ticketing, Fiona, Sony VOD)

### F-350: Ticketing Widget Integration

| Feld | Wert |
|------|------|
| **ID** | F-350 |
| **Feature group** | 4. API Integrationen |
| **Feature sub group** | Ticketing |
| **Feature title** | Ticketing & Akkreditierung Embed |
| **Sub feature title** | Widget-Integration |
| **(Sub-)Feature description** | Integration externes Ticketing-System via Embed/iFrame/Widget, Buchung, Warenkorb, Ticket-Export als PDF & QR-Code, responsive Einbindung |
| **Assumptions** | Primär Embed, keine tiefe API-Integration. Ticketing-System liefert Widget. |
| **Risks** | R-30 |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 2 |
| Development | 3 |
| Test | 1 |
| Bugfix | 1 |
| **Total** | **7** |

---

### F-430: Fiona Festival REST API Integration

| Feld | Wert |
|------|------|
| **ID** | F-430 |
| **Feature group** | 4. API Integrationen |
| **Feature sub group** | Fiona Festival |
| **Feature title** | Fiona Festival REST API Integration |
| **Sub feature title** | Events & Screenings |
| **(Sub-)Feature description** | Integration der Fiona Festival Plattform (https://fiona-festival.com) via REST API: Synchronisation von Events, Pressekonferenzen, Masterclasses, Screenings. Custom Drupal Module mit Guzzle HTTP Client. Queue-basierte Synchronisation alle 15 Min während Festival. Data Mapping Fiona Events → Drupal Event Nodes. Venue-Referenzen, Datum/Zeit-Handling. Error-Handling mit Retry-Logik, Fallback bei API-Ausfall, Admin-Benachrichtigung. |
| **Assumptions** | Fiona API-Dokumentation und Testzugang werden vor Entwicklungsstart bereitgestellt. API ist stabil und versioniert. Datenformat ist dokumentiert. |
| **Risks** | R-20 |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 2 |
| Development | 6 |
| Test | 3 |
| Bugfix | 1 |
| **Total** | **12** |

---

### F-440: Sony VOD Streaming Integration (sVOD/fVOD)

| Feld | Wert |
|------|------|
| **ID** | F-440 |
| **Feature group** | 4. API Integrationen |
| **Feature sub group** | Video Streaming |
| **Feature title** | Sony VOD Streaming Integration |
| **Sub feature title** | sVOD & fVOD |
| **(Sub-)Feature description** | Integration Sony Pictures Core für Video on Demand: sVOD (Subscription-based VOD) und fVOD (Free VOD). API-Anbindung für Catalog-Sync. Responsive Video Player mit DRM-Unterstützung (Widevine, FairPlay). Access Control basierend auf Keycloak-Rollen/Berechtigungen (Paywall). VOD-Inhalte als Drupal Media Entities mit Metadaten-Sync. |
| **Assumptions** | Sony Pictures Core API-Zugang und Dokumentation verfügbar. DRM-Anforderungen sind definiert. Multi-DRM Strategy abgestimmt. |
| **Risks** | R-VOD |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 2 |
| Development | 4 |
| Test | 1 |
| Bugfix | 1 |
| **Total** | **8** |

---

### F-360: Video & Maps Integration

| Feld | Wert |
|------|------|
| **ID** | F-360 |
| **Feature group** | 4. API Integrationen |
| **Feature sub group** | Media |
| **Feature title** | Video & Maps |
| **Sub feature title** | YouTube, Vimeo, Google Maps |
| **(Sub-)Feature description** | YouTube/Vimeo oEmbed für Trailer, Google Maps für Venue-Standorte, responsive Einbindung, Lazy Loading |
| **Assumptions** | Standard-Integrationen, API-Keys verfügbar. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 0 |
| Development | 1 |
| Test | 0 |
| Bugfix | 0 |
| **Total** | **1** |

---

### F-370: Newsletter & Analytics

| Feld | Wert |
|------|------|
| **ID** | F-370 |
| **Feature group** | 4. API Integrationen |
| **Feature sub group** | Marketing |
| **Feature title** | Newsletter & Analytics |
| **Sub feature title** | - |
| **(Sub-)Feature description** | Newsletter-Signup (Mailchimp/Sendinblue), GA4 Integration via GTM, Cookie Consent Integration |
| **Assumptions** | Standard-Module verfügbar. Newsletter-Provider-Account vorhanden. |
| **Risks** | - |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 1 |
| Development | 2 |
| Test | 1 |
| Bugfix | 0 |
| **Total** | **4** |

---

## 5. Registration und Anmelden (Keycloak oAuth2)

### F-450: Keycloak oAuth2 SSO Integration

| Feld | Wert |
|------|------|
| **ID** | F-450 |
| **Feature group** | 5. Keycloak oAuth2 |
| **Feature sub group** | - |
| **Feature title** | Keycloak oAuth2 SSO Integration |
| **Sub feature title** | Single Sign-On |
| **(Sub-)Feature description** | Integration mit bestehendem Keycloak Identity Provider des Festivals: oAuth 2.0 / OpenID Connect Protokoll. Simple OAuth + OpenID Connect Drupal Module Setup. Keycloak Client Configuration (Client-ID/Secret, Redirect URIs, Scope-Mapping). Automatische Drupal-User-Erstellung bei erstem Login (User Provisioning). Rollen-Mapping: Keycloak Groups → Drupal Roles (Public, Press, Pro/Industry, Admin). Session Management mit Token Refresh, Logout-Propagation, Session Timeout Sync. User Account Anzeige und Anpassung im Frontend. |
| **Assumptions** | Keycloak-Testzugang wird vor Entwicklungsstart bereitgestellt. Client-ID/Secret und Scopes sind definiert. Keycloak-Version ist kompatibel (v20+). |
| **Risks** | R-KEYCLOAK |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 2 |
| Development | 4 |
| Test | 1 |
| Bugfix | 1 |
| **Total** | **8** |

---

## 6. Datenintegration bisheriger Website

### F-380: Film-Datenbank-Import / Migration

| Feld | Wert |
|------|------|
| **ID** | F-380 |
| **Feature group** | 6. Datenintegration |
| **Feature sub group** | Migration |
| **Feature title** | Datenintegration bisheriger Website |
| **Sub feature title** | Magnolia Content Export |
| **(Sub-)Feature description** | Import-Schnittstelle für Film-Daten und Content aus bestehendem Magnolia CMS. Content Export (JCR XML + CSV). Data Mapping & Transformation. Drupal Migrate Plugin Development. Migration der letzten 4 Jahre: Films (~800), News (~400), Press Releases (~200), Events (~500), Persons (~1.000). Film-Archiv komplett (10.000+ Einträge). Media Assets Migration (~8.000 Dateien). URL Redirects für 2.000+ Legacy-URLs. Validation & Quality Checks. |
| **Assumptions** | Magnolia Export-Zugang verfügbar. Format und Struktur der Quelldaten werden dokumentiert. Historische Daten sind vollständig. |
| **Risks** | R-10 |
| **Ref. ID** | - |

| Phase | PT |
|-------|-----|
| Design | 2 |
| Development | 5 |
| Test | 2 |
| Bugfix | 1 |
| **Total** | **10** |

---

## Risiken-Referenz

| Risk-ID | Titel | Beschreibung |
|---------|-------|--------------|
| R-10 | Migration komplexer als erwartet | Datenstrukturen des Altsystems undokumentiert |
| R-20 | Fiona API-Format unklar | Format und Struktur der externen Daten unklar |
| R-30 | Ticketing-Widget nicht verfügbar | Ticketing-System liefert kein geeignetes Widget |
| R-40 | Design-Änderungen während Projekt | Geliefertes Design wird während Entwicklung geändert |
| R-50 | Legacy-URL-Struktur komplex | Bestehende URL-Struktur komplex und inkonsistent |
| R-60 | Solr-Hosting nicht verfügbar | Hosting bietet kein Solr |
| R-70 | Programm-Kalender-Komplexität | Zeit/Venue-Matrix komplexer als erwartet |
| R-AZURE | Azure Service-Limits | Limits während Festival-Peak |
| R-KEYCLOAK | Keycloak-Version Inkompatibilität | Version nicht kompatibel |
| R-VOD | DRM-Kompatibilität | Browser-DRM-Unterstützung |

---

## Zusammenfassung für Excel-Import

### Feature-Summen nach Position

| Position | Features | Design | Dev | Test | Bugfix | Total PT |
|----------|----------|--------|-----|------|--------|----------|
| 1. Azure Infrastructure | 1 | 2 | 6 | 3 | 2 | **13** |
| 2. CMS Setup | 3 | 3 | 6 | 2 | 1 | **12** |
| 3. CMS Webpublishing | 32 | 43 | 86 | 27 | 14 | **170** |
| 4. API Integrationen | 5 | 7 | 16 | 6 | 3 | **32** |
| 5. Keycloak oAuth2 | 1 | 2 | 4 | 1 | 1 | **8** |
| 6. Datenintegration | 1 | 2 | 5 | 2 | 1 | **10** |
| **TOTAL FEATURES** | **43** | **59** | **123** | **41** | **22** | **245 PT** |

---

::: tip EXCEL-IMPORT
Kopieren Sie die Tabellen oben in das Features-Sheet des adesso Calculators.
Die Feature Groups entsprechen den 8 Kern-Positionen der Offerte.
:::

[→ Offerte Übersicht](/kosten/offerte)
[→ Kostenschätzung Details](/kosten/schaetzung)
