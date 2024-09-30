import { MongoClient } from 'mongodb';

const url = 'mongodb://localhost:27017/mydb';

MongoClient.connect(url, function (err, db) {
	if (err) throw err;
	console.log('Database yaratildi');
	db.close();
});
