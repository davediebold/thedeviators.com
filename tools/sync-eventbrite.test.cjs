const {test} = require('node:test');
const assert = require('node:assert/strict');
const {parseEvents} = require('./sync-eventbrite.cjs');
const event = {id:'1', primary_organizer_id:'120962217576', name:'Test show', url:'https://www.eventbrite.ie/e/test-1', start_date:'2026-11-01', start_time:'16:30:00', timezone:'Europe/Dublin', primary_venue:{name:'Venue',address:{city:'Dublin'}}, ticket_availability:{minimum_ticket_price:{major_value:'17.07',currency:'EUR'}}};
function page(overrides={}) {
  const data = {organizer:{id:'120962217576'}, upcomingEventsFailed:false, hasMoreUpcoming:false, upcomingEventsTotal:1, upcomingEvents:[event], ...overrides};
  return '<script id="__NEXT_DATA__" type="application/json">' + JSON.stringify({props:{pageProps:data}}) + '</script>';
}
test('extracts public listing fields including actual ticket price and venue time', () => {
  const [result] = parseEvents(page());
  assert.equal(result.price, 'From €17.07');
  assert.equal(result.start_local, '2026-11-01T16:30:00');
  assert.equal(result.venue_name, 'Venue');
  assert.equal(result.url, event.url);
});
test('accepts a genuine empty calendar', () => assert.deepEqual(parseEvents(page({upcomingEvents:[],upcomingEventsTotal:0})), []));
test('refuses errors, schema changes, incomplete lists, and wrong organisers', () => {
  for (const data of [{upcomingEventsFailed:true},{hasMoreUpcoming:true},{upcomingEventsTotal:2},{organizer:{id:'wrong'}}]) assert.throws(() => parseEvents(page(data)));
  assert.throws(() => parseEvents('<html>Access denied</html>'));
});
test('omits cancelled or protected listings and rejects unsafe links', () => {
  assert.deepEqual(parseEvents(page({upcomingEvents:[{...event,is_cancelled:true}]})), []);
  assert.deepEqual(parseEvents(page({upcomingEvents:[{...event,is_protected_event:true}]})), []);
  assert.throws(() => parseEvents(page({upcomingEvents:[{...event,url:'javascript:alert(1)'}]})));
});
