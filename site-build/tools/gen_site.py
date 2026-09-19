#!/usr/bin/env python3
"""Generates the static pages for thedeviators.com.

Run:  python3 tools/gen_site.py   (from the site-build folder)
Edits to copy go in this file OR directly in the generated HTML — pick one and
stick to it (docs/DEVELOPMENT.md). Shared chrome (head, nav, footer) lives here
so it stays identical across pages.
"""
import os, datetime, re

SITE = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'docs')
BASE = 'https://davediebold.github.io/thedeviators.com'
BASE_PATH = '/thedeviators.com'
YEAR = datetime.date.today().year

# ---------- Shared content ----------
CONTACT_NAME = 'Dave Diebold'
CONTACT_EMAIL = 'dave.diebold@gmail.com'
CONTACT_TEL_DISPLAY = '087 997 3953'
CONTACT_TEL_HREF = 'tel:+353879973953'
SOCIAL = [  # TODO(launch): replace # with real profile URLs
    ('Facebook', '#'), ('Instagram', '#'), ('X · @tDeviators', 'https://x.com/tDeviators'), ('SoundCloud', '#'),
]
YOUTUBE_LIVE_ID = ''  # TODO(launch): YouTube video id of "Live at The Grand Social" (from EPK link)

PLAY = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>'
DOWNLOAD = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3v12"/><path d="m7 10 5 5 5-5"/><path d="M4 21h16"/></svg>'
REFRESH = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 12a9 9 0 1 1-3-6.7"/><path d="M21 3v6h-6"/></svg>'

def img(name, alt, sizes='100vw', cls='', style='', loading='lazy'):
    return (f'<img src="/img/{name}-1600.jpg" srcset="/img/{name}-800.jpg 800w, /img/{name}-1600.jpg 1600w" '
            f'sizes="{sizes}" alt="{alt}" loading="{loading}" decoding="async"'
            + (f' class="{cls}"' if cls else '') + (f' style="{style}"' if style else '') + '>')

def head(title, desc, path, og_type='website'):
    full = 'The Deviators' if path == '/' else f'{title} — The Deviators'
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}{path}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="The Deviators">
<meta property="og:title" content="{full}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{BASE}{path}">
<meta property="og:image" content="{BASE}/img/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@tDeviators">
<meta name="theme-color" content="#0d0d0d">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"MusicGroup","name":"The Deviators","url":"{BASE}/","genre":["Punk","Rock"],"foundingLocation":{{"@type":"Place","name":"Dublin, Ireland"}},"logo":"{BASE}/img/logo-white.png","image":"{BASE}/img/og-image.jpg","member":[{{"@type":"Person","name":"Bitzy"}},{{"@type":"Person","name":"Bren"}},{{"@type":"Person","name":"Andy"}}],"sameAs":["https://x.com/tDeviators"]}}
</script>
</head>
<body data-events-endpoint="/api/events" data-events-fallback="/data/events.json">
<a class="skip-link" href="#main">Skip to content</a>
'''

def nav(active):
    items = [('Live', '/live/', 'live'), ('About', '/about/', 'about'), ('Media', '/media/', 'media'), ('Press / EPK', '/press/', 'press')]
    CUR = ' aria-current="page"'
    links = ''.join(f'<a href="{h}"{CUR if k == active else ""}>{l}</a>' for l, h, k in items)
    return f'''<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/" aria-label="The Deviators — home"><img src="/img/logo-white.png" alt="The Deviators" width="623" height="149"></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Menu">
      <svg class="icon-menu" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
      <svg class="icon-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>
    </button>
    <nav class="nav" id="site-nav" aria-label="Main">
      {links}
      <a class="btn btn--accent" href="#book">Book the band</a>
    </nav>
  </div>
</header>
<main id="main">
'''

EXT = ' target="_blank" rel="noopener"'

def footer():
    press = [('Download EPK (PDF)', '/downloads/The_Deviators_EPK_2026-08.pdf'), ('Hi-res press photos &amp; logo', '/media/'), ('Band bio', '/press/#bio'), ('Stage plot &amp; tech spec', '/press/#assets')]
    return f'''</main>
