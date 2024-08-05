import mysql.connector
# SQL ni import qilish
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Shoh1221web:py",
  database="shohruh"
)
mycursor = mydb.cursor()


# Bu yerda yangi db yaratish 
mycursor.execute("CREATE DATABASE shohruh")

# Bu bor yoqligini tekshirish
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

# Bu yerda jadval yarattik
mycursor.execute("CREATE TABLE (jadval nomi) (name VARCHAR(255), address VARCHAR(255))")

# bu yerda jadvalni tekshirish
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

# Yangi jadval yaratadi kaliti bilan
mycursor.execute("CREATE TABLE shohruh (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# Jadvalga malumot kiritish
sql = "INSERT INTO shohruh (name, address) VALUES (%s, %s)"
val =  [ 
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')]

# Bu kop kiritish uchun
mycursor.executemany(sql, val)

# Har doimgidek o'zgarish kiritish ucun
mydb.commit()

print(mycursor.rowcount, "record inserted.")

# Bu birinchi identifikatorni oladi. kop bolsa oxirgi kiritilgan qatorning identifikatori qaytariladi.
print("1 record inserted, ID:", mycursor.lastrowid)

# Bu yerda jadvaldan olish

# Bu yerda u hammanarsani oladi
mycursor.execute("SELECT * FROM shohruh")

# Bu yerda esa u aytilganni oladi
mycursor.execute("SELECT name, address FROM shohruh")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)


'''Agar siz faqat bitta qatorga qiziqsangiz, fetchone()usuldan foydalanishingiz mumkin.'''


# Bu yerda esa filtr bilan tanlash

sql = "SELECT * FROM shohruh WHERE address = 'Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
	print(x)



# Bu yerda % belgisi bilan belgilash
sql = "SELECT * FROM shohruh WHERE address LIKE '%way%'"
# Bu belgi esa shu bolan boshlangan yoki tugagan qatorlarni qaytaradi

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


# Bu yerda esa qochishni belgilaydi

sql = "SELECT * FROM shohruh WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


# Bu yerda esa tartiblash 

sql = "SELECT * FROM shohruh ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
	print(x)


# Bu yerda esa teskari tartiblash 

sql = "SELECT * FROM shohruh ORDER BY name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
	print(x)



# Bu yerda ochirish

sql = "DELETE FROM shohruh WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")


# Bu yerda esa jadvalni o'chirish uchun...

mycursor = mydb.cursor()

sql = "DROP TABLE shohruh"
sql = "DROP TABLE IF EXISTS shohruh"

mycursor.execute(sql)


# Python MySQL yangilash jadvali

sql = "UPDATE shohruh SET address = 'Canyon 123' WHERE address = 'Valley 345'"

# sql = "UPDATE shohruh SET address = %s WHERE address = %s"
# val = ("Valley 345", "Canyon 123")

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")


#  Bu yerda esa nechta olishini belgilash
# mycursor.execute("SELECT * FROM shohruh LIMIT 5")

# Bu yerda qayerdan boshlab qayerda tugashi
mycursor.execute("SELECT * FROM shohruh LIMIT 5 OFFSET 2") 

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# Bu yerda esa jadvallarni qoshish
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

sql = "INSERT INTO users (name, email) VALUES (%s, %s)"

# Agar bu yerda LEFT dan foydalansangiz chapga RINGT desangiz onga qoshiladi.

val = ("John Doe", "john.doe@example.com")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
