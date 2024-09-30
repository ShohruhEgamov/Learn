import mysql from 'mysql2';

const con = mysql.createConnection({
	host: "localhost",
	user: "root",
	password: "Shoh1221web:py",
	database: "shohruh_sql"
});

//                                  Bu yerda esa datdabase yaratish
con.connect(function (err) {
	if (err) throw err;
	console.log("Connected!");
	con.query("CREATE DATABASE shohruh_sql", function (err, result) {
		if (err) throw err;
		console.log("Database created");
	});
});

//                                     Bu yerda esa table (jadval) yaratish

con.connect(function (err) {
	if (err) throw err;
	console.log("Tugallandi");
	var sql = "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))";
	con.query(sql, function (err, result) {
		if (err) throw err;
		console.log('Jadval yaratildi');
	});
});


// Buni har bir yozuv uchun noyob raqam kiritadigan "INT AUTO_INCREMENT PRIMARY KEY" ustunini belgilash orqali amalga oshirish mumkin. 1 dan boshlanadi va har bir rekord uchun bittaga oshiriladi.
con.connect(function (err) {
	if (err) throw err;
	console.log("Tugallandi");

	// Bu yerda esa savolni va SQL buyrug'ini kiritish kerak
	var sql = "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY";
	con.query(sql, function (err, result) {
		if (err) throw err;
		console.log('Jadval yaratildi');
	});
});


// MySQL-da jadvalni to'ldirish uchun "INSERT INTO" iborasidan foydalaning.

con.connect(function (err) {
	if (err) throw err;
	console.log('Tugallandi');
	var sql = "INSERT INTO customers (name,address) VALUES ('Company ALBIYA', 'Bretskaya 9')";
	con.query(sql, function (err, result) {
		if (err) throw err;
		console.log('1 chi manzil');
	});
});


// Bir nechta yozuvlarni qo'shish uchun qiymatlarni o'z ichiga olgan massiv tuzing va sql-ga savol belgisini qo'ying, bu qiymatlar massivi bilan almashtiriladi:
// INSERT INTO customers (name, address) VALUES ?
con.connect(function (err) {
	if (err) throw err;
	console.log('Tugallandi');
	var sql = "INSERT INTO customers (name,address) VALUES ?";
	var values = [
		['John', 'Highway 71'],
		['Peter', 'Lowstreet 4'],
		['Amy', 'Apple st 652'],
		['Hannah', 'Mountain 21'],
		['Michael', 'Valley 345'],
		['Sandy', 'Ocean blvd 2'],
		['Betty', 'Green Grass 1'],
		['Richard', 'Sky st 331'],
		['Susan', 'One way 98'],
		['Vicky', 'Yellow Garden 2'],
		['Ben', 'Park Lane 38'],
		['William', 'Central st 954'],
		['Chuck', 'Main Road 989'],
		['Viola', 'Sideway 1633']
	]
	con.query(sql, [values], function (err, result) {
		if (err) throw err;
		console.log('Toplam manzil' + result.affectedRows);
	});
});


con.connect(function (err) {
	if (err) throw err;
	var sql = "INSERT INTO customers (name, address) VALUES ('Michelle','Blue Village 1')";
	con.query(sql, function (err, result) {
		if (err) throw err;
		console.log("1 yozuv kiritildi ID " + result.insertId);
	});
});


con.connect(function (err) {
	if (err) throw err;
	con.query("SELECT name, address FROM customers", function (err, result, fields) {
		if (err) throw err;
		console.log(result[4].address); // Bu yerda esa 4 qatorning address bolimini oladi
		console.log(result[5].name); // Bu yerda esa 4 qatorning address bolimini oladi
		console.log(fields);
	});
});


con.connect(function (err) {
	if (err) throw err;
	con.query("SELECT name, address FROM customers", function (err, result, fields) {
		if (err) throw err;
		console.log(fields);
	});
});


// Bu yerda qidirish uchun
con.connect(function (err) {
	if (err) throw err;
	var sql = "SELECT * FROM customers WHERE address = 'Park Lane 38'";
	con.query(sql, function (err, result) {
		if (err) throw err;
		console.log(result);
	});
});


con.connect(function (err) {
	if (err) throw err;
	var sql = "SELECT * FROM customers WHERE address LIKE 'S%'";
	con.query(sql, function (err, result) {
		if (err) throw err;
		console.log(result);
	});
});

// Usul yordamida so'rov qiymatlaridan qochish mysql.escape() :

con.connect(function (err) {
	if (err) throw err;
	var adr = 'Mountain 21';
	var sql = 'SELECT * FROM customers WHERE address =  ' + mysql.escape(adr);
	con.query(sql, function (err, result) {
		if (err) throw err;
		console.log(result);
	});
});


// ORDER BY kalit so‘zi natijani sukut bo‘yicha o‘sish bo‘yicha tartiblaydi. Natijani kamayish tartibida saralash uchun DESC kalit so'zidan foydalaning.
con.connect(function (err) {
	if (err) throw err;
	var sql = 'SELECT * FROM customers ORDER BY name';
	con.query(sql, function (err, result) {
		if (err) throw err;
		console.log(result);
	});
});
