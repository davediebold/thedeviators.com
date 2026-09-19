# The Deviators website and complete project backup

Website: https://thedeviators.com/

The entire project is tracked in this public repository, including original photographs, documents, notes, and the original build ZIP. Only `docs/` is published by GitHub Pages.

Agent instructions are in `AGENTS.md` at this folder's root: preview and test changes in the ChatGPT/Codex browser on localhost first, then commit and push only when the user asks to publish.

## Layout

- `docs/`: published HTML, CSS, JavaScript, optimized images, downloads, and events data.
- `tools/`: local preview server, daily Eventbrite importer, and importer tests.
- `.github/workflows/`: production deployment and daily event-refresh workflow.
- `source-assets/photos/`: original photos, artwork, and logos; photographer collections retain their names.
- `source-assets/documents/`: original EPK and stage-layout document.
- `project-notes/`: correspondence, launch details, asset provenance, and the current content checklist.
- `archive/`: historical build documentation, old generator and Netlify implementation, original ZIP, and initial planning.
- `AGENTS.md`: instructions for future agents; this README is the current project guide.

## Editing

Edit the published HTML, CSS, and JavaScript directly in `docs/`. These files are the source of truth; no build step is required. Shared navigation/footer changes must be applied to all relevant HTML pages and checked locally. The former generator is archived and must not be used to overwrite the current pages.

The `docs/` name is retained for the publishing folder; it is the website, not project documentation. Original assets are kept separately from optimized website images and public downloads. Keep both copies where appropriate: the originals are backups and the published copies serve the website.

## Publishing and backup

The active Pages workflow publishes only `/docs` from `main`. GitHub Pages is already configured to use GitHub Actions. Updates publish after an approved commit is pushed. Git does not automatically upload local edits: commit and push the reviewed changes when the user asks to publish.

```powershell
git add --all
git commit -m "Update website and project backup"
git push origin main
```

The site is configured for the custom domain `thedeviators.com`, already set in GitHub Pages. Links and metadata use that domain. The existing `docs/CNAME` is retained.

## Events and existing content

Upcoming shows use compact cards on the homepage and Live page. `tools/sync-eventbrite.cjs` reads the public organiser page at https://www.eventbrite.ie/o/120962217576 and saves just its event titles, venue-local dates and times, venues, images, prices, and ticket links in `docs/data/events.json`. It does not require credentials or access private account data.

The workflow refreshes once daily at 06:17 UTC, on deployment, and on manual runs. GitHub may delay scheduled jobs and may disable schedules in inactive public repositories after 60 days. Each successful snapshot is committed for backup and the site is deployed from the same run. A bot commit does not start another workflow. These event-only updates are automatic; other website edits still follow local review and explicit commit/push authorization.

This reads Eventbrite's public page data, not a guaranteed API contract. If the page structure changes, events cannot be loaded, or the list becomes paginated, the refresh fails instead of overwriting the last successful snapshot. The workflow deploys the saved data and then reports the refresh failure. Cards display their last checked date, and a direct organiser link always remains available. Tickets are purchased on Eventbrite, where availability is current.

Run `node tools/sync-eventbrite.cjs` to refresh locally, and `node --test tools/sync-eventbrite.test.cjs` to check the parser. The website filters out events once their local calendar day has passed.

The homepage uses SoundCloud's hosted player for Creatures Mix 5, with the private sharing token supplied by the owner. SoundCloud provides the audio and player details live. The track must remain available with embedding enabled; the supplied sharing link is visible in the website source when published.

The original Eventbrite server proxy is retained for backup but is not used. Netlify redirects and response headers do not apply on Pages.

Remaining content work is listed in `project-notes/CONTENT-CHECKLIST.md`. Archived checklists describe the original build and are not current deployment instructions.

## Preview

Run `node tools/preview.cjs` and open http://localhost:8000/ in the ChatGPT/Codex in-app browser. Test affected pages and interactions locally and leave the preview available for review. The older http://localhost:8000/thedeviators.com/ alias also works. Commit and push only when the user requests publication; pushing deploys to production. Opening HTML directly from disk will not resolve the site paths correctly.
