# High-Scale Strategie

## Peak Load: 8.000 Requests/Minute

**Equivalent:** 133 Requests/Sekunde
**Szenario:** Festival-Periode (2 Wochen/Jahr)

---

## Architektur-Pattern

### Horizontal Scaling
- **App Service:** 3-12 Instances (Auto-Scale)
- **Database:** Read Replica (70% Read Traffic)
- **Shared-Nothing:** Stateless App Tier

### Caching Layers
1. **CDN (Front Door)** - 98% Hit Ratio
2. **Drupal Page Cache** - Anonymous Users
3. **Redis Cache** - Render Cache, Entities
4. **Database Query Cache** - MySQL Buffer Pool

---

## Traffic Distribution

### CDN (Front Door) - 98% cached
- 7.840 req/min (130 req/sec) → CDN serves
- 160 req/min (2,7 req/sec) → App Service

### App Service - 160 req/min
- Static Assets: Nginx direkt (50 req/min)
- Drupal PHP-FPM: 110 req/min

### Database - Read/Write Split
- 77 req/min Reads → Read Replica
- 33 req/min Writes → Primary

---

## Load Testing

### Scenarios
1. **Baseline:** 100 req/sec, 5min
2. **Peak:** 133 req/sec, 10min
3. **Stress:** 200 req/sec bis Failure
4. **Soak:** 80 req/sec, 2 Stunden

**Tool:** Artillery

---

## Bottleneck Prevention

### Database
- **Connection Pooling:** ProxySQL (200 max connections)
- **Read Replica:** 70% Traffic
- **Indexes:** field_year, field_country
- **Slow Query Threshold:** 2 Sekunden

### App Service
- **PHP-FPM Workers:** 50 pro Instance
- **OPcache:** 128MB
- **Memory Limit:** 512MB
- **Max Execution:** 60 Sekunden

### Redis
- **Eviction Policy:** volatile-lru
- **Max Memory:** 6GB
- **Persistence:** RDB Snapshots

---

## Failover & HA

### App Service
- **Health Check:** /user/login (200 expected)
- **Unhealthy Instance:** Auto-removed
- **New Instance:** 60 Sekunden Warmup

### Database
- **Zone-Redundant HA:** Auto-Failover 60sec
- **Read Replica:** Manual Promotion möglich

### CDN
- **Multi-Region:** 115+ Edge Locations
- **Origin Failover:** Automatic

---

## Monitoring & Alerts

### Critical Alerts (Page On-Call)
- Site Down (HTTP 500/503 > 5 in 5min)
- Response Time > 3s für 10min
- Database CPU > 90% für 5min

### Warning Alerts (Email)
- Response Time > 1s für 15min
- Cache Hit Ratio < 85% für 30min

---

## Cost Optimization

### Off-Season (10 Monate)
- Scale down zu 3 Instances
- Consider pausing Read Replica
- **Savings:** CHF 3.996/Jahr

### Reserved Instances (3 Jahre)
- 30% Discount auf Compute
- **Savings:** CHF 8.580/Jahr

**Total Potential Savings:** CHF 16.668/Jahr
**Optimized Annual Cost:** CHF 35.400 (vs CHF 50.400)
