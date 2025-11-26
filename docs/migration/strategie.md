# Migrations-Strategie

## Übersicht

**Quelle:** Magnolia CMS 6.3 (Java/JCR)
**Ziel:** Drupal 11 (PHP/MySQL)
**Umfang:** 1.700-2.200 Seiten + 10.000+ Filme
**Aufwand:** 460 Stunden (10 Wochen)
**Ansatz:** Hybrid (Automatisiert + Manuell)

---

## Export-Methoden

### 1. JCR XML/YAML Export ⭐ PRIMARY
**Feasibility:** High
**Vollständigkeit:** Very High
**Aufwand:** 40h
**Risk:** Low

**Tools:**
- Content App Export
- JCR Tools App Exporter
- exportAction Command

**Scope:**
- Vollständiger JCR-Baum
- Alle Properties & Metadaten
- Hierarchien erhalten

**Implementation:**
1. Export aller Content-Nodes via JCR Tools (XML)
2. Export Assets via Asset Export (separate)
3. Parse XML → Intermediate Format (JSON/CSV)
4. Mappe Magnolia Node-Types → Drupal Content Types
5. Validiere Export-Vollständigkeit

---

### 2. Content Exporter Module ⭐ SECONDARY
**Feasibility:** Medium
**Aufwand:** 50h

**Formats:** CSV, JSON
**Use Case:** Structured Data (Films, News, People)

**Pros:**
- CSV direkt Drupal Migrate-kompatibel
- Selective Field Export
- Gut für Film Archive & News

**Implementation:**
1. Installiere Content Exporter Module
2. Konfiguriere Export-Templates
3. Export Films, News, People → CSV/JSON
4. Mappe CSV Columns → Drupal Fields
5. Import via Drupal Migrate CSV Source

---

## Content-Mapping

### Magnolia → Drupal

| Magnolia Template | Drupal Content Type | Strategie | Aufwand |
|-------------------|---------------------|-----------|--------:|
| Homepage | `homepage` | **Manual** | 12h |
| Film Detail | `film_program` | Automated | 60h |
| Film Archive | `film_archive` | Automated Batch | 100h |
| News | `news` | Automated | 25h |
| Person | `person` | Automated | 30h |
| Press Release | `press_release` | Automated | 15h |
| Event | `event` | Automated | 20h |
| Landing Page | `landing_page` | **Hybrid** | 40h |
| Page | `page` | Automated | 20h |

---

## Film Archive Migration ⚠️ KRITISCH

**Volume:** 10.000+ Einträge
**Batch Size:** 500 items/batch
**Tool:** Drupal Migrate API

### Process
1. Export Magnolia Film Archive → CSV
2. Parse & Transform Data
3. Create Person Nodes (Directors) FIRST
4. Create Film Archive Nodes (Batch 500)
5. Index in Solr
6. Validate Data Quality

**Aufwand:** 100 Stunden
**Requires:** Search API + Solr MANDATORY

---

## Asset Migration

**Volume:** 5.000-8.000 Images/Videos
**Storage:** Azure Blob Storage

### Process
1. Export Assets from Magnolia DAM
2. Convert to WebP (Images) 
3. Upload to Azure Blob Storage
4. Create Drupal Media Entities
5. Update Entity References

**Optimization:**
- Images → WebP (-50% Size)
- Videos → Lazy Loading
- CDN Integration

**Aufwand:** 60 Stunden

---

## URL Redirects

**Tool:** Redirect Module
**Scope:** 1.700-2.200 Redirects

### Mapping
- Magnolia: `/locarno/pages/films/{film}`
- Drupal: `/festival/program/{film-slug}`

**301 Redirects:** Alle alten URLs → Neue URLs

**Aufwand:** 20 Stunden

---

## Migrations-Reihenfolge

### Phase 1: Preparation (2 Wochen)
1. Magnolia Content Inventory
2. Export-Scripts Development
3. Mapping-Tabellen Creation

### Phase 2: Core Content (3 Wochen)
1. Taxonomies (Countries, Sections, etc.)
2. Person Nodes
3. Venue Nodes
4. Film Nodes (Program + Archive)

### Phase 3: Editorial Content (2 Wochen)
1. News Articles
2. Press Releases
3. Events
4. Basic Pages

### Phase 4: Landing Pages (2 Wochen)
1. Manual Recreation of complex pages
2. Layout Builder Configuration
3. Component Mapping

### Phase 5: Validation (1 Woche)
1. Data Quality Checks
2. URL Redirects Testing
3. Media Assets Verification
4. Content Editor UAT

---

## Risk Mitigation

### Risk 1: Data Loss
**Mitigation:**
- Incremental Migration
- Validation Checkpoints
- Rollback Plan

### Risk 2: Performance (10k+ Films)
**Mitigation:**
- Batch Processing (500 items)
- Search API + Solr MANDATORY
- Load Testing

### Risk 3: URL Changes
**Mitigation:**
- 301 Redirects für alle URLs
- Sitemap Update
- Google Search Console Submit

---

## Success Criteria

✅ Zero Data Loss
✅ All URLs redirected (301)
✅ Media Assets optimized (WebP)
✅ Film Archive searchable (Solr)
✅ Content Editor Training completed

**Validation:** 2-week UAT period before Go-Live
