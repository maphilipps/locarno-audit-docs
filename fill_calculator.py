#!/usr/bin/env python3
"""
Fill adesso Calculator 2.01 with Locarno Film Festival audit data.
Based on VitePress documentation and audit findings.
"""

from openpyxl import load_workbook
from pathlib import Path
import sys

def fill_start_sheet(sheet):
    """Fill the Start sheet with project metadata."""
    print("Filling Start sheet...")

    sheet["B8"] = "Locarno Film Festival - Drupal CMS 2.0 Relaunch"
    sheet["B10"] = "Locarno Film Festival"
    sheet["B11"] = "adesso Schweiz AG"
    sheet["B14"] = "CMS Relaunch"
    sheet["B16"] = "Calculation with two teams"
    sheet["B17"] = "1. Preparation"

def fill_features_sheet(sheet):
    """Fill Features sheet with Content Types and Paragraphs."""
    print("Filling Features sheet...")

    row = 11  # First data row

    # Content Types (17)
    content_types = [
        ("F-10", "Content Type & Template", "", "Homepage", "", "Komplexe Homepage mit Hero Carousel und Content Sections", "", "", "L"),
        ("F-20", "Content Type & Template", "", "Film Program", "", "Aktuelle Festival-Filme mit 15 Feldern und Entity References", "", "", "L"),
        ("F-30", "Content Type & Template", "", "Film Archive", "", "10.000+ historische Filme mit Search API Integration", "", "", "L"),
        ("F-40", "Content Type & Template", "", "Film VOD", "", "Video on Demand mit Streaming-Integration", "", "", "M"),
        ("F-50", "Content Type & Template", "", "Person", "", "Regisseure, Cast, Jury mit 8 Feldern", "", "", "M"),
        ("F-60", "Content Type & Template", "", "News", "", "Festival-Nachrichten und Updates", "", "", "M"),
        ("F-70", "Content Type & Template", "", "Press Release", "", "Pressemitteilungen mit Media-Integration", "", "", "S"),
        ("F-80", "Content Type & Template", "", "Event", "", "Festival-Events mit Date Range und Location", "", "", "M"),
        ("F-90", "Content Type & Template", "", "Landing Page", "", "Flexible Marketing-Pages mit Layout Builder", "", "", "L"),
        ("F-100", "Content Type & Template", "", "Page", "", "Standard-Seiten mit 4 Feldern", "", "", "S"),
        ("F-110", "Content Type & Template", "", "Venue", "", "Veranstaltungsorte mit Geolocation", "", "", "S"),
        ("F-120", "Content Type & Template", "", "Sponsor", "", "Sponsoren mit Logo und Link", "", "", "S"),
        ("F-130", "Content Type & Template", "", "Partner", "", "Partner mit Media-Integration", "", "", "S"),
        ("F-140", "Content Type & Template", "", "Award", "", "Auszeichnungen und Preise", "", "", "S"),
        ("F-150", "Content Type & Template", "", "Jury Member", "", "Jurymitglieder mit Person Reference", "", "", "S"),
        ("F-160", "Content Type & Template", "", "FAQ", "", "Häufige Fragen", "", "", "S"),
        ("F-170", "Content Type & Template", "", "Testimony", "", "Testimonials und Zitate", "", "", "S"),
    ]

    for feature in content_types:
        sheet[f"A{row}"] = feature[0]  # ID
        sheet[f"C{row}"] = feature[1]  # Group
        sheet[f"D{row}"] = feature[2]  # Sub Group
        sheet[f"E{row}"] = feature[3]  # Title
        sheet[f"F{row}"] = feature[4]  # Sub Title
        sheet[f"G{row}"] = feature[5]  # Description
        sheet[f"H{row}"] = feature[6]  # Assumptions
        sheet[f"I{row}"] = feature[7]  # Risks
        sheet[f"L{row}"] = feature[8]  # T-shirt size
        row += 1

    # Paragraph Types / Components (35)
    paragraphs = [
        ("F-180", "Content Elements", "Hero Components", "Hero - Full Width", "", "Komplexer Hero mit Background Image/Video, Headline, CTA", "", "", "M"),
        ("F-190", "Content Elements", "Hero Components", "Hero Carousel", "", "Automatischer Carousel mit mehreren Hero-Slides", "", "", "M"),
        ("F-200", "Content Elements", "Layout", "Multi-Column Layout", "", "Flexible 2-4 Column Layouts", "", "", "M"),
        ("F-210", "Content Elements", "Layout", "Accordion", "", "Expandable Accordion Component", "", "", "M"),
        ("F-220", "Content Elements", "Layout", "Tabs", "", "Tab Navigation Component", "", "", "M"),
        ("F-230", "Content Elements", "Content", "Text Section", "", "Text mit Heading und Alignment", "", "", "S"),
        ("F-240", "Content Elements", "Content", "Image-Text Combo", "", "Bild und Text Side-by-Side", "", "", "M"),
        ("F-250", "Content Elements", "Content", "Two-Column Section", "", "2-Spalten Content Layout", "", "", "M"),
        ("F-260", "Content Elements", "Content", "Three-Column Section", "", "3-Spalten Content Layout", "", "", "M"),
        ("F-270", "Content Elements", "Content", "Quote Block", "", "Zitat mit Author und Styling", "", "", "S"),
        ("F-280", "Content Elements", "Media", "Image Gallery", "", "Responsive Image Gallery mit Lightbox", "", "", "M"),
        ("F-290", "Content Elements", "Media", "Video Embed", "", "Embedded Video (YouTube, Vimeo, Sony)", "", "", "M"),
        ("F-300", "Content Elements", "Media", "Image Slider", "", "Automatischer Image Slider/Carousel", "", "", "M"),
        ("F-310", "Content Elements", "Media", "Video Background Section", "", "Section mit Video Background", "", "", "M"),
        ("F-320", "Content Elements", "Media", "Audio Player", "", "Custom Audio Player Component", "", "", "S"),
        ("F-330", "Content Elements", "Film", "Film Card", "", "Film Display Card mit Poster und Info", "", "", "M"),
        ("F-340", "Content Elements", "Film", "Film List/Grid", "", "Grid oder List View für Filme", "", "", "M"),
        ("F-350", "Content Elements", "Film", "Screening Info", "", "Screening Times und Location", "", "", "M"),
        ("F-360", "Content Elements", "Film", "Film Filter/Search", "", "Faceted Search für Film Archive", "", "", "L"),
        ("F-370", "Content Elements", "Interactive", "Modal/Lightbox", "", "Modal Dialog Component", "", "", "M"),
        ("F-380", "Content Elements", "Interactive", "Map Component", "", "Interactive Map für Venues", "", "", "M"),
        ("F-390", "Content Elements", "CTA", "CTA Block", "", "Call-to-Action Block mit Button", "", "", "S"),
        ("F-400", "Content Elements", "CTA", "Button Group", "", "Multiple Buttons in Group", "", "", "S"),
        ("F-410", "Content Elements", "CTA", "Banner", "", "Promotional Banner Component", "", "", "S"),
        ("F-420", "Content Elements", "Lists", "News Teaser Grid", "", "Grid of News Teasers", "", "", "M"),
        ("F-430", "Content Elements", "Lists", "Event Card", "", "Event Display Card", "", "", "M"),
        ("F-440", "Content Elements", "Lists", "Person Card", "", "Person/Director Card", "", "", "M"),
        ("F-450", "Content Elements", "Lists", "Partner Logo Grid", "", "Sponsor/Partner Logo Display", "", "", "S"),
        ("F-460", "Content Elements", "Lists", "Timeline", "", "Timeline Display Component", "", "", "M"),
        ("F-470", "Content Elements", "Special", "Social Links", "", "Social Media Links Component", "", "", "S"),
        ("F-480", "Content Elements", "Special", "Contact Form", "", "Webform Integration Component", "", "", "M"),
        ("F-490", "Content Elements", "Special", "Newsletter Signup", "", "Newsletter Subscription Form", "", "", "S"),
        ("F-500", "Content Elements", "Special", "Search Block", "", "Site Search Component", "", "", "M"),
        ("F-510", "Content Elements", "Special", "Language Switcher", "", "4-Language Navigation Component", "", "", "S"),
        ("F-520", "Content Elements", "Special", "Breadcrumb", "", "Custom Breadcrumb Navigation", "", "", "S"),
    ]

    for paragraph in paragraphs:
        sheet[f"A{row}"] = paragraph[0]
        sheet[f"C{row}"] = paragraph[1]
        sheet[f"D{row}"] = paragraph[2]
        sheet[f"E{row}"] = paragraph[3]
        sheet[f"F{row}"] = paragraph[4]
        sheet[f"G{row}"] = paragraph[5]
        sheet[f"H{row}"] = paragraph[6]
        sheet[f"I{row}"] = paragraph[7]
        sheet[f"L{row}"] = paragraph[8]
        row += 1

    print(f"  Added {len(content_types)} Content Types")
    print(f"  Added {len(paragraphs)} Paragraph Components")

