# Solr Enterprise Search

::: danger KRITISCH
**8 PT** | CHF 10.000 | Priorität: **KRITISCH**

Das Film-Archiv mit 10.000+ Einträgen erfordert eine Enterprise-Suche.
:::

## Beschreibung

Das Film-Archiv umfasst über **10.000 Einträge**, die performant durchsuchbar sein müssen. Die Standard-Drupal-Suche ist hierfür nicht ausreichend.

**Apache Solr bietet:**
- Faceted Search (Filter)
- Fuzzy Matching (Tippfehler-Toleranz)
- Multilingual Search (4 Sprachen)
- Hohe Performance (< 100ms Response)

## Technische Anforderungen

| Anforderung | Details |
|-------------|---------|
| Search Engine | Apache Solr 9.x |
| Hosting | Azure Container oder Managed Service |
| Drupal Integration | Search API + Search API Solr |
| Index-Größe | ~10.000 Dokumente |
| Response Time | < 100ms (p95) |

## Facetten (Filter)

| Facette | Feld | Typ |
|---------|------|-----|
| Jahr | `field_year` | Range (1946-2025) |
| Genre | `field_genre` | Multiselect |
| Sektion | `field_section` | Select |
| Land | `field_country` | Multiselect |
| Regisseur | `field_director` | Autocomplete |
| Sprache | `field_language` | Multiselect |
| Auszeichnungen | `field_awards` | Multiselect |
| Dauer | `field_duration` | Range |

## Vorgehensweise

### 1. Solr Infrastructure Setup (2 PT)
- Azure Solr Container oder Self-Hosted
- Core-Konfiguration
- Schema-Definition

### 2. Search API Configuration (2 PT)
- Search API Solr Modul installieren
- Server-Verbindung konfigurieren
- Index-Definition erstellen

### 3. Facet & Filter Setup (2 PT)
- Facetten konfigurieren
- Filter-UI implementieren
- Autocomplete für Regisseur/Titel

### 4. Performance Tuning (1 PT)
- Query-Optimierung
- Caching-Strategie
- Monitoring einrichten

### 5. Testing (1 PT)
- Suchergebnis-Qualität prüfen
- Performance-Tests
- Multilingual Testing

## Zeitschätzung

| Phase | PT |
|-------|-----|
| Solr Infrastructure Setup | 2 |
| Search API Configuration | 2 |
| Facet & Filter Setup | 2 |
| Performance Tuning | 1 |
| Testing mit Archiv-Daten | 1 |
| **Gesamt** | **8** |

## Architektur

```
┌─────────────────────────────────────────┐
│              Drupal CMS                 │
│  ┌─────────────────────────────────┐   │
│  │         Search API              │   │
│  │  ┌───────────────────────────┐  │   │
│  │  │    Search API Solr        │  │   │
│  │  └───────────┬───────────────┘  │   │
│  └──────────────┼──────────────────┘   │
└─────────────────┼───────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│           Apache Solr 9.x               │
│  ┌─────────────────────────────────┐   │
│  │    locarno_films (Core)         │   │
│  │    - 10.000+ Documents          │   │
│  │    - Multilingual Analyzer      │   │
│  │    - Facet Fields               │   │
│  └─────────────────────────────────┘   │
│  ┌─────────────────────────────────┐   │
│  │    locarno_content (Core)       │   │
│  │    - News, Events, Pages        │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

## Solr Schema (Auszug)

```xml
<!-- schema.xml für Film-Archiv -->
<fields>
  <field name="id" type="string" indexed="true" stored="true" required="true"/>
  <field name="title" type="text_general" indexed="true" stored="true"/>
  <field name="title_de" type="text_de" indexed="true" stored="false"/>
  <field name="title_en" type="text_en" indexed="true" stored="false"/>
  <field name="title_fr" type="text_fr" indexed="true" stored="false"/>
  <field name="title_it" type="text_it" indexed="true" stored="false"/>

  <field name="year" type="pint" indexed="true" stored="true"/>
  <field name="genre" type="strings" indexed="true" stored="true"/>
  <field name="country" type="strings" indexed="true" stored="true"/>
  <field name="director" type="text_general" indexed="true" stored="true"/>
  <field name="section" type="string" indexed="true" stored="true"/>

  <!-- Facet Fields -->
  <field name="year_facet" type="pint" indexed="true" stored="false" docValues="true"/>
  <field name="genre_facet" type="strings" indexed="true" stored="false" docValues="true"/>
</fields>

<!-- Multilingual Copyfields -->
<copyField source="title" dest="title_*"/>
```

## Drupal Konfiguration

```yaml
# search_api.server.solr.yml
id: solr
name: 'Solr Server'
backend: search_api_solr
backend_config:
  connector: standard
  connector_config:
    scheme: https
    host: solr.locarnofestival.ch
    port: 8983
    path: /solr
    core: locarno_films
```

## Risiken & Mitigation

| Risiko | Wahrsch. | Auswirkung | Mitigation |
|--------|----------|------------|------------|
| Solr Performance bei 10k+ Docs | Niedrig | Mittel | Index-Optimierung, Sharding bei Bedarf |
| Index-Sync Verzögerung | Niedrig | Niedrig | Near-Realtime Indexing aktivieren |
| Komplexität Multilingual Search | Mittel | Mittel | Separate Indizes pro Sprache |

## Azure Hosting Options

| Option | Kosten/Monat | Vorteile |
|--------|--------------|----------|
| **Container (ACI)** | ~CHF 80 | Flexibel, günstig |
| **AKS (Kubernetes)** | ~CHF 150 | Skalierbar, HA |
| **Elastic Cloud** | ~CHF 200 | Managed, einfach |

**Empfehlung:** Azure Container Instance für Kosteneffizienz.

## Voraussetzungen

- [ ] Azure Container oder Managed Service entscheiden
- [ ] Solr-Version festlegen (9.x empfohlen)
- [ ] Film-Archiv-Daten für Index-Test bereitstellen

---

[← Mobile App REST API](/integrationen/mobile-api)
[→ Zurück zur Übersicht](/integrationen/)
