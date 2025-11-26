# Budget-Analyse

::: info QUELLE
Basiert auf **adesso Calculator 2.01** (Locarno-Festival-Kalkulation.xlsm)
:::

## Projekt-Budget (adesso Calculator)

| Position | Aufwand | Kosten | Preis |
|----------|--------:|-------:|------:|
| **Features** | 137,5 PT | 106.147 € | 110.000 € |
| **Project Tasks** | 96,0 PT | 53.600 € | 76.800 € |
| **Risikopuffer** | 28,4 PT | 14.200 € | 22.720 € |
| **TOTAL** | **261,9 PT** | **173.947 €** | **209.520 €** |

::: tip UMRECHNUNG
**EUR 209.520** ≈ **CHF 219.996** (Kurs 1,05)
:::

::: info HINWEIS
Inkl. **F-450 Keycloak oAuth2** mit 3,33 PT
:::

---

## Aufwand nach Rolle (adesso Calculator)

| Rolle | Seniority | Aufwand (PT) | Kosten (€) |
|-------|-----------|-------------:|----------:|
| Developer | Middle | 108,5 | 97.710 |
| Project Manager | Senior | 43,0 | 21.500 |
| Requirement Engineer | Middle | 39,5 | 19.733 |
| Sonstige Rollen | Mixed | 33,4 | 16.700 |
| Test Engineer | Middle | 17,7 | 8.850 |
| Software Architect | Senior | 10,8 | 5.383 |
| DevOps Engineer | Middle | 5,6 | 2.800 |
| Test Manager | Senior | 3,4 | 1.700 |
| **TOTAL** | | **261,9 PT** | **173.947 €** |

### Kennzahlen

| Parameter | Wert |
|-----------|------|
| Projektlänge | **20 Wochen** |
| Team-Größe (Ø) | **3,1 FTE** |
| Durchschn. Tagessatz | **663 € / 800 € (Preis)** |
| Gross Profit Ratio | **800 €/Tag** |

---

### Infrastructure: CHF 35.400

| Service | Monatlich | Jährlich |
|---------|----------:|---------:|
| Azure App Service | 564 | 6.768 |
| MySQL Database | 1.364 | 16.368 |
| Redis Cache | 390 | 4.680 |
| Front Door CDN | 467 | 5.604 |
| Storage + Search | 118 | 1.416 |
| Monitoring | 78 | 936 |
| **Total** | **2.950** | **35.400** |

*(Optimized with Reserved Instances)*

---

### Support & Maintenance: CHF 36.000

- 20 Stunden/Monat @ CHF 150/h
- Security Updates
- Module Updates
- Bug Fixes
- Content Support

---

### Monitoring Tools: CHF 3.000

- New Relic APM
- Blackfire.io
- StatusCake
- Security Module

---

### Training: CHF 8.000

- Content Editor Training (3 Sessions)
- Administrator Training (2 Sessions)
- Video Tutorials
- Documentation

---

### Contingency: CHF 15.000

- 15% Reserve
- Migration Risks
- Performance Optimization
- Scope Changes

---

## Budget-Lösungen

### Option A: Budget erhöhen ⭐ EMPFOHLEN

**Neues Budget:** CHF 330.000
**Increase:** +CHF 80.000 (+32%)

**Vorteile:**
- ✅ Vollständiger Scope (23 Content Types, 35 Components)
- ✅ Alle 10.000+ Filme
- ✅ Proper Contingency
- ✅ Zero Compromises
- ✅ Timeline: 17 Wochen

**Risiko:** Low

---

### Option B: Phased Approach ✅ AKZEPTABEL

#### Phase 1 (MVP): CHF 239.400 ✅ IM BUDGET

**Scope:**
- 15 Core Content Types (defer 8)
- 25 Essential Components (defer 10)
- 1.700 Seiten Migration
- 5.000 Film Archive (defer 5.000+)
- Essential Features only

**Breakdown:**
- Development: CHF 180.000
- Infrastructure: CHF 35.400
- Support: CHF 24.000
- **Total:** **CHF 239.400** ✅

#### Phase 2: CHF 80.000 (Jahr 2)

**Scope:**
- 8 Advanced Content Types
- 10 Advanced Components
- 5.000+ Film Archive (rest)
- Advanced Features

**Timeline:**
- Phase 1: 6 Monate
- Phase 2: 2 Monate
- **Total:** 8 Monate

**Vorteile:**
- ✅ Fits CHF 250k Budget (Phase 1)
- ✅ Delivers Core Value quickly
- ✅ Phase 2 aus Jahr 2 Budget

**Risiko:** Medium (2 Deployment Cycles)

---

### Option C: Reduce Team Size ❌ NICHT EMPFOHLEN

**Savings:** CHF 45.000
**Year 1 Total:** CHF 283.800

**STILL OVER BUDGET**

**Cons:**
- ❌ Timeline +6-8 Wochen
- ❌ Höheres Risiko
- ❌ Immer noch über Budget

**Empfehlung:** NICHT EMPFOHLEN

---

### Option D: Reduce Azure Tier ❌ NICHT EMPFOHLEN

**Savings:** CHF 18.000
**Year 1 Total:** CHF 310.800

**STILL OVER BUDGET**

**Cons:**
- ❌ Kann 8.000 rpm NICHT handeln
- ❌ Performance-Risiko
- ❌ Immer noch über Budget

**Empfehlung:** NICHT EMPFOHLEN - Performance-Requirements kritisch

---

## Empfehlung

### Präferierte Strategie

**Option A + Phased Approach Discussion**

1. **Diskutieren:** Budget-Erhöhung auf CHF 330k
2. **Fallback:** Phased Approach (CHF 250k Phase 1)
3. **Entscheidung:** Stakeholder Meeting

**Business Case:**
- Drupal spart CHF 195k vs. Magnolia (5 Jahre)
- BörsenXperts Baseline spart CHF 72k
- Zero License Costs forever
- Best ROI long-term

---

## Payment Schedule

### Milestone-Based

| Milestone | % | CHF | Timing |
|-----------|--:|----:|--------|
| Kickoff | 20% | 46.280 | Woche 0 |
| Infrastructure Complete | 15% | 34.710 | Woche 4 |
| Theme Complete | 20% | 46.280 | Woche 11 |
| Migration Complete | 25% | 57.850 | Woche 22 |
| Testing Complete | 10% | 23.140 | Woche 27 |
| Go-Live | 10% | 23.140 | Woche 31 |

**Development Total:** CHF 231.400

### Infrastructure (monatlich)

- **Monat 1-12:** CHF 2.950/Monat
- **Jährlich:** CHF 35.400

### Support (nach Go-Live)

- **Ab Monat 8:** CHF 3.000/Monat
- **Rest Jahr 1:** CHF 15.000

---

## Fazit

**Realistische Year 1 Kosten:** CHF 328.800

**Lösungen:**
1. **Option A (Preferred):** Budget auf CHF 330k erhöhen
2. **Option B (Acceptable):** Phased Approach (Phase 1 = CHF 239k)

**Business Case:** Drupal spart langfristig CHF 195k vs. Magnolia (5 Jahre)
