# Risiken & Mitigation

## Risiko-Übersicht

| ID | Risiko | Wahrsch. | Auswirkung | Score | Reserve (PT) |
|----|--------|----------|------------|-------|--------------|
| R1 | Fiona API-Änderungen | Mittel | Hoch | 🔴 | 5 |
| R2 | Fiona API-Ausfall (Festival) | Niedrig | Kritisch | 🔴 | 3 |
| R3 | Sony VOD DRM-Probleme | Mittel | Hoch | 🔴 | 4 |
| R4 | Keycloak-Version Inkompatibilität | Niedrig | Hoch | 🟡 | 2 |
| R5 | Migration Data Quality | Mittel | Mittel | 🟡 | 5 |
| R6 | Film Archive Performance | Niedrig | Mittel | 🟡 | 3 |
| R7 | Peak Traffic Azure-Limits | Mittel | Hoch | 🔴 | 4 |
| R8 | Mobile App API Breaking Changes | Mittel | Mittel | 🟡 | 3 |
| R9 | Multilingual Komplexität | Mittel | Mittel | 🟡 | 3 |
| R10 | Scope Creep | Hoch | Mittel | 🟡 | 5 |
| R11 | Team-Verfügbarkeit | Niedrig | Hoch | 🟡 | 3 |
| R12 | Go-Live Verzögerung | Niedrig | Kritisch | 🔴 | 2 |
| | **TOTAL RESERVE** | | | | **42 PT** |

---

## Externe Integrationen

### R1: Fiona API-Änderungen 🔴

**Beschreibung:** API-Struktur ändert sich während der Entwicklung

| Aspekt | Wert |
|--------|------|
| Wahrscheinlichkeit | Mittel |
| Auswirkung | Hoch |
| Risiko-Score | 🔴 HOCH |
| Reserve | 5 PT |

**Mitigation:**
- ✅ Versionierte API nutzen (falls verfügbar)
- ✅ Change Detection implementieren
- ✅ Abstraction Layer für API-Calls
- ✅ Regelmäßige API-Checks in CI/CD

---

### R2: Fiona API-Ausfall während Festival 🔴

**Beschreibung:** API nicht erreichbar während Peak-Zeiten

| Aspekt | Wert |
|--------|------|
| Wahrscheinlichkeit | Niedrig |
| Auswirkung | **KRITISCH** |
| Risiko-Score | 🔴 HOCH |
| Reserve | 3 PT |

**Mitigation:**
- ✅ Lokaler Cache (24 Stunden)
- ✅ Graceful Degradation UI
- ✅ Fallback: Statische Daten anzeigen
- ✅ Admin-Benachrichtigung bei Cache > 1h

**Fallback-Logik:**
```
API Request → Cache Check → API Call
                   ↓
              [API Timeout?]
                   ↓
         [JA: Return Cached Data]
         [NEIN: Update Cache + Return]
```

---

### R3: Sony VOD DRM-Probleme 🔴

**Beschreibung:** DRM-Inkompatibilität mit bestimmten Browsern

| Aspekt | Wert |
|--------|------|
| Wahrscheinlichkeit | Mittel |
| Auswirkung | Hoch |
| Risiko-Score | 🔴 HOCH |
| Reserve | 4 PT |

**Mitigation:**
- ✅ Multi-DRM Strategy (Widevine + FairPlay + PlayReady)
- ✅ Frühe Browser-Tests (Chrome, Safari, Firefox, Edge)
- ✅ Mobile Device Testing (iOS, Android)
- ✅ Fallback: Progressive Download für ältere Browser

---

### R4: Keycloak-Version Inkompatibilität 🟡

**Beschreibung:** Drupal OAuth-Module inkompatibel mit Keycloak-Version

| Aspekt | Wert |
|--------|------|
| Wahrscheinlichkeit | Niedrig |
| Auswirkung | Hoch |
| Risiko-Score | 🟡 MITTEL |
| Reserve | 2 PT |