def fill_project_tasks_sheet(sheet):
    """Fill Project Tasks sheet with development phases."""
    print("Filling Project Tasks sheet...")

    row = 13  # First data row

    tasks = [
        # Phase 1: Setup & Architecture
        ("P-10", "Setup & Architektur", "", "DDEV Environment Setup", "Local development setup mit Drupal CMS 2.0", "", "", ""),
        ("P-20", "Setup & Architektur", "", "Drupal 11 Installation", "Fresh Drupal 11 install mit Drupal CMS 2.0 Baseline", "", "", ""),
        ("P-30", "Setup & Architektur", "", "Drupal CMS 2.0 Baseline Integration", "Integration des Drupal CMS 2.0 Starter Kit", "", "", ""),
        ("P-40", "Setup & Architektur", "", "Mercury Theme Setup", "Theme-Konfiguration basierend auf Drupal CMS 2.0", "", "", ""),
        ("P-50", "Setup & Architektur", "", "Core Module Configuration", "Essential Module Setup (Pathauto, Metatag, etc.)", "", "", ""),
        ("P-60", "Setup & Architektur", "", "CI/CD Pipeline Setup", "GitHub Actions für Testing und Deployment", "", "", ""),
        ("P-70", "Setup & Architektur", "", "Azure Infrastructure Setup", "App Service, Database, Blob Storage, CDN", "", "", ""),

        # Phase 2: Content Architecture
        ("P-80", "Content-Architektur", "", "Content Types Implementation", "17 Content Types basierend auf Drupal CMS 2.0 Templates", "", "", ""),
        ("P-90", "Content-Architektur", "", "Paragraph Types Implementation", "35 wiederverwendbare Paragraph Components", "", "", ""),
        ("P-100", "Content-Architektur", "", "Taxonomy Setup", "Vocabularies: Countries, Sections, Genres, Years", "", "", ""),
        ("P-110", "Content-Architektur", "", "Media Configuration", "Image Styles, Responsive Images, Azure Blob", "", "", ""),
        ("P-120", "Content-Architektur", "", "View Modes Configuration", "Full, Teaser, Card, Search Result View Modes", "", "", ""),

        # Phase 3: Integrations
        ("P-130", "Integrationen", "", "Keycloak SSO Integration", "OAuth 2.0 Single Sign-On mit Keycloak", "", "", ""),
        ("P-140", "Integrationen", "", "Fiona Festival API Integration", "REST API Client für Film-Daten", "API kann sich ändern (R1)", "", ""),
        ("P-150", "Integrationen", "", "Sony VOD Streaming Integration", "Video Streaming mit DRM", "DRM Browser-Kompatibilität (R3)", "", ""),
        ("P-160", "Integrationen", "", "Mobile App REST API", "JSON:API für mobile iOS/Android App", "", "", ""),
        ("P-170", "Integrationen", "", "Solr Enterprise Search", "Search API + Solr für 10.000+ Film Archive", "", "", ""),
        ("P-180", "Integrationen", "", "CloudFront CDN Integration", "Azure CDN für Media Assets", "", "", ""),

        # Phase 4: Migration
        ("P-190", "Migration", "", "Magnolia Content Export", "JCR XML + CSV Exports aus Magnolia 6.3", "", "", ""),
        ("P-200", "Migration", "", "Data Mapping & Transformation", "Field-Mapping Magnolia → Drupal", "Data Quality Issues (R5)", "", ""),
        ("P-210", "Migration", "", "Drupal Migrate Plugin Development", "Source + Process Plugins für alle Content Types", "", "", ""),
        ("P-220", "Migration", "", "Film Archive Migration", "10.000+ historische Filme migrieren", "Performance-Probleme (R6)", "", ""),
        ("P-230", "Migration", "", "Media Assets Migration", "Bilder, Videos nach Azure Blob Storage", "", "", ""),
        ("P-240", "Migration", "", "URL Redirects", "2.000+ URL Redirects von Magnolia → Drupal", "", "", ""),

        # Phase 5: Testing
        ("P-250", "Testing", "", "Unit Testing (PHPUnit)", "Backend Unit Tests für Custom Code", "", "", ""),
        ("P-260", "Testing", "", "E2E Testing (Playwright)", "End-to-End Tests für Critical Paths", "", "", ""),
        ("P-270", "Testing", "", "Accessibility Testing", "WCAG 2.1 AA Compliance Testing", "", "", ""),
        ("P-280", "Testing", "", "Performance Testing", "Load Testing für 5.000 req/min", "Azure Limits (R7)", "", ""),
        ("P-290", "Testing", "", "Multilingual Testing", "Testing für DE, IT, FR, EN", "Komplexität (R9)", "", ""),
        ("P-300", "Testing", "", "Browser/Device Testing", "Cross-browser und Responsive Testing", "", "", ""),

        # Phase 6: Deployment
        ("P-310", "Deployment", "", "Staging Deployment", "Deployment zu Azure Staging Environment", "", "", ""),
        ("P-320", "Deployment", "", "UAT & Content Entry", "User Acceptance Testing durch Client", "", "", ""),
        ("P-330", "Deployment", "", "Production Deployment", "Go-Live zu Azure Production", "Verzögerung-Risiko (R12)", "", ""),
        ("P-340", "Deployment", "", "Post-Launch Support", "Monitoring, Bugfixes erste 2 Wochen", "", "", ""),

        # Phase 7: Project Management
        ("P-350", "Projektmanagement", "", "Sprint Planning & Tracking", "Bi-weekly Sprints über 8 Monate", "Scope Creep (R10)", "", ""),
        ("P-360", "Projektmanagement", "", "Stakeholder Communication", "Regular Updates und Status Reports", "", "", ""),
        ("P-370", "Projektmanagement", "", "Risk Management", "Aktives Risiko-Monitoring", "", "", ""),
        ("P-380", "Projektmanagement", "", "Documentation", "Technical Docs, User Guides, Training Materials", "", "", ""),
        ("P-390", "Projektmanagement", "", "Training & Handover", "CMS Training für Redakteure", "", "", ""),
    ]

    for task in tasks:
        sheet[f"A{row}"] = task[0]  # ID
        sheet[f"B{row}"] = task[1]  # Group
        sheet[f"C{row}"] = task[2]  # Summary task
        sheet[f"D{row}"] = task[3]  # Title
        sheet[f"E{row}"] = task[4]  # Description
        sheet[f"F{row}"] = task[5]  # Assumptions
        sheet[f"H{row}"] = task[6]  # Risks
        sheet[f"J{row}"] = task[7]  # Effort
        row += 1

    print(f"  Added {len(tasks)} project tasks")

