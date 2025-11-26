# Timeline & Meilensteine

## Projektübersicht

| Kennzahl | Wert |
|----------|------|
| **Projektstart** | 06.01.2026 |
| **Go-Live** | 11.08.2026 |
| **Gesamtdauer** | 8 Monate |
| **Gesamtaufwand** | 280 PT |

---

## Projektphasen

```
2026
Jan     Feb     Mär     Apr     Mai     Jun     Jul     Aug
│       │       │       │       │       │       │       │
├───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│ PHASE 1: Foundation                                    │
│ Setup, Azure, Content Modeling                         │
│ [███████████████]                                      │
│       │       │                                        │
│       │ PHASE 2: Development                           │
│       │ Components, Theme, Integrations                │
│       │ [████████████████████████████]                 │
│       │       │       │       │                        │
│       │       │       │ PHASE 3: Migration             │
│       │       │       │ Content, Media, Testing        │
│       │       │       │ [█████████████████]            │
│       │       │       │       │       │                │
│       │       │       │       │       │ PHASE 4: Launch│
│       │       │       │       │       │ Beta, Go-Live  │
│       │       │       │       │       │ [██████]       │
│       │       │       │       │       │       │    ▲   │
│       │       │       │       │       │       │ GO-LIVE│
└───────┴───────┴───────┴───────┴───────┴───────┴───────┘
```

---

## Phase 1: Foundation (Januar - Februar)

**Dauer:** 6 Wochen | **Aufwand:** 49 PT

### Arbeitspakete

| Arbeitspaket | PT | Wochen | Abhängigkeiten |
|--------------|-----|--------|----------------|
| Setup & Architektur | 15 | 1-2 | - |
| Azure Infrastructure | 13 | 1-3 | - |
| Keycloak oAuth.2 | 8 | 3-4 | Azure |
| Content-Modellierung (Start) | 13 | 4-6 | Setup |

### Meilensteine Phase 1

| ID | Meilenstein | Datum | Deliverables |
|----|-------------|-------|--------------|
| **M1** | Kickoff | 06.01.2026 | Projektplan, Team-Setup, Environments |
| **M2** | Foundation Complete | 14.02.2026 | Azure live, Drupal installiert, CI/CD |

---

## Phase 2: Development (Februar - Mai)

**Dauer:** 12 Wochen | **Aufwand:** 113 PT

### Arbeitspakete

| Arbeitspaket | PT | Wochen | Abhängigkeiten |
|--------------|-----|--------|----------------|
| Content-Modellierung (Ende) | 12 | 7-8 | Phase 1 |
| Paragraphs / Components | 28 | 7-12 | Content Types |
| Theme & Frontend | 30 | 8-14 | Components |
| Mehrsprachigkeit | 15 | 10-12 | Content Types |
| Fiona Festival API | 12 | 9-12 | Keycloak |
| Sony VOD | 8 | 10-12 | Keycloak |

### Meilensteine Phase 2

| ID | Meilenstein | Datum | Deliverables |
|----|-------------|-------|--------------|
| **M3** | Content Model Complete | 14.03.2026 | Alle 23 Content Types, Multilingual |
| **M4** | Components Complete | 11.04.2026 | Alle 35 Paragraphs, Theme fertig |
| **M5** | Integrations Complete | 09.05.2026 | Keycloak, Fiona, Sony, Mobile API |

---

## Phase 3: Migration & Testing (April - Juli)

**Dauer:** 12 Wochen | **Aufwand:** 83 PT

### Arbeitspakete

| Arbeitspaket | PT | Wochen | Abhängigkeiten |
|--------------|-----|--------|----------------|
| Content Migration | 40 | 13-20 | Phase 2 |
| Solr Enterprise Search | 8 | 15-17 | Film Archive |
| Mobile App REST API | 10 | 16-19 | Content Types |
| CloudFront CDN | 2 | 17-18 | Media Migration |
| SEO & Analytics | 5 | 19-20 | Migration |
| Accessibility | 8 | 18-21 | Theme |
| Testing & QA | 25 | 18-24 | Alle |

### Migration-Timeline (Detail)

```
Woche 13-14: Preparation
├── Magnolia Content Inventory
├── Export Method Testing
└── Mapping Tables

Woche 15-17: Core Content
├── Taxonomies & Persons
├── Venues & Film Program
└── Film Archive (10.000+) ⚠️ KRITISCH

Woche 18-19: Editorial Content
├── News Articles
├── Press Releases
└── Events & Basic Pages

Woche 20-21: Assets & Landing Pages
├── Media Asset Migration
├── Complex Landing Pages
└── URL Redirects (2.000+)

Woche 22-24: Validation
├── Data Quality Checks
├── UAT
└── Bug Fixes
```