**Mitigation:**
- ✅ Frühe Testphase (Woche 3-4)
- ✅ Version-Lock dokumentieren
- ✅ Fallback: Custom OAuth Implementation

---

## Migration

### R5: Migration Data Quality 🟡

**Beschreibung:** Inkonsistente oder korrupte Daten in Magnolia

| Aspekt | Wert |
|--------|------|
| Wahrscheinlichkeit | Mittel |
| Auswirkung | Mittel |
| Risiko-Score | 🟡 MITTEL |
| Reserve | 5 PT |

**Mitigation:**
- ✅ Data Cleaning Phase vor Import
- ✅ Validierung vor Import
- ✅ Conflict Resolution Strategy
- ✅ Incremental Migration (nicht Big Bang)
- ✅ Rollback Plan prepared

---

### R6: Film Archive Performance 🟡

**Beschreibung:** 10.000+ Einträge verursachen Performance-Probleme

| Aspekt | Wert |
|--------|------|
| Wahrscheinlichkeit | Niedrig |
| Auswirkung | Mittel |
| Risiko-Score | 🟡 MITTEL |
| Reserve | 3 PT |

**Mitigation:**
- ✅ **Solr MANDATORY** (nicht optional)
- ✅ Batch Processing (500 items/batch)
- ✅ Database Indexing (field_year, field_country)
- ✅ Read Replica für Views
- ✅ Early Load Testing (Woche 15)

---

## Performance & Skalierung

### R7: Peak Traffic Azure-Limits 🔴

**Beschreibung:** Azure-Ressourcen reichen während Festival nicht aus

| Aspekt | Wert |
|--------|------|
| Wahrscheinlichkeit | Mittel |
| Auswirkung | Hoch |
| Risiko-Score | 🔴 HOCH |
| Reserve | 4 PT |

**Mitigation:**
- ✅ Pre-Scaling 1 Woche vor Festival
- ✅ Reserved Instances (nicht Spot)
- ✅ Auto-Scaling Policies konfiguriert
- ✅ Load Tests mit 2x Peak-Kapazität
- ✅ CDN für statische Assets

**Scaling-Plan:**
```
Normal:     2 Instances (P2v3)
Festival:   6 Instances (P2v3) + Auto-Scale bis 10
Peak Night: 10 Instances + CDN Full Caching
```

---

## Projekt & Organisation

### R8: Mobile App API Breaking Changes 🟡

**Beschreibung:** API-Änderungen brechen bestehende App

| Aspekt | Wert |
|--------|------|
| Wahrscheinlichkeit | Mittel |
| Auswirkung | Mittel |
| Risiko-Score | 🟡 MITTEL |
| Reserve | 3 PT |

**Mitigation:**
- ✅ API Versionierung (v1, v2)
- ✅ Deprecation Policy (6 Monate)
- ✅ Mock Server für Parallel-Entwicklung
- ✅ Enge Koordination mit App-Team

---

### R9: Multilingual Komplexität 🟡

**Beschreibung:** Übersetzungs-Workflows verzögern Projekt

| Aspekt | Wert |
|--------|------|
| Wahrscheinlichkeit | Mittel |
| Auswirkung | Mittel |
| Risiko-Score | 🟡 MITTEL |
| Reserve | 3 PT |

**Mitigation:**
- ✅ Frühe Content-Freeze-Strategie
- ✅ Translation Memory einsetzen
- ✅ Priorität: EN zuerst, dann IT/FR/DE

---

### R10: Scope Creep 🟡

**Beschreibung:** Zusätzliche Anforderungen während Projekt

| Aspekt | Wert |
|--------|------|
| Wahrscheinlichkeit | **Hoch** |
| Auswirkung | Mittel |
| Risiko-Score | 🟡 MITTEL |
| Reserve | 5 PT |

