# Content Types (17)

Die Drupal-Architektur umfasst 17 Content Types für die Locarno Festival-Website mit insgesamt **400 Stunden** Entwicklungsaufwand.

## Übersicht

| Content Type | Machine Name | Komplexität | Felder | Stunden |
|--------------|--------------|-------------|---------|---------|
| Homepage | `homepage` | Komplex | Hero Carousel, Content Sections, Meta Tags | 40 |
| Film Program | `film_program` | Komplex | 15 Felder (aktuelles Festival) | 60 |
| Film Archive | `film_archive` | Komplex | 11 Felder (10.000+ historische Filme) | 50 |
| Film VOD | `film_vod` | Mittel | 10 Felder (Video on Demand) | 35 |
| Person | `person` | Mittel | 8 Felder (Regisseure, Cast, Jury) | 30 |
| News | `news` | Mittel | 7 Felder (Nachrichten) | 25 |
| Press Release | `press_release` | Niedrig | 5 Felder (Pressemitteilungen) | 15 |
| Event | `event` | Mittel | 7 Felder (Veranstaltungen) | 20 |
| Landing Page | `landing_page` | Komplex | Flexible Sections (Layout Builder) | 45 |
| Page | `page` | Niedrig | 4 Felder (Standardseite) | 15 |
| Venue | `venue` | Niedrig | 8 Felder (Veranstaltungsorte) | 12 |
| Sponsor | `sponsor` | Niedrig | 6 Felder (Sponsoren) | 10 |
| Partner | `partner` | Niedrig | 6 Felder (Partner) | 10 |
| Award | `award` | Niedrig | 5 Felder (Auszeichnungen) | 8 |
| Jury Member | `jury_member` | Niedrig | 7 Felder (Jurymitglieder) | 12 |
| FAQ | `faq` | Niedrig | 3 Felder (Häufige Fragen) | 6 |
| Testimony | `testimony` | Niedrig | 4 Felder (Testimonials) | 7 |

**Gesamt:** 400 Stunden (50 Personentage)

---

## Film Program (film_program)

**Zweck:** Aktuelle Festival-Filme mit Screening-Zeiten und vollständigen Informationen

### Felder (15)

| Feld | Machine Name | Typ | Pflicht |
|------|--------------|-----|---------|
| Titel (Original) | `field_original_title` | String |  |
| Regisseur(e) | `field_directors` | Entity Ref ’ Person (mehrfach) |  |
| Land | `field_country` | Taxonomy ’ Countries (mehrfach) |  |
| Jahr | `field_year` | Integer |  |
| Dauer (Min) | `field_duration` | Integer |  |
| Filmsektion | `field_film_section` | Taxonomy ’ Sections |  |
| Genres | `field_genres` | Taxonomy ’ Genres (mehrfach) | - |
| Synopsis | `field_synopsis` | Text Long (übersetzbar) |  |
| Poster | `field_poster` | Media Image |  |
| Trailer | `field_trailer` | Media Remote Video | - |
| Screenings | `field_screenings` | Paragraph (mehrfach) | - |
| Cast | `field_cast` | Entity Ref ’ Person (mehrfach) | - |
| Produzenten | `field_producers` | Entity Ref ’ Person (mehrfach) | - |
| Kameramann | `field_cinematographer` | Entity Ref ’ Person (mehrfach) | - |
| Awards | `field_awards` | Paragraph (mehrfach) | - |

**View Modes:** full, teaser, card, search_result
**Instanzen:** ~200-300 pro Festival
**Komplexität:** Hoch (umfangreiche Entity References)

---

## Film Archive (film_archive)

**Zweck:** Historische Filmeinträge aus 75+ Festivaljahren (10.000+ Datensätze)

### Felder (11)

| Feld | Machine Name | Typ | Pflicht |
|------|--------------|-----|---------|
| Titel (Original) | `field_original_title` | String |  |
| Regisseur(e) | `field_directors` | Entity Ref ’ Person (mehrfach) |  |
| Land | `field_country` | Taxonomy ’ Countries (mehrfach) |  |
| Festivaljahr | `field_festival_year` | Taxonomy ’ Festival Years |  |
| Jahr | `field_year` | Integer |  |
| Dauer | `field_duration` | Integer | - |
| Sektion | `field_film_section` | Taxonomy ’ Sections | - |
| Synopsis | `field_synopsis` | Text Long (übersetzbar) | - |
| Poster | `field_poster` | Media Image | - |
| Awards | `field_awards` | Paragraph (mehrfach) | - |
| Credits | `field_credits` | Text Long | - |

**Performance:** Requires **Search API + Solr**

**Facets:** Land, Jahr, Festivaljahr, Sektion, Regisseur
**Pagination:** 20 Ergebnisse/Seite
**Komplexität:** Hoch (Skalierung kritisch)

---

## Person (person)

**Zweck:** Regisseure, Schauspieler, Produzenten, Jurymitglieder, Staff

### Felder (8)

| Feld | Machine Name | Typ | Pflicht |
|------|--------------|-----|---------|
| Vorname | `field_first_name` | String |  |
| Nachname | `field_last_name` | String |  |
| Rolle(n) | `field_roles` | Taxonomy ’ Person Roles (mehrfach) |  |
| Biografie | `field_biography` | Text Long (übersetzbar) | - |
| Foto | `field_photo` | Media Image | - |
| Land | `field_country` | Taxonomy ’ Countries | - |
| Website | `field_website` | Link | - |
| Social Media | `field_social_media` | Paragraph (mehrfach) | - |

**View Modes:** full, teaser, card, inline
**Instanzen:** ~500-1000
**Referenzen:** Umfangreich von Film-Nodes referenziert