<footer class="site-footer" id="book">
  <div class="wrap">
    <div class="grid">
      <div class="col-6 stack stack--sm contact">
        <h2>Book the band</h2>
        <p class="soft">Bookings / Management: {CONTACT_NAME}</p>
        <a class="email" href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>
        <a class="tel" href="{CONTACT_TEL_HREF}">{CONTACT_TEL_DISPLAY}</a>
      </div>
      <div class="col-3 links">
        <div class="label">Press</div>
        {''.join(f'<a href="{h}">{l}</a>' for l, h in press)}
      </div>
      <div class="col-3 links">
        <div class="label">Follow</div>
        {''.join(f'<a href="{h}"{EXT if h.startswith("http") else ""}>{l}</a>' for l, h in SOCIAL)}
      </div>
    </div>
    <div class="legal">
      <div class="left"><img src="/img/logo-white.png" alt="" width="623" height="149"><span>© {YEAR} The Deviators · Dublin, Ireland</span></div>
      <div class="right"><a href="/privacy/">Privacy</a></div>
    </div>
  </div>
</footer>
<script src="/js/main.js" defer></script>
</body>
</html>
'''

def write(path, html):
    full = os.path.join(SITE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    html = html.replace('/api/events', '/data/events.json')
    html = re.sub(r'''(?<=["'])/(?!/)''', BASE_PATH + '/', html)
    html = html.replace(', /img/', ', ' + BASE_PATH + '/img/')
    with open(full, 'w', encoding='utf-8') as f:
        f.write(html)
    print('wrote', path)

def shows_block(limit, heading='Upcoming shows', foot=True, note=''):
    return f'''<section class="section section--accent" id="live" aria-labelledby="shows-h">
  <div class="wrap">
    <div class="shows__head">
      <h2 id="shows-h">{heading}</h2>
      <div class="shows__source">{REFRESH}<span>Live from Eventbrite · updates automatically</span></div>
    </div>
    <div class="shows__list" data-shows data-limit="{limit}" aria-live="polite">
      <div class="shows__empty">Loading shows…</div>
    </div>
    {note}
    {'<div class="shows__foot"><a class="link-u" href="/live/">All dates &amp; past shows →</a></div>' if foot else ''}
  </div>
</section>
'''

VIDEO = lambda cls='': f'''<div class="video {cls}" data-youtube="{YOUTUBE_LIVE_ID}">
  {img('hero-pub', 'Bitzy playing guitar standing on a pub table in front of a packed crowd', '(max-width: 900px) 100vw, 60vw', style='object-position: 50% 25%')}
  <a class="video__play" href="{('https://www.youtube.com/watch?v=' + YOUTUBE_LIVE_ID) if YOUTUBE_LIVE_ID else '#'}" aria-label="Play: The Deviators live at The Grand Social">{PLAY}</a>
  <div class="video__caption"><span class="label">Watch</span><strong>Live at The Grand Social</strong></div>
</div>'''

# =====================================================================
# HOME
# =====================================================================
home = head('Home', 'The Deviators — Dublin three-piece. Original high-energy punk, pop and rock ’n’ roll. Next show, new single Tokyo, debut album More Volume, Less Reverb.', '/')
home += nav('home')
home += f'''
<section class="hero" aria-label="Introduction">
  {img('jump', 'Bitzy mid-air with his guitar at The Grand Social, Bren on bass and Andy on drums under the distressed Deviators backdrop', '100vw', cls='hero__img', loading='eager')}
  <div class="hero__shade" aria-hidden="true"></div>
  <div class="wrap">
    <h1 class="visually-hidden">The Deviators</h1>
    <img class="hero__logo" src="/img/logo-white.png" alt="" width="623" height="149" aria-hidden="true">
    <p class="hero__tag">Dublin three-piece.<br>Original high-energy punk, pop and rock ’n’ roll.</p>
    <div class="hero__actions">
      <a class="btn btn--primary" href="#listen">{PLAY}Listen to Creatures</a>
      <a class="btn btn--ghost" href="#watch">Watch live</a>
      <span class="hero__credit">The Grand Social, Dublin · Photo: [credit]</span>
    </div>
  </div>
</section>

{shows_block(limit=3)}

<section class="section" id="listen" aria-labelledby="listen-h">
  <div class="wrap grid">
    <div class="col-7 stack">
      <span class="label">Listen</span>
      <h2 id="listen-h">Creatures</h2>
      <!-- When Creatures is cleared for public release, replace this block with the SoundCloud embed:
           <div class="player player--embed"><iframe title="The Deviators — Creatures" src="https://w.soundcloud.com/player/?url=TRACK_URL&color=%238f1a3a&auto_play=false&show_user=false" loading="lazy"></iframe></div> -->
      <div class="player" aria-label="Creatures — player placeholder">
        <button class="player__play" type="button" aria-label="Play Creatures (not yet public)" disabled>{PLAY}</button>
        <div class="player__body">
          <div class="player__title"><span><strong>The Deviators — Creatures</strong></span><span class="muted">SoundCloud</span></div>
          <div class="player__wave" aria-hidden="true"></div>
          <div class="player__time"><span>0:00</span><span>[duration]</span></div>
        </div>
      </div>
      <p class="muted" style="font-size:14px">Public stream goes live with the single. Promoters and press: request the private link from management.</p>
    </div>
    <div class="col-5 panel" id="album">
      <div class="stack stack--sm">
        <span class="label">Debut album · Produced by Stano</span>
        <h2 style="font-size:clamp(40px,4.4vw,64px)">More Volume,<br>Less Reverb</h2>
        <p class="soft">First single <em>Tokyo</em> launches at The Grand Social on 1 November. Artwork, track listing and release date to follow.</p>
      </div>
      <div class="pills">
        <a href="#" rel="noopener">Bandcamp</a><a href="#" rel="noopener">Spotify</a><a href="#" rel="noopener">Apple Music</a><a href="#" rel="noopener">YouTube</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight" id="watch" aria-labelledby="watch-h">
  <div class="wrap grid">
    <div class="col-7">
      <h2 id="watch-h" class="visually-hidden">Watch</h2>
      {VIDEO()}
    </div>
    <div class="col-5 stack" style="justify-content:space-between">
      <div class="quote quote--rule">
        <blockquote>“Terrific gig by both the Devs and the DeValeras.”</blockquote>
        <span class="label">— Colm O’Hare, music journalist</span>
      </div>
      <div class="stack stack--sm">
        <span class="label">Selected past shows</span>
        <div class="pastlist">
          <div><span>Special guests to Rocky De Valera &amp; the Gravediggers (sold out)</span><span>The Grand Social</span></div>
          <div><span>With The Prongs</span><span>Annesley House</span></div>
          <div><span>Grand Social debut, with Tony St Ledger · 31 May 2026</span><span>The Grand Social</span></div>
        </div>
        <a class="link-u" href="/live/">All dates →</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--rule" id="about" aria-labelledby="band-h">
  <div class="wrap grid" style="align-items:center">
    <div class="col-5 frame frame--4x3">{img('rehearsal', 'The Deviators in rehearsal: Bren on bass, Andy on drums, Bitzy on guitar', '(max-width: 900px) 100vw, 40vw')}</div>
    <div class="col-6 push-6 stack">
      <span class="label">The band</span>
      <h2 id="band-h" style="font-size:clamp(36px,3.9vw,56px)">New songs.<br>Played like the room depends on it.</h2>
      <p class="soft">Three Dublin musicians making new original material together: short, melodic, high-energy punk and guitar pop. Their histories run back through the city’s punk scene — The Strougers, The End, The Lee Harveys, Trouble Pilgrims, Clash Jam Wallop and more — but The Deviators aren’t interested in recreating any of it.</p>
      <div class="row soft" style="font-size:15px">
        <span><strong style="color:var(--fg)">Bitzy</strong> · guitar, vocals</span>
        <span><strong style="color:var(--fg)">Bren</strong> · bass, vocals</span>
        <span><strong style="color:var(--fg)">Andy</strong> · drums, vocals</span>
      </div>
      <a class="link-u" href="/about/">Meet the band →</a>
    </div>
  </div>
</section>

<section class="section section--alt" aria-label="Press quote">
  <div class="wrap quote quote--big">
    <blockquote>“The songs were riotous and the crowd ate up every second of it.”</blockquote>
    <span class="label">— The Goo</span>
  </div>
</section>
'''
home += footer()
write('index.html', home)

# =====================================================================
# LIVE
# =====================================================================
live = head('Live', 'Upcoming shows and selected past gigs from The Deviators, Dublin. Tickets via Eventbrite.', '/live/')
live += nav('live')
live += f'''
<section class="page-head">
  <div class="wrap grid">
    <div class="col-6 stack stack--sm"><span class="label">Live</span><h1>Shows</h1></div>
    <div class="col-5 push-7 quote quote--rule">
      <blockquote>“Terrific gig by both the Devs and the DeValeras.”</blockquote>
      <span class="label">— Colm O’Hare, music journalist</span>
    </div>
  </div>
</section>

{shows_block(limit=0, heading='Upcoming', foot=False)}

<section class="section" aria-labelledby="live-video-h">
  <div class="wrap grid" style="align-items:center">
    <div class="col-8">
      <h2 id="live-video-h" class="visually-hidden">Live video</h2>
      <div class="video" data-youtube="{YOUTUBE_LIVE_ID}">
        {img('jump', 'Bitzy mid-air with his guitar at The Grand Social', '(max-width: 900px) 100vw, 66vw', style='object-position: 50% 30%')}
        <a class="video__play" href="{('https://www.youtube.com/watch?v=' + YOUTUBE_LIVE_ID) if YOUTUBE_LIVE_ID else '#'}" aria-label="Play: Live at The Grand Social">{PLAY}</a>
        <div class="video__caption"><span class="label">Watch</span><strong>Live at The Grand Social</strong></div>
      </div>
    </div>
    <div class="col-4 stack">
      <span class="label">What to expect</span>
      <h2 style="font-size:clamp(34px,3.3vw,48px)">Forty minutes.<br>No ballads.</h2>
      <p class="soft">Short, melodic, high-energy songs played with the urgency of people who know exactly what a live room needs. Three-piece, own backdrop, in-ear monitoring — stage plot and tech spec on the Press page.</p>
      <a class="link-u" href="/press/#assets">Stage plot &amp; tech spec →</a>
    </div>
  </div>
</section>

<section class="section section--rule" aria-labelledby="past-h">
  <div class="wrap stack" style="gap:28px">
    <div class="shows__head" style="margin:0"><h2 id="past-h" style="font-size:clamp(36px,3.9vw,56px)">Selected past shows</h2><span class="muted" style="font-size:14px">A short list, not a gig diary</span></div>
    <div class="cards">
      <article class="card">
        <div class="frame frame--16x9">{img('stage', 'Bitzy and Bren on stage at The Grand Social', '(max-width: 900px) 100vw, 33vw', style='object-position: 50% 30%')}</div>
        <div class="card__title">Special guests to Rocky De Valera &amp; the Gravediggers</div>
        <div class="card__meta">Sold-out reunion · The Grand Social, Dublin · [date]</div>
      </article>
      <article class="card">
        <div class="frame frame--16x9">{img('hero-pub', 'Bitzy playing on a pub table in front of the crowd', '(max-width: 900px) 100vw, 33vw', style='object-position: 50% 30%')}</div>
        <div class="card__title">With The Prongs</div>
        <div class="card__meta">Annesley House, Dublin · [date]</div>
      </article>
      <article class="card">
        <div class="frame frame--16x9">{img('may31-poster', 'Poster: The Deviators + Tony St Ledger, Grand Social Ballroom, May 31st', '(max-width: 900px) 100vw, 33vw', style='object-position: 50% 15%')}</div>
        <div class="card__title">Grand Social debut, with Tony St Ledger</div>
        <div class="card__meta">The Grand Social Ballroom, Dublin · 31 May 2026</div>
      </article>
    </div>
  </div>
</section>
'''
live += footer()
write('live/index.html', live)

# =====================================================================
# ABOUT
# =====================================================================
def member(name, role, image, pos, bio, extra='', flip=False):
    pic = f'<div class="col-5{" push-7" if flip else ""} frame">{img(image, name, "(max-width: 900px) 100vw, 40vw", style=f"object-position: {pos}")}</div>'
    txt = f'''<div class="col-6{"" if flip else " push-6"} stack stack--sm">
      <span class="label">{role}</span>
      <h2 style="font-size:clamp(36px,3.9vw,56px)">{name}</h2>
      <p class="soft">{bio}</p>{extra}
    </div>'''
    inner = (txt + pic) if flip else (pic + txt)
    return f'<section class="member" id="{name.lower()}"><div class="wrap grid">{inner}</div></section>\n'

about = head('About', 'Who The Deviators are: Bitzy, Bren and Andy — three Dublin musicians with decades in the city’s punk scene, making new songs together.', '/about/')
about += nav('about')
about += f'''
<section class="section" aria-labelledby="about-h">
  <div class="wrap grid" style="align-items:end">
    <div class="col-7 stack">
      <span class="label">About</span>
      <h1 id="about-h" style="font-size:clamp(48px,6.6vw,96px)">Three Dublin musicians.<br>New songs.</h1>
      <p class="lede soft">The Deviators are Bitzy, Bren and Andy: three Dublin musicians with histories stretching back through the city’s punk scene, now making new original material together. The songs are short, melodic and high-energy — punk and guitar pop played with the urgency that comes from knowing exactly what a live room needs.</p>
      <p class="lede soft">Their first album, <em>More Volume, Less Reverb</em>, produced by Stano, is nearly ready. There is plenty of history in the band, but they are not interested in recreating it.</p>
    </div>
    <div class="col-4 push-8 frame frame--3x4">{img('selfie', 'Bitzy, Andy and Bren grinning in a backstage selfie', '(max-width: 900px) 100vw, 33vw')}</div>
  </div>
</section>
'''
about += member('Bitzy', 'Guitar · vocals', 'bitzy-blue', '50% 20%',
  'Started in 1976 with The Slum and was fronting The Strougers by 1978. Baby Goes Boom followed, then a long break from music. Returned in 2009 with The Lee Harveys and spent 15 years with the band until their 2024 break; a brief spell with The Last Pop Stars came before The Deviators.',
  '''<div class="book-card"><div class="book-card__cover" aria-hidden="true"></div><div><strong>Past the Point of Rescue</strong><small>Bitzy’s punk memoir, now on its third reprint · <a href="#">Buy the book</a></small></div></div>''')
about += member('Bren', 'Bass · vocals', 'stage', '85% 40%',
  'Started playing bass with The End in 1979 and later played alongside Andy in The Cathedral. In 2014 he teamed up with former The End drummer Johnny Bonnie in Trouble Pilgrims, the band that rose from the ashes of The Radiators From Space.', flip=True)
about += member('Andy', 'Drums · vocals', 'rehearsal', '45% 25%',
  'Started his first band, Slit Possex, at 14. The Cathedral followed in the early 1980s, then Cabra bands Purdah, Primatevo and Lure through the ’90s. Inspired by the loss of Joe Strummer, Clash Jam Wallop was born and Andy spent 16 years with them. Complete Control followed, then three years with The Modfathers before The Deviators.')
tags = ['The Slum','The Strougers','Baby Goes Boom','The End','The Cathedral','Purdah','Primatevo','Lure','The Lee Harveys','Trouble Pilgrims','Clash Jam Wallop','Complete Control','The Modfathers','The Last Pop Stars']
about += f'''
<section class="section section--alt" aria-labelledby="from-h">
  <div class="wrap stack stack--sm">
    <span class="label" id="from-h">Where they’ve come from</span>
    <div class="tags">{''.join(f'<span>{t}</span>' for t in tags)}</div>
  </div>
</section>
'''
about += footer()
write('about/index.html', about)

# =====================================================================
# MEDIA
# =====================================================================
def tile(image, alt, cap, cls, pos='50% 40%'):
    return f'''<figure class="tile {cls}">
      {img(image, alt, '(max-width: 520px) 100vw, (max-width: 900px) 50vw, 60vw', style=f'object-position: {pos}')}
      <figcaption class="tile__bar"><span>{cap}</span><a class="tile__dl" href="/img/{image}-1600.jpg" download aria-label="Download {cap}">{DOWNLOAD}</a></figcaption>
    </figure>'''

media = head('Media', 'Live and press photography of The Deviators, plus logo files, for promoters and journalists.', '/media/')
media += nav('media')
media += f'''
<section class="page-head">
  <div class="wrap grid">
    <div class="col-6 stack stack--sm"><span class="label">Media</span><h1>Photos</h1></div>
    <div class="col-5 push-7 stack">
      <p class="soft">Live and press photography for promoters and journalists. Credit the photographer where named.</p>
      <div class="row">
        <a class="btn btn--primary" href="/downloads/deviators-press-photos.zip">{DOWNLOAD}Download hi-res press photos</a>
        <a class="btn btn--ghost" href="#logo">Logo files</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight" aria-label="Photo gallery">
  <div class="wrap gallery">
    {tile('jump', 'Bitzy mid-air at The Grand Social', 'Live · The Grand Social · Photo: [credit]', 'tile--8', '50% 30%')}
    {tile('hero-pub', 'Bitzy on a pub table in front of the crowd', 'Live · [venue] · Photo: [credit]', 'tile--4', '50% 25%')}
    {tile('wall', 'Band against a brick wall with the painted logo', 'Press · trio · Photo: [credit]', 'tile--4s', '50% 45%')}
    {tile('stage', 'Bitzy and Bren on stage', 'Live · The Grand Social · Photo: [credit]', 'tile--4s', '50% 30%')}
    {tile('amber', 'Andy and Bren under amber light', 'Live · [venue] · Photo: [credit]', 'tile--4s', '50% 35%')}
    {tile('rehearsal', 'The band in rehearsal', 'Rehearsal · Photo: [credit]', 'tile--5', '50% 45%')}
    {tile('bitzy-blue', 'Bitzy singing at the mic', 'Live · [venue] · Photo: [credit]', 'tile--3', '50% 20%')}
    {tile('selfie', 'Backstage selfie', 'Backstage · self-portrait', 'tile--4s', '50% 50%')}
  </div>
</section>

<section class="section section--rule" id="logo" aria-labelledby="logo-h">
  <div class="wrap grid" style="align-items:center">
    <div class="col-4 stack stack--sm">
      <span class="label">Logo</span>
      <h2 id="logo-h" style="font-size:clamp(34px,3.3vw,48px)">Wordmark files</h2>
      <p class="soft">Light and dark versions. Use on plain backgrounds; don’t recolour or stretch.</p>
    </div>
    <div class="col-4 logo-tile logo-tile--light"><img src="/img/logo-dark.png" alt="The Deviators wordmark, dark on light" width="623" height="149"><a href="/img/logo-dark.png" download>Download dark PNG</a></div>
    <div class="col-4 logo-tile logo-tile--dark"><img src="/img/logo-white.png" alt="The Deviators wordmark, light on dark" width="623" height="149"><a href="/img/logo-white.png" download>Download light PNG</a></div>
  </div>
</section>
'''
media += footer()
write('media/index.html', media)

# =====================================================================
# PRESS / EPK
# =====================================================================
def fact(k, v):
    return f'<div><span class="label">{k}</span><span style="font-size:17px;line-height:1.4">{v}</span></div>'

press = head('Press / EPK', 'Electronic press kit for The Deviators: bio, quotes, music, live video, photos, logo, stage plot and management contact.', '/press/')
press += nav('press')
press += f'''
<section class="page-head">
  <div class="wrap grid">
    <div class="col-6 stack stack--sm"><span class="label">Press / EPK</span><h1>Press kit</h1></div>
    <div class="col-5 push-7 stack">
      <p class="soft">Everything a promoter or journalist needs on one page. Revised August 2026.</p>
      <div class="row">
        <a class="btn btn--primary" href="/downloads/The_Deviators_EPK_2026-08.pdf">{DOWNLOAD}Download EPK (PDF)</a>
        <a class="btn btn--ghost" href="mailto:{CONTACT_EMAIL}">Contact management</a>
      </div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="pitch-h">
  <div class="wrap grid">
    <div class="col-7 stack stack--sm">
      <span class="label">The pitch</span>
      <h2 id="pitch-h" style="font-size:clamp(36px,3.9vw,56px)">Dublin three-piece.<br>Original high-energy punk, pop and rock ’n’ roll.</h2>
      <p class="soft">New songs, decades of Dublin stage time, and a debut album produced by Stano on the way. Recent shows include a special-guest slot at Rocky De Valera &amp; the Gravediggers’ sold-out Grand Social reunion.</p>
    </div>
    <div class="col-4 push-8 facts">
      {fact('Hometown', 'Dublin, Ireland')}
      {fact('Line-up', 'Bitzy (guitar/vocals) · Bren (bass/vocals) · Andy (drums/vocals)')}
      {fact('Debut album', '<em>More Volume, Less Reverb</em> · produced by Stano · release [TBC]')}
      {fact('Management', f'{CONTACT_NAME}<br>{CONTACT_EMAIL}<br>{CONTACT_TEL_DISPLAY}')}
    </div>
  </div>
</section>

<section class="section section--tight" id="bio" aria-labelledby="bio-h">
  <div class="wrap grid">
    <div class="col-5 stack stack--sm">
      <span class="label" id="bio-h">The band</span>
      <p class="soft">The Deviators came together recently, but the three of them have been around Dublin music for decades. Between Bitzy, Bren and Andy, the trail runs through The Strougers, The End, The Cathedral, The Lee Harveys, Trouble Pilgrims, Clash Jam Wallop, The Modfathers and a fair few other bands along the way.</p>
      <p class="soft">The songs are all new: short, melodic, high-energy punk and guitar pop, played with the sort of urgency that comes from knowing exactly what a live room needs. There is plenty of history in the band, but they are not interested in recreating it.</p>
      <p class="soft">Their first album, <em>More Volume, Less Reverb</em>, produced by Stano, is nearly ready to go. Recent shows have included a special-guest slot with Rocky De Valera and the Gravediggers at their sold-out Grand Social reunion. Next up is the <em>Tokyo</em> single launch at The Grand Social Ballroom on 1 November.</p>
    </div>
    <div class="col-6 push-6 stack">
      <span class="label">Where they’ve come from</span>
      <div class="stack stack--sm"><h3>Bitzy</h3><p class="soft">Bitzy started in 1976 with The Slum and was fronting The Strougers by 1978. Baby Goes Boom followed, then a long break from music. He returned in 2009 with The Lee Harveys and spent 15 years with the band until their 2024 break. He is also the author of the punk memoir <em>Past the Point of Rescue</em>, now on its third reprint. A brief spell with The Last Pop Stars came before The Deviators.</p></div>
      <div class="stack stack--sm"><h3>Bren</h3><p class="soft">Bren started playing bass with The End in 1979 and later played alongside Andy in The Cathedral. In 2014 he teamed up with former The End drummer Johnny Bonnie in Trouble Pilgrims, the band that rose from the ashes of The Radiators From Space.</p></div>
      <div class="stack stack--sm"><h3>Andy</h3><p class="soft">Andy started his first band, Slit Possex, at 14. The Cathedral followed in the early 1980s, then Cabra bands Purdah, Primatevo and Lure through the ’90s. Inspired by the loss of Joe Strummer, Clash Jam Wallop was born and Andy spent 16 years with them. Complete Control followed, then three years with The Modfathers, including festivals and larger stages, before The Deviators.</p></div>
    </div>
  </div>
</section>

<section class="section section--alt" aria-label="Press quotes">
  <div class="wrap quotes3">
    <div class="quote"><blockquote style="font-size:clamp(24px,2.1vw,30px)">“Bounced onstage with the energy of a trio of 20 year olds… the songs were riotous and the crowd ate up every second of it.”</blockquote><span class="label">— The Goo · <a href="#" style="border-bottom:1px solid var(--muted)">source</a></span></div>
    <div class="quote"><blockquote style="font-size:clamp(24px,2.1vw,30px)">“Terrific gig by both the Devs and the DeValeras.”</blockquote><span class="label">— Colm O’Hare, music journalist</span></div>
    <div class="quote quote--pending"><blockquote style="font-size:clamp(24px,2.1vw,30px)">“[Exact quotation to be retrieved]”</blockquote><span class="label">— Ferdia Mac Anna · source [TBC]</span></div>
  </div>
</section>

<section class="section" id="assets" aria-labelledby="assets-h">
  <div class="wrap grid">
    <div class="col-4 stack stack--sm">
      <span class="label">Assets</span>
      <h2 id="assets-h" style="font-size:clamp(34px,3.3vw,48px)">Music, video, photos, logo, stage plot</h2>
      <p class="muted" style="font-size:15px">Public links only. <em>Creatures</em> stays a private stream until cleared for release.</p>
    </div>
    <div class="col-7 push-5 linklist linklist--2col">
      <a href="mailto:{CONTACT_EMAIL}?subject=Creatures%20private%20stream"><span>Listen · <em>Creatures</em></span><span class="muted">private · on request</span></a>
      <a href="{('https://www.youtube.com/watch?v=' + YOUTUBE_LIVE_ID) if YOUTUBE_LIVE_ID else '#'}" target="_blank" rel="noopener"><span>Watch · Live at The Grand Social</span><span class="muted">YouTube</span></a>
      <a href="/downloads/deviators-press-photos.zip"><span>Hi-res press photos</span><span class="muted">ZIP</span></a>
      <a href="/media/#logo"><span>Logo · light &amp; dark</span><span class="muted">PNG</span></a>
      <a href="/downloads/The_Deviators_Stage_Layout.pdf"><span>Stage plot &amp; tech spec</span><span class="muted">PDF</span></a>
      <a href="/downloads/The_Deviators_EPK_2026-08.pdf"><span>Full EPK</span><span class="muted">PDF · Aug 2026</span></a>
    </div>
  </div>
</section>
'''
press += footer()
write('press/index.html', press)

# =====================================================================
# PRIVACY + 404
# =====================================================================
privacy = head('Privacy', 'Privacy notice for thedeviators.com.', '/privacy/') + nav('') + f'''
<section class="section">
  <div class="wrap grid">
    <div class="col-7 stack">
      <span class="label">Privacy</span>
      <h1 style="font-size:clamp(48px,6.6vw,96px)">Privacy notice</h1>
      <p class="soft">This site does not use cookies for tracking and does not run analytics by default. Fonts are loaded from Google Fonts, which may log your IP address. Videos are embedded only after you press play, using YouTube’s privacy-enhanced mode. Ticketing is handled by Eventbrite under its own privacy policy. If you email us, we keep your message only for as long as needed to reply.</p>
      <p class="soft">Contact: {CONTACT_NAME} · <a href="mailto:{CONTACT_EMAIL}" style="border-bottom:1px solid var(--muted)">{CONTACT_EMAIL}</a></p>
      <p class="muted" style="font-size:14px">[Review before launch — add analytics/cookie wording if analytics are enabled.]</p>
    </div>
  </div>
</section>
''' + footer()
write('privacy/index.html', privacy)

nf = head('Page not found', 'Page not found.', '/404.html') + nav('') + f'''
<section class="section">
  <div class="wrap stack">
    <span class="label">404</span>
    <h1 style="font-size:clamp(48px,6.6vw,96px)">Wrong room.</h1>
    <p class="lede soft">That page isn’t here. Try the <a href="/" style="border-bottom:2px solid var(--accent)">homepage</a> or the <a href="/live/" style="border-bottom:2px solid var(--accent)">next show</a>.</p>
  </div>
</section>
''' + footer()
write('404.html', nf)

# Favicon (simple wordmark initial) + apple touch icon placeholder note
fav = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#0d0d0d"/><text x="32" y="46" text-anchor="middle" font-family="Anton, Impact, sans-serif" font-size="40" fill="#f4f1ec">D</text><rect x="8" y="52" width="48" height="4" fill="#8f1a3a"/></svg>'''
write('favicon.svg', fav)
print('done')
