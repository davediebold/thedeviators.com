# Current content checklist

Checked against the website files on 19 September 2026. This replaces the archived build checklist for ongoing work. It records outstanding content; it is not permission to invent missing facts or publish changes.

## Already implemented

- GitHub Pages hosting and the `thedeviators.com` custom domain.
- Compact Eventbrite event cards with real ticket links and daily public-listing refreshes. No Eventbrite API token is required by the current implementation.
- Working SoundCloud player using the owner's supplied sharing link, plus SoundCloud profile links.
- Homepage live video embedded from the YouTube clip in the EPK.
- The same live video is linked from the Live and Press pages.
- Bitzy's book cover and owner-supplied Bandcamp purchase link on About.
- Tokyo SoundCloud player and direct track link on the homepage and Press page.
- Facebook and Instagram links in every footer.
- Public draft labels, TBC text, missing-credit brackets and empty links removed.
- Local browser review before an explicitly approved commit and push.

## Still needed

- Album links for Bandcamp, Spotify, Apple Music, and YouTube when available; empty homepage buttons have been removed.
- Photographer credits and the venue names for the unlabelled Media photos. The public placeholders have been removed. Sanda Semeika is credited for the original Annesley House collection; confirm which published photos are hers before applying that credit.
- Confirmed album release date and approved album artwork when available. Public TBC text has been removed.
- Exact Ferdia Mac Anna quote and its source, plus the source for The Goo quote. The incomplete quote and empty source link have been removed from the public site.
- Dates for the Rocky De Valera reunion and The Prongs show. Public date placeholders have been removed.
- Review the EPK PDF against current band information before replacing the public download. Preserve its original in `source-assets/documents/`.
- Better-resolution originals, a vector logo, a dedicated Bren portrait, and a new group press photo remain possible asset improvements from the original brief; confirm priorities with the user.
- Owner review of the privacy notice for the services actually used.

## Editing and verification

Edit the current pages in `docs/`, not archived templates. Update shared footer links on all seven HTML pages. Preserve originals in `source-assets/`; keep optimized public assets in `docs/img/` and `docs/downloads/`. Follow the root `AGENTS.md` for localhost browser checks, review, and production deployment.
