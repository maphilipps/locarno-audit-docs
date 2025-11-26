# Sony VOD Streaming Integration

::: info AUFWAND
**8 PT** | CHF 10.000 | Priorität: **HOCH**
:::

## Beschreibung

Das Locarno Film Festival bietet Video-on-Demand Inhalte über **Sony Pictures Core** an. Die Integration umfasst:

- **fVOD** (Free Video on Demand) - Kostenlose Trailer, Interviews
- **sVOD** (Subscription Video on Demand) - Kostenpflichtige Filme

Der Video-Player muss in die Website eingebettet werden, mit entsprechender Zugriffskontrolle für zahlende Nutzer.

## Technische Anforderungen

| Anforderung | Details |
|-------------|---------|
| Streaming-Provider | Sony Pictures Core |
| DRM | Widevine, FairPlay, PlayReady |
| Player | Eingebetteter Web-Player |
| Authentifizierung | Via Keycloak (Paywall-Logik) |
| Geoblocking | Optional pro Content |

## Content-Typen

| Typ | Zugang | Beschreibung |
|-----|--------|--------------|
| fVOD | Öffentlich | Trailer, Behind-the-Scenes, Interviews |
| sVOD | Zahlend | Vollständige Filme, Retrospektiven |
| Exclusive | Pro/Industry | Screener, Pressevorführungen |

## Vorgehensweise

### 1. Sony API Integration (3 PT)
- API-Dokumentation analysieren
- Authentifizierung implementieren
- Content-Katalog abrufen

### 2. Video Player Implementation (2 PT)
- Responsive Video Player einbetten
- DRM-Unterstützung konfigurieren
- Branding/Customization

### 3. Access Control & Paywall (2 PT)
- Integration mit Keycloak-Rollen
- Paywall-Logik implementieren:

```
┌─────────────────────────────────────────┐
│           Video Request                 │
└─────────────────┬───────────────────────┘
                  │
                  ▼
         ┌───────────────┐
         │  Content Type │
         └───────┬───────┘
                 │
    ┌────────────┼────────────┐
    ▼            ▼            ▼
  [fVOD]      [sVOD]     [Exclusive]
    │            │            │
    ▼            ▼            ▼
  Public    Paid User?   Pro Role?
    │            │            │
    │      ┌─────┴─────┐      │
    │      ▼           ▼      │
    │   [JA]        [NEIN]    │
    │     │            │      │
    │     ▼            ▼      │
    │  Play Video  Paywall    │
    │                         │
    └─────────┬───────────────┘
              ▼
         Video Player
```

### 4. Testing (1 PT)
- Cross-Browser Testing (Chrome, Safari, Firefox, Edge)
- Mobile Device Testing
- DRM-Kompatibilität prüfen

## Zeitschätzung

| Phase | PT |
|-------|-----|
| Sony API Integration | 3 |
| Video Player Implementation | 2 |
| Access Control & Paywall | 2 |
| Testing (Browser, Devices) | 1 |
| **Gesamt** | **8** |

## Drupal Content Type: VOD

```yaml
# Film VOD Content Type
fields:
  - field_vod_id: string (Sony Content ID)
  - field_vod_type: list (fvod, svod, exclusive)
  - field_vod_thumbnail: media_image
  - field_vod_duration: integer (Sekunden)
  - field_vod_availability: daterange
  - field_vod_geo_restriction: list (countries)
  - field_film_reference: entity_reference (Film)
```

## Risiken & Mitigation

| Risiko | Wahrsch. | Auswirkung | Mitigation |
|--------|----------|------------|------------|
| **DRM-Kompatibilität Browser** | Mittel | Hoch | Multi-DRM Strategy (Widevine, FairPlay, PlayReady) |
| Streaming-Performance | Niedrig | Mittel | Adaptive Bitrate, CDN für Delivery |
| Zahlungs-Integration | Mittel | Mittel | Klare Schnittstelle zu Ticketing definieren |

## Player-Integration

```html
<!-- Sony Pictures Core Player Embed -->
<div id="sony-player"
     data-content-id="{{ node.field_vod_id.value }}"
     data-user-token="{{ keycloak_token }}"
     data-drm-config="{{ drm_config }}">
</div>

<script src="https://player.sonypicturescore.com/embed.js"></script>
<script>
  SonyPlayer.init({
    container: '#sony-player',
    contentId: '{{ content_id }}',
    auth: {
      token: '{{ user_token }}',
      provider: 'keycloak'
    },
    ui: {
      branding: 'locarno',
      primaryColor: '#FFD700'
    }
  });
</script>
```

## Voraussetzungen

- [ ] Sony Pictures Core API-Zugang beantragen
- [ ] DRM-Lizenzen klären
- [ ] Test-Content verfügbar
- [ ] Paywall-Logik mit Ticketing abstimmen

---

[← Fiona Festival API](/integrationen/fiona-api)
[→ Mobile App REST API](/integrationen/mobile-api)
