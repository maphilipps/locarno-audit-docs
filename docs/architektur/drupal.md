# Drupal 11 Architektur

Übersicht der vorgeschlagenen Drupal-Architektur für Locarno Film Festival.

## Technologie-Stack

### Core
- **Drupal:** 11.x (Latest)
- **PHP:** 8.3
- **Database:** MySQL 8.0
- **Cache:** Redis 7.x + Varnish
- **Search:** Search API + Apache Solr 9.x

### Frontend
- **Theme:** Mercury (BörsenXperts)
- **CSS:** Tailwind CSS 3.x
- **Components:** Single Directory Components (SDC) + Paragraphs
- **JavaScript:** Vanilla JS + Alpine.js für Interaktivität

### Development
- **Environment:** DDEV (Docker-basiert)
- **Version Control:** Git
- **CI/CD:** Azure DevOps Pipelines
- **Testing:** PHPUnit, Playwright, Axe-core

## BörsenXperts Baseline

**693 Stunden bewährte Architektur:**

- ✅ Mercury Theme (Tailwind CSS)
- ✅ Content Type Blueprints
- ✅ Paragraph Type Library (20 häufige Types)
- ✅ Storybook-Integration
- ✅ DDEV-Environment
- ✅ Testing-Framework
- ✅ CI/CD Pipeline Templates
- ✅ WCAG 2.1 AA Foundation

**Ersparnis:** 480 Stunden = CHF 72.000

[→ Content Types Details](/architektur/content-types)
[→ Paragraphs Details](/architektur/paragraphs)
[→ Views & Listings](/architektur/views)
