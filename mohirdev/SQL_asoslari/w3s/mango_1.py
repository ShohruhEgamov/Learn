import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

print(myclient.list_database_names())

#                       Malumotlar bazasini tekshirish
dblist = myclient.list_database_names()
if "admin" in dblist:
  print("The database exists.")


#                       Bu yerda yangi data base yaratish
mydb = myclient('mydatabase')
mycol = mydb('xaridorlar')



# Toplam mavjudligini tekshirish
mydb = myclient['loyihalar']

mycol = mydb["admin"]

print(mydb.list_collection_names())



# Bu yerda yangi yaratish
# 'mydatabase' ma'lumotlar bazasini olish
mydb = myclient["loyihalar"]

# 'users' to'plamini (collection) olish
mycol = mydb["admin"]

# Ma'lumot qo'shish
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)

print(x.inserted_id)



mydb = myclient["loyihalar"]
mycol = mydb["admin"]

mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]


mydict = { "name": "Peter", "address": "Lowstreet 27" }

x = mycol.insert_many(mylist)

# Buyerda find_one() Birrasini qidirish uchun
y = mycol.find_one()

# Bu yerda hammasini topadi
# Bu yerda o'rniga nima qoyishini belgilaydi
for a in mycol.find({},{"_id": 0, "name": 1, "address": 1}):
	print(a)
# Agar biz 0 olsak u hech narsa olmaydi va qolganlari atamatik esa 1 ga teng bo'ladi

# print list of the _id values of the inserted documents:

print(y)

x = mycol.insert_many(mylist)
print(x.inserted_id)

# Sonini topish
print(x.inserted_ids)



# Bu yerda shart qoyib qidirish uychun

myquery = {"address": "Park Lane 38"}

# Bu yerda S va S dan katta harflar bolsa chiqaradi
myquery = { "address": {"$gt": "S"} }

# Oddiy iboralar orqali sorash

myquery = { "address": {"$regex": "^S"} }

mydoc = mycol.find(myquery)

# Bu yerda esa tartiblash uchun

mydoc = mycol.find().sort("name")

# Tartiblash turlari
# sort("ism", 1) #o'sish bo'yicha
# tartiblash("ism", -1) #kamayuvchi

for x in mydoc:
	print(x)



# Bitta hujjatni o'chirish uchun biz delete_one()usuldan foydalanamiz.
# Bir nechta hujjatni o'chirish uchun usuldan foydalaning delete_many().
myquery = { "address": "Mountain 21" }

mycol.delete_one(myquery)

for x in mycol.find():
  print(x)



myquery = { "address": {"$regex": "^S"} }

x = mycol.delete_many(myquery)

print(x.deleted_count, "documents deleted")


# Bu yerda esa to'plamni o'chirishingiz mumkin

mycol.drop()


# Bu yerrda esa yangilash
myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(myquery, newvalues)

# print "customers" after the update:
for x in mycol.find():
  print(x)


# MongoDB-da natijani cheklash uchun biz limit() usuldan foydalanamiz.
myresult = mycol.find().limit(5)

for x in myresult:
  print(x)
