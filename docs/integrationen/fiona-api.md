# Fiona Festival API Integration

::: danger KRITISCH
**12 PT** | CHF 15.000 | Priorität: **KRITISCH**

Die Fiona API ist die zentrale Datenquelle für alle Veranstaltungsdaten während des Festivals.
:::

## Beschreibung

Die Veranstaltungsdaten (Events, Screenings, Locations) werden über die **Fiona REST API** bezogen. Diese externe Datenquelle muss regelmäßig synchronisiert werden, um aktuelle Programminformationen auf der Website anzuzeigen.

**Die API liefert:**
- Screenings (Filmvorführungen)
- Venues (Spielstätten)
- Zeitpläne
- Ticketing-Links

## Technische Anforderungen

| Anforderung | Details |
|-------------|---------|
| API-Typ | REST API (JSON) |
| Authentifizierung | API-Key |
| Sync-Frequenz | Alle 15 Minuten (während Festival) |
| Datenvolumen | ~5.000 Events/Jahr |
| Fallback | Lokaler Cache bei API-Ausfall |

## Daten-Mapping

| Fiona Entität | Drupal Content Type | Felder |
|---------------|---------------------|--------|
| Screening | Event (Node) | Titel, Film-Ref, Venue-Ref, Datum/Zeit |
| Venue | Venue (Node) | Name, Adresse, Kapazität, Geo |
| Film | Film Program (Reference) | Bereits in Drupal |
| Ticket | Link-Feld | URL zum Ticketing-System |

## Vorgehensweise

### 1. API-Analyse (1 PT)
- Dokumentation der Fiona API Endpoints
- Datenstruktur-Mapping erstellen
- Rate Limits prüfen

### 2. Custom Modul Architektur (2 PT)
```
modules/custom/locarno_fiona/
├── locarno_fiona.info.yml
├── locarno_fiona.module
├── locarno_fiona.services.yml
├── src/
│   ├── FionaApiClient.php
│   ├── FionaSyncService.php
│   ├── Plugin/
│   │   └── QueueWorker/
│   │       └── FionaSyncWorker.php
│   └── Form/
│       └── FionaSettingsForm.php
└── config/
    └── install/
        └── locarno_fiona.settings.yml
```

### 3. REST Client Implementation (3 PT)
- Guzzle HTTP Client für API-Kommunikation
- Retry-Logik bei Fehlern
- Response-Caching

### 4. Data Mapping & Transformation (3 PT)
- Fiona Events → Drupal Event Nodes
- Venue-Referenzen auflösen
- Datum/Zeit-Handling (Zeitzonen)

### 5. Queue & Cron Setup (2 PT)
- Queue-basierte Synchronisation
- Cron-Jobs konfigurieren
- Admin-Dashboard für Sync-Status

### 6. Error Handling & Logging (1 PT)
- Fehlerbehandlung bei API-Ausfall
- Admin-Benachrichtigung
- Logging für Debugging

## Zeitschätzung

| Phase | PT |
|-------|-----|
| API Analyse & Dokumentation | 1 |
| Custom Module Architektur | 2 |
| REST Client Implementation | 3 |
| Data Mapping & Transformation | 3 |
| Queue & Cron Setup | 2 |
| Error Handling & Logging | 1 |
| **Gesamt** | **12** |

## Risiken & Mitigation

| Risiko | Wahrsch. | Auswirkung | Mitigation |
|--------|----------|------------|------------|
| **API-Änderungen durch Fiona** | Mittel | Hoch | Versionierte API nutzen, Change-Detection |
| **API-Ausfall während Festival** | Niedrig | **KRITISCH** | Lokaler Cache (24h), Graceful Degradation |
| Daten-Inkonsistenzen | Mittel | Mittel | Validierung vor Import, Conflict Resolution |
| Rate Limiting | Niedrig | Mittel | Request Throttling, Bulk-Endpoints |

## Fallback-Strategie

```
┌─────────────────────────────────────────┐
│           Fiona API Request             │
└─────────────────┬───────────────────────┘
                  │
                  ▼
         ┌───────────────┐
         │  API Online?  │
         └───────┬───────┘
                 │
        ┌────────┴────────┐
        ▼                 ▼
   [JA: Sync]      [NEIN: Cache]
        │                 │
        ▼                 ▼
   Live Daten       Cached Daten
   + Cache Update   (max 24h alt)
        │                 │
        └────────┬────────┘
                 ▼
         Admin-Notification
         (wenn Cache > 1h)
```

## Code-Beispiel

```php
<?php

namespace Drupal\locarno_fiona;

use GuzzleHttp\ClientInterface;
use Drupal\Core\Cache\CacheBackendInterface;

class FionaApiClient {

  public function __construct(
    private ClientInterface $httpClient,
    private CacheBackendInterface $cache,
    private string $apiKey,
  ) {}

  public function getScreenings(): array {
    $cacheId = 'fiona:screenings';

    if ($cached = $this->cache->get($cacheId)) {
      return $cached->data;
    }

    try {
      $response = $this->httpClient->get('/api/v1/screenings', [
        'headers' => ['X-API-Key' => $this->apiKey],
      ]);

      $data = json_decode($response->getBody(), TRUE);
      $this->cache->set($cacheId, $data, time() + 900); // 15 min

      return $data;
    }
    catch (\Exception $e) {
      // Fallback to stale cache
      if ($cached = $this->cache->get($cacheId, TRUE)) {
        return $cached->data;
      }
      throw $e;
    }
  }
}
```

## Voraussetzungen

- [ ] Fiona API-Dokumentation anfordern
- [ ] API-Key erhalten
- [ ] Test-Endpoint verfügbar
- [ ] Datenstruktur dokumentiert

---

[← Keycloak oAuth.2](/integrationen/keycloak)
[→ Sony VOD Streaming](/integrationen/sony-vod)