def fill_project_roles_sheet(sheet):
    """Fill Project Roles sheet with 8 core positions."""
    print("Filling Project Roles sheet (8 Kernpositionen)...")

    row = 9  # First data row

    # 8 Kernpositionen für Locarno Project
    roles = [
        ("R-1", "Project manager", "", "", "100", "adesso Schweiz AG", "", "Schweiz", "", "Zürich", "Senior"),
        ("R-2", "Software architect", "", "Technical Lead", "100", "adesso Schweiz AG", "", "Schweiz", "", "Zürich", "Expert"),
        ("R-3", "Developer", "", "Senior Backend Developer #1", "100", "adesso Schweiz AG", "", "Schweiz", "", "Zürich", "Senior"),
        ("R-4", "Developer", "", "Senior Backend Developer #2", "100", "adesso Schweiz AG", "", "Schweiz", "", "Zürich", "Senior"),
        ("R-5", "Developer", "", "Frontend Developer", "100", "adesso Schweiz AG", "", "Schweiz", "", "Zürich", "Middle"),
        ("R-6", "UI/UX Designer", "", "UX/UI Designer", "100", "adesso Schweiz AG", "", "Schweiz", "", "Zürich", "Middle"),
        ("R-7", "DevOps Engineer", "", "DevOps Engineer", "100", "adesso Schweiz AG", "", "Schweiz", "", "Zürich", "Middle"),
        ("R-8", "Test Engineer", "", "QA/Test Engineer", "100", "adesso Schweiz AG", "", "Schweiz", "", "Zürich", "Middle"),
    ]

    for role in roles:
        sheet[f"A{row}"] = role[0]   # Role ID
        sheet[f"B{row}"] = role[1]   # Project Role
        sheet[f"E{row}"] = role[3]   # Sub role
        sheet[f"F{row}"] = role[4]   # Percentage
        sheet[f"G{row}"] = role[5]   # Company
        sheet[f"I{row}"] = role[7]   # Country
        sheet[f"K{row}"] = role[9]   # Location
        sheet[f"L{row}"] = role[10]  # Seniority Level
        row += 1

    print(f"  Added {len(roles)} project roles")

