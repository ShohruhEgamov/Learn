// const MongoClient = require('mongodb').MongoClient;

// const { createConnection } = require('mysql');

// const url = 'mongodb://localhost:27017/blog';

// MongoClient.connect(url, function (err, client) {
// 	if (err) throw err;
// 	console.log('Database yaratildi');
// 	client.close();
// });

// console.log("Hello Word");


// MongoClient.connect(url, function (err, db) {
// 	if (err) throw err;
// 	var dbo = db.db("mydb");
// 	var myobj = { name: "Company Inc", address: "Highway 37" };
// 	dbo.collection("customers").insertOne(myobj, function (err, res) {
// 		if (err) throw err;
// 		console.log("1 document inserted");
// 		db.close();
// 	});
// });



// MongoClient.connect(url, function (err, db) {
// 	if (err) throw err;
// 	var dbo = db.db("mydb");
// 	var myobj = [
// 		{ name: 'John', address: 'Highway 71' },
// 		{ name: 'Peter', address: 'Lowstreet 4' },
// 		{ name: 'Amy', address: 'Apple st 652' },
// 		{ name: 'Hannah', address: 'Mountain 21' },
// 		{ name: 'Michael', address: 'Valley 345' },
// 		{ name: 'Sandy', address: 'Ocean blvd 2' },
// 		{ name: 'Betty', address: 'Green Grass 1' },
// 		{ name: 'Richard', address: 'Sky st 331' },
// 		{ name: 'Susan', address: 'One way 98' },
// 		{ name: 'Vicky', address: 'Yellow Garden 2' },
// 		{ name: 'Ben', address: 'Park Lane 38' },
// 		{ name: 'William', address: 'Central st 954' },
// 		{ name: 'Chuck', address: 'Main Road 989' },
// 		{ name: 'Viola', address: 'Sideway 1633' }
// 	];
// 	dbo.collection("customers").insertMany(myobj, function (err, res) {
// 		if (err) throw err;
// 		console.log("Number of documents inserted: " + res.insertedCount);
// 		db.close();
// 	});
// });



// //                                                             Bu yerda mongoga ulash uchun
// const MongoClient = require('mongodb').MongoClient;

// const url = 'mongodb://localhost:27017';
// const dbName = 'blog';

// async function main() {
// 	const client = new MongoClient(url);

// 	try {
// 		// MongoDB serveriga ulanish
// 		await client.connect();
// 		console.log('MongoDB ga ulanish muvaffaqiyatli bo\'ldi.');

// 		const db = client.db(dbName);
// 		// Boshqa operatsiyalarni bajaring, masalan, collection ni olish
// 		const collection = db.collection('your_collection_name'); // o'zingizga mos nom yozing

// 		// Hozircha nima qilishni xohlayotganingizni ko'rsatish
// 		const items = await collection.find({}).toArray();
// 		console.log(items);
// 	} catch (err) {
// 		console.error('Xato:', err);
// 	} finally {
// 		// Clientni yopish
// 		await client.close();
// 	}
// }

// main().catch(console.error);




// const MongoClient = require('mongodb').MongoClient;

// const url = 'mongodb://localhost:27017';
// const dbName = 'blog';

// async function run() {
// 	const client = new MongoClient(url);

// 	try {
// 		await client.connect();
// 		console.log("MongoDB ga ulanish muvaffaqiyatli bo'ldi.");

// 		const db = client.db(dbName);
// 		const collection = db.collection('customers'); // o'z kollektsiyangiz nomini yozing
// 		// const collection = db.collection('shohruh'); // o'z kollektsiyangiz nomini yozing

// 		// Ma'lumot qo'shish
// 		// const insertResult = await collection.insertOne({ name: "nok", type: "hol meva" });
// 		// console.log('Qo\'shilgan ma\'lumot:', insertResult.insertedId);



// 		// const jadvalYaratish = await db.createCollection("customers")
// 		// console.log('Jadval Yaratdik');

// 		var myobj = [
// 			{ name: 'John', address: 'Highway 71' },
// 			{ name: 'Peter', address: 'Lowstreet 4' },
// 			{ name: 'Amy', address: 'Apple st 652' },
// 			{ name: 'Hannah', address: 'Mountain 21' },
// 			{ name: 'Michael', address: 'Valley 345' },
// 			{ name: 'Sandy', address: 'Ocean blvd 2' },
// 			{ name: 'Betty', address: 'Green Grass 1' },
// 			{ name: 'Richard', address: 'Sky st 331' },
// 			{ name: 'Susan', address: 'One way 98' },
// 			{ name: 'Vicky', address: 'Yellow Garden 2' },
// 			{ name: 'Ben', address: 'Park Lane 38' },
// 			{ name: 'William', address: 'Central st 954' },
// 			{ name: 'Chuck', address: 'Main Road 989' },
// 			{ name: 'Viola', address: 'Sideway 1633' }
// 		];;
// 		// const qoshish = db.collection('customers').insertOne(myobj);
// 		const qoshish = await db.collection('customers').insertMany(myobj);
// 		console.log("Element qo'shildi yangi jadvalga");

// 		// Ma'lumotlarni olish
// 		const data = await collection.find({}).toArray();
// 		console.log(data);



