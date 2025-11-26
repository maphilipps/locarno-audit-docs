# Mobile App REST API

::: info AUFWAND
**10 PT** | CHF 12.500 | Priorität: **HOCH**
:::

## Beschreibung

Die bestehende Mobile App des Locarno Film Festivals benötigt eine REST API für den Zugriff auf:

- **Content** - Filme, Events, News, Venues
- **User-Daten** - Favoriten, Watchlist, Tickets
- **Push-Benachrichtigungen** - Breaking News, Screening-Reminder

Die API muss performant, versioniert und dokumentiert sein.

## Technische Anforderungen

| Anforderung | Details |
|-------------|---------|
| API-Standard | JSON:API (Drupal Core) |
| Authentifizierung | OAuth 2.0 (via Keycloak) |
| Versionierung | URL-basiert (/api/v1/, /api/v2/) |
| Rate Limiting | 1000 req/min pro User |
| Push | Firebase Cloud Messaging (FCM) |

## Endpoints

### Content Endpoints

| Endpoint | Methode | Beschreibung |
|----------|---------|--------------|
| `/api/v1/films` | GET | Alle Filme (paginated) |
| `/api/v1/films/{id}` | GET | Film-Details |
| `/api/v1/events` | GET | Alle Events/Screenings |
| `/api/v1/events/{id}` | GET | Event-Details |
| `/api/v1/news` | GET | Aktuelle News |
| `/api/v1/venues` | GET | Alle Spielstätten |
| `/api/v1/program` | GET | Tagesprogramm |

### User Endpoints

| Endpoint | Methode | Beschreibung |
|----------|---------|--------------|
| `/api/v1/user/me` | GET | Aktueller User |
| `/api/v1/user/favorites` | GET/POST/DELETE | Favoriten verwalten |
| `/api/v1/user/watchlist` | GET/POST/DELETE | Watchlist |
| `/api/v1/user/tickets` | GET | Gekaufte Tickets |
| `/api/v1/user/notifications` | GET/PATCH | Notification Settings |

### Push Endpoints

| Endpoint | Methode | Beschreibung |
|----------|---------|--------------|
| `/api/v1/push/register` | POST | FCM Token registrieren |
| `/api/v1/push/unregister` | DELETE | FCM Token entfernen |

## Vorgehensweise

### 1. JSON:API Konfiguration (2 PT)
- Drupal Core JSON:API aktivieren
- Resource Types konfigurieren
- Feldfilter definieren

### 2. Custom Endpoints Development (4 PT)
- Spezifische App-Endpoints erstellen
- Response-Optimierung (sparse fieldsets)
- Caching-Header setzen

### 3. Push Notification Service (2 PT)
- Firebase Cloud Messaging (FCM) Integration
- Token-Management
- Notification-Typen:

| Typ | Trigger | Beispiel |
|-----|---------|----------|
| Breaking News | Manuell | "Goldener Leopard geht an..." |
| Screening Reminder | 30min vor Event | "Ihr Film beginnt in 30 Minuten" |
| Favorite Update | Content-Änderung | "Neuer Film von Regisseur X" |
| System | Automatisch | "App-Update verfügbar" |

### 4. API Dokumentation (1 PT)
- OpenAPI/Swagger Spezifikation
- Beispiel-Requests/Responses
- Error-Codes dokumentieren

### 5. App-Team Koordination (1 PT)
- Mock Server für Parallel-Entwicklung
- API Review mit App-Entwicklern
- Breaking Changes kommunizieren

## Zeitschätzung

| Phase | PT |
|-------|-----|
| JSON:API Konfiguration | 2 |
| Custom Endpoints Development | 4 |
| Push Notification Service (FCM) | 2 |
| API Dokumentation | 1 |
| App-Team Koordination | 1 |
| **Gesamt** | **10** |

## API Response Format

```json
// GET /api/v1/films/123
{
  "data": {
    "type": "film",
    "id": "123",
    "attributes": {
      "title": "Il Leopardo",
      "year": 2025,
      "duration": 120,
      "synopsis": "Ein Film über...",
      "director": "Mario Rossi",
      "country": "IT",
      "language": "it",
      "poster_url": "https://cdn.locarno.ch/films/123/poster.webp"
    },
    "relationships": {
      "section": {
        "data": { "type": "section", "id": "piazza-grande" }
      },
      "screenings": {
        "data": [
          { "type": "screening", "id": "456" },
          { "type": "screening", "id": "789" }
        ]
      }
    }
  },
  "included": [
    {
      "type": "screening",
      "id": "456",
      "attributes": {
        "datetime": "2025-08-07T21:30:00+02:00",
        "venue": "Piazza Grande"
      }
    }
  ]
}
```

## Risiken & Mitigation

| Risiko | Wahrsch. | Auswirkung | Mitigation |
|--------|----------|------------|------------|
| **API Breaking Changes** | Mittel | Hoch | Versionierung (v1, v2), Deprecation Policy |
| Performance bei Peak | Mittel | Hoch | Response Caching, Rate Limiting |
| Koordination mit App-Team | Mittel | Mittel | Frühe API-Specs, Mock Server |

## Drupal Module

```php
// composer.json
{
  "require": {
    "drupal/jsonapi_extras": "^3.0",
    "drupal/jsonapi_resources": "^1.0",
    "drupal/restui": "^1.0",
    "drupal/firebase": "^3.0"
  }
}
```

## Voraussetzungen

- [ ] Firebase-Projekt anlegen
- [ ] FCM Server Key erhalten
- [ ] App-Team Kontakt herstellen
- [ ] API-Specs abstimmen

---

[← Sony VOD Streaming](/integrationen/sony-vod)
[→ Solr Enterprise Search](/integrationen/solr)
