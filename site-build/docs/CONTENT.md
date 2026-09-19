# Content

All copy on the site, where it came from, and what is still missing. Anything in `[square brackets]`
appears on the live pages exactly like that until replaced.

## Open items — needed from the band before launch

| # | Item | Where it appears | Who | Notes |
|---|---|---|---|---|
| 1 | **Eventbrite API token + organisation id** | Shows feed (Home, Live) | Dave | DEVELOPMENT.md §4. Until then the site shows `data/events.json` (1 Nov gig). |
| 2 | **Eventbrite ticket URL for 1 Nov** | `data/events.json` → `url` | Dave | Currently points at eventbrite.ie home. |
| 3 | **YouTube video id** — "Live at The Grand Social" | Home, Live, Press | Dave | From the link in the EPK. Set `YOUTUBE_LIVE_ID` in `tools/gen_site.py`. |
| 4 | **Streaming links** — Bandcamp, Spotify, Apple Music, YouTube | Home album panel | Dave | Currently `#`. Remove any platform the band isn't on. |
| 5 | **Social profile URLs** — Facebook, Instagram, SoundCloud | Footer (every page) | Dave | X is set to @tDeviators. |
| 6 | **Photographer credits** for all 8 photos | Media captions, Home hero credit | Dave | Written as `Photo: [credit]`. Also venue for the pub-table and amber shots. |
| 7 | **Original high-resolution photos** | Press ZIP | Dave / photographers | `stage`, `bitzy-blue`, `amber` are only 720 px wide; `wall` 1024. Not truly "hi-res". |
| 8 | **Album artwork** (approved) | Home album panel | Band | Dashed placeholder box. |
| 9 | **Release date** for *More Volume, Less Reverb* / *Tokyo* | Home, Press quick facts | Band | Written `[TBC]`. |
| 10 | **Creatures public link** | Home player | Band | Only when cleared; the EPK stream is private (DECISIONS D12). |
| 11 | **Ferdia Mac Anna quotation** — exact wording + source | Press quotes | Dave | Third quote slot is a dashed placeholder. |
| 12 | **Source links** for The Goo and Colm O'Hare quotes | Press quotes | Dave | The Goo "source" link is `#`. |
| 13 | **Dates** for the Rocky De Valera reunion and The Prongs / Annesley House shows | Live past shows | Band | Written `[date]`. |
| 14 | **Buy link** for *Past the Point of Rescue* | About → Bitzy | Bitzy | Book card link is `#`. |
| 15 | **Logo vector (SVG/AI)** | Media logo tiles, favicon | Whoever made the logo | PNGs re-cut from a JPG; a vector original would be sharper and allow a proper favicon. |
| 16 | **Proper photo of Bren** | About → Bren | Band | Currently a crop of the stage shot; a solo photo would be better. |
| 17 | **Deliberately shot press photo of all three** | About, Media | Band | Email notes asked for this "eventually". |
| 18 | **Old GoDaddy URL slugs** | `netlify.toml` redirects | Zach | Confirm against the live site before DNS switch. |
| 19 | **EPK PDF wording** | Press download | Dave | Aug 2026 file says "next up is The Last Days of Dalymount" and links the private stream — revise before public distribution. |
| 20 | **Privacy notice** review | /privacy/ | Dave | Add cookie/analytics wording if analytics are enabled. |

## Site-wide copy

- **Tagline:** Dublin three-piece. Original high-energy punk, pop and rock 'n' roll. *(email notes)*
- **Header CTA:** Book the band
- **Footer:** Book the band · Bookings / Management: Dave Diebold · dave.diebold@gmail.com · 087 997 3953 ·
  Press: Download EPK (PDF), Hi-res press photos & logo, Band bio, Stage plot & tech spec ·
  Follow: Facebook, Instagram, X · @tDeviators, SoundCloud · © 2026 The Deviators · Dublin, Ireland · Privacy
- **Meta description (Home):** The Deviators — Dublin three-piece. Original high-energy punk, pop and rock 'n' roll. Next show, new single Tokyo, debut album More Volume, Less Reverb.

## Home
- Hero buttons: **Listen to Creatures** · **Watch live** · credit line "The Grand Social, Dublin · Photo: [credit]"
- **Upcoming shows** (Eventbrite) · "Live from Eventbrite · updates automatically" · "All dates & past shows →"
- **Listen / Creatures** — player; note: "Public stream goes live with the single. Promoters and press: request the private link from management."
- **Debut album · Produced by Stano — More Volume, Less Reverb** — "First single *Tokyo* launches at The Grand Social on 1 November. Artwork, track listing and release date to follow." Pills: Bandcamp · Spotify · Apple Music · YouTube
- **Watch — Live at The Grand Social**
- Quote: "Terrific gig by both the Devs and the DeValeras." — Colm O'Hare, music journalist *(EPK)*
- **Selected past shows:** Special guests to Rocky De Valera & the Gravediggers (sold out) — The Grand Social · With The Prongs — Annesley House · Grand Social debut, with Tony St Ledger · 31 May 2026 — The Grand Social *(email notes; May 31 poster)*
- **The band — New songs. Played like the room depends on it.** "Three Dublin musicians making new original material together: short, melodic, high-energy punk and guitar pop. Their histories run back through the city's punk scene — The Strougers, The End, The Lee Harveys, Trouble Pilgrims, Clash Jam Wallop and more — but The Deviators aren't interested in recreating any of it." Bitzy · guitar, vocals / Bren · bass, vocals / Andy · drums, vocals *(Stage Layout doc)* · "Meet the band →"
- Quote: "The songs were riotous and the crowd ate up every second of it." — The Goo *(EPK)*

