# Azure High-Scale Architektur

## Übersicht

**Ziel:** 8.000 Requests/Minute (133 req/sec) @ 99,9% SLA
**Region:** Switzerland North (Primary)
**Monatliche Kosten:** CHF 2.950 (optimiert) | CHF 4.200 (Standard)

---

## Compute - App Service

**Service:** Azure App Service Premium v3 P1V3
**Instances:** 3-12 (Auto-Scaling)
**Specs pro Instance:** 2 vCPU, 8GB RAM, 250GB Storage

### Auto-Scaling Rules
- CPU > 70% für 5min → +1 Instance
- Memory > 80% für 5min → +1 Instance
- HTTP Queue > 100 → +2 Instances
- CPU < 30% für 10min → -1 Instance

**Cost:** CHF 564/Monat

---

## Database - MySQL Flexible Server

**Tier:** Business Critical
**Specs:** 4 vCores, 16GB RAM, 128GB Storage
**IOPS:** 400 baseline, 3.100 burst

### High Availability
- Zone-Redundant HA
- Failover: 60 Sekunden
- Read Replica (Switzerland North)
- Traffic Split: 70% Reads → Replica

**Cost:** CHF 1.364/Monat (Primary + Replica)

---

## Caching - Redis Premium P1

**Specs:** 6GB Cache, 1.500 Mbps Bandwidth
**Max Connections:** 7.500
**Zone Redundancy:** Enabled
**Persistence:** RDB Snapshots (15min)

### Use Cases
- Drupal Cache Backend
- Session Storage (10-20 editors)
- Lock Backend
- Flood Control

**Cost:** CHF 390/Monat

---

## CDN - Azure Front Door Premium

**Coverage:** 115+ Edge Locations Global
**Hit Ratio Target:** 98%

### Features
- WAF (OWASP 3.2)
- DDoS Protection Standard
- Brotli/Gzip Compression
- Managed SSL/TLS Certificates

### Caching
- Static Assets: 365 Tage TTL
- Pages: 1 Stunde TTL
- Bypass: /admin/*, /user/*

**Cost:** CHF 467/Monat

---

## Storage - Blob Storage Hot Tier

**Redundancy:** LRS (Switzerland North)
**Total:** 260GB

### Containers
- `drupal-public` (50GB) - Public files, CDN-integrated
- `drupal-private` (10GB) - Private files, SAS tokens
- `drupal-backups` (200GB) - DB + File backups

**Cost:** CHF 48/Monat

---

## Search - Azure Cognitive Search

**Tier:** Basic
**Specs:** 2GB Storage, 1M Docs, 100 queries/sec

### Features
- Full-text Search
- Faceted Search
- Autocomplete/Suggestions
- Multi-language (EN/DE/FR/IT)

**Cost:** CHF 70/Monat

---

## Monitoring - Application Insights

### Components
- Application Performance Monitoring (APM)
- Log Analytics Workspace
- Availability Tests (5 Locations, 5min)

### Dashboards
- **Executive:** Uptime, Response Time, Requests, Errors
- **Technical:** CPU/Memory, Database IOPS, Cache Hit Ratio, Slow Queries

**Cost:** CHF 78/Monat

---

## Security

### Key Vault
- mysql-password
- redis-password
- azure-storage-key
- drupal-hash-salt

**Rotation:** 90 days

### SSL/TLS
- Minimum: TLS 1.2
- Preferred: TLS 1.3
- HSTS Enabled (31.536.000 sec)

### WAF Policy
- Mode: Prevention
- Ruleset: OWASP 3.2
- Rate Limiting: 1.000 req/min per IP
- Admin IP Whitelist

**Cost:** CHF 22/Monat

---

## Backup & DR

**RPO:** 5 Minuten
**RTO:** 30 Minuten

### Strategie
- **Database:** Continuous Transaction Log (5min)
- **Files:** Real-time (Blob Storage)
- **Config:** Per Git Commit

**Retention:** 35 Tage

---

## Kostenübersicht

### Monatlich (Standard)
| Service | CHF/Monat |
|---------|----------:|
| App Service | 564 |
| MySQL DB | 1.364 |
| Redis Cache | 390 |
| Front Door CDN | 467 |
| Blob Storage | 48 |
| Cognitive Search | 70 |
| Monitoring | 78 |
| Backup | 23 |
| Networking | 21 |
| Key Vault | 1 |
| Azure DevOps | 38 |
| **Contingency 10%** | 388 |
| **Total** | **4.452** |
| **Rounded** | **4.200** |

### Optimiert (Reserved Instances)
**Monatlich:** CHF 2.950
**Jährlich:** CHF 35.400
**Savings:** CHF 16.668/Jahr (30%)

---

## Performance Targets

- Homepage (cached): < 100ms
- Homepage (uncached): < 500ms
- Node Page (cached): < 100ms
- Admin Page: < 1.000ms
- CDN Hit Ratio: 98%
- Uptime: 99,9%
