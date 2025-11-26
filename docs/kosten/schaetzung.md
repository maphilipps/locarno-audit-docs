# Kostenschätzung: Drupal Relaunch

## Feature-Schätzung & Bepreisung

::: tip KALKULATION
Die vollständige Feature-Schätzung inkl. Aufwände, Rollen und Risiken befindet sich im **adesso Calculator**:

📊 **[Locarno-Festival-Kalkulation.xlsm](https://o365adessogroup.sharepoint.com/:x:/r/sites/Drupal/Shared%20Documents/General/Akquisen/Locarno%20Filmfestival/Locarno-Festival-Kalkulation.xlsm?d=wdda7cd93b37f46fb8233d671e1f1110e&csf=1&web=1&e=K6r1UQ)**

**Inhalt:**
- 42 Features mit Aufwandsschätzung
- Rollen-Verteilung (Developer, PM, Architect, etc.)
- 8 Risiken mit gewichtetem Puffer
- Project Tasks (PM, Testing, Migration, etc.)
:::

---

## Betriebskosten (Jahr 1)

### Azure Hosting: CHF 35.400/Jahr

| Service | Kosten/Jahr |
|---------|------------:|
| App Service (Linux, P2v3) | CHF 14.400 |
| MySQL Database | CHF 9.600 |
| Redis Cache | CHF 2.880 |
| Blob Storage | CHF 480 |
| CDN | CHF 1.440 |
| Application Insights | CHF 600 |
| Staging Environment | CHF 6.000 |
| **Total** | **CHF 35.400** |

::: info HOSTING-VORTEIL DRUPAL
PHP/Linux-Hosting ist **40-50% günstiger** als .NET (Umbraco) oder Java (Magnolia):
- PHP: Weniger RAM-Bedarf (2GB vs 4-8GB)
- Linux-Container günstiger als Windows
- MySQL günstiger als SQL Server
:::

### Support & Wartung: CHF 36.000/Jahr

- 20 Stunden/Monat @ CHF 150/h
- Security Updates, Bugfixes, Content Support

### Monitoring & Tools: CHF 3.000/Jahr

- New Relic APM, Blackfire, Sentry

### Training: CHF 8.000 (einmalig)

- Admin & Editor Training
- Video Tutorials

---

## 5-Jahres TCO-Vergleich

| CMS | Lizenzen (5J) | Hosting (5J) | Entwicklung | Support (5J) | **Total TCO** |
|-----|---------------|--------------|-------------|--------------|---------------|
| **Drupal** | **CHF 0** | CHF 177.000 | ~CHF 220.000 | CHF 180.000 | **~CHF 577.000** |
| Umbraco | CHF 150.000 | CHF 240.000 | ~CHF 280.000 | CHF 180.000 | **~CHF 850.000** |
| Magnolia | CHF 345.000 | CHF 273.000 | ~CHF 260.000 | CHF 180.000 | **~CHF 1.058.000** |

::: info UMBRACO LIZENZKOSTEN
Umbraco Enterprise (Cloud oder On-Prem mit Support):
- Cloud Enterprise: ~€83.000/Jahr ([Quelle](https://umbraco.com/blog/annual-price-changes-2026))
- On-Prem Enterprise: ~€15.000 Setup + €5.000/Jahr
- Heartcore (Headless API): zusätzlich ~€14.000/Jahr
:::

::: warning DRUPAL-ERSPARNIS
- **vs. Umbraco:** ~CHF 273.000 günstiger (32%)
- **vs. Magnolia:** ~CHF 481.000 günstiger (45%)
:::

**Hauptgründe für Drupal-Kostenvorteil:**
1. ✅ **Keine Lizenzkosten** (CHF 0 vs. CHF 70k-345k)
2. ✅ **Günstigeres Hosting** (PHP/Linux vs. .NET/Java)
3. ✅ **adessoCMS Baseline** (~CHF 72k Ersparnis)
4. ✅ **Günstigere Entwickler** (PHP CHF 120-150/h vs. .NET CHF 160-200/h)

---

## Empfehlung

### Für Budget CHF 330.000: Vollumfang

- Alle 23 Content Types
- Alle 35 Components
- Volles Film-Archiv (10.000+)
- Keine Kompromisse

### Für Budget CHF 250.000: Phasen-Ansatz

- Phase 1: Core Features (CHF 250k)
- Phase 2: Advanced Features (CHF 80k in Jahr 2)

---

[→ Feature-Liste](/kosten/features)
[→ Budget-Analyse](/kosten/budget)
[→ ROI-Analyse](/kosten/roi)
[→ CMS-Vergleich](/cms-vergleich/)
