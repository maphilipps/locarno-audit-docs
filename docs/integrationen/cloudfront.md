# Amazon CloudFront CDN

::: tip AUFWAND
**2 PT** | CHF 2.500 | Priorität: **MITTEL**
:::

## Beschreibung

Statische Assets (Bilder, CSS, JS, Downloads) sollen über **Amazon CloudFront** ausgeliefert werden, um:

- Globale Performance zu optimieren
- Azure-Infrastruktur zu entlasten
- Bandbreitenkosten zu senken

Dies ist besonders relevant für das **Film-Archiv mit über 10.000 Einträgen** und zugehörigen Medien (Poster, Stills, Trailer-Thumbnails).

## Technische Anforderungen

| Anforderung | Details |
|-------------|---------|
| Origin | AWS S3 Bucket |
| CDN | Amazon CloudFront |
| Drupal Integration | S3FS Modul |
| SSL | AWS Certificate Manager |
| Cache TTL | 1 Jahr (versionierte Assets) |

## Architektur

```
┌─────────────────────────────────────────┐
│              User Request               │
└─────────────────┬───────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│          CloudFront Edge               │
│          (Global 400+ POPs)             │
└─────────────────┬───────────────────────┘
                  │
         ┌────────┴────────┐
         ▼                 ▼
    [Cache HIT]      [Cache MISS]
         │                 │
         ▼                 ▼
   Return cached      Fetch from S3
   content (<5ms)     + Cache (50-100ms)
         │                 │
         └────────┬────────┘
                  ▼
┌─────────────────────────────────────────┐
│            AWS S3 Bucket                │
│     (locarno-media-production)          │
│  ┌─────────────────────────────────┐   │
│  │ /images/films/                   │   │
│  │ /images/events/                  │   │
│  │ /documents/press/                │   │
│  │ /css/                            │   │
│  │ /js/                             │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

## Vorgehensweise

### 1. AWS S3 + CloudFront Setup (1 PT)
- S3 Bucket erstellen (Region: eu-central-1)
- CloudFront Distribution konfigurieren
- SSL-Zertifikat (ACM)
- Cache-Policies definieren

### 2. Drupal S3FS Integration (1 PT)
- S3FS Modul installieren
- File System auf S3 umstellen
- CDN URL Rewriting aktivieren
- Cache Invalidation bei Updates

## Zeitschätzung

| Phase | PT |
|-------|-----|
| AWS S3 + CloudFront Setup | 1 |
| Drupal S3FS Integration | 1 |
| **Gesamt** | **2** |

## Drupal Konfiguration

```yaml
# settings.php
$settings['s3fs.access_key'] = getenv('AWS_ACCESS_KEY_ID');
$settings['s3fs.secret_key'] = getenv('AWS_SECRET_ACCESS_KEY');

$config['s3fs.settings'] = [
  'bucket' => 'locarno-media-production',
  'region' => 'eu-central-1',
  'use_cname' => TRUE,
  'domain' => 'cdn.locarnofestival.ch',
  'root_folder' => 'drupal',
];
```

## CloudFront Cache Policy

```json
{
  "Name": "Locarno-Static-Assets",
  "DefaultTTL": 86400,
  "MaxTTL": 31536000,
  "MinTTL": 0,
  "ParametersInCacheKeyAndForwardedToOrigin": {
    "EnableAcceptEncodingGzip": true,
    "EnableAcceptEncodingBrotli": true,
    "HeadersConfig": {
      "HeaderBehavior": "none"
    },
    "CookiesConfig": {
      "CookieBehavior": "none"
    },
    "QueryStringsConfig": {
      "QueryStringBehavior": "whitelist",
      "QueryStrings": ["v", "h"]
    }
  }
}
```

## Kosten-Schätzung (AWS)

| Service | Nutzung | Kosten/Monat |
|---------|---------|--------------|
| S3 Storage | 100 GB | ~CHF 2.50 |
| S3 Requests | 1M GET | ~CHF 0.50 |
| CloudFront Transfer | 500 GB | ~CHF 50 |
| CloudFront Requests | 5M | ~CHF 5 |
| **Total** | - | **~CHF 60/Monat** |

**Jährliche Kosten:** ~CHF 720

## Risiken & Mitigation

| Risiko | Wahrsch. | Auswirkung | Mitigation |
|--------|----------|------------|------------|
| Multi-Cloud Komplexität | Niedrig | Niedrig | Klare Verantwortlichkeiten Azure vs. AWS |
| Cache-Inkonsistenzen | Niedrig | Niedrig | Versionierte Asset-URLs, Cache-Busting |
| Kosten AWS zusätzlich | Niedrig | Niedrig | CloudFront Pricing transparent kalkulieren |

## Vorteile

- **Performance:** < 50ms TTFB global
- **Skalierung:** Unbegrenzte Bandbreite während Festival-Peak
- **Kosten:** Günstiger als Azure CDN für hohe Volumes
- **Zuverlässigkeit:** 99.99% SLA

## Voraussetzungen

- [ ] AWS Account
- [ ] S3 Bucket erstellen
- [ ] CloudFront Distribution konfigurieren
- [ ] DNS CNAME: cdn.locarnofestival.ch

---

[← Solr Enterprise Search](/integrationen/solr)
[→ Zurück zur Übersicht](/integrationen/)
