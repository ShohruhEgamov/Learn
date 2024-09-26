import mysql from 'mysql2';

const con = mysql.createConnection({
	host: "localhost",
	user: "root",
	password: "Shoh1221web:py",
	database: 'mydatabase'
	// database: 'shohruh'
});
const sql = "SELECT * FROM mytable";
// const createTableQuery = `
// CREATE TABLE IF NOT EXISTS mytable (
// 	id INT AUTO_INCREMENT PRIMARY KEY,
// 	name VARCHAR(255),
// 	age INT
// );
// `;
con.connect(function (err) {
	if (err) throw err;
	console.log("Connected");
	con.query(sql, function (err, result) {
		if (err) throw err;
		console.log('Result: ', result); // Natijani to'g'ri ko'rsatish uchun
	});
	// con.connect(function (err) {
	// 	if (err) throw err;
	// 	console.log("Connected!");
	// 	con.query("CREATE DATABASE shohruh", function (err, result) {
	// 		if (err) throw err;
	// 		console.log("Database created");
	// 	});
	// });
});

