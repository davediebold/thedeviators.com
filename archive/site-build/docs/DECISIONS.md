# Decisions

Short records of the choices that shape this build, with the reasoning, so nobody re-litigates them by
accident. Newest last.

---

### D1 — Visual direction: "Blackout" (dark, photographic, burgundy accent)
**Decided:** 19 Sep 2026, after reviewing three directions on the Design canvas.
**Why:** The plan asked for "mostly monochrome, large live photographs, restrained accent colour". Of the
three directions, Blackout let the photography and the distressed logo carry the attitude (the email's
"it should look like somebody in the band made a very good punk website") while keeping body text and
controls clean. Burgundy (#8f1a3a) nods to the existing site's purple without inheriting it; it is used
for the shows band, the header CTA and small underlines only.
**Alternatives:** B "Zine" (newsprint, red) — more personality but busier; C "Gallery" (white, serif) —
elegant but too polite for the band. Both removed from the canvas.

### D2 — Typography: Anton for display, IBM Plex Sans for body
**Why:** Anton is a heavy condensed grotesque that sits well next to the distressed wordmark without
imitating it. Plex Sans is neutral, readable at 17 px on dark ground and free. Both from Google Fonts,
loaded with `display=swap`. Fallbacks: Impact / Arial Narrow; system-ui.
**Rule:** two-sentence headlines break at the full stop with `<br>`; `text-wrap: balance` on headings,
`text-wrap: pretty` on paragraphs, so no orphan words.

### D3 — Positioning: current band first, history underneath
**Why:** From the 27 Aug notes. Every page orders content sound-now → doing-now → came-from. Previous
bands appear as a tag row at the bottom of About and inside member bios only.

### D4 — First names only for band members
**Decided:** review comment, 19 Sep. Bitzy, Bren, Andy everywhere on the site (page copy, structured data).
Surnames remain only inside the verbatim EPK bio text on the Press page where the EPK uses them? — **No:**
also first names there; the EPK PDF itself is untouched.

### D5 — Gig dates come from Eventbrite, never typed into the site
**Why:** The single most frequently-changing fact. A hand-typed date is how the old site ended up with
"Live @TGS 31st May 2026" in its navigation months later. The band already sells on Eventbrite.
**How:** `js/main.js` fetches `/api/events` → Netlify Function `netlify/functions/events.js` → Eventbrite
API (token stays server-side). Cached 10 min at the edge. Falls back to `data/events.json` if the function
is unavailable, so the page is never blank. Home shows up to 3; Live shows all.
**Rejected:** Eventbrite's embeddable widget (iframe, poor styling control, no empty state); calling the
API from the browser (would expose the private token).

### D6 — Static site on Netlify (or Cloudflare Pages), domain stays at GoDaddy
**Why:** GoDaddy Website Builder cannot host uploaded HTML (its "HTML section" is a fixed-height iframe).
GoDaddy cPanel hosting can, but costs ~$10/month renewing to serve five static pages and lacks serverless
functions for D5. Netlify's free tier gives hosting, SSL, CDN, redirects and functions. The band keeps
the domain and email exactly where they are; only two DNS records change.
**Consequence:** no visual editor for Dave. Mitigated by D5 (dates need no edits) and by keeping the HTML
plain and commented. The Website Builder subscription can be cancelled after launch.

### D7 — Plain HTML/CSS/JS, no framework, no build step
**Why:** Five pages, one maintainer, content changes a few times a year. A framework adds dependencies to
keep updated and a build to remember. `tools/gen_site.py` exists only to keep header/footer identical
across pages; the generated HTML is committed and can be edited directly if preferred (see DEVELOPMENT.md).

### D8 — Video and audio load only on click
**Why:** Performance and privacy (plan §4: no autoplay; privacy page promises no tracking by default).
The video block shows a still with a play button; clicking injects a `youtube-nocookie.com` iframe.
The Creatures player is a styled placeholder until the track is cleared, then a SoundCloud embed.

### D9 — Placeholders are visible, never invented
**Why:** Plan §3: keep unconfirmed dates, credentials and release claims out of published copy. Anything
not confirmed appears as `[credit]`, `[date]`, `[TBC]` so it is caught before launch (CONTENT.md lists all).

### D10 — Pretty URLs via folders (`/live/index.html`), root-relative links
**Why:** Works identically on Netlify, Cloudflare Pages, GitHub Pages and cPanel without host-specific
"pretty URL" settings. Consequence: the site must be served over HTTP, not opened from disk.

### D11 — Images: JPEG at 800 and 1600 px, `srcset`, lazy below the fold
**Why:** Several supplied photos are only 720–1024 px wide; upscaling would look bad, so 1600 is a cap not
a target. The press ZIP contains the originals at their supplied size and names the resolution problem in
CONTENT.md so originals can be requested from photographers.

### D12 — Creatures stays private
**Why:** The EPK's SoundCloud link is a private stream. The site links to "request from management" and
the player is disabled until the band clears public release. Do not paste the private URL into the site.

### D13 — Old URLs redirect (301) rather than 404
**Why:** Plan Phase 3: preserve useful URLs. Rules are in `netlify.toml`; the exact old slugs must be
checked against the live GoDaddy site before launch (LAUNCH-CHECKLIST.md §3).
