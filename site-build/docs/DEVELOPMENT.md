# Development guide

Everything needed to run, change, deploy and maintain the site. Assumes basic comfort with a terminal;
no prior knowledge of the project.

## 1. Run it locally

The site uses root-relative links (`/css/style.css`, `/live/`), so it must be served, not opened from disk.

```bash
cd site
python3 -m http.server 8000        # or: npx serve .   or: php -S localhost:8000
# open http://localhost:8000
```

Locally there is no `/api/events`, so the shows list falls back to `site/data/events.json`. That is
expected. To test the real Eventbrite function locally, use the Netlify CLI:

```bash
npm i -g netlify-cli
cd site
netlify dev                        # serves site + functions on http://localhost:8888
# needs EVENTBRITE_TOKEN / EVENTBRITE_ORG_ID in a .env file in site/ (never commit it)
```

## 2. Project layout and where to change things

| You want to… | Edit |
|---|---|
| Change copy on one page | The page's `index.html` directly (`site/about/index.html` etc.). Or the same text in `tools/gen_site.py` and re-run it — **pick one approach for the project and stick to it** (see §3). |
| Change the header, footer, contact details, social links | `tools/gen_site.py` (constants at the top: `CONTACT_*`, `SOCIAL`, `YOUTUBE_LIVE_ID`), then run it. This is the one case where editing the HTML by hand means editing 7 files. |
| Change colours, fonts, spacing | `site/css/style.css` → section "1. Tokens" (`:root` variables). Everything derives from them. |
| Add or replace a photo | Export two JPEGs at 800 and 1600 px wide into `site/img/` as `name-800.jpg` and `name-1600.jpg`, then reference with the `img()` helper in `gen_site.py` or copy an existing `<img … srcset>` tag. Update the press ZIP in `site/downloads/` if it's a press photo. |
| Change how shows render | `site/js/main.js` → `renderShows()` and the `.show*` rules in CSS. |
| Change what the Eventbrite feed returns | `site/netlify/functions/events.js`. |
| Add a page | Copy `site/privacy/index.html` as a template (or add a block in `gen_site.py`), add it to `sitemap.xml`, add a nav link in `gen_site.py → nav()`. |

### CSS conventions
- One file, ordered: tokens → base → layout primitives (`.wrap`, `.grid`, `.col-*`, `.section*`) →
  components (`.btn`, `.frame`, `.video`, `.quote`, …) → page blocks → utilities.
- 12-column grid on desktop; every `.col-*` collapses to full width under 900 px. Use `push-*` classes
  for offset columns (`.col-6.push-6` = columns 7–12).
