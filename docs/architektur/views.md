# Views (12)

## Übersicht

Die Drupal-Architektur umfasst **12 Views** für Content-Auflistungen, Suche und Daten-Exports.

**Gesamtaufwand:** 310 Stunden

---

## 1. Film Archive Listing   KRITISCH

**Machine Name:** `film_archive_listing`
**Content Type:** `film_archive`
**Aufwand:** 50 Stunden
**Komplexität:** Complex

### Displays
- **Page:** `/festival/program-archive/film-list`
- **Block:** Einbettbare Archiv-Suche

### Features
- **Search API + Solr Backend** (MANDATORY für 10.000+ Einträge)
- Faceted Search (Jahr, Regisseur, Land, Sektion)
- AJAX Pagination
- Exposed Filters
- CSV Export

**Performance:** CRITICAL - Requires Solr

---

## 2. Current Program Films

**Machine Name:** `current_program_films`
**Content Type:** `film_program`
**Aufwand:** 30 Stunden

### Displays
- **Page:** `/festival/program`
- **Block:** Featured Films Block

### Features
- Filter by Section
- Sort by Screening Date
- AJAX Filtering
- Calendar View Integration

---

## 3. VOD Catalog

**Machine Name:** `vod_catalog`
**Content Type:** `film_vod`
**Aufwand:** 25 Stunden

### Displays
- **Page:** `/vod`

### Features
- Filter by Availability
- Sort by Date Added
- Grid/List View Toggle

---

## 4. News Listing

**Machine Name:** `news_listing`
**Content Type:** `news`
**Aufwand:** 25 Stunden

### Displays
- **Page:** `/news`
- **Block:** Latest News Block
- **Feed:** `/news/rss.xml` (RSS)

### Features
- Category Filters
- Date Range Filter
- Tag Filters
- AJAX Pagination
- RSS Feed

---

## 5. Press Releases

**Machine Name:** `press_releases`
**Content Type:** `press_release`
**Aufwand:** 20 Stunden

### Displays
- **Page:** `/press/press-releases`
- **Feed:** `/press/press-releases/rss.xml`

### Features
- Date Filters
- Search
- RSS Feed

---

## 6. Palmarès by Year

**Machine Name:** `palmares_by_year`
**Content Type:** `palmares`
**Aufwand:** 20 Stunden

### Displays
- **Page:** `/festival/palmares`

### Features
- Year Dropdown Filter
- Timeline View

---

## 7. Person Directory

**Machine Name:** `person_directory`
**Content Type:** `person`
**Aufwand:** 25 Stunden

### Displays
- **Page:** `/people`
- **Block:** Featured People Block

### Features
- Alphabetical Sorting
- Role Filter
- Search
- AJAX Pagination

---

## 8. Juries by Year

**Machine Name:** `juries_by_year`
**Content Type:** `jury`
**Aufwand:** 20 Stunden

### Displays
- **Page:** `/festival/juries`

### Features
- Year Filter
- Category Filter

---

## 9. Pro/Industry Projects

**Machine Name:** `pro_projects`
**Content Type:** `pro_project`
**Aufwand:** 25 Stunden

### Displays
- **Page:** `/pro/projects`

### Features
- Project Type Filter
- Year Filter
- Country Filter

---

## 10. Venues Map

**Machine Name:** `venues_map`
**Content Type:** `venue`
**Aufwand:** 30 Stunden

### Displays
- **Page:** `/festival/venues`

### Features
- Interactive Map (Leaflet/Google Maps)
- List View
- Filter by Type
- Geolocation Integration

---

## 11. Events Calendar

**Machine Name:** `events_calendar`
**Content Type:** `event`
**Aufwand:** 30 Stunden

### Displays
- **Page:** `/festival/events`
- **Block:** Upcoming Events

### Features
- Calendar View (Month/Week/Day)
- Filter by Event Type
- Date Range Selection
- Export to iCal

---

## 12. Film Screenings Schedule

**Machine Name:** `film_screenings`
**Content Type:** `film_program`
**Aufwand:** 30 Stunden

### Displays
- **Page:** `/festival/schedule`
- **Block:** Today's Screenings

### Features
- Filter by Date
- Filter by Venue
- Filter by Section
- Grid/Timeline View
- Export to PDF/iCal

---

## Performance-Optimierung

### Caching
- **Tag-basiertes Caching** für alle Views
- Cache per URL + Taxonomy Term
- BigPipe für Below-the-Fold Content

### Database Indexes
- `field_year`, `field_country` für Filterung
- Entity Reference Preloading
- Views mit Read Replica

### Search API (Film Archive)
- **Solr Backend MANDATORY** für 10.000+ Einträge
- Faceted Search (Land, Jahr, Sektion, Regisseur)
- Autocomplete für Regisseur-Suche

---

## Zusammenfassung

- **Total Views:** 12
- **Kritisch:** Film Archive Listing (requires Solr)
- **Gesamtaufwand:** 310 Stunden
- **Read Replica:** Empfohlen für alle Views (70% Read-Traffic)
