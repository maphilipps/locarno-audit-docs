# Indikationsofferte: Locarno Film Festival Relaunch

::: info DOKUMENTTYP
**Indikationsofferte** für Website-Relaunch auf Drupal CMS
:::

## Zusammenfassung

| Position | PT | EUR |
|----------|-----|-----|
| 1. Azure einrichten und aufsetzen | 13 | 14.300 |
| 2. CMS installieren und einrichten | 15 | 16.500 |
| 3. CMS Webpublishing Umsetzung Website | 78 | 85.800 |
| 4. APIs anbinden (Ticketing, Fiona, Sony VOD) | 30 | 33.000 |
| 5. Registration und Anmelden (Keycloak oAuth2) | 8 | 8.800 |
| 6. Datenintegration bisheriger Website | 40 | 44.000 |
| 7. Dokumentation und Bereitstellen GitHub | 5 | 5.500 |
| 8. Projektleitung, Testing, Bugfix, Performance | 43 | 47.300 |
| **TOTAL** | **232 PT** | **EUR 255.200** |

---

## Kalkulation

| Parameter | Wert |
|-----------|------|
| **Blended Rate** | 1.000 EUR/PT |
| **+ 10% Fee** | 100 EUR/PT |
| **Tagessatz (inkl. Fee)** | **1.100 EUR/PT** |
| **Gesamtaufwand** | 232 PT |
| **Gesamtbetrag** | **EUR 255.200** |

::: tip BUDGET-CHECK
Bei Wechselkurs 0,94 (EUR/CHF): **≈ 239.888 CHF** ✓ unter 250.000 CHF
:::

---

## Position 1: Azure einrichten und aufsetzen

**Aufwand:** 13 PT | **Kosten:** EUR 14.300

| Teilleistung | PT |
|--------------|----|
| Azure Subscription Setup (Switzerland North) | 1 |
| App Service Plan (Premium v3, HA) | 2 |
| Azure Database for MySQL (Flexible Server) | 2 |
| Azure Front Door + WAF Configuration | 3 |
| Blob Storage für Medien | 1 |
| Application Insights + Monitoring | 2 |
| CI/CD Pipeline (GitHub Actions → Azure) | 2 |

**Deliverables:**
- ✅ Production & Staging Environment
- ✅ WAF + Anti-DDoS Protection
- ✅ Monitoring & Alerting
- ✅ Infrastructure as Code (Terraform/Bicep)

---

## Position 2: CMS installieren und einrichten

**Aufwand:** 15 PT | **Kosten:** EUR 16.500

| Teilleistung | PT |
|--------------|----|
| DDEV Entwicklungsumgebung | 1 |
| Drupal CMS 2.0 Installation | 2 |
| Core Recipes Aktivierung (SEO, A11y, Forms) | 2 |
| Modul-Stack Konfiguration | 3 |
| Mehrsprachigkeit Setup (EN, IT, FR, DE) | 3 |
| Admin UI Anpassungen | 2 |
| Team Onboarding & Schulung | 2 |

**Deliverables:**
- ✅ Drupal CMS 2.0 mit 22 Recipes
- ✅ 4-sprachige Konfiguration
- ✅ SEO, Accessibility, Cookie Consent

---

## Position 3: CMS Webpublishing Umsetzung Website

**Aufwand:** 78 PT | **Kosten:** EUR 85.800

| Teilleistung | PT |
|--------------|----|
| **Content Types (23 Typen)** | 23 |
| **Paragraph/Components (35 Typen)** | 25 |
| **Theme & Frontend Design** | 30 |

### 3.1 Content Types (23 PT)

| Content Type | PT |
|--------------|----|
| Homepage | 3 |
| Film Program | 4 |
| Film Archive | 4 |
| Film VOD | 2 |
| Person Profile | 2 |
| News Article | 1.5 |
| Press Release | 1 |
| Palmarès | 1 |
| Venue | 1 |
| Event | 1 |
| Landing Page | 2 |
| Weitere (12 Typen) | 0.5 |

### 3.2 Components/Paragraphs (25 PT)

| Kategorie | Anzahl | PT |
|-----------|--------|-----|
| Hero Components | 3 | 4 |
| Content Sections | 8 | 8 |
| Media Components | 5 | 5 |
| Film Components | 4 | 4 |
| Interactive Elements | 4 | 2 |
| CTA & Navigation | 6 | 2 |

