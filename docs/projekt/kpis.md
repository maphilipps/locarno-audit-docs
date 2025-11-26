# KPIs & Erfolgskriterien

## Technische KPIs

### Performance

| Metrik | Zielwert | Messung | Kritikalität |
|--------|----------|---------|--------------|
| **Response Time (p95)** | < 1 Sekunde | Application Insights | **KRITISCH** |
| **Time to First Byte (TTFB)** | < 200ms | Lighthouse | HOCH |
| **Largest Contentful Paint (LCP)** | < 2.5s | Core Web Vitals | HOCH |
| **Cumulative Layout Shift (CLS)** | < 0.1 | Core Web Vitals | MITTEL |
| **First Input Delay (FID)** | < 100ms | Core Web Vitals | MITTEL |

### Verfügbarkeit & Skalierung

| Metrik | Zielwert | Messung | Kritikalität |
|--------|----------|---------|--------------|
| **Uptime** | 99.9% | Azure Monitor | **KRITISCH** |
| **Peak Capacity** | 5.000 req/min | k6 Load Tests | **KRITISCH** |
| **Error Rate** | < 0.1% | Sentry | HOCH |
| **Database Response** | < 50ms (p95) | Slow Query Log | HOCH |

### Qualität

| Metrik | Zielwert | Messung | Kritikalität |
|--------|----------|---------|--------------|
| **Lighthouse Score** | > 90/100 | Lighthouse CI | HOCH |
| **Accessibility** | WCAG 2.1 AA | Axe-core | **KRITISCH** |
| **Test Coverage** | > 80% | PHPUnit | MITTEL |
| **Security Scan** | 0 Critical | Drupal Security | **KRITISCH** |

## Projekt-KPIs

### Timeline

| Metrik | Zielwert | Toleranz | Kritikalität |
|--------|----------|----------|--------------|
| **Go-Live Datum** | 11.08.2026 | ±2 Wochen | **KRITISCH** |
| **Meilenstein-Einhaltung** | 100% | 1 Woche Puffer | HOCH |
| **Sprint Velocity** | Stabil ±10% | - | MITTEL |

### Budget

| Metrik | Zielwert | Toleranz | Kritikalität |
|--------|----------|----------|--------------|
| **Budget-Einhaltung** | 100% | ±10% | **KRITISCH** |
| **Change Request Budget** | < 15% | - | HOCH |
| **Burn Rate** | Linear | ±20% | MITTEL |

### Qualität

| Metrik | Zielwert | Toleranz | Kritikalität |
|--------|----------|----------|--------------|
| **Content Migration** | 99.5% Vollständigkeit | - | **KRITISCH** |
| **404 Errors (Monat 1)** | < 1% | - | HOCH |
| **Bug Density** | < 5 Bugs/Sprint | - | MITTEL |
| **UAT Approval** | 100% | - | **KRITISCH** |

## Dashboard

```
┌─────────────────────────────────────────────────────────────┐
│                   PROJECT HEALTH DASHBOARD                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PERFORMANCE              AVAILABILITY          QUALITY     │
│  ┌──────────────┐        ┌──────────────┐     ┌──────────┐ │
│  │ Response <1s │        │ Uptime 99.9% │     │ A11y AA  │ │
│  │     ✅       │        │      ✅      │     │    ✅    │ │
│  └──────────────┘        └──────────────┘     └──────────┘ │
│                                                             │
│  BUDGET                  TIMELINE              MIGRATION    │
│  ┌──────────────┐        ┌──────────────┐     ┌──────────┐ │
│  │    ±10%     │        │  On Track    │     │  99.5%   │ │
│  │     ✅       │        │      ✅      │     │    ✅    │ │
│  └──────────────┘        └──────────────┘     └──────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Messmethoden

### Performance-Messung

```bash
# Lighthouse CI (automatisch in CI/CD)
lighthouse https://staging.locarnofestival.ch \
  --output=json \
  --chrome-flags="--headless"

# k6 Load Test
k6 run \
  --vus 100 \
  --duration 5m \
  load-test.js
```

### Verfügbarkeit

- **Azure Monitor:** Uptime-Checks alle 5 Minuten
- **Application Insights:** Request/Response Tracking
- **Sentry:** Error Tracking & Alerting

### Accessibility

```bash
# Axe-core CLI
axe https://staging.locarnofestival.ch \
  --tags wcag2aa \
  --reporter html
```

## Schwellenwerte & Alerting

### Kritische Alerts (sofortige Reaktion)

| Bedingung | Alert | Aktion |
|-----------|-------|--------|
| Response Time > 3s | PagerDuty | On-Call kontaktieren |
| Uptime < 99% | SMS/Call | Incident Management |
| Error Rate > 1% | Slack #incidents | Debugging starten |
| Security Vulnerability | Email + Slack | Sofort patchen |

### Warn-Alerts (Business Hours)

| Bedingung | Alert | Aktion |
|-----------|-------|--------|
| Response Time > 1.5s | Slack | Untersuchen |
| 404 Rate > 0.5% | Email | Redirects prüfen |
| CPU > 80% | Slack | Skalierung prüfen |

## Reporting

### Wöchentliches Reporting

| Sektion | Inhalte |
|---------|---------|
| Status Summary | Ampel-Status aller KPIs |
| Sprint Progress | Velocity, Burndown |
| Risiken | Top 3 aktive Risiken |
| Blockers | Aktuelle Hindernisse |
| Next Week | Geplante Aktivitäten |

### Monatliches Reporting

| Sektion | Inhalte |
|---------|---------|
| Executive Summary | 1-Seite Übersicht |
| Budget Status | Ist vs. Plan |
| Timeline Status | Meilenstein-Tracking |
| Quality Metrics | Test Coverage, Bugs |
| Risk Register | Vollständige Übersicht |
| Decisions Needed | Offene Entscheidungen |

## Acceptance Criteria (Go-Live)

### Must-Have (Blocker)

- [ ] Alle 23 Content Types funktionsfähig
- [ ] Alle 35 Components implementiert
- [ ] Migration 99.5%+ vollständig
- [ ] WCAG 2.1 AA konform
- [ ] 5.000 req/min bestanden
- [ ] Keycloak SSO funktioniert
- [ ] Fiona API Sync funktioniert
- [ ] Mobile API dokumentiert
- [ ] 0 kritische Bugs
- [ ] UAT abgeschlossen

### Should-Have (Nice to Have)

- [ ] Lighthouse Score > 95
- [ ] 100% Test Coverage kritischer Pfade
- [ ] Full Video-Tutorial-Set
- [ ] Advanced Caching konfiguriert

---

[← Team & Ressourcen](/projekt/team)
[→ Timeline & Meilensteine](/migration/timeline)
