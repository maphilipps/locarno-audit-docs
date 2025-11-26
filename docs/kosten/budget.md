# Budget-Analyse

## Projekt-Budget

::: tip KALKULATION
Die vollständige Kostenkalkulation befindet sich im **adesso Calculator**:

📊 **[Locarno-Festival-Kalkulation.xlsm](https://o365adessogroup.sharepoint.com/:x:/r/sites/Drupal/Shared%20Documents/General/Akquisen/Locarno%20Filmfestival/Locarno-Festival-Kalkulation.xlsm?d=wdda7cd93b37f46fb8233d671e1f1110e&csf=1&web=1&e=K6r1UQ)**

**Inhalt:**
- 42 Features mit Aufwandsschätzung
- Rollen-Verteilung und Tagessätze
- 8 Risiken mit gewichtetem Puffer
- Project Tasks (PM, Testing, Migration)
:::

---

## Betriebskosten (Jahr 1)

### Infrastructure: CHF 35.400/Jahr

| Service | Monatlich | Jährlich |
|---------|----------:|---------:|
| Azure App Service | CHF 564 | CHF 6.768 |
| MySQL Database | CHF 1.364 | CHF 16.368 |
| Redis Cache | CHF 390 | CHF 4.680 |
| Front Door CDN | CHF 467 | CHF 5.604 |
| Storage + Search | CHF 118 | CHF 1.416 |
| Monitoring | CHF 78 | CHF 936 |
| **Total** | **CHF 2.950** | **CHF 35.400** |

### Support & Maintenance: CHF 36.000/Jahr

- 20 Stunden/Monat @ CHF 150/h
- Security Updates, Module Updates, Bug Fixes

### Monitoring Tools: CHF 3.000/Jahr

- New Relic APM, Blackfire.io, StatusCake

### Training: CHF 8.000 (einmalig)

- Content Editor Training (3 Sessions)
- Administrator Training (2 Sessions)
- Video Tutorials & Documentation

### Contingency: CHF 15.000

- 15% Reserve für Migration Risks, Scope Changes

---

## Budget-Lösungen

### Option A: Budget erhöhen ⭐ EMPFOHLEN

**Neues Budget:** CHF 330.000

**Vorteile:**
- ✅ Vollständiger Scope (23 Content Types, 35 Components)
- ✅ Alle 10.000+ Filme
- ✅ Proper Contingency
- ✅ Zero Compromises

**Risiko:** Low

---

### Option B: Phased Approach ✅ AKZEPTABEL

#### Phase 1 (MVP): ~CHF 250.000

- 15 Core Content Types
- 25 Essential Components
- 1.700 Seiten Migration
- 5.000 Film Archive

#### Phase 2 (Jahr 2): ~CHF 80.000

- 8 Advanced Content Types
- 10 Advanced Components
- Rest Film Archive
- Advanced Features

**Vorteile:**
- ✅ Fits CHF 250k Budget
- ✅ Delivers Core Value quickly
- ✅ Phase 2 aus Jahr 2 Budget

**Risiko:** Medium (2 Deployment Cycles)

---

## Empfehlung

**Option A + Phased Approach Discussion**

1. **Diskutieren:** Budget-Erhöhung auf CHF 330k
2. **Fallback:** Phased Approach (CHF 250k Phase 1)
3. **Entscheidung:** Stakeholder Meeting

**Business Case:**
- Drupal spart ~CHF 273k vs. Umbraco (5 Jahre)
- Drupal spart ~CHF 481k vs. Magnolia (5 Jahre)
- adessoCMS Baseline spart ~CHF 72k
- Zero License Costs forever

---

[→ Feature-Liste](/kosten/features)
[→ Kostenschätzung](/kosten/schaetzung)
[→ ROI-Analyse](/kosten/roi)