**Mitigation:**
- ✅ Change Request Process etabliert
- ✅ Backlog Management strikt
- ✅ MoSCoW-Priorisierung
- ✅ Bi-weekly Scope Reviews

---

### R11: Team-Verfügbarkeit 🟡

**Beschreibung:** Key Resources nicht verfügbar (Krankheit, Kündigung)

| Aspekt | Wert |
|--------|------|
| Wahrscheinlichkeit | Niedrig |
| Auswirkung | Hoch |
| Risiko-Score | 🟡 MITTEL |
| Reserve | 3 PT |

**Mitigation:**
- ✅ Backup-Ressourcen identifiziert
- ✅ Knowledge Sharing (Pair Programming)
- ✅ Dokumentation aktuell halten
- ✅ Keine Single Points of Failure

---

### R12: Go-Live Verzögerung 🔴

**Beschreibung:** Festival-Deadline (August 2026) wird verpasst

| Aspekt | Wert |
|--------|------|
| Wahrscheinlichkeit | Niedrig |
| Auswirkung | **KRITISCH** |
| Risiko-Score | 🔴 HOCH |
| Reserve | 2 PT |

**Mitigation:**
- ✅ Puffer in Timeline (2 Wochen)
- ✅ Feature-Priorisierung (MoSCoW)
- ✅ Phased Launch möglich (Core First)
- ✅ Weekly Progress Tracking

**Fallback:**
```
IF Go-Live gefährdet:
├── Phase 1: Core Website ohne VOD (01.08.)
├── Phase 2: VOD-Integration (15.08.)
└── Phase 3: Advanced Features (01.09.)
```

---

## Risiko-Matrix

```
              │ Niedrig    │ Mittel     │ Hoch       │ Kritisch
──────────────┼────────────┼────────────┼────────────┼────────────
Hoch          │            │ R10        │            │
──────────────┼────────────┼────────────┼────────────┼────────────
Mittel        │            │ R5,R8,R9   │ R1,R3,R7   │
──────────────┼────────────┼────────────┼────────────┼────────────
Niedrig       │            │ R6,R11     │ R4         │ R2,R12
──────────────┼────────────┼────────────┼────────────┼────────────
              Auswirkung →
```

---

## Risiko-Reserve Zusammenfassung

| Kategorie | Anzahl | Reserve (PT) | Budget |
|-----------|--------|--------------|--------|
| Externe Integrationen (R1-R4) | 4 | 14 | CHF 17.500 |
| Migration (R5-R6) | 2 | 8 | CHF 10.000 |
| Performance (R7) | 1 | 4 | CHF 5.000 |
| Projekt/Organisation (R8-R12) | 5 | 16 | CHF 20.000 |
| **TOTAL RESERVE** | **12** | **42 PT** | **CHF 52.500** |

---

## Risk Response Plan

### IF Fiona API ausfällt (R2)
→ Aktiviere 24h Cache-Fallback
→ Zeige "Daten von [Datum]" Hinweis
→ Eskalation an Fiona-Vendor

### IF Film Archive Migration scheitert (R5+R6)
→ Reduziere auf 5.000 Filme (Phase 1)
→ Rest in Phase 2 nach Go-Live
→ Timeline Impact: 0 (parallel möglich)

### IF Go-Live gefährdet (R12)
→ Priorisiere Core Features
→ Verschiebe VOD auf Post-Launch
→ Informiere Stakeholder frühzeitig

---

## Erfolgswahrscheinlichkeit

| Szenario | Wahrscheinlichkeit |
|----------|-------------------|
| **Vollständiger Erfolg** (alle Features, on time, on budget) | 75% |
| **Erfolg mit Anpassungen** (Core Features, ±2 Wochen, ±10% Budget) | 95% |
| **Kritischer Fehler** (Go-Live scheitert) | < 5% |

**Confidence Level:** Hoch (8/10)

---

[← Timeline & Meilensteine](/migration/timeline)
[→ Migrations-Strategie](/migration/strategie)
