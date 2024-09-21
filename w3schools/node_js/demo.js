var http = require('http');
var fs = require('fs');
http.createServer(function (req, res) {
	fs.readFile('demofile1.html', function (err, data) {
		res.writeHead(200, { 'Content-Type': 'text/html' });
		res.write(data);
		return res.end();
	});
}).listen(3000);


// appendFile() usuli yordamida yangi fayl yarating:
var fs = require('fs');

fs.appendFile('mynewfile1.txt', 'Hello content!', function (err) {
	if (err) throw err;
	console.log('Saved!');
});


// Usul fs.open()ikkinchi argument sifatida "bayroq" ni oladi, agar bayroq "yozish" uchun "w" bo'lsa, ko'rsatilgan fayl yozish uchun ochiladi. Agar fayl mavjud bo'lmasa, bo'sh fayl yaratiladi:
var fs = require('fs');
fs.open('mynewfile2.txt', 'w', function (err, file) {
	if (err) throw err;
	console.log('Shohruh')
});


// Usul fs.writeFile()belgilangan fayl va agar mavjud bo'lsa, tarkibni almashtiradi. Agar fayl mavjud bo'lmasa, ko'rsatilgan tarkibni o'z ichiga olgan yangi fayl yaratiladi:
var fs = require('fs');

fs.writeFile('mynewfile3.txt', 'Salom', function (err) {
	if (err) throw err;
	console.log('Farrux')
});

// Fayl tizimi modulida fayllarni yangilash usullari mavjud:

// fs.appendFile()
// fs.writeFile()
// Usul fs.appendFile()belgilangan faylning oxiriga ko'rsatilgan tarkibni qo'shadi:


var url = require('url');
var adr = 'http://localhost:3000/default.htm?year=2000&month=dekabr';
var q = url.parse(adr, true);

console.log(q.host); // Bu qaytaradi 'localhost:3000'
console.log(q.pathname); // Bu qaytaradi '/default.htm'
console.log(q.search); // Bu qaytaradi '?year=2017&month=february'

var qdata = q.query;
console.log(qdata.month); // Bu qaytaradi 'february'

// Bu yerda esa topilgan fayni o'qiydi topilmaganini 404 xatosi beradi
var http = require('http');
var url = require('url');
var fs = require('fs');

http.createServer(function (req, res) {
	var q = url.parse(req.url, true);
	var filename = '.' + q.pathname;
	fs.readFile(filename, function (err, data) {
		if (err) {
			res.writeHead(404, {
				'Content-Type': 'text/html'
			});
			return res.end('404 Not Found');
		}
		res.writeHead(200, { 'Content-Type': 'text/html' });
		res.write(date);
		return res.end();
	});
}).listen(3000);

