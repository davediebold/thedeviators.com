# Launch checklist

From "folder of files" to "live on thedeviators.com". Do the sections in order; each is short.

## 1. Content sign-off (band / Dave)
- [ ] Work through **CONTENT.md → Open items** 1–20; supply what you can, decide what ships as-is.
- [ ] Confirm the 1 Nov details one last time: Grand Social **Ballroom**, **doors 4.30pm**, **€15**, Amadán as special guests.
- [ ] Approve the About page story and the three member paragraphs (first names only).
- [ ] Approve which 8 photos are public and downloadable; confirm photographer permissions and credits.
- [ ] Decide whether the Aug 2026 EPK PDF can be public as-is, or needs the Dalymount line and private link removed first.

## 2. Put the content in (Zach)
- [ ] Set `YOUTUBE_LIVE_ID`, `SOCIAL` URLs in `tools/gen_site.py`; run `python3 tools/gen_site.py`.
- [ ] Replace `#` streaming links in the Home album panel.
- [ ] Fill photographer credits and venues in Media captions + Home hero credit.
- [ ] Add dates for the two past shows on Live; buy link for the book on About.
- [ ] Put the real Eventbrite ticket URL in `data/events.json` (fallback only, but keep it right).
- [ ] `grep -rn "\[" site/*.html site/*/index.html` — everything left in brackets is a conscious choice.

## 3. Redirect map (Zach)
- [ ] Open the live GoDaddy site and note every page URL (Home, Music, Meet the band, Gallery, Get in touch, the dated live page, anything under "More").
- [ ] Make `netlify.toml` `[[redirects]]` `from` paths match those slugs exactly.

## 4. Deploy to Netlify (Zach) — see DEVELOPMENT.md §6
- [ ] Create the site (drag-and-drop for a first look; Git-connected for the real thing).
- [ ] Add env vars `EVENTBRITE_TOKEN`, `EVENTBRITE_ORG_ID`; redeploy; open `/api/events` and confirm `"source":"eventbrite"` and the 1 Nov show.
- [ ] Send the `*.netlify.app` preview link to Dave and the band for a final look on phones.

## 5. Pre-flight checks on the preview URL
- [ ] Phone (≤ 390 px), tablet, desktop: no horizontal scroll, hero crop shows Bitzy, gig details readable, buttons full-width on phone.
- [ ] Keyboard: Tab through the header and shows list — visible focus ring everywhere; skip link works; menu opens/closes with Escape.
- [ ] Every link clicked once: nav, footer, tickets, streaming, socials, downloads (EPK, ZIP, stage plot), mailto and tel.
- [ ] Video: play button embeds YouTube (nocookie) and plays. Creatures player state matches decision (placeholder or public embed).
- [ ] Lighthouse (mobile): Performance ≥ 90, Accessibility ≥ 95, SEO ≥ 95.
- [ ] Share a page to WhatsApp/iMessage: the OG image (jumping shot) and title appear.
- [ ] `/this-does-not-exist` shows the 404 page. Old URLs from §3 redirect.
- [ ] Privacy page wording matches reality (no analytics unless added).

## 6. Switch the domain (Zach, with Dave's GoDaddy login) — see DEVELOPMENT.md §7
- [ ] In Netlify → Domain management → add `thedeviators.com` and `www.thedeviators.com`; note the A record / CNAME it asks for.
- [ ] In GoDaddy DNS: **screenshot the current records first.** Replace the A `@` and CNAME `www` records that point to Website Builder. Leave MX/TXT (email) alone.
- [ ] Wait for propagation (minutes to a few hours). Confirm https://thedeviators.com serves the new site with a valid certificate; `www` redirects to the bare domain (or vice-versa — pick one in Netlify).
- [ ] Only now: cancel or let lapse the GoDaddy **Websites + Marketing** plan. Keep the **domain** registration. Check auto-renew on the domain is ON.

## 7. After launch
- [ ] Update the link in the band's Facebook/Instagram/X bios and Eventbrite organiser profile.
- [ ] Submit `https://thedeviators.com/sitemap.xml` in Google Search Console (verify the domain via a DNS TXT record at GoDaddy).
- [ ] Put a reminder in the calendar: monthly link check; EPK refresh when the album drops (DEVELOPMENT.md §8).
- [ ] When *Tokyo* is released: artwork, release date, real streaming links, SoundCloud embed; consider making the Home quote the best new review.

## Rollback
If anything is wrong after the DNS switch, restore the GoDaddy A/CNAME records from the screenshot in §6 —
the old Website Builder site keeps existing until the plan is cancelled, so it comes back within minutes.