def fill_project_risks_sheet(sheet):
    """Fill Project Risks sheet with identified risks."""
    print("Filling Project Risks sheet...")

    row = 8  # First data row

    risks = [
        ("R-1", "Fiona API-Änderungen", "API-Struktur ändert sich während der Entwicklung", "P-140", 3, 5),
        ("R-2", "Fiona API-Ausfall (Festival)", "API nicht erreichbar während Peak-Zeiten", "P-140", 2, 3),
        ("R-3", "Sony VOD DRM-Probleme", "DRM-Inkompatibilität mit bestimmten Browsern", "P-150", 3, 4),
        ("R-4", "Keycloak-Version Inkompatibilität", "Drupal OAuth-Module inkompatibel mit Keycloak-Version", "P-130", 2, 2),
        ("R-5", "Migration Data Quality", "Schlechte Datenqualität in Magnolia erschwert Migration", "P-200", 3, 5),
        ("R-6", "Film Archive Performance", "10.000+ Datensätze verursachen Performance-Probleme", "P-220", 2, 3),
        ("R-7", "Peak Traffic Azure-Limits", "5.000 req/min übersteigen Azure App Service Limits", "P-280", 3, 4),
        ("R-8", "Mobile App API Breaking Changes", "JSON:API Änderungen brechen mobile App", "P-160", 3, 3),
        ("R-9", "Multilingual Komplexität", "4 Sprachen verursachen Content-Management-Overhead", "P-290", 3, 3),
        ("R-10", "Scope Creep", "Neue Features während Entwicklung hinzugefügt", "P-350", 4, 5),
        ("R-11", "Team-Verfügbarkeit", "Key-Developer nicht verfügbar zu kritischen Zeiten", "", 2, 3),
        ("R-12", "Go-Live Verzögerung", "Launch verschiebt sich kurz vor Festival", "P-330", 2, 2),
    ]

    for risk in risks:
        sheet[f"A{row}"] = risk[0]  # ID
        sheet[f"B{row}"] = risk[1]  # Title
        sheet[f"C{row}"] = risk[2]  # Description
        sheet[f"D{row}"] = risk[3]  # Source (Feature/Task ID)
        sheet[f"E{row}"] = risk[4]  # Likelihood (1-5)
        sheet[f"F{row}"] = risk[5]  # Impact (days)
        row += 1

    print(f"  Added {len(risks)} project risks")

