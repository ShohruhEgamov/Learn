import mysql from 'mysql2';

const con = mysql.createConnection({
	host: "localhost",
	user: "root",
	password: "Shoh1221web:py",
	database: "shohruh_sql"
});

// //                                  Bu yerda esa datdabase yaratish
// con.connect(function (err) {
// 	if (err) throw err;
// 	console.log("Connected!");
// 	con.query("CREATE DATABASE shohruh_sql", function (err, result) {
// 		if (err) throw err;
// 		console.log("Database created");
// 	});
// });

// //                                     Bu yerda esa table (jadval) yaratish

// con.connect(function (err) {
// 	if (err) throw err;
// 	console.log("Tugallandi");
// 	var sql = "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))";
// 	con.query(sql, function (err, result) {
// 		if (err) throw err;
// 		console.log('Jadval yaratildi');
// 	});
// });


// // Buni har bir yozuv uchun noyob raqam kiritadigan "INT AUTO_INCREMENT PRIMARY KEY" ustunini belgilash orqali amalga oshirish mumkin. 1 dan boshlanadi va har bir rekord uchun bittaga oshiriladi.
// con.connect(function (err) {
// 	if (err) throw err;
// 	console.log("Tugallandi");

// 	// Bu yerda esa savolni va SQL buyrug'ini kiritish kerak
// 	var sql = "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY";
// 	con.query(sql, function (err, result) {
// 		if (err) throw err;
// 		console.log('Jadval yaratildi');
// 	});
// });


// // MySQL-da jadvalni to'ldirish uchun "INSERT INTO" iborasidan foydalaning.

// con.connect(function (err) {
// 	if (err) throw err;
// 	console.log('Tugallandi');
// 	var sql = "INSERT INTO customers (name,address) VALUES ('Company ALBIYA', 'Bretskaya 9')";
// 	con.query(sql, function (err, result) {
// 		if (err) throw err;
// 		console.log('1 chi manzil');
// 	});
// });


// // Bir nechta yozuvlarni qo'shish uchun qiymatlarni o'z ichiga olgan massiv tuzing va sql-ga savol belgisini qo'ying, bu qiymatlar massivi bilan almashtiriladi:
// // INSERT INTO customers (name, address) VALUES ?
// con.connect(function (err) {
// 	if (err) throw err;
// 	console.log('Tugallandi');
// 	var sql = "INSERT INTO customers (name,address) VALUES ?";
// 	var values = [
// 		['John', 'Highway 71'],
// 		['Peter', 'Lowstreet 4'],
// 		['Amy', 'Apple st 652'],
// 		['Hannah', 'Mountain 21'],
// 		['Michael', 'Valley 345'],
// 		['Sandy', 'Ocean blvd 2'],
// 		['Betty', 'Green Grass 1'],
// 		['Richard', 'Sky st 331'],
// 		['Susan', 'One way 98'],
// 		['Vicky', 'Yellow Garden 2'],
// 		['Ben', 'Park Lane 38'],
// 		['William', 'Central st 954'],
// 		['Chuck', 'Main Road 989'],
// 		['Viola', 'Sideway 1633']
// 	]
// 	con.query(sql, [values], function (err, result) {
// 		if (err) throw err;
// 		console.log('Toplam manzil' + result.affectedRows);
// 	});
// });


con.connect(function (err) {
	if (err) throw err;
	var sql = "INSERT INTO customers (name, address) VALUES ('Michelle','Blue Village 1')";
	con.query(sql, function (err, result) {
		if (err) throw err;
		console.log("1 yozuv kiritildi ID " + result.insertId);
	});
});