import { withMermaid } from 'vitepress-plugin-mermaid'

export default withMermaid({
  title: 'Locarno Film Festival - Website Audit',
  description: 'Drupal Relaunch Audit & Indikationsofferte',
  lang: 'de-CH',
  // Für GitHub Pages: '/repo-name/' setzen
  // Für Netlify oder Custom Domain: '/' lassen
  base: process.env.GITHUB_PAGES ? '/locarno-audit-docs/' : '/',

  // Disable dark mode (adesso theme is light mode only)
  appearance: false,

  // Load Google Fonts for adesso corporate typography
  head: [
    // Preconnect to Google Fonts for performance
    ['link', {
      rel: 'preconnect',
      href: 'https://fonts.googleapis.com'
    }],
    ['link', {
      rel: 'preconnect',
      href: 'https://fonts.gstatic.com',
      crossorigin: ''
    }],
    // Load Fira Sans (body) and Fira Sans Condensed (headings)
    ['link', {
      rel: 'stylesheet',
      href: 'https://fonts.googleapis.com/css2?family=Fira+Sans:wght@400;600;700&family=Fira+Sans+Condensed:wght@400;600;700&display=swap'
    }]
  ],

  mermaid: {
    theme: 'dark'
  },

  themeConfig: {
    logo: '/logo.svg',

    nav: [
      { text: 'Zusammenfassung', link: '/zusammenfassung' },
      { text: 'Integrationen', link: '/integrationen/' },
      { text: 'Timeline', link: '/migration/timeline' },
      { text: 'Offerte', link: '/kosten/offerte' },
      { text: 'Empfehlung', link: '/empfehlung' }
    ],

    sidebar: {
      '/': [
        {
          text: 'Übersicht',
          items: [
            { text: 'Executive Summary', link: '/' },
            { text: 'Detaillierte Zusammenfassung', link: '/zusammenfassung' }
          ]
        },
        {
          text: 'Aktuelle Technologie',
          collapsed: true,
          items: [
            { text: 'Tech-Stack Überblick', link: '/technologie/' },
            { text: 'Magnolia CMS 6.3', link: '/technologie/magnolia' }
          ]
        },
        {
          text: 'Website-Analyse',
          collapsed: true,
          items: [
            { text: 'Seitentypen (23)', link: '/analyse/seitentypen' },
            { text: 'Components (35)', link: '/analyse/components' },
            { text: 'Performance-Audit', link: '/analyse/performance' },
            { text: 'Accessibility-Audit', link: '/analyse/accessibility' }
          ]
        },
        {
          text: 'Drupal-Architektur',
          collapsed: true,
          items: [
            { text: 'Architektur-Übersicht', link: '/architektur/drupal' },
            { text: 'Content Types (17)', link: '/architektur/content-types' },
            { text: 'Paragraphs (35)', link: '/architektur/paragraphs' },
            { text: 'Views & Listings', link: '/architektur/views' }
          ]
        },
        {
          text: 'CMS-Vergleich',
          collapsed: true,
          items: [
            { text: 'Vergleichsübersicht', link: '/cms-vergleich/' },
            { text: 'Drupal CMS 2.0 ⭐⭐⭐⭐⭐', link: '/cms-vergleich/drupal' },
            { text: 'Umbraco ⭐⭐⭐⭐', link: '/cms-vergleich/umbraco' },
            { text: 'Magnolia ⭐⭐⭐', link: '/cms-vergleich/magnolia' }
          ]
        },
        {
          text: 'Hosting & Infrastruktur',
          collapsed: true,
          items: [
            { text: 'Azure-Architektur', link: '/hosting/azure' },
            { text: 'High-Scale (5k req/min)', link: '/hosting/high-scale' }
          ]
        },
        {
          text: '🔌 Integrationen',
          collapsed: false,
          items: [
            { text: 'Übersicht & Systemlandschaft', link: '/integrationen/' },
            { text: 'Keycloak oAuth2 (SSO)', link: '/integrationen/keycloak' },
            { text: 'Fiona Festival API ⚠️', link: '/integrationen/fiona-api' },
            { text: 'Sony VOD Streaming', link: '/integrationen/sony-vod' },
            { text: 'Mobile App REST API', link: '/integrationen/mobile-api' },
            { text: 'Solr Enterprise Search ⚠️', link: '/integrationen/solr' },
            { text: 'CloudFront CDN', link: '/integrationen/cloudfront' }
          ]
        },
        {
          text: '📅 Migration & Projekt',
          collapsed: false,
          items: [
            { text: 'Migrations-Strategie', link: '/migration/strategie' },
            { text: 'Timeline & Meilensteine', link: '/migration/timeline' },
            { text: 'Risiken & Mitigation (12)', link: '/migration/risiken' }
          ]
        },
        {
          text: '👥 Projekt-Organisation',
          collapsed: false,
          items: [
            { text: 'Team & Ressourcen', link: '/projekt/team' },
            { text: 'KPIs & Erfolgskriterien', link: '/projekt/kpis' }
          ]
        },
        {
          text: '💰 Kosten & Budget',
          collapsed: false,
          items: [
            { text: '⭐ Indikationsofferte', link: '/kosten/offerte' },
            { text: 'Feature-Liste (Excel)', link: '/kosten/features' },
            { text: 'Kostenschätzung (Detail)', link: '/kosten/schaetzung' },
            { text: 'Budget-Analyse', link: '/kosten/budget' },
            { text: 'ROI & TCO (5 Jahre)', link: '/kosten/roi' }
          ]
        },
        {
          text: '✅ Empfehlung',
          items: [
            { text: 'Finale Empfehlung', link: '/empfehlung' }
          ]
        }
      ]
    },

    search: {
      provider: 'local'
    },

    footer: {
      message: 'Website-Audit für Locarno Film Festival',
      copyright: 'Copyright © 2025 adesso SE'
    }
  }
})
