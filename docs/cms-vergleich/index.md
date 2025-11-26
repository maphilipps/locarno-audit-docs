# CMS-Vergleich: Übersicht

Vergleich von drei Enterprise-CMS-Lösungen für den Relaunch der Locarno Film Festival Website.

## Zusammenfassung

| CMS | Gesamtbewertung | Jahr 1 Kosten | 5-Jahres TCO | Empfehlung |
|-----|----------------|---------------|--------------|------------|
| **Drupal 11** | ⭐⭐⭐⭐⭐ (9.4/10) | CHF 328.800 | CHF 669.638 | **EMPFOHLEN** |
| **Umbraco** | ⭐⭐⭐⭐ (8.8/10) | CHF 303.500 | CHF 667.282 | Gute Alternative |
| **Magnolia** | ⭐⭐⭐ (7.2/10) | CHF 432.570 | CHF 863.995 | Nicht empfohlen |

## Detaillierter Vergleich

### Lizenzkosten (5 Jahre)

```
Drupal:    CHF 0           ✅ Open Source
Umbraco:   CHF 0           ✅ Open Source
Magnolia:  CHF 345.000     ❌ Teuer (CHF 69k/Jahr)
```

### Entwicklungskosten (Jahr 1)

| Aufwand-Kategorie | Drupal 11 | Umbraco | Magnolia |
|-------------------|-----------|---------|----------|
| Setup & Architektur | 120h | 120h | 80h |
| Content Types | 180h | 220h | 160h |
| Components | 200h | 240h | 180h |
| Theme/Design | 240h | 280h | 200h |
| Migration | 320h | 350h | 300h |
| Testing | 200h | 220h | 180h |
| **Mit Baseline** | **1.680h** | **1.950h** | **1.700h** |
| **Ohne Baseline** | 2.160h | 2.450h | 1.900h |
| **Baseline-Vorteil** | **480h** | **500h** | **200h** |

**Entwicklung @ CHF 150/h:**
- Drupal: CHF 231.400 (mit Baseline)
- Umbraco: CHF 292.500
- Magnolia: CHF 255.000

### Hosting-Kosten (Azure)

| Position | Drupal | Umbraco | Magnolia |
|----------|--------|---------|----------|
| App Service | CHF 17.400 | CHF 21.000 | CHF 28.200 |
| Database | CHF 12.000 | CHF 14.400 | CHF 18.000 |
| Redis Cache | CHF 3.600 | CHF 3.600 | CHF 4.800 |
| Blob Storage | CHF 600 | CHF 600 | CHF 1.200 |
| CDN | CHF 1.800 | CHF 1.800 | CHF 2.400 |
| **Jahr 1 Total** | **CHF 35.400** | **CHF 41.400** | **CHF 54.600** |

**Warum teurer für Magnolia?**
- Java-Runtime benötigt mehr CPU/RAM
- JCR-Datenbank ressourcenhungrig
- Höhere App Service Tier erforderlich

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
| Komplexität | Medium | BörsenXperts Baseline vereinfacht Setup |
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

4. **BörsenXperts Baseline**
   - 480 Stunden Entwicklungszeit gespart
   - Bewährte Architektur
   - Best Practices out-of-the-box

### Umbraco: Gute Alternative, aber teurer

- ✅ Stabiles System
- ✅ Gute Performance
- ❌ 13% höhere Entwicklungskosten
- ❌ Kleinere Developer-Community

### Magnolia: Nicht empfohlen

- ❌ 29% höhere Gesamtkosten
- ❌ CHF 345k Lizenzkosten (5 Jahre)
- ❌ Sehr limitierte Developer-Verfügbarkeit
- ❌ Hoher Vendor Lock-in

---

[→ Detaillierte Drupal-Analyse](/cms-vergleich/drupal)
[→ Umbraco-Details](/cms-vergleich/umbraco)
[→ Magnolia-Analyse](/cms-vergleich/magnolia)
[→ Kostenschätzung](/kosten/schaetzung)
