# The Deviators website and complete project backup

Website: https://davediebold.github.io/thedeviators.com/

The entire project is tracked in this public repository, including original photographs, documents, notes, and the original build ZIP. Only `docs/` is published by GitHub Pages.

## Layout

- `docs/`: published HTML, CSS, JavaScript, optimized images, downloads, and events data.
- `site-build/tools/gen_site.py`: optional page generator, updated to write to `docs/`.
- `site-build/docs/`: original design, content, and development documentation.
- `site-build/netlify/` and `site-build/netlify.toml`: preserved original Netlify implementation; not used on GitHub Pages.
- Remaining root files and photo folders: original project assets and backup material.

## Publishing and backup

The Pages workflow publishes only `/docs` from `main`. Updates publish after an approved commit is pushed. Git does not automatically upload local edits: commit and push the whole project when changes are ready. To activate this new workflow on the first deployment, change Settings → Pages → Source from "Deploy from a branch" to "GitHub Actions".

```powershell
git add --all
git commit -m "Update website and project backup"
git push origin main
```

The site is configured for the GitHub project URL above. No custom domain or DNS changes have been made. Links and metadata must be updated if a custom domain is configured later.

## Events and existing content

Upcoming shows use compact cards on the homepage and Live page. `tools/sync-eventbrite.cjs` reads the public organiser page at https://www.eventbrite.ie/o/120962217576 and saves just its event titles, venue-local dates and times, venues, images, prices, and ticket links in `docs/data/events.json`. It does not require credentials or access private account data.

The workflow refreshes once daily at 06:17 UTC, on deployment, and on manual runs. GitHub may delay scheduled jobs and may disable schedules in inactive public repositories after 60 days. Each successful snapshot is committed for backup and the site is deployed from the same run. A bot commit does not start another workflow. These event-only updates are automatic; other website edits still follow local review and explicit commit/push authorization.

This reads Eventbrite's public page data, not a guaranteed API contract. If the page structure changes, events cannot be loaded, or the list becomes paginated, the refresh fails instead of overwriting the last successful snapshot. The workflow deploys the saved data and then reports the refresh failure. Cards display their last checked date, and a direct organiser link always remains available. Tickets are purchased on Eventbrite, where availability is current.

Run `node tools/sync-eventbrite.cjs` to refresh locally, and `node --test tools/sync-eventbrite.test.cjs` to check the parser. The website filters out events once their local calendar day has passed.

The homepage uses SoundCloud's hosted player for Creatures Mix 5, with the private sharing token supplied by the owner. SoundCloud provides the audio and player details live. The track must remain available with embedding enabled; the supplied sharing link is visible in the website source when published.

The original Eventbrite server proxy is retained for backup but is not used. Netlify redirects and response headers do not apply on Pages.

Existing content placeholders and unfinished social/ticket links are retained; see `site-build/docs/CONTENT.md` for the original content checklist.

## Preview

Run `node tools/preview.cjs` and open http://localhost:8000/thedeviators.com/. Review website changes locally before authorizing a commit and push; pushing deploys to production. Opening HTML directly from disk will not resolve the site paths correctly.
