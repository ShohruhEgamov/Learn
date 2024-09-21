// var http = require('http');
// var url = require('url');
// var fs = require('fs');

// http.createServer(function (req, res) {
// 	var q = url.parse(req.url, true);
// 	var filename = '.' + q.pathname;
// 	fs.readFile(filename, function (err, data) {
// 		if (err) {
// 			res.writeHead(404, { 'Content-Type': 'text/html' });
// 			return res.end('404 Xatoligi mavjud');
// 		}
// 		var date = new Date(); // Hozirgi sana va vaqtni oladi
// 		res.writeHead(200, { 'Content-Type': 'text/html' });
// 		res.write(date.toString()); // Sana va vaqtni matn ko'rinishida yozadi
// 		return res.end();
// 	});
// }).listen(3003);



// //Modullar bilan ishlash
// import http from 'http';
// import { readFile } from 'fs';
// // import { upperCase } from 'upper-case';
// // import { upperCase } from 'capitalizeeveryfirstletter';


// function capitalizeEveryFirstLetter(text) {
// 	return text.replace(/\b\w/g, (char) => char.toUpperCase());
// }

// http.createServer(function (req, res) {
// 	res.writeHead(200, { 'Content-Type': 'text/html' });
// 	res.write(capitalizeEveryFirstLetter('Salom dunyo dd ff '));
// 	res.end();
// }).listen(3004);

// import http from 'http';
// import formidable from 'formidable';
// import fs from 'fs';

// const server = http.createServer((req, res) => {
// 	if (req.url === '/fileupload' && req.method.toLowerCase() === 'post') {
// 		const form = new formidable.IncomingForm();
// 		form.parse(req, (err, fields, files) => {
// 			if (err) {
// 				res.writeHead(400, { 'Content-Type': 'text/plain' });
// 				res.end('File upload error');
// 				return;
// 			}
// 			const oldpath = files.filetoupload.filepath;
// 			const newpath = 'C:/Users/YourName/' + files.filetoupload.originalFilename;
// 			fs.rename(oldpath, newpath, (err) => {
// 				if (err) {
// 					res.writeHead(500, { 'Content-Type': 'text/plain' });
// 					res.end('Error moving file');
// 					return;
// 				}
// 				res.writeHead(200, { 'Content-Type': 'text/plain' });
// 				res.end('File uploaded and moved!');
// 			});
// 		});
// 	} else {
// 		res.writeHead(200, { 'Content-Type': 'text/html' });
// 		res.write('<form action="fileupload" method="post" enctype="multipart/form-data">');
// 		res.write('<input type="file" name="filetoupload"><br>');
// 		res.write('<input type="submit">');
// 		res.write('</form>');
// 		return res.end();
// 	}
// });

// server.listen(3005);

import dotenv from 'dotenv';
import nodemailer from 'nodemailer';

dotenv.config();

const transporter = nodemailer.createTransport({
	service: 'gmail',
	auth: {
		user: process.env.EMAIL,
		pass: process.env.PASSWORD
	}
});

const mailOptions = {
	from: process.env.EMAIL,
	to: 'shohruhwebdev@gmail.com',
	subject: 'Sending Email using Node.js',
	text: 'That was easy!'
};

transporter.sendMail(mailOptions, (error, info) => {
	if (error) {
		console.log(error);
	} else {
		console.log('Email sent: ' + info.response);
	}
});
