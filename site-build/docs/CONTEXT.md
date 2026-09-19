# Context

## The band

**The Deviators** are a Dublin three-piece: **Bitzy** (guitar/vocals), **Bren** (bass/vocals) and **Andy**
(drums/vocals). Original, high-energy punk and guitar pop — all new songs. Between them their histories run
through The Strougers, The End, The Cathedral, The Lee Harveys, Trouble Pilgrims, Clash Jam Wallop, The
Modfathers and others; Bitzy is also the author of the punk memoir *Past the Point of Rescue*.

Debut album **More Volume, Less Reverb**, produced by **Stano**, is nearly ready. First single **Tokyo**
launches at **The Grand Social Ballroom, Dublin, on Sunday 1 November 2026 (doors 4.30pm, €15, special
guests Amadán, tickets on Eventbrite)**.

Management / bookings: **Dave Diebold · dave.diebold@gmail.com · 087 997 3953**.

## Why the site is being redone

The live site (GoDaddy Website Builder, dark purple theme) had a large empty header, no way to actually
hear the band on the Music page, a thin "Meet the band" page, a dated gig item in the main navigation
("Live @TGS 31st May 2026"), and no press kit. Promoters and journalists had to work to find out what the
band sounds like, when they're next playing, and who to call.

The goal, from the Website Improvement Plan (19 Sep 2026): **make thedeviators.com a living electronic
press kit** — a promoter, journalist or new listener should understand the band, hear or see a performance,
find the next gig and contact management within seconds.

## Positioning (important — governs every page)

From the 27 Aug 2026 email notes: **do not describe The Deviators primarily as a heritage punk band.**
The order on every page is:

1. here's what The Deviators sound like *now* →
2. here's what they're doing *now* (gig, single, album) →
3. incidentally, look where these three came from.

The impressive previous-band credits sit underneath the current band so that *More Volume, Less Reverb*
never reads as a nostalgia exercise. The homepage tagline is therefore "Dublin three-piece. Original
high-energy punk, pop and rock 'n' roll." — not a list of old bands.

## Source material used

| Source | Used for |
|---|---|
| `The_Deviators_EPK.pdf` (Aug 2026, 2 pp.) | Band bio, member bios, quotes (The Goo, Colm O'Hare), album/producer credit, management contact |
| `Website Improvement Plan.md` (19 Sep 2026) | Site structure (Home · Live · About · Media · Press/EPK), homepage order, visual direction, content decisions, delivery phases, checks |
| `Website email notes.md` (email, 27 Aug 2026) | Tagline, "Listen to Creatures / Watch live" buttons, selected past shows list, footer contact rule, "keep it slightly rough", positioning rule |
| `Single launch details.md` (email, 1 Sep 2026) | Venue = Grand Social Ballroom, **doors 4.30pm**, single launch + support |
| `Stage Layout.docx` | Instruments per member; converted to `downloads/The_Deviators_Stage_Layout.pdf` |
| `deviators logo.jpg` | Wordmark, re-cut as white-on-transparent and dark-on-transparent PNGs |
| `deviators live shot mono.jpg` | Homepage hero (the "jumping Grand Social" shot the email asked for) |
| 9 further photos | Media page, section imagery, past-show cards |
| Live site thedeviators.com | Existing nav labels (for redirects), Eventbrite €15 price, @tDeviators handle, "Tokyo" announcement |
| Design canvas "The Deviators — Website Design" | The approved visual design this build implements |

## Design history (short)

Three homepage directions were mocked up — **A Blackout** (dark, full-bleed photo, burgundy accent),
**B Zine** (newsprint, heavy rules, red), **C Gallery** (white, serif, no accent). **A was chosen** and
developed into all five pages; B and C were removed from the canvas. The build in `site/` is direction A.
Comments on the canvas during review led to: real logo with clean edges; Eventbrite-fed shows list
replacing a hand-typed "next show"; first names only for band members; EPK text used verbatim for the press
bio (no "short bio / long bio" labels); deliberate line breaks in two-sentence headlines.
