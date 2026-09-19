# Requirements

Derived from the Website Improvement Plan, the 27 Aug email notes and review comments. ✅ = implemented in
this build · ◻ = needs content or a decision from the band (see CONTENT.md → Open items).

## 1. Site-wide

| # | Requirement | Status |
|---|---|---|
| S1 | Five pages: Home · Live · About · Media · Press/EPK; consistent header and footer | ✅ |
| S2 | "Book the band" visible in the header on every page | ✅ |
| S3 | Footer on every page: *Bookings / Management: Dave Diebold · email · phone* + social links. No anonymous contact form as the only route | ✅ (social URLs ◻) |
| S4 | Keep the domain thedeviators.com; redirect old GoDaddy URLs (Music, Meet the Band, Gallery, Get in Touch, dated live page) | ✅ rules in `netlify.toml` — verify slugs ◻ |
| S5 | Mobile-first: hero crop, gig details and booking links must work on a phone | ✅ tested at 390 px |
| S6 | Visual direction: mostly monochrome, big live photographs, one restrained accent (burgundy), distressed logo used sparingly, clean body type | ✅ |
| S7 | Minimal motion; respect `prefers-reduced-motion` | ✅ |
| S8 | Accessible: real links/buttons, visible focus, heading order, alt text, ≥4.5:1 text contrast, ≥44 px touch targets, skip link | ✅ |
| S9 | Descriptive `<title>` and meta description per page; social-sharing image | ✅ |
| S10 | No autoplay audio/video; third-party embeds load only on user action | ✅ |
| S11 | Nothing unconfirmed is presented as fact — placeholders are visible `[…]` | ✅ |

## 2. Home

| # | Requirement | Status |
|---|---|---|
| H1 | First screen does almost everything: full-width jumping Grand Social photo, distressed logo, one-line intro, two buttons **Listen to Creatures** / **Watch live** | ✅ |
| H2 | Next gig with full date, venue, doors time, price and direct ticket link — fed automatically from Eventbrite | ✅ (needs Eventbrite keys ◻) |
| H3 | Music on the site, not just links out: Creatures player | ✅ placeholder player; real SoundCloud embed once cleared ◻ |
| H4 | Album panel: *More Volume, Less Reverb*, Stano credit, Tokyo mention, streaming links | ✅ (artwork, links ◻) |
| H5 | One live video (Grand Social) | ✅ click-to-play; video id ◻ |
| H6 | Concise band introduction, first names only, current sound first | ✅ |
| H7 | The Goo quote between sections; Colm O'Hare quote near live content | ✅ |
| H8 | Selected past shows (Rocky De Valera reunion, The Prongs, Grand Social debut) | ✅ (two dates ◻) |

## 3. Live

| # | Requirement | Status |
|---|---|---|
| L1 | Upcoming shows chronologically, from Eventbrite; clear empty state with booking contact when none | ✅ |
| L2 | Selected past shows as a short section, not a full diary | ✅ |
| L3 | Grand Social live video | ✅ |
| L4 | Link to stage plot / tech spec for promoters | ✅ |
| L5 | *Last Days of Dalymount* listed once confirmed | ◻ publish it on Eventbrite → appears automatically |

## 4. About

| # | Requirement | Status |
|---|---|---|
| A1 | ~150-word band story first: current sound → what they're doing → history | ✅ |
| A2 | Individual bios for Bitzy, Bren, Andy adapted from the EPK; first names only; instruments confirmed | ✅ (instruments from Stage Layout doc) |
| A3 | Bitzy's book as a discreet related link | ✅ (buy link ◻) |
| A4 | Previous-band history concise and secondary | ✅ tag row at the bottom |
| A5 | Photograph of all three members | ✅ backstage selfie; proper press photo ◻ |

## 5. Media

| # | Requirement | Status |
|---|---|---|
| M1 | Lead with the jumping Grand Social photo; 8–12 strong images, no near-duplicates | ✅ 8 images |
| M2 | Photographer credits and clear download labels | ✅ structure; credits ◻ |
| M3 | "Download hi-res press photos" for journalists | ✅ ZIP (note: several supplied files are only 720 px wide ◻) |
| M4 | Logo files, light and dark | ✅ PNG; SVG ◻ (needs vector original) |
| M5 | Descriptive alt text, no "image1" labels | ✅ |

## 6. Press / EPK

| # | Requirement | Status |
|---|---|---|
| P1 | Short pitch, quick facts, management contact on the page — no PDF needed to understand the band | ✅ |
| P2 | Bio text taken from the EPK verbatim, without "short/long bio" labels | ✅ |
| P3 | Press quotes with accurate attribution and source links (The Goo, Colm O'Hare, Ferdia Mac Anna) | ✅ two; Ferdia quote + sources ◻ |
| P4 | Downloadable EPK PDF; show revision date | ✅ Aug 2026 file; recheck time-sensitive wording ◻ |
| P5 | Links to music (private Creatures on request), live video, photos, logo, stage plot | ✅ |

## 7. Non-functional

| # | Requirement | Status |
|---|---|---|
| N1 | Fast: no framework, one CSS file, one JS file, responsive images with `srcset`, lazy loading below the fold | ✅ (Home ≈ 1.1 MB incl. hero at 1600 px) |
| N2 | No tracking cookies by default; privacy page present | ✅ |
| N3 | Hosting cost: free tier (Netlify / Cloudflare Pages); domain stays at GoDaddy | ✅ |
| N4 | Maintainable by one person: dates come from Eventbrite; other edits are plain HTML | ✅ |
| N5 | Deferred (out of scope v1): shop, news/blog, mailing list, full gig archive, elaborate animation | — |