### 3.3 Theme & Frontend (30 PT)

| Teilleistung | PT |
|--------------|----|
| Base Theme Setup (Tailwind CSS) | 5 |
| Component Styling | 10 |
| Responsive Implementation | 6 |
| Animations & Interactions | 4 |
| Performance Optimization | 3 |
| Cross-Browser Testing | 2 |

**Deliverables:**
- ✅ 23 Content Types + 35 Components
- ✅ Responsive Design (Mobile First)
- ✅ WCAG 2.1 Level AA
- ✅ Lighthouse Score > 90

---

## Position 4: APIs anbinden

**Aufwand:** 30 PT | **Kosten:** EUR 33.000

| API-Integration | PT |
|-----------------|----|
| **Fiona Festival API** (Events, Screenings) | 12 |
| **Sony Pictures Core** (VOD Streaming) | 8 |
| **Mobile App REST API** | 10 |

### 4.1 Fiona Festival API (12 PT)

| Teilleistung | PT |
|--------------|----|
| API-Analyse & Dokumentation | 1 |
| Custom Drupal Module | 3 |
| REST Client Implementation | 3 |
| Data Mapping & Transformation | 3 |
| Queue & Cron (15-Min-Sync) | 2 |

### 4.2 Sony VOD Streaming (8 PT)

| Teilleistung | PT |
|--------------|----|
| Sony API Integration | 3 |
| Video Player (DRM-fähig) | 2 |
| Access Control & Paywall | 2 |
| Testing (Browser/Devices) | 1 |

### 4.3 Mobile App REST API (10 PT)

| Teilleistung | PT |
|--------------|----|
| JSON:API Konfiguration | 2 |
| Custom Endpoints | 4 |
| Push Notifications (FCM) | 2 |
| API Dokumentation (OpenAPI) | 1 |
| App-Team Koordination | 1 |

**Deliverables:**
- ✅ Fiona-Sync (Events, Venues, Screenings)
- ✅ VOD-Integration (fVOD + sVOD)
- ✅ Mobile API mit Push-Support

---

## Position 5: Registration und Anmelden (Keycloak oAuth2)

**Aufwand:** 8 PT | **Kosten:** EUR 8.800

| Teilleistung | PT |
|--------------|----|
| OAuth/OIDC Module Setup | 2 |
| Keycloak Client Integration | 3 |
| User Provisioning & Rollen-Mapping | 2 |
| Session Management & Testing | 1 |

**Rollen-Mapping:**

| Keycloak Group | Drupal Role |
|----------------|-------------|
| `public` | Authenticated |
| `press` | Press |
| `pro` | Pro/Industry |
| `admin` | Administrator |

**Deliverables:**
- ✅ Single Sign-On (SSO)
- ✅ Automatische User-Erstellung
- ✅ Rollen-Synchronisation

---

## Position 6: Datenintegration bisheriger Website

**Aufwand:** 40 PT | **Kosten:** EUR 44.000

| Teilleistung | PT |
|--------------|----|
| Magnolia Content Export | 6 |
| Data Mapping & Transformation | 8 |
| Drupal Migrate Plugin Development | 10 |
| Film Archive Migration (10.000+) | 5 |
| Media Assets Migration | 4 |
| URL Redirects (2.000+) | 2 |
| Validation & Quality Checks | 5 |

**Migrationsumfang:**

| Content | Menge |
|---------|-------|
| Film Program | ~800 |
| Film Archive | 10.000+ |
| News | ~400 |
| Press Releases | ~200 |
| Events | ~500 |
| Persons | ~1.000 |
| Media Assets | ~8.000 |

**Deliverables:**
- ✅ 99.5%+ Content-Vollständigkeit
- ✅ Alle URLs redirected (301)
- ✅ Media optimiert (WebP)

---

## Position 7: Dokumentation und Bereitstellen GitHub

**Aufwand:** 5 PT | **Kosten:** EUR 5.500

| Teilleistung | PT |
|--------------|----|
| Technische Dokumentation (Architecture) | 1.5 |
| Redakteurs-Handbuch | 1.5 |
| API-Dokumentation | 1 |
| GitHub Repository Setup | 1 |

