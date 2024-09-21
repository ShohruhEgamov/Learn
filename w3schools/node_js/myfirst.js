var http = require('http');
var dt = require('./myfirstmodule');
var url = require('url');

http.createServer(function (req, res) {
	res.writeHead(200, { 'Content-Type': 'text/html' });
	// res.write("Bugun " + dt.myDateTime() + ", Hafta " + dt.myDateTimeday())
	// res.write(req.url);
	var q = url.parse(req.url, true).query;
	var txt = q.year + " " + q.month;
	res.end(txt);
}).listen(3000);

