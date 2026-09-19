// Netlify Function: GET /api/events
// Proxies the Eventbrite organisation events feed so the private API token
// never reaches the browser. Cached at the CDN edge for 10 minutes.
//
// Required environment variables (Netlify → Site settings → Environment):
//   EVENTBRITE_TOKEN   private token from https://www.eventbrite.com/platform/api-keys
//   EVENTBRITE_ORG_ID  numeric organisation id (see docs/DEVELOPMENT.md → "Finding your organisation id")
//
// Response shape (consumed by js/main.js):
//   { "events": [ { title, start_local, venue_name, city, price, image, url, sold_out, summary } ] }

exports.handler = async function () {
  const token = process.env.EVENTBRITE_TOKEN;
  const org = process.env.EVENTBRITE_ORG_ID;

  const headers = {
    'Content-Type': 'application/json; charset=utf-8',
    'Cache-Control': 'public, max-age=60, s-maxage=600, stale-while-revalidate=3600',
    'Access-Control-Allow-Origin': '*'
  };

  if (!token || !org) {
    return { statusCode: 503, headers, body: JSON.stringify({ error: 'Eventbrite not configured', events: [] }) };
  }

  const url = `https://www.eventbriteapi.com/v3/organizations/${org}/events/?status=live&order_by=start_asc&expand=venue,ticket_availability,logo&page_size=20`;

  try {
    const res = await fetch(url, { headers: { Authorization: `Bearer ${token}` } });
    if (!res.ok) {
      return { statusCode: 502, headers, body: JSON.stringify({ error: `Eventbrite ${res.status}`, events: [] }) };
    }
    const data = await res.json();
    const events = (data.events || []).map(ev => ({
      id: ev.id,
      title: ev.name && ev.name.text,
      summary: ev.summary || '',
      start_local: ev.start && ev.start.local,
      end_local: ev.end && ev.end.local,
      venue_name: ev.venue && ev.venue.name,
      city: ev.venue && ev.venue.address && ev.venue.address.city,
      price: ev.is_free ? 'Free'
        : (ev.ticket_availability && ev.ticket_availability.minimum_ticket_price && ev.ticket_availability.minimum_ticket_price.display) || '',
      sold_out: !!(ev.ticket_availability && ev.ticket_availability.is_sold_out),
      image: (ev.logo && ((ev.logo.original && ev.logo.original.url) || ev.logo.url)) || '',
      url: ev.url
    }));
    return { statusCode: 200, headers, body: JSON.stringify({ source: 'eventbrite', fetched_at: new Date().toISOString(), events }) };
  } catch (err) {
    return { statusCode: 502, headers, body: JSON.stringify({ error: String(err), events: [] }) };
  }
};
