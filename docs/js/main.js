/* The Deviators — site JS
   1. Mobile nav toggle
   2. Upcoming shows feed (Eventbrite via /data/events.json, falls back to /data/events.json)
   3. Video poster → YouTube embed on click
   No dependencies. */

(function () {
  'use strict';

  /* ---------- 1. Nav ---------- */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.getAttribute('data-open') === 'true';
      nav.setAttribute('data-open', String(!open));
      toggle.setAttribute('aria-expanded', String(!open));
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.getAttribute('data-open') === 'true') {
        nav.setAttribute('data-open', 'false');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  /* ---------- 2. Shows feed ---------- */
  var feeds = document.querySelectorAll('[data-shows]');
  if (feeds.length) {
    var endpoint = document.body.getAttribute('data-events-endpoint') || '/thedeviators.com/data/events.json';
    var fallback = document.body.getAttribute('data-events-fallback') || '/thedeviators.com/data/events.json';

    fetchJSON(endpoint)
      .catch(function () { return fetchJSON(fallback); })
      .then(function (data) {
        var events = normalise(data);
        feeds.forEach(function (el) { renderShows(el, events); });
      })
      .catch(function () {
        feeds.forEach(function (el) { renderShows(el, []); });
      });
  }

  function fetchJSON(url) {
    return fetch(url, { headers: { Accept: 'application/json' } }).then(function (r) {
      if (!r.ok) throw new Error(r.status);
      return r.json();
    });
  }

  /* Accepts either our own shape ({events:[...]}) or a raw Eventbrite
     /organizations/{id}/events response, and returns a flat sorted list. */
  function normalise(data) {
    var list = (data && data.events) || [];
    var now = Date.now();
    return list.map(function (ev) {
      var start = ev.start_local || (ev.start && (ev.start.local || ev.start.utc)) || ev.start;
      var venue = ev.venue_name || (ev.venue && ev.venue.name) || '';
      var city = ev.city || (ev.venue && ev.venue.address && ev.venue.address.city) || '';
      var name = ev.title || (ev.name && (ev.name.text || ev.name)) || '';
      var summary = ev.summary || ev.description_short || '';
      var img = ev.image || (ev.logo && (ev.logo.original && ev.logo.original.url || ev.logo.url)) || '';
      var price = ev.price || priceFrom(ev);
      var doors = ev.doors || '';
      return {
        start: new Date(start),
        name: name,
        venue: venue,
        city: city,
        summary: summary,
        image: img,
        price: price,
        doors: doors,
        url: ev.url || '#',
        soldOut: !!(ev.sold_out || (ev.ticket_availability && ev.ticket_availability.is_sold_out))
      };
    }).filter(function (e) {
      return !isNaN(e.start) && e.start.getTime() > now - 6 * 3600 * 1000; // keep today's show until 6h after start
    }).sort(function (a, b) { return a.start - b.start; });
  }

  function priceFrom(ev) {
    var ta = ev.ticket_availability;
    if (ta && ta.minimum_ticket_price && ta.minimum_ticket_price.display) return ta.minimum_ticket_price.display;
    if (ev.is_free) return 'Free';
    return '';
  }

  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  var DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];

  function renderShows(el, events) {
    var limit = parseInt(el.getAttribute('data-limit') || '0', 10);
    var shown = limit ? events.slice(0, limit) : events;
    el.innerHTML = '';
    if (!shown.length) {
      var empty = document.createElement('div');
      empty.className = 'shows__empty';
      empty.innerHTML = 'No shows announced right now — <a href="/thedeviators.com/#book">book the band</a> or follow us for the next date.';
      el.appendChild(empty);
      return;
    }
    shown.forEach(function (ev) {
      var d = ev.start;
      var day = String(d.getDate()).padStart(2, '0');
      var mon = MONTHS[d.getMonth()];
      var dow = DAYS[d.getDay()];
      var yr = d.getFullYear();
      var time = ev.doors ? ('Doors ' + ev.doors) : d.toLocaleTimeString('en-IE', { hour: 'numeric', minute: '2-digit' }).replace(':00', '').toLowerCase();
      var meta = [ev.venue + (ev.city ? ', ' + ev.city : ''), time, ev.price].filter(Boolean).join(' · ');

      var row = document.createElement('article');
      row.className = 'show';
      row.innerHTML =
        '<div class="show__date"><div class="show__day">' + day + '</div><div class="show__mon"><span>' + mon + '</span><span>' + dow + ' · ' + yr + '</span></div></div>' +
        (ev.image ? '<div class="show__img"><img src="' + esc(ev.image) + '" alt="" loading="lazy"></div>' : '<div class="show__img" aria-hidden="true"></div>') +
        '<div class="show__body"><div class="show__title">' + esc(ev.name) + '</div><div class="show__meta">' + esc(meta) + '</div></div>' +
        '<div class="show__cta"><a class="btn btn--dark" href="' + esc(ev.url) + '" target="_blank" rel="noopener">' + (ev.soldOut ? 'Sold out' : 'Tickets →') + '</a></div>';
      el.appendChild(row);
    });
  }

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  /* ---------- 3. Video embed on demand (no autoplay, no third-party load until clicked) ---------- */
  document.querySelectorAll('.video[data-youtube]').forEach(function (box) {
    var id = box.getAttribute('data-youtube');
    var btn = box.querySelector('.video__play');
    if (!id || !btn) return;
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      var iframe = document.createElement('iframe');
      iframe.src = 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(id) + '?autoplay=1&rel=0';
      iframe.title = btn.getAttribute('aria-label') || 'Video';
      iframe.allow = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture';
      iframe.allowFullscreen = true;
      box.appendChild(iframe);
    });
  });
})();
