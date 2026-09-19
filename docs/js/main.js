/* The Deviators — site JS
   1. Mobile nav toggle
   2. Upcoming shows from the daily Eventbrite snapshot
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

  /* ---------- 2. Eventbrite cards ---------- */
  var feeds = document.querySelectorAll('[data-shows]');
  var siteScript = document.currentScript;
  if (feeds.length && siteScript) {
    var eventsUrl = new URL('../data/events.json', siteScript.src);
    fetch(eventsUrl, {cache: 'no-cache'})
      .then(function (response) {
        if (!response.ok) throw new Error('Events unavailable');
        return response.json();
      })
      .then(function (data) {
        if (!Array.isArray(data.events)) throw new Error('Invalid events');
        var events = data.events.filter(function (event) {
          var today = new Intl.DateTimeFormat('sv-SE', {timeZone:event.timezone || 'Europe/Dublin'}).format(new Date());
          return event.start_local && event.start_local.slice(0,10) >= today;
        });
        feeds.forEach(function (feed) {
          feed.replaceChildren();
          var limit = Number(feed.dataset.limit) || events.length;
          if (!events.length) feed.appendChild(element('p', 'shows__empty', 'No upcoming shows announced. Check Eventbrite for the latest dates.'));
          events.slice(0, limit).forEach(function (event) { feed.appendChild(eventCard(event)); });
        });
        document.querySelectorAll('[data-events-updated]').forEach(function (label) {
          var fetched = new Date(data.fetched_at);
          label.textContent = Number.isNaN(fetched.getTime()) ? '' : 'Eventbrite · checked ' + fetched.toLocaleDateString('en-IE', {day:'numeric',month:'short',year:'numeric',timeZone:'Europe/Dublin'});
        });
      }).catch(function () {
        feeds.forEach(function (feed) {
          feed.replaceChildren(element('p', 'shows__empty', 'Show details are temporarily unavailable. View all events on Eventbrite below.'));
        });
      });
  }

  function element(tag, className, text) {
    var node = document.createElement(tag);
    node.className = className;
    if (text !== undefined) node.textContent = text;
    return node;
  }

  function eventCard(event) {
    var row = element('article', 'show');
    var date = element('div', 'show__date');
    // Use the venue's calendar date, without shifting it to the visitor's timezone.
    var day = new Date(event.start_local.slice(0,10) + 'T12:00:00Z');
    if (!event.hide_start_date) {
      date.appendChild(element('div', 'show__day', event.start_local.slice(8,10)));
      var month = element('div', 'show__mon');
      month.appendChild(element('span', '', day.toLocaleDateString('en-IE',{month:'short',timeZone:'UTC'})));
      month.appendChild(element('span', '', day.toLocaleDateString('en-IE',{weekday:'short',timeZone:'UTC'}) + ' · ' + event.start_local.slice(0,4)));
      date.appendChild(month);
    } else date.textContent = 'Date on Eventbrite';
    row.appendChild(date);
    var picture = element('div', 'show__img');
    if (event.image && /^https:\/\//.test(event.image)) {
      var image = document.createElement('img');
      image.src = event.image;
      image.alt = '';
      image.loading = 'lazy';
      picture.appendChild(image);
    }
    row.appendChild(picture);
    var body = element('div', 'show__body');
    body.appendChild(element('div', 'show__title', event.title));
    var time = event.hide_start_date ? '' : event.start_local.slice(11,16);
    body.appendChild(element('div', 'show__meta', [event.venue_name, event.city, time, event.price].filter(Boolean).join(' · ')));
    row.appendChild(body);
    var cta = element('div', 'show__cta');
    var link = element('a', 'btn btn--dark', event.sold_out ? 'Sold out · details ↗' : 'Tickets ↗');
    var url;
    try { url = new URL(event.url); } catch (_) { url = null; }
    link.href = url && url.protocol === 'https:' && /(^|\.)eventbrite\.(ie|com)$/.test(url.hostname) ? url.href : 'https://www.eventbrite.ie/o/120962217576';
    link.target = '_blank';
    link.rel = 'noopener';
    link.setAttribute('aria-label', (event.sold_out ? 'Sold out: ' : 'Tickets for ') + event.title + ' on Eventbrite');
    cta.appendChild(link);
    row.appendChild(cta);
    return row;
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
