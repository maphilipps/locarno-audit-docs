# Keycloak oAuth.2 Integration

::: info AUFWAND
**8 PT** | CHF 10.000 | Priorität: **HOCH**
:::

## Beschreibung

Die Benutzer-Authentifizierung muss über den bestehenden Keycloak Identity Provider erfolgen. Dies ermöglicht Single Sign-On (SSO) für:

- **Registrierte Besucher** - Festival-Besucher mit Account
- **Presse-Akkreditierung** - Journalisten mit Pressezugang
- **Pro/Industry** - Branchenvertreter mit erweiterten Rechten

Die Integration muss **oAuth 2.0 / OpenID Connect** unterstützen.

## Technische Anforderungen

| Anforderung | Details |
|-------------|---------|
| Protokoll | OAuth 2.0 + OpenID Connect |
| Provider | Keycloak (bestehende Instanz) |
| Drupal Module | Simple OAuth, OpenID Connect |
| User Provisioning | Automatisch bei Erstanmeldung |
| Rollen-Mapping | Keycloak Groups → Drupal Roles |

## Vorgehensweise

### 1. Modul-Setup (2 PT)
- Installation Simple OAuth + OpenID Connect Module
- Konfiguration der OAuth-Provider

### 2. Keycloak Client Configuration (3 PT)
- Client-ID/Secret anlegen
- Redirect URIs konfigurieren
- Scope-Mapping definieren

### 3. User Provisioning (2 PT)
- Automatische Drupal-User-Erstellung bei erstem Login
- Rollen-Mapping implementieren:

| Keycloak Group | Drupal Role | Berechtigungen |
|----------------|-------------|----------------|
| `public` | Authenticated | Basis-Zugang |
| `press` | Press | Pressematerial, Downloads |
| `pro` | Pro/Industry | Industry-Bereich, VOD |
| `admin` | Administrator | Backend-Zugang |

### 4. Session Management (1 PT)
- Token Refresh implementieren
- Logout-Propagation
- Session Timeout Sync

## Zeitschätzung

| Phase | PT |
|-------|-----|
| OAuth Modul Setup & Config | 2 |
| Keycloak Client Integration | 3 |
| User Mapping & Rollen | 2 |
| Testing & Edge Cases | 1 |
| **Gesamt** | **8** |

## Risiken & Mitigation

| Risiko | Wahrsch. | Auswirkung | Mitigation |
|--------|----------|------------|------------|
| Keycloak-Version Inkompatibilität | Niedrig | Hoch | Frühe Testphase, Version-Lock dokumentieren |
| Token-Expiry während Session | Mittel | Mittel | Silent Refresh implementieren |
| Bestehende User-Migration | Mittel | Mittel | Mapping-Script, Parallel-Betrieb |

## Drupal Module

```php
// composer.json
{
  "require": {
    "drupal/simple_oauth": "^6.0",
    "drupal/openid_connect": "^3.0"
  }
}
```

## Konfiguration

```yaml
# config/install/openid_connect.settings.keycloak.yml
settings:
  client_id: 'locarno-drupal'
  client_secret: '${KEYCLOAK_CLIENT_SECRET}'
  authorization_endpoint: 'https://auth.locarnofestival.ch/realms/locarno/protocol/openid-connect/auth'
  token_endpoint: 'https://auth.locarnofestival.ch/realms/locarno/protocol/openid-connect/token'
  userinfo_endpoint: 'https://auth.locarnofestival.ch/realms/locarno/protocol/openid-connect/userinfo'
```

## Voraussetzungen

- [ ] Keycloak-Testzugang beantragen
- [ ] Client-ID/Secret erhalten
- [ ] Redirect URIs abstimmen
- [ ] Rollen-Mapping dokumentieren

---

[← Zurück zur Übersicht](/integrationen/)
[→ Fiona Festival API](/integrationen/fiona-api)
