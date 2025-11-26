# Accessibility-Audit

WCAG 2.1 AA Compliance-Analyse der aktuellen Website.

## Gesamt-Score: 75/100 ⚠️

**Status:** Nicht WCAG 2.1 AA konform

## Kritische Issues

### 1. Navigation ❌
- Kein Skip-Navigation-Link
- Fehlendes `<main>` Landmark
- Inkonsistente Heading-Hierarchie

### 2. Bilder ❌
- 29 von 72 Bildern ohne Alt-Text (40%)
- Dekorative Bilder nicht als solche markiert

### 3. Formulare ❌
- Alle Inputs ohne Labels
- Keine Error-Messages für Screen Reader
- Submit-Buttons nicht eindeutig

### 4. Kontraste ⚠️
- Einige Text-Farben unter 4.5:1 Ratio
- Buttons im Hover-State problematisch

### 5. Keyboard Navigation ⚠️
- Nicht alle Elemente mit Tastatur erreichbar
- Focus-Indicator teilweise unsichtbar

## Aufwand für WCAG 2.1 AA

**Total:** 54 Stunden

- Navigation-Fixes: 12h
- Alt-Text nachpflegen: 16h
- Formular-Labels: 10h
- Kontrast-Anpassungen: 8h
- Keyboard Navigation: 8h

## Drupal-Vorteile

Drupal 11 bietet out-of-the-box:
- ✅ Semantisches HTML
- ✅ ARIA-Attribute
- ✅ Skip-Links
- ✅ Form-Labels
- ✅ Accessibility-Testing Tools

**adessoCMS Baseline:** WCAG 2.1 AA Foundation included

[→ Drupal Accessibility-Features](/architektur/drupal#accessibility)