**Deliverables:**
- ✅ Architecture Decision Records (ADR)
- ✅ Redakteurs-Handbuch (DE)
- ✅ API-Dokumentation (OpenAPI/Swagger)

---

## Position 8: Projektleitung, Testing, Bugfix, Performance

**Aufwand:** 43 PT | **Kosten:** EUR 47.300

| Teilleistung | PT |
|--------------|----|
| **Projektleitung** | 17 |
| **Testing & QA** | 20 |
| **Performance Testing** | 3 |
| **Bugfix Reserve** | 3 |

### 8.1 Projektleitung (17 PT)

| Teilleistung | PT |
|--------------|----|
| Sprint Planning & Tracking | 6 |
| Stakeholder-Kommunikation | 4 |
| Risiko-Management | 3 |
| Reporting | 4 |

### 8.2 Testing & QA (20 PT)

| Test-Typ | PT |
|----------|----|
| Unit Tests (PHPUnit) | 5 |
| Integration Tests | 4 |
| E2E Tests (Playwright) | 5 |
| Accessibility Tests | 3 |
| UAT Koordination | 3 |

### 8.3 Performance Testing (3 PT)

| Teilleistung | PT |
|--------------|----|
| Load Tests (k6) | 2 |
| Optimierung | 1 |

**Deliverables:**
- ✅ Wöchentliche Status-Reports
- ✅ Test Coverage > 80%
- ✅ Performance validiert (5.000 req/min)
- ✅ WCAG 2.1 AA bestätigt

---

## Gesamtübersicht

| # | Position | PT | EUR |
|---|----------|-----|-----|
| 1 | Azure einrichten und aufsetzen | 13 | 14.300 |
| 2 | CMS installieren und einrichten | 15 | 16.500 |
| 3 | CMS Webpublishing Umsetzung Website | 78 | 85.800 |
| 4 | APIs anbinden (Fiona, Sony VOD, Mobile) | 30 | 33.000 |
| 5 | Registration und Anmelden (Keycloak) | 8 | 8.800 |
| 6 | Datenintegration bisheriger Website | 40 | 44.000 |
| 7 | Dokumentation und Bereitstellen GitHub | 5 | 5.500 |
| 8 | Projektleitung, Testing, Bugfix, Performance | 43 | 47.300 |
| | **TOTAL** | **232 PT** | **EUR 255.200** |

---

## Zusätzliche Kosten (nicht im Projektbudget)

| Position | Jahr 1 | Bemerkung |
|----------|--------|-----------|
| Azure Hosting | ~33.000 EUR | Laufende Kosten |
| Support & Wartung | ~34.000 EUR | 20h/Monat |
| Monitoring Tools | ~2.800 EUR | New Relic, Sentry |
| **Total Betrieb** | **~70.000 EUR** | |

---

## Timeline

| Meilenstein | Datum |
|-------------|-------|
| Kickoff | 06.01.2026 |
| Azure + CMS Setup fertig | 14.02.2026 |
| Content Model fertig | 14.03.2026 |
| Components + Theme fertig | 11.04.2026 |
| Integrationen fertig | 09.05.2026 |
| Migration fertig | 20.06.2026 |
| Testing fertig | 18.07.2026 |
| Beta Launch | 01.08.2026 |
| **GO-LIVE** | **11.08.2026** |

---

## Zahlungsplan

| Meilenstein | % | EUR |
|-------------|---|-----|
| Kickoff (M1) | 20% | 51.040 |
| Foundation Complete (M2) | 15% | 38.280 |
| Components Complete (M4) | 25% | 63.800 |
| Migration Complete (M6) | 25% | 63.800 |
| Go-Live (M9) | 15% | 38.280 |
| **TOTAL** | **100%** | **EUR 255.200** |

---

## Konditionen

| Parameter | Wert |
|-----------|------|
| **Tagessatz (Blended Rate)** | 1.000 EUR |
| **+ 10% Fee** | 100 EUR |
| **Tagessatz inkl. Fee** | **1.100 EUR/PT** |
| **Gültigkeit** | bis 31.12.2025 |
| **Zahlungsziel** | 30 Tage netto |

---

**Erstellt von:** adesso SE
**Datum:** November 2025
**Version:** 2.0

---

[→ Timeline & Meilensteine](/migration/timeline)
[→ Risiken & Mitigation](/migration/risiken)
[→ Team & Ressourcen](/projekt/team)
