const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '../docs');
const base = '/thedeviators.com/';
const types = {'.html':'text/html; charset=utf-8','.css':'text/css','.js':'text/javascript','.json':'application/json','.jpg':'image/jpeg','.png':'image/png','.svg':'image/svg+xml','.pdf':'application/pdf','.xml':'application/xml','.txt':'text/plain','.zip':'application/zip'};
http.createServer((req, res) => {
  let pathname;
  try { pathname = decodeURIComponent(new URL(req.url, 'http://localhost').pathname); }
  catch { res.writeHead(400).end(); return; }
  if (pathname === base.slice(0, -1)) { res.writeHead(302, {Location:base}).end(); return; }
  let file = path.resolve(root, pathname.startsWith(base) ? pathname.slice(base.length) : pathname.slice(1));
  if (file !== root && !file.startsWith(root + path.sep)) { res.writeHead(403).end(); return; }
  if (fs.existsSync(file) && fs.statSync(file).isDirectory()) {
    if (!pathname.endsWith('/')) { res.writeHead(302, {Location:pathname + '/'}).end(); return; }
    file = path.join(file, 'index.html');
  }
  fs.readFile(file, (err, data) => {
    if (err) { res.writeHead(404, {'Content-Type':'text/html'}).end(fs.readFileSync(path.join(root,'404.html'))); return; }
    res.writeHead(200, {'Content-Type':types[path.extname(file)] || 'application/octet-stream', 'Cache-Control':'no-store'}).end(data);
  });
}).listen(8000, '127.0.0.1', () => console.log('Preview: http://localhost:8000/thedeviators.com/'));
