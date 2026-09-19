# thedeviators.com — website build

> Hosting update: the website has moved to `../docs/` for GitHub Pages. The repository-root README contains the current publishing instructions. The Netlify instructions below are preserved as original project documentation.

Complete, deployable redesign of **thedeviators.com** for The Deviators (Dublin three-piece).
Static HTML/CSS/JS, no framework, no build step required. Gigs are pulled live from Eventbrite.

Prepared 19 September 2026 from the Design canvas ("The Deviators — Website Design") and the
material in this folder (EPK, photos, logo, improvement plan, email notes).

## What's in this folder

```
site-build/
├── README.md                 ← you are here
├── site/                     ← THE WEBSITE. Deploy this folder as-is.
│   ├── index.html            Home
│   ├── live/index.html       Live (upcoming + past shows)
│   ├── about/index.html      About (band story, Bitzy / Bren / Andy)
│   ├── media/index.html      Media (photos, logo downloads)
│   ├── press/index.html      Press / EPK
│   ├── privacy/index.html    Privacy notice
│   ├── 404.html
│   ├── css/style.css         One stylesheet, design tokens at the top
│   ├── js/main.js            Mobile nav, Eventbrite feed, click-to-play video
│   ├── img/                  Optimised photos (800 + 1600 px), logo PNGs, OG image
│   ├── downloads/            EPK PDF, stage plot PDF, press-photo ZIP
│   ├── data/events.json      Fallback shows list (used if Eventbrite is unreachable / not configured)
│   ├── netlify/functions/events.js   Serverless proxy for the Eventbrite API
│   ├── netlify.toml          Redirects (old GoDaddy URLs), headers, function routing
│   ├── robots.txt · sitemap.xml · favicon.svg · apple-touch-icon.png
├── tools/gen_site.py         Page generator (shared head/nav/footer). Optional — see DEVELOPMENT.md
└── docs/
    ├── CONTEXT.md            Who the band are, where the content came from, positioning
    ├── REQUIREMENTS.md       What the site must do, page by page, plus non-functional requirements
    ├── DECISIONS.md          Design and technical decisions and why (ADR-style)
    ├── DEVELOPMENT.md        How to run, edit, deploy, wire Eventbrite, point the domain
    ├── CONTENT.md            Every piece of copy on the site + the open-items checklist
    └── LAUNCH-CHECKLIST.md   Step-by-step from "files in a folder" to "live on thedeviators.com"
```

## Quick start (5 minutes)

1. **Preview locally:** open a terminal in `site/` and run `python3 -m http.server 8000`, then visit
   http://localhost:8000. (Opening `index.html` directly from disk won't work because links are root-relative.)
2. **Deploy:** drag the `site/` folder onto https://app.netlify.com/drop — you get a live URL immediately.
3. **Turn on the Eventbrite feed:** in Netlify → Site settings → Environment variables, add
   `EVENTBRITE_TOKEN` and `EVENTBRITE_ORG_ID` (how to get them: docs/DEVELOPMENT.md §4), redeploy.
4. **Point the domain:** in GoDaddy DNS, follow docs/LAUNCH-CHECKLIST.md §5.

Until step 3 is done the site shows the show(s) listed in `site/data/events.json`, so it is never blank.

## Status

The site is **complete and deployable**, with a short list of content items that only the band can supply
(streaming links, photographer credits, album artwork, the Ferdia Mac Anna quote, social URLs, the YouTube
video id). Each one is marked `[…]` in the page copy and listed in **docs/CONTENT.md → Open items**.
Nothing false or invented is published: unconfirmed facts appear as visible placeholders.

## Who to contact

Site design and build: Zach (this project). Band / content approvals: Dave Diebold (management),
dave.diebold@gmail.com.
