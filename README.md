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

GitHub Pages uses the `main` branch and `/docs` folder. Updates publish after a commit is pushed. Git does not automatically upload local edits: commit and push the whole project when changes are ready.

```powershell
git add --all
git commit -m "Update website and project backup"
git push origin main
```

The site is configured for the GitHub project URL above. No custom domain or DNS changes have been made. Links and metadata must be updated if a custom domain is configured later.

## Events and existing content

GitHub Pages serves static files, so upcoming shows read `docs/data/events.json` directly. Update that file and push to publish show changes. The original Eventbrite proxy is retained as source backup but does not run here. Netlify redirects and response headers also do not apply on Pages.

Existing content placeholders and unfinished social/ticket links are retained; see `site-build/docs/CONTENT.md` for the original content checklist.

## Preview

Run `node tools/preview.cjs` and open http://localhost:8000/thedeviators.com/. Review website changes locally before authorizing a commit and push; pushing deploys to production. Opening HTML directly from disk will not resolve the site paths correctly.