## Live
- H1 **Shows** · Colm O'Hare quote
- **Upcoming** (Eventbrite, all)
- Video · **What to expect — Forty minutes. No ballads.** "Short, melodic, high-energy songs played with the urgency of people who know exactly what a live room needs. Three-piece, own backdrop, in-ear monitoring — stage plot and tech spec on the Press page." *(Stage Layout doc; "Forty minutes. No ballads." is new copy — confirm set length)*
- **Selected past shows** (three cards, as Home) · "A short list, not a gig diary"

## About
- H1 **Three Dublin musicians. New songs.**
- Story (≈110 words): "The Deviators are Bitzy, Bren and Andy: three Dublin musicians with histories stretching back through the city's punk scene, now making new original material together. The songs are short, melodic and high-energy — punk and guitar pop played with the urgency that comes from knowing exactly what a live room needs. / Their first album, *More Volume, Less Reverb*, produced by Stano, is nearly ready. There is plenty of history in the band, but they are not interested in recreating it." *(EPK + email notes)*
- **Bitzy — Guitar · vocals:** "Started in 1976 with The Slum and was fronting The Strougers by 1978. Baby Goes Boom followed, then a long break from music. Returned in 2009 with The Lee Harveys and spent 15 years with the band until their 2024 break; a brief spell with The Last Pop Stars came before The Deviators." Book card: *Past the Point of Rescue* — "Bitzy's punk memoir, now on its third reprint · Buy the book"
- **Bren — Bass · vocals:** "Started playing bass with The End in 1979 and later played alongside Andy in The Cathedral. In 2014 he teamed up with former The End drummer Johnny Bonnie in Trouble Pilgrims, the band that rose from the ashes of The Radiators From Space."
- **Andy — Drums · vocals:** "Started his first band, Slit Possex, at 14. The Cathedral followed in the early 1980s, then Cabra bands Purdah, Primatevo and Lure through the '90s. Inspired by the loss of Joe Strummer, Clash Jam Wallop was born and Andy spent 16 years with them. Complete Control followed, then three years with The Modfathers before The Deviators."
- **Where they've come from** tags: The Slum · The Strougers · Baby Goes Boom · The End · The Cathedral · Purdah · Primatevo · Lure · The Lee Harveys · Trouble Pilgrims · Clash Jam Wallop · Complete Control · The Modfathers · The Last Pop Stars

## Media
- H1 **Photos** · "Live and press photography for promoters and journalists. Credit the photographer where named." · **Download hi-res press photos** · **Logo files**
- Captions: Live · The Grand Social · Photo: [credit] (jump) / Live · [venue] · Photo: [credit] (pub table) / Press · trio · Photo: [credit] (wall) / Live · The Grand Social · Photo: [credit] (stage) / Live · [venue] · Photo: [credit] (amber) / Rehearsal · Photo: [credit] / Live · [venue] · Photo: [credit] (Bitzy blue) / Backstage · self-portrait
- **Logo — Wordmark files:** "Light and dark versions. Use on plain backgrounds; don't recolour or stretch." · Download dark PNG · Download light PNG

## Press / EPK
- H1 **Press kit** · "Everything a promoter or journalist needs on one page. Revised August 2026." · **Download EPK (PDF)** · **Contact management**
- **The pitch — Dublin three-piece. Original high-energy punk, pop and rock 'n' roll.** "New songs, decades of Dublin stage time, and a debut album produced by Stano on the way. Recent shows include a special-guest slot at Rocky De Valera & the Gravediggers' sold-out Grand Social reunion."
- **Quick facts:** Hometown — Dublin, Ireland · Line-up — Bitzy (guitar/vocals) · Bren (bass/vocals) · Andy (drums/vocals) · Debut album — *More Volume, Less Reverb* · produced by Stano · release [TBC] · Management — Dave Diebold / dave.diebold@gmail.com / 087 997 3953
- **The band** — EPK page 1 text verbatim (three paragraphs, first names). **Where they've come from** — EPK page 2 member paragraphs verbatim (first names).
- **Quotes:** The Goo (full) · Colm O'Hare · Ferdia Mac Anna [placeholder]
- **Assets:** Listen · Creatures — private · on request (mailto) · Watch · Live at The Grand Social — YouTube · Hi-res press photos — ZIP · Logo · light & dark — PNG · Stage plot & tech spec — PDF · Full EPK — PDF · Aug 2026. Note: "Public links only. *Creatures* stays a private stream until cleared for release."

## Privacy (draft)
"This site does not use cookies for tracking and does not run analytics by default. Fonts are loaded from Google Fonts, which may log your IP address. Videos are embedded only after you press play, using YouTube's privacy-enhanced mode. Ticketing is handled by Eventbrite under its own privacy policy. If you email us, we keep your message only for as long as needed to reply."

## 404
"Wrong room. That page isn't here. Try the homepage or the next show."

## Facts deliberately NOT on the site
- *The Last Days of Dalymount* — mentioned in the EPK and email as a coming show, but no date/venue/ticket link supplied. Publish on Eventbrite and it appears.
- The private SoundCloud URL for *Creatures*.
- Surnames of band members (review decision).
- Any release date or track listing for the album.