def main():
    """Main execution function."""
    print("=" * 60)
    print("adesso Calculator 2.01 - Locarno Film Festival Filler")
    print("=" * 60)
    print()

    # Paths
    template_path = Path("/Users/marc.philipps/Downloads/adesso calculator 2.01 - Default Template CMS 1.xlsm")
    output_path = Path("/Users/marc.philipps/Sites/audit_lucarnofestival.ch/locarno-audit-docs/adesso_calculator_locarno_filled.xlsm")

    # Validate template exists
    if not template_path.exists():
        print(f"❌ ERROR: Template not found at {template_path}")
        sys.exit(1)

    print(f"📂 Loading template: {template_path.name}")

    # Load workbook (DON'T keep_vba due to openpyxl compatibility issues)
    try:
        wb = load_workbook(template_path, keep_vba=False)
        print("✅ Template loaded successfully")
        print("⚠️  WARNING: Macros will NOT be preserved (openpyxl limitation)")
        print("   You'll need to copy macros manually from the template")
    except Exception as e:
        print(f"❌ ERROR loading template: {e}")
        sys.exit(1)

    print()

    # Fill all sheets
    try:
        fill_start_sheet(wb["Start"])
        fill_features_sheet(wb["Features"])
        fill_project_tasks_sheet(wb["Project tasks"])
        fill_project_roles_sheet(wb["Project roles"])
        fill_project_risks_sheet(wb["Project risks"])
    except Exception as e:
        print(f"❌ ERROR filling sheets: {e}")
        sys.exit(1)

    print()
    print(f"💾 Saving to: {output_path}")

    # Save as .xlsm (macro-enabled)
    try:
        wb.save(output_path)
        print("✅ Calculator saved successfully!")
    except Exception as e:
        print(f"❌ ERROR saving: {e}")
        sys.exit(1)

    print()
    print("=" * 60)
    print("✅ DONE! Calculator filled successfully.")
    print("=" * 60)
    print()
    print(f"📊 Summary:")
    print(f"  - Project: Locarno Film Festival - Drupal CMS 2.0 Relaunch")
    print(f"  - Content Types: 17")
    print(f"  - Paragraph Components: 35")
    print(f"  - Project Tasks: 39")
    print(f"  - Team Roles: 8 Kernpositionen")
    print(f"  - Risks: 12")
    print()
    print(f"📁 File: {output_path}")
    print(f"   Open in Excel to review and run macros")
    print()

if __name__ == "__main__":
    main()