// 		// Bu hato bormi yo'qmi bildiradi
// 	} catch (err) {
// 		console.error(err);


// 		// Bu yerda bitganini bildiradi
// 	} finally {
// 		await client.close();
// 	}
// }

// run().catch(console.dir);



// const { MongoClient } = require('mongodb');

// const url = 'mongodb://localhost:27017';

// const client = new MongoClient(url);

// async function run() {
// 	try {
// 		await client.connect();
// 		console.log("MongoDB ga ulanish muvaffaqiyatli bo'ldi.");

// 		const database = client.db('blog');
// 		const collection = database.collection('shohruh'); // 'fruits' o'rniga sizning kollektsiyangiz nomini qo'ying

// 		const data = await collection.find().toArray();
// 		console.log("Kiritilgan ma'lumotlar:", data);
// 	} finally {
// 		await client.close();
// 	}
// }

// run().catch(console.dir);



// // Bu yerda esa yaratish
// var MongoClient = require('mongodb').MongoClient;
// //Create a database named "mydb":
// var url = "mongodb://localhost:27017/mydb";

// MongoClient.connect(url, function (err, db) {
// 	if (err) throw err;
// 	console.log("Database created!");

// 	var dbo = db.db("mydb");
// 	var myobj = { name: "Shohruh", famila: "Egamov" };

// 	// Ma'lumot qo'shish
// 	dbo.collection("fruits").insertOne(myobj, function (err, res) {
// 		if (err) throw err;
// 		console.log("1 ta ma'lumot qo'shildi");
// 		db.close();
// 	});
// });


// MongoClient.connect(url, function (err, db) {
// 	if (err) throw err;
// 	var dbo = db.db("blog");

// 	// Ma'lumotlarni olish
// 	dbo.collection("shohruh").find({}).toArray(function (err, result) {
// 		if (err) throw err;
// 		console.log(result); // Kiritilgan ma'lumotlarni ko'rsatadi
// 		db.close();
// 	});
// });



// // Bu yerda esa TOPLAM yaratish kiradi.
// var MongoClient = require('mongodb').MongoClient;
// var url = "mongodb://localhost:27017/";

// MongoClient.connect(url, function (err, db) {
// 	if (err) throw err;

// 	// Bu yerga buyruq yoziladi
// 	var dbo = db.db("blog");
// 	dbo.createCollection("customers", function (err, res) {
// 		if (err) throw err;
// 		console.log("Toplam yaratildi!");
// 		db.close();
// 	});
// });

// MongoClient.connect(url, function (err, db) {
// 	if (err) throw err;
// 	var dbo = db.db("blog");
// 	var myobj = { name: "Company Inc", type: "Highway 37" };
// 	dbo.collection("customers").insertOne(myobj, function (err, res) {
// 		if (err) throw err;
// 		console.log("1 document inserted");
// 		db.close();
// 	});
// });



// const MongoClient = require('mongodb').MongoClient;

// const url = 'mongodb://localhost:27017';
// const dbName = 'blog';

// MongoClient.connect(url, function (err, client) {  // Eslatma: "client" o'zgaruvchisi "db" emas
// 	if (err) throw err;

// 	console.log("MongoDB ga ulanish muvaffaqiyatli bo'ldi!");

// 	const db = client.db(dbName);
// 	const collection = db.collection('customers');

// 	const myobj = { name: "Company Inc", type: "Highway 37" };

// 	collection.insertOne(myobj, function (err, res) {
// 		if (err) throw err;
// 		console.log("1 document inserted");
// 		client.close(); // Ulanishni yopish
// 	});
// });



const MongoClient = require('mongodb').MongoClient;

const url = 'mongodb://localhost:27017';
const dbName = 'blog';

async function run() {
	const client = new MongoClient(url);

	try {
		await client.connect();
		console.log("MongoDB ga ulanish muvaffaqiyatli bo'ldi.");

		const db = client.db(dbName);
		const collection = db.collection('customers'); // o'z kollektsiyangiz nomini yozinglection 

		// // Bu yerda birinchi elementni oladi
		// const search = await db.collection('customers').findOne();
		// console.log(search);

		// // Bu yerda "name" va "address" chiqaradi
		// const search = await db.collection('customers').find({},
		// 	{ projection: { _id: 0, name: 1, address: 1 } }).toArray();
		// console.log(search);

		// // Bu yerda esa faqat bitta manzilni chiqaradi 
		// var query = query = { address: "Park Lane 38" };
		// const search = await db.collection('customers').find(query).toArray();
		// console.log(search);

		// // Bu yerda biz hariflarga yoki 1 chi  harifiga qarab yozamiz
		var query = { address: /^S/ };
		const search = await db.collection('customers').find(query).toArray();
		console.log(search);

		// const search = await db.collection('customers').find({},
		// 	{ projection: { _id: 0 } }).toArray();
		// console.log(search[2].address);


		// Ma'lumotlarni olish
		// const data = await collection.find({}).toArray();
		// console.log(data);



		// Bu hato bormi yo'qmi bildiradi
	} catch (err) {
		console.error(err);


		// Bu yerda bitganini bildiradi
	} finally {
		await client.close();
	}
}

run().catch(console.dir);