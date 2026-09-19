// Read only the public organiser page; never request account or attendee data.
const fs = require('node:fs');
const path = require('node:path');
const ORGANIZER = '120962217576';
const SOURCE = `https://www.eventbrite.ie/o/${ORGANIZER}`;
const OUTPUT = path.resolve(__dirname, '../docs/data/events.json');

function parseEvents(html) {
  const match = html.match(/<script\b[^>]*\bid="__NEXT_DATA__"[^>]*>([\s\S]*?)<\/script>/i);
  if (!match) throw new Error('Eventbrite public page format changed; existing events were preserved.');
  const page = JSON.parse(match[1]).props?.pageProps;
  if (String(page?.organizer?.id) !== ORGANIZER || page.upcomingEventsFailed !== false ||
      !Array.isArray(page.upcomingEvents) || !Number.isInteger(page.upcomingEventsTotal)) {
    throw new Error('Eventbrite did not supply a verified event list; existing events were preserved.');
  }
  if (page.hasMoreUpcoming !== false || page.upcomingEventsTotal !== page.upcomingEvents.length) {
    throw new Error('Eventbrite list is paginated or incomplete; refusing to publish a partial list.');
  }
  return page.upcomingEvents.filter(e => !e.is_cancelled && !e.is_protected_event).map(e => {
    if (String(e.primary_organizer_id) !== ORGANIZER || !e.name || !/^\d{4}-\d{2}-\d{2}$/.test(e.start_date) ||
        !/^\d{2}:\d{2}:\d{2}$/.test(e.start_time) || !e.timezone) throw new Error('Invalid Eventbrite event.');
    const url = new URL(e.url);
    if (url.protocol !== 'https:' || !['www.eventbrite.ie', 'www.eventbrite.com'].includes(url.hostname)) throw new Error('Invalid ticket URL.');
    const ticket = e.ticket_availability || {};
    const amount = ticket.minimum_ticket_price;
    let price = '';
    if (ticket.is_free) price = 'Free';
    else if (amount && Number.isFinite(Number(amount.major_value)) && amount.currency) {
      price = 'From ' + new Intl.NumberFormat('en-IE', {style:'currency', currency:amount.currency}).format(Number(amount.major_value));
    }
    return {
      id: String(e.id), title: e.name, start_local: `${e.start_date}T${e.start_time}`,
      timezone: e.timezone, hide_start_date: !!e.hide_start_date,
      venue_name: e.is_online_event ? 'Online event' : (e.primary_venue?.name || ''),
      city: e.is_online_event ? '' : (e.primary_venue?.address?.city || ''),
      price, image: e.image?.url || '', url: url.href, sold_out: !!ticket.is_sold_out
    };
  }).sort((a,b) => a.start_local.localeCompare(b.start_local));
}

async function main() {
  let html;
  if (process.argv[2] === '--html' && process.argv[3]) html = fs.readFileSync(process.argv[3], 'utf8');
  else {
    const response = await fetch(SOURCE, {signal:AbortSignal.timeout(30000), headers:{'User-Agent':'Deviators-Website-Events/1.0', Accept:'text/html'}});
    if (!response.ok) throw new Error(`Eventbrite HTTP ${response.status}; existing events were preserved.`);
    html = await response.text();
  }
  const events = parseEvents(html);
  const data = {source:SOURCE, fetched_at:new Date().toISOString(), refresh_interval:'daily', events};
  // Validation completes before replacing the last successful snapshot.
  fs.writeFileSync(OUTPUT + '.tmp', JSON.stringify(data, null, 2) + '\n');
  fs.renameSync(OUTPUT + '.tmp', OUTPUT);
  console.log(`Updated ${events.length} public Eventbrite event(s).`);
}
if (require.main === module) main().catch(error => { console.error(error.message); process.exitCode = 1; });
module.exports = {parseEvents};