### Meilensteine Phase 3

| ID | Meilenstein | Datum | Deliverables |
|----|-------------|-------|--------------|
| **M6** | Migration Complete | 20.06.2026 | Alle Inhalte migriert, validiert |
| **M7** | Testing Complete | 18.07.2026 | Alle Tests bestanden, UAT abgeschlossen |

---

## Phase 4: Launch (Juli - August)

**Dauer:** 4 Wochen | **Aufwand:** 18 PT

### Arbeitspakete

| Arbeitspaket | PT | Wochen | Abhängigkeiten |
|--------------|-----|--------|----------------|
| Deployment & Go-Live | 10 | 25-27 | Testing Complete |
| Training & Dokumentation | 8 | 26-28 | Go-Live |

### Launch-Sequenz

```
Woche 25 (27.07.)
├── Staging Deployment vollständig
├── Content Freeze in Magnolia
└── Finale Migration

Woche 26 (03.08.)
├── Beta Launch (10% Traffic)
├── Real-World Testing
└── Performance Monitoring

Woche 27 (10.08.)
├── Production Cutover
├── DNS Switch
└── Full Traffic

Woche 28+ (ab 17.08.)
├── Hypercare Period (24/7)
├── Bug Fixes
└── Post-Launch Optimierung
```

### Meilensteine Phase 4

| ID | Meilenstein | Datum | Deliverables |
|----|-------------|-------|--------------|
| **M8** | Beta Launch | 01.08.2026 | Staging live, 10% Traffic |
| **M9** | **GO-LIVE** | **11.08.2026** | **PRODUCTION LIVE** |
| **M10** | Hypercare Complete | 01.09.2026 | Post-Launch Support abgeschlossen |

---

## Kritischer Pfad

```
Azure Setup (M2)
    ↓
Keycloak Integration
    ↓
Content Types Complete (M3)
    ↓
Components Complete (M4)
    ↓
Fiona API Integration (M5)
    ↓
Content Migration Start
    ↓
Film Archive Migration ← ⚠️ KRITISCH (10k+ Einträge)
    ↓
Solr Indexing
    ↓
Migration Complete (M6)
    ↓
Testing Complete (M7)
    ↓
Beta Launch (M8)
    ↓
GO-LIVE (M9) ← 🎯 ZIEL
```

---

## Alle Meilensteine

| ID | Meilenstein | Datum | Phase | Status |
|----|-------------|-------|-------|--------|
| M1 | Kickoff | 06.01.2026 | 1 | ⏳ |
| M2 | Foundation Complete | 14.02.2026 | 1 | ⏳ |
| M3 | Content Model Complete | 14.03.2026 | 2 | ⏳ |
| M4 | Components Complete | 11.04.2026 | 2 | ⏳ |
| M5 | Integrations Complete | 09.05.2026 | 2 | ⏳ |
| M6 | Migration Complete | 20.06.2026 | 3 | ⏳ |
| M7 | Testing Complete | 18.07.2026 | 3 | ⏳ |
| M8 | Beta Launch | 01.08.2026 | 4 | ⏳ |
| **M9** | **GO-LIVE** | **11.08.2026** | 4 | ⏳ |
| M10 | Hypercare Complete | 01.09.2026 | 4 | ⏳ |

---

## Ressourcen-Allokation pro Phase

| Phase | PT | % Gesamt |
|-------|-----|----------|
| Phase 1: Foundation | 49 | 18% |
| Phase 2: Development | 113 | 40% |
| Phase 3: Migration & Testing | 83 | 30% |
| Phase 4: Launch | 18 | 6% |
| Projektmanagement | 17 | 6% |
| **TOTAL** | **280** | **100%** |

---

## Abhängigkeiten & Voraussetzungen

### Vor Projektstart benötigt

- [ ] Budget-Freigabe
- [ ] Azure Subscription provisioniert
- [ ] Keycloak-Testzugang verfügbar
- [ ] Fiona API-Dokumentation erhalten
- [ ] Sony VOD API-Zugang beantragt
- [ ] Team vollständig allokiert

### Externe Abhängigkeiten

| Abhängigkeit | Verantwortlich | Deadline |
|--------------|----------------|----------|
| Keycloak-Zugang | Locarno IT | M1 |
| Fiona API-Docs | Fiona Vendor | M1+2 Wochen |
| Sony API-Zugang | Sony | M4 |
| Magnolia Export-Zugang | Locarno IT | M3 |
| Content Freeze | Locarno Redaktion | M6+1 Woche |

---

[← Migrations-Strategie](/migration/strategie)
[→ Risiken & Mitigation](/migration/risiken)