---

## Landing Page (landing_page)

**Zweck:** Flexible Marketing-Pages mit Layout Builder

### Felder (3)

| Feld | Machine Name | Typ | Pflicht |
|------|--------------|-----|---------|
| Titel | `title` | String |  |
| Content Sections | `field_content_sections` | Paragraph (mehrfach) | - |
| Meta Tags | `field_meta_tags` | Metatag | - |

**Layout:** Layout Builder für individuelle Layouts
**Instanzen:** ~20-30 Festival-Pages
**Komplexität:** Hoch (maximale Flexibilität)

---

## News (news)

**Zweck:** Festival-Nachrichten und Updates

### Felder (7)

| Feld | Machine Name | Typ | Pflicht |
|------|--------------|-----|---------|
| Headline | `title` | String |  |
| Datum | `field_publish_date` | Date |  |
| Kategorie | `field_category` | Taxonomy | - |
| Teaser | `field_teaser` | Text |  |
| Body | `body` | Text Long (übersetzbar) |  |
| Hero Image | `field_hero_image` | Media Image | - |
| Gallery | `field_gallery` | Media Image (mehrfach) | - |

**View Modes:** full, teaser, card
**Instanzen:** ~100-200 pro Jahr

---

## Event (event)

**Zweck:** Festival-Events (Empfänge, Parties, Workshops)

### Felder (7)

| Feld | Machine Name | Typ | Pflicht |
|------|--------------|-----|---------|
| Event-Titel | `title` | String |  |
| Datum | `field_event_date` | Date Range |  |
| Ort | `field_location` | Entity Ref ’ Venue | - |
| Beschreibung | `body` | Text Long (übersetzbar) |  |
| Ticket-Link | `field_ticket_link` | Link | - |
| Zielgruppe | `field_target_audience` | Taxonomy | - |
| Bild | `field_image` | Media Image | - |

**View Modes:** full, teaser, card, calendar
**Instanzen:** ~30-50 pro Festival

---

## Venue (venue)

**Zweck:** Veranstaltungsorte (Kinos, Plätze)

### Felder (8)

| Feld | Machine Name | Typ | Pflicht |
|------|--------------|-----|---------|
| Name | `title` | String |  |
| Adresse | `field_address` | Address |  |
| Kapazität | `field_capacity` | Integer | - |
| Beschreibung | `field_description` | Text Long | - |
| Foto | `field_photo` | Media Image | - |
| Karte | `field_map` | Geofield | - |
| Typ | `field_venue_type` | Taxonomy | - |
| Ausstattung | `field_facilities` | Text | - |

**View Modes:** full, teaser, card, map_popup
**Instanzen:** ~10-15 Locations

---

## Weitere Content Types (Übersicht)

### Press Release (press_release)
**Felder:** Titel, Datum, Body, Attachments, Category
**Instanzen:** ~50-80 pro Jahr
**Aufwand:** 15h

### Film VOD (film_vod)
**Felder:** 10 Felder inkl. Video Stream, Availability Period, Access Type
**Instanzen:** ~50-100
**Aufwand:** 35h

### Sponsor (sponsor)
**Felder:** Name, Logo, Description, Website, Level, Year
**Instanzen:** ~30-50
**Aufwand:** 10h

### Partner (partner)
**Felder:** Name, Logo, Description, Website, Type
**Instanzen:** ~20-40
**Aufwand:** 10h

### Award (award)
**Felder:** Name, Year, Category, Description, Winner
**Instanzen:** ~15-25
**Aufwand:** 8h

### Jury Member (jury_member)
**Felder:** Person Ref, Jury Type, Year, Position, Bio
**Instanzen:** ~20-30 pro Jahr
**Aufwand:** 12h

### FAQ (faq)
**Felder:** Question, Answer, Category
**Instanzen:** ~40-60
**Aufwand:** 6h

### Testimony (testimony)
**Felder:** Quote, Author, Role, Photo
**Instanzen:** ~10-20
**Aufwand:** 7h

### Page (page)
**Felder:** Title, Body, Sections, Meta Tags
**Instanzen:** ~800-1200 Standard-Seiten
**Aufwand:** 15h

---

## BörsenXperts Baseline Advantage

**Vordefinierte Content Types:**
- Page (Standardseite)
- Article (News-Basis)
- Landing Page (Layout Builder-Grundlage)

**Eingesparte Zeit:** ~40 Stunden

---

## Migrations-Reihenfolge

1. **Taxonomien** (Countries, Sections, Genres, Festival Years)
2. **Person-Nodes** (vor Film-Nodes wegen Entity References)
3. **Venue-Nodes** (vor Events/Screenings)
4. **Film-Nodes** (nach Personen und Taxonomien)
5. **News, Press, Events** (parallelisierbar)
6. **Landing Pages** (manuell nach Migration)

---

## Performance-Überlegungen

### Caching
- Tag-based cache für Views
- Cache per URL + Taxonomy Term
- BigPipe für below-the-fold Content

### Database Indexes
- `field_year`, `field_country` für Filterung
- Entity Reference preloading
- Views mit Read Replica

### Search API
- **Film Archive:** Solr für 10.000+ Einträge
- Faceted Search (Land, Jahr, Sektion, Regisseur)
- Autocomplete für Regisseur-Suche

---

## Nächste Schritte

- [Paragraph Components](/architektur/paragraphs) ’ 35 wiederverwendbare Komponenten
- [Views](/architektur/views) ’ 12 Content-Listings
- [Migration-Strategie](/migration/strategie) ’ Content-Mapping Magnolia ’ Drupal
