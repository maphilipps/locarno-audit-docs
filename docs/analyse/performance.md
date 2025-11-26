# Performance-Audit

Analyse der aktuellen Website-Performance.

## Core Web Vitals

| Metrik | Aktuell | Ziel | Status |
|--------|---------|------|--------|
| **LCP** | 364ms | <2.500ms | ✅ Exzellent |
| **CLS** | 0.0 | <0.1 | ✅ Perfekt |
| **TTFB** | 53ms | <600ms | ✅ Sehr gut |

## Probleme

### 1. Vimeo-Video (6 MB)
- Autoload eines 6 MB Videos
- Blockiert Page-Load
- **Fix:** Lazy Loading + Thumbnail

### 2. Keine WebP-Bilder
- Nur JPEG/PNG
- Größere Dateien
- **Fix:** WebP mit JPEG Fallback

### 3. Font-Loading
- 235ms blockierendes Font-Loading
- **Fix:** Font-Display Swap

## Drupal-Optimierungen

- BigPipe für Below-the-Fold
- Redis Cache
- CDN (Azure)
- Image Lazy Loading
- WebP-Konvertierung

[→ Azure High-Scale Architektur](/hosting/high-scale)
