# The Deviators: project context and required workflow

This file applies to the entire `Deviators Website` project. Read `README.md` for implementation details. These instructions persist in the local folder and do not depend on the original conversation.

## Project

- Local folder: `C:\Users\edito\Desktop\Deviators Website`.
- Repository: `https://github.com/davediebold/thedeviators.com`, branch `main`.
- Production: `https://thedeviators.com/`, hosted by GitHub Pages using `.github/workflows/pages.yml`.
- Published files: `docs/`. Keep root-relative URLs such as `/css/style.css`; the production custom domain does not use a `/thedeviators.com/` prefix.
- Editing source of truth: the HTML, CSS, and JavaScript in `docs/`. Edit these files directly. There is no required build step.
- Original assets: `source-assets/`; source correspondence and provenance: `project-notes/`.
- Historical build, Netlify setup, planning, and ZIP: `archive/`. The old generator in `archive/site-build/tools/gen_site.py` is retained only as a reference; do not run it or maintain it alongside current HTML. Its old paths and deployment instructions are obsolete.

## Local review before deployment

When website changes are requested in this folder:

1. Check the working tree and remote state. Preserve user changes. Daily event refreshes may have added remote commits; reconcile them without overwriting local work or force-pushing.
2. Start `node tools/preview.cjs`, or reuse the existing server if it is serving this project. The preferred preview URL is `http://localhost:8000/`; the older `/thedeviators.com/` preview alias also works.
3. Open the localhost preview in the ChatGPT/Codex in-app browser. Make the requested changes and reload affected pages there. Do not substitute inspecting files or HTTP responses for browser testing.
4. Test the changed appearance and behavior in that browser: relevant links, images, controls, embeds, and desktop/mobile layouts as applicable. Check browser errors when relevant. Run focused code tests where needed; Eventbrite parser tests use `node --test tools/sync-eventbrite.test.cjs`. Report any testing limitation honestly.
5. Leave the local preview available and summarize what changed and what was tested. Suggest committing and pushing after the user's review. Do not commit, push, change production settings, or manually run a deployment without user authorization.
6. When the user says "push", "push live", "deploy", or otherwise explicitly approves publication, commit the reviewed changes and push to GitHub `main`. This is authorization to complete the deployment without asking again. Reconcile remote updates first and keep unrelated changes intact.
7. A push to `main` deploys production. Wait for the GitHub Actions run, resolve any failures within scope, verify the live site at `https://thedeviators.com/`, and report the result. Do not call deployment complete merely because Git accepted the push.

Keep all original project files, images, documents, and archives tracked for backup. Only `docs/` is served publicly as the website; the repository itself is also public.

## Existing integrations and automatic-update exception

The user approved automatic daily Eventbrite data refreshes. The active Pages workflow refreshes the public organiser listing at 06:17 UTC, commits `docs/data/events.json`, and deploys that snapshot. This does not authorize unrelated website edits. GitHub Pages is already configured to use GitHub Actions; no initial setup switch remains.

Eventbrite uses compact custom cards, not the full organiser-page iframe. SoundCloud uses the real hosted player supplied by the user. Preserve these choices unless the user requests a change. Failed Eventbrite refreshes retain the last successful snapshot and report failure.
