# Website workflow

When website changes are requested in this folder:

1. Start the local preview with `node tools/preview.cjs` and open http://localhost:8000/thedeviators.com/ so the user can review the site.
2. Make the requested changes and check them in the local preview.
3. Suggest a commit and push after review. Do not commit and push website changes without user authorization.
4. Treat pushing to `main` as a production deployment: GitHub Pages automatically publishes `docs/` and updates the final website.

Keep all original project files, images, documents, and archives tracked for backup. Only `docs/` is served publicly as the website; the repository itself is also public.

The user approved automatic daily Eventbrite data refreshes. The Pages workflow may commit updated `docs/data/events.json` and deploy that snapshot daily; this does not authorize unrelated website edits. Before future local work, check for remote daily-refresh commits and reconcile them without overwriting local changes. The new workflow requires GitHub Pages source to be set to GitHub Actions when its first deployment is authorized.
