# Paragraph Types (35)

## Übersicht

Die Drupal-Architektur umfasst **35 Paragraph Types** für flexible, wiederverwendbare Komponenten.

**Gesamtaufwand:** 265 Stunden

---

## Layout Components (7)

### 1. Hero - Full Width
**Machine Name:** `hero`
**Aufwand:** 15h
**Komplexität:** Complex

**Felder:**
- Background Type (Image/Video)
- Background Image (Media)
- Background Video (Media Remote Video)
- Headline (String)
- Subheadline (String)
- Text (Text Long)
- CTA Buttons (Nested Paragraph)
- Overlay Opacity (Integer 0-100)

---

### 2. Hero Carousel
**Machine Name:** `hero_carousel`
**Aufwand:** 12h

**Felder:**
- Slides (Nested Hero Paragraphs)
- Autoplay (Boolean)
- Autoplay Speed (Integer)

---

### 3. Multi-Column Layout
**Machine Name:** `multi_column`
**Aufwand:** 8h

**Felder:**
- Columns (Nested Paragraphs)
- Column Count (List: 2, 3, 4)

---

### 4. Accordion
**Machine Name:** `accordion`
**Aufwand:** 8h

**Felder:**
- Items (Nested accordion_item Paragraphs)

---

### 5. Accordion Item
**Machine Name:** `accordion_item`
**Aufwand:** 4h

**Felder:**
- Title (String)
- Content (Text Long)

---

### 6. Tabs
**Machine Name:** `tabs`
**Aufwand:** 8h

**Felder:**
- Tabs (Nested tab_item Paragraphs)

---

### 7. Tab Item
**Machine Name:** `tab_item`
**Aufwand:** 4h

**Felder:**
- Tab Label (String)
- Content (Text Long)

---

## Content Components (7)

### 8. Text Section
**Machine Name:** `text_section`
**Aufwand:** 5h

**Felder:**
- Heading (String)
- Text (Text Long, Full HTML)
- Text Alignment (List: left, center, right)

---

### 9. Text with Image
**Machine Name:** `text_with_image`
**Aufwand:** 6h

**Felder:**
- Heading (String)
- Text (Text Long)
- Image (Media Image)
- Image Position (List: left, right)

---

### 10. Quote
**Machine Name:** `quote`
**Aufwand:** 4h

**Felder:**
- Quote Text (Text Long)
- Attribution (String)
- Attribution Subtitle (String)

---

### 11. CTA Button
**Machine Name:** `cta_button`
**Aufwand:** 4h

**Felder:**
- Button Text (String)
- Button Link (Link)
- Button Style (List: primary, secondary, outline)

---

### 12. Webform
**Machine Name:** `webform_embed`
**Aufwand:** 4h

**Felder:**
- Webform (Entity Reference Webform)

---

### 13. Embed Code
**Machine Name:** `embed_code`
**Aufwand:** 5h

**Felder:**
- Embed Code (Text Long, sanitized HTML/JS)
- Description (String, admin-only)

---

### 14. Spacer
**Machine Name:** `spacer`
**Aufwand:** 2h

**Felder:**
- Height (List: small, medium, large)

---

## Media Components (3)

### 15. Video Embed
**Machine Name:** `video_embed`
**Aufwand:** 5h

**Felder:**
- Video (Media Remote Video)
- Caption (Text Long)

---

### 16. Image Gallery
**Machine Name:** `image_gallery`
**Aufwand:** 10h

**Felder:**
- Heading (String)
- Images (Media Image, Multiple)
- Gallery Layout (List: grid, masonry, carousel)

---

### 17. Divider
**Machine Name:** `divider`
**Aufwand:** 2h

**Felder:**
- Style (List: solid, dashed, dotted)

---

## Card Components (5)

### 18. Film Card
**Machine Name:** `film_card`
**Aufwand:** 6h

**Felder:**
- Film Reference (Entity Ref: film_program, film_archive, film_vod)
- Display Style (List: default, compact, featured)

---

### 19. Film Listing
**Machine Name:** `film_listing`
**Aufwand:** 10h

**Felder:**
- Heading (String)
- List Type (List: manual, automatic)
- Films Manual (Entity Ref Multiple)
- Filter by Section Auto (Taxonomy Ref)
- Limit (Integer)

---

### 20. News Card
**Machine Name:** `news_card`
**Aufwand:** 5h

**Felder:**
- News Reference (Entity Ref: news)
- Display Style (List: default, compact, featured)

---

### 21. News Listing
**Machine Name:** `news_listing`
**Aufwand:** 10h

**Felder:**
- Heading (String)
- Category Filter (Taxonomy Ref Multiple)
- Limit (Integer)
- Show Filters (Boolean)

---

### 22. Person Card
**Machine Name:** `person_card`
**Aufwand:** 5h

**Felder:**
- Person Reference (Entity Ref: person)
- Display Style (List: default, compact, with_bio)

---

## Special Components (6)

### 23. Screening Schedule
**Machine Name:** `screening`
**Aufwand:** 6h

**Felder:**
- Date & Time (DateTime)
- Venue (Entity Ref: venue)
- Ticket Link (Link)
- Notes (String, e.g., "World Premiere", "Director Q&A")

---

### 24. Award Winner
**Machine Name:** `award_winner`
**Aufwand:** 6h

**Felder:**
- Award Name (String)
- Film (Entity Ref: film_program, film_archive)
- Winner(s) (Entity Ref: person, Multiple)
- Description (Text Long)

---

### 25. Contact Info
**Machine Name:** `contact_info`
**Aufwand:** 4h

**Felder:**
- Name (String)
- Title (String)
- Email (Email)
- Phone (Telephone)

---

### 26. Social Link
**Machine Name:** `social_link`
**Aufwand:** 4h

**Felder:**
- Platform (List: facebook, twitter, instagram, linkedin, youtube, vimeo, website)
- URL (Link)

---

### 27. Benefit Item
**Machine Name:** `benefit_item`
**Aufwand:** 4h

**Felder:**
- Icon (Media SVG)
- Title (String)
- Description (Text Long)

---

### 28. Shopify Product
**Machine Name:** `shopify_product`
**Aufwand:** 12h
**Komplexität:** Medium

**Felder:**
- Product ID (String, Shopify product ID)
- Display Style (List: card, inline, featured)

**Integration:** Shopify Buy Button SDK

---

## Zusammenfassung

**Total:** 35 Paragraph Types
- **Komplexität:**
  - Complex: 2 (Hero, Shopify Product)
  - Medium: 6 (Image Gallery, Film Listing, News Listing, etc.)
  - Simple: 27
- **Gesamtaufwand:** 265 Stunden
- **BörsenXperts Baseline:** 120h gespart (Foundation, Hero, Text, Button, Cards vorhanden)