- Sizes use `clamp()` so type and spacing scale between phone and 1440 px without breakpoints.
- Touch targets ≥ 44 px, contrast ≥ 4.5:1: `--muted` (#b8b3ab) is the lightest allowed body colour on
  `--bg`; on the burgundy band use `--accent-tint`.

### HTML conventions
- Semantic sections with `aria-labelledby`; one `<h1>` per page (Home's is visually hidden behind the logo).
- Real `<a href>`/`<button>` for every control. Icon-only controls have `aria-label`.
- External links: `target="_blank" rel="noopener"`.
- Placeholders for content the band must supply are written `[credit]`, `[date]`, `[TBC]` — grep for `\[` before launch.

## 3. The generator (`tools/gen_site.py`)

`python3 tools/gen_site.py` regenerates all seven HTML files into `site/`. It exists so the header,
footer and `<head>` stay identical everywhere. Two workable approaches — choose one:

- **Generator is the source of truth (recommended while the site is young).** Edit copy in `gen_site.py`,
  run it, commit both. Never hand-edit `site/**/index.html`.
- **HTML is the source of truth.** Delete `tools/` and edit pages directly. Simpler for one-off text
  fixes; header/footer changes then need doing in every file.

The generator has no dependencies beyond Python 3.8+.

## 4. Eventbrite feed

### How it works
```
browser  ──GET /api/events──▶  Netlify Function (events.js)  ──▶  Eventbrite API v3
   ▲                              │  adds Bearer token, trims fields, caches 10 min
   └──── falls back to /data/events.json if the function 5xx's or is missing
```
The function returns `{ events: [ { title, start_local, venue_name, city, price, image, url, sold_out } ] }`.
`main.js` also understands a raw Eventbrite response, so the function can be swapped for another proxy.

### One-time setup
1. Log in to Eventbrite as the organiser → https://www.eventbrite.com/platform/api-keys → **Create API key**
   → copy the **Private token**.
2. Find the organisation id: `curl -H "Authorization: Bearer TOKEN" https://www.eventbriteapi.com/v3/users/me/organizations/`
   → use `organizations[0].id`.
3. Netlify → Site → **Site configuration → Environment variables** → add `EVENTBRITE_TOKEN` and
   `EVENTBRITE_ORG_ID` → **Deploy → Trigger deploy**.
4. Check `https://<your-site>/api/events` returns JSON with `"source":"eventbrite"`.

### Behaviour
- Shows `status=live` events, soonest first; Home shows 3, Live shows all (`data-limit` attribute).
- Events disappear 6 hours after their start time.
- Empty state: "No shows announced right now — book the band…".
- Price comes from Eventbrite's minimum ticket price; "Doors" text comes from `doors` in `events.json`
  only (Eventbrite has no doors field — put "Doors 4.30pm" in the event's title or summary if it matters).

### Not using Eventbrite?
Point `data-events-endpoint` on `<body>` (set in `gen_site.py → head()`) at `/data/events.json` and
edit that file by hand. Same shape as the function output. Dates are local Dublin time, ISO format.

### Cloudflare Pages instead of Netlify
Move `netlify/functions/events.js` to `functions/api/events.js`, change `exports.handler` to
`export async function onRequest(context)` reading `context.env.EVENTBRITE_TOKEN`, and return a
`Response`. Redirects move from `netlify.toml` to a `_redirects` file; headers to `_headers`. Everything else is unchanged.

## 5. Media embeds

- **Live video:** set `YOUTUBE_LIVE_ID` in `gen_site.py` (the 11-character id from the YouTube URL in the
  EPK) and regenerate. Until set, the play button links to `#`.
- **Creatures (SoundCloud):** once cleared for public release, replace the `.player` placeholder in
  `index.html` with the commented-out embed just above it, using the **public** track URL.
- **Album artwork:** replace the `.placeholder` box in the album panel with an `<img>` (800 + 1600 px).

## 6. Deploy

### Netlify (recommended)
- **Drag-and-drop:** https://app.netlify.com/drop → drop the `site/` folder. Good for a first preview.
- **Git-connected (better for ongoing edits):** push this folder to a GitHub repo; Netlify → Add new site
  → Import → set *Base directory* `site`, *Publish directory* `site`, *Functions directory*
  `site/netlify/functions`. Every push deploys. `netlify.toml` already declares these.
- Site name: e.g. `thedeviators.netlify.app`; add custom domain `thedeviators.com` + `www` in Domain settings.

### Anything else (cPanel, GitHub Pages, S3…)
Upload the contents of `site/` to the web root. You lose the function → the shows list uses
`data/events.json`; edit that file when dates change, or set up the Cloudflare variant above.

## 7. Domain (GoDaddy) → Netlify

In GoDaddy → My Products → thedeviators.com → **DNS**:

| Type | Name | Value |
|---|---|---|
| A | `@` | `75.2.60.5` (Netlify's load balancer — confirm the current value in Netlify's domain panel) |
| CNAME | `www` | `<your-site>.netlify.app` |

Delete or replace the existing A/CNAME records that point at Website Builder. **Do not touch MX or TXT
records** — those are email. Netlify then provisions SSL automatically (allow up to an hour).
Alternative: move nameservers to Netlify DNS — simpler long-term, but only if GoDaddy isn't also serving
email via records you'd need to recreate.

## 8. Routine maintenance

| When | Do |
|---|---|
| A new gig is booked | Publish it on Eventbrite. Nothing to do on the site. |
| A gig is over | Nothing — it drops off automatically. Optionally add it to *Selected past shows* on Live (edit HTML). |
| Album release | Add artwork, release date, real streaming links in the Home album panel; update Press quick facts and `data/`. |
| New photos | Add 800/1600 px versions to `img/`, a tile on Media, refresh the press ZIP. |
| New press quote | Add to Press quotes and consider swapping the Home quote. |
| EPK revised | Replace `downloads/The_Deviators_EPK_<date>.pdf`, update the two links and the "Revised …" text. |
| Monthly | Click every external link; check `/api/events` still returns `source: eventbrite` (tokens can be revoked). |

## 9. Checks before any deploy

```bash
# 1. Regenerate (if using the generator)
python3 tools/gen_site.py
# 2. Serve and eyeball at 390 px and 1440 px
cd site && python3 -m http.server 8000
# 3. No horizontal scroll on any page at 390 px; no [placeholder] text you didn't mean to ship
grep -rn "\[" site/*.html site/*/index.html | grep -v "\[\[" 
# 4. Validate HTML (optional)  https://validator.w3.org/nu/   and Lighthouse in Chrome DevTools
```
Targets: Lighthouse Performance ≥ 90 on mobile, Accessibility ≥ 95, no console errors.
