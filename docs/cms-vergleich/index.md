# CMS-Vergleich: Übersicht

Vergleich von drei Enterprise-CMS-Lösungen für den Relaunch der Locarno Film Festival Website.

::: tip KALKULATION
Die vollständige Kostenkalkulation inkl. TCO-Vergleich befindet sich im **adesso Calculator**:

📊 **[Locarno-Festival-Kalkulation.xlsm](https://o365adessogroup.sharepoint.com/:x:/r/sites/Drupal/Shared%20Documents/General/Akquisen/Locarno%20Filmfestival/Locarno-Festival-Kalkulation.xlsm?d=wdda7cd93b37f46fb8233d671e1f1110e&csf=1&web=1&e=K6r1UQ)**
:::

## Zusammenfassung

| CMS | Gesamtbewertung | Lizenzkosten (5J) | Empfehlung |
|-----|----------------|-------------------|------------|
| **Drupal 11** | ⭐⭐⭐⭐⭐ (9.4/10) | **CHF 0** | **EMPFOHLEN** |
| **Umbraco** | ⭐⭐⭐⭐ (7.5/10) | CHF 70.000 | Teurer, kleinere Community |
| **Magnolia** | ⭐⭐⭐ (6.2/10) | CHF 345.000 | Nicht empfohlen |

## Detaillierter Vergleich

### Lizenzkosten (5 Jahre)

```
Drupal:    CHF 0           ✅ 100% Open Source, keine versteckten Kosten
Umbraco:   CHF 70.000      ⚠️ Heartcore für Headless/API (CHF 14k/Jahr)
Magnolia:  CHF 345.000     ❌ Enterprise-Lizenz (CHF 69k/Jahr)
```

**Wichtig:** Umbraco Open Source ist gratis, aber für Enterprise-Features (Headless API, Forms, Deploy) fallen Lizenzkosten an. Für Locarno mit Mobile-App-Integration ist Heartcore erforderlich.

### Entwicklungskosten (Jahr 1)

| Aufwand-Kategorie | Drupal 11 | Umbraco | Magnolia |
|-------------------|-----------|---------|----------|
| Setup & Architektur | 120h | 160h | 80h |
| Content Types | 180h | 240h | 160h |
| Components | 200h | 280h | 180h |
| Theme/Design | 240h | 320h | 200h |
| Migration | 320h | 380h | 300h |
| Testing | 200h | 240h | 180h |
| **Mit adessoCMS Baseline** | **1.680h** | - | - |
| **Ohne Baseline** | 2.160h | **2.620h** | **2.100h** |
| **Baseline-Vorteil** | **480h gespart** | Keine Baseline | Nur Template |

**Stundensätze (CH-Markt):**
- PHP/Drupal: CHF 140-160/h → Durchschnitt **CHF 150/h**
- .NET/Umbraco: CHF 170-200/h → Durchschnitt **CHF 185/h**
- Java/Magnolia: CHF 180-220/h → Durchschnitt **CHF 200/h**

**Entwicklungskosten:**
| CMS | Stunden | Rate | Total |
|-----|---------|------|-------|
| **Drupal** | 1.680h | CHF 150 | **CHF 252.000** |
| **Umbraco** | 2.620h | CHF 185 | **CHF 484.700** |
| **Magnolia** | 2.100h | CHF 200 | **CHF 420.000** |

**Drupal-Vorteil:** CHF 232.700 günstiger als Umbraco (48% Ersparnis)

### Hosting-Kosten (Azure, pro Jahr)

| Position | Drupal | Umbraco | Magnolia |
|----------|--------|---------|----------|
| App Service | CHF 14.400 | CHF 24.000 | CHF 28.200 |
| Database | CHF 9.600 | CHF 16.800 | CHF 18.000 |
| Redis Cache | CHF 3.600 | CHF 4.800 | CHF 4.800 |
| Blob Storage | CHF 600 | CHF 600 | CHF 1.200 |
| CDN | CHF 1.800 | CHF 1.800 | CHF 2.400 |
| **Jahr Total** | **CHF 30.000** | **CHF 48.000** | **CHF 54.600** |

**Warum ist .NET/Umbraco teurer?**
- .NET-Runtime benötigt mehr RAM als PHP (min. 4GB vs 2GB)
- SQL Server teurer als MySQL/PostgreSQL
- Windows-Container teurer als Linux
- Höhere App Service Tier (B2 vs B1) erforderlich

**Warum ist Java/Magnolia am teuersten?**
- Java-Runtime benötigt min. 8GB RAM
- JCR-Datenbank ressourcenhungrig
- Premium App Service Tier erforderlich

## Technische Eignung

### Multilingual (4 Sprachen)

| CMS | Bewertung | Details |
|-----|-----------|---------|
| **Drupal** | ⭐⭐⭐⭐⭐ | Best-in-class, Content Translation Module (core) |
| **Umbraco** | ⭐⭐⭐⭐ | Gut, aber mehr Konfiguration nötig |
| **Magnolia** | ⭐⭐⭐ | Basis-Support, komplexere Workflows |

### High-Scale Performance (8.000 req/min)

| CMS | Capacity | Bewertung |
|-----|----------|-----------|
| **Drupal** | 52.000+ concurrent users | ⭐⭐⭐⭐⭐ |
| **Umbraco** | 40.000+ concurrent users | ⭐⭐⭐⭐ |
| **Magnolia** | 30.000 concurrent users | ⭐⭐⭐ |

**Drupal Performance-Vorteile:**
- Ausgereiftes Caching (Varnish, Redis)
- BigPipe für below-the-fold content
- Progressive Web App Capabilities

### Film-Archiv (10.000+ Einträge)

| CMS | Lösung | Bewertung |
|-----|--------|-----------|
| **Drupal** | Search API + Solr | ⭐⭐⭐⭐⭐ |
| **Umbraco** | Examine (Lucene) | ⭐⭐⭐⭐ |
| **Magnolia** | JCR Query | ⭐⭐⭐ |

### Content-Modellierung (23 Content Types, 35 Components)

| CMS | Approach | Bewertung |
|-----|----------|-----------|
| **Drupal** | Content Types + Paragraphs | ⭐⭐⭐⭐⭐ |
| **Umbraco** | Document Types + Nested Content | ⭐⭐⭐⭐ |
| **Magnolia** | Templates + Dialog Definitions | ⭐⭐⭐ |

**Drupal-Vorteil:**
- Paragraphs = wiederverwendbare Components
- Field API = unbegrenzte Flexibilität
- Layout Builder für Landing Pages

## Entwickler-Verfügbarkeit

### Marktgröße (weltweit)

```
Drupal:    500.000+ Entwickler   ✅
Umbraco:   100.000+ Entwickler   ✅
Magnolia:  10.000 Entwickler     ⚠️
```

### Durchschnittliche Stundensätze (CH)

| CMS | Junior | Mid | Senior | Durchschnitt |
|-----|--------|-----|--------|--------------|
| Drupal | CHF 120 | CHF 150 | CHF 180 | **CHF 150** |
| Umbraco | CHF 140 | CHF 170 | CHF 200 | **CHF 170** |
| Magnolia | CHF 160 | CHF 200 | CHF 240 | **CHF 200** |

### Verfügbarkeit in der Schweiz

| CMS | Rating | Kommentar |
|-----|--------|-----------|
| Drupal | ⭐⭐⭐⭐⭐ | Große Community, viele Freelancer |
| Umbraco | ⭐⭐⭐ | Kleiner, aber wachsend |
| Magnolia | ⭐⭐ | Sehr limitiert, meist via Magnolia selbst |

## Upgrade-Pfad & Langlebigkeit

### Update-Frequenz

| CMS | Major Releases | LTS-Support | Bewertung |
|-----|----------------|-------------|-----------|
| Drupal | 2 Jahre | 2+ Jahre | ⭐⭐⭐⭐ |
| Umbraco | 1-2 Jahre | 2 Jahre | ⭐⭐⭐⭐ |
| Magnolia | 3-4 Jahre | 5 Jahre | ⭐⭐⭐ |

### Backwards Compatibility

| CMS | Rating | Details |
|-----|--------|---------|
| Drupal | ⭐⭐⭐⭐ | Gute Migration-Pfade (8→9→10→11) |
| Umbraco | ⭐⭐⭐⭐⭐ | Sehr stabil, sanfte Upgrades |
| Magnolia | ⭐⭐⭐ | Breaking Changes zwischen Major Versions |

## Risiko-Bewertung

### Drupal 11

| Risiko | Level | Mitigation |
|--------|-------|------------|
| Komplexität | Medium | adessoCMS Baseline vereinfacht Setup |
| Upgrades | Low | Bewährte Migration-Pfade |
| Entwickler-Lock-in | Low | Große Developer-Community |
| Performance | Low | Bewährt für High-Traffic |

**Gesamt-Risiko:** ✅ **Niedrig**

### Umbraco

| Risiko | Level | Mitigation |
|--------|-------|------------|
| .NET Dependency | Medium | Stabiles Ökosystem |
| Kleinere Community | Medium | Wachsende Community |
| Azure-Lock-in | Medium | Funktioniert auch auf anderen Clouds |
| Performance | Low | Gut optimierbar |

**Gesamt-Risiko:** ⚠️ **Mittel**

### Magnolia

| Risiko | Level | Mitigation |
|--------|-------|------------|
| Lizenzkosten | High | Keine - fixe Kosten |
| Entwickler-Verfügbarkeit | High | Schwer zu mitigieren |
| Vendor Lock-in | High | Migration zu anderem CMS schwierig |
| Performance | Medium | Requires mehr Infrastruktur |

**Gesamt-Risiko:** ❌ **Hoch**

## Fazit & Empfehlung

### 🏆 Drupal 11 ist die beste Wahl, weil:

1. **Beste Kosten-Nutzen-Relation**
   - Keine Lizenzkosten
   - CHF 72.000 Ersparnis durch Baseline
   - Günstigere Entwickler-Stundensätze

2. **Technisch optimal geeignet**
   - Best-in-class Multilingual
   - Bewährt für High-Scale (8k req/min)
   - Perfekt für Film-Archiv (Search API)

3. **Geringste Risiken**
   - Große Developer-Community
   - Kein Vendor Lock-in
   - Langfristig wartbar

4. **adessoCMS Baseline**
   - 480 Stunden Entwicklungszeit gespart
   - Bewährte Architektur
   - Best Practices out-of-the-box

### Umbraco: Deutlich teurer

- ✅ Stabiles System
- ✅ Gute Performance
- ❌ **50% höhere Gesamtkosten** (5-Jahres TCO)
- ❌ **92% höhere Entwicklungskosten** (CHF 484k vs CHF 252k)
- ❌ **60% höhere Hosting-Kosten** (.NET vs PHP)
- ❌ Kleinere Developer-Community in DACH
- ❌ Heartcore-Lizenz für API (CHF 70k über 5 Jahre)

### Magnolia: Nicht empfohlen

- ❌ **76% höhere Gesamtkosten** (5-Jahres TCO)
- ❌ CHF 345k Lizenzkosten (5 Jahre)
- ❌ Sehr limitierte Developer-Verfügbarkeit
- ❌ Hoher Vendor Lock-in

---

[→ Detaillierte Drupal-Analyse](/cms-vergleich/drupal)
[→ Umbraco-Details](/cms-vergleich/umbraco)
[→ Magnolia-Analyse](/cms-vergleich/magnolia)
[→ Kostenschätzung](/kosten/schaetzung)
