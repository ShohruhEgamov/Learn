-- Bu yerda istalgan yeridan olish uchun
SELECT DISTINCT country FROM customers;


-- Bu yerda faqat belgilangan mijozlarni oladi
SELECT * FROM customers
WHERE city = 'London';


-- Bu yerda esa saralash uchun(price ni saralaydi)
SELECT * FROM products
ORDER BY price;


-- Teskari saralash
SELECT * FROM products
ORDER BY price DESC;


-- Bu yeda qancha kerakligini belgilaydi
SELECT * FROM customers
LIMIT 20;


-- Bu yerda qayerdan boshlab qancha kerakligini belgilaydi
SELECT * FROM customers
LIMIT 20 OFFSET 40;


-- Eng kattasi
SELECT MAX(price)
FROM products;

-- Eng kichigi
SELECT MIN(price)
FROM products;

-- Buni nomlash ham mumkin
SELECT MIN(price) AS eng_qimma
FROM products;  


-- Endi sonini bilish 
SELECT COUNT(customer_id)
FROM customers;


-- Bu yerda esa umumiy qiymati
SELECT SUM(quantity)
FROM order_details;


-- Funktsiya AVG() raqamli ustunning o'rtacha qiymatini qaytaradi.
SELECT AVG(price)
FROM products;


-- Qisqartirish uchun
SELECT AVG(price)::NUMERIC(10,1)
FROM products;


-- Endi qanday boshlangan yoki qanday tugagan harflar kerakligini yozamiz
SELECT * FROM customers
WHERE customer_name LIKE 'A%';
-- Eslatma: Operator LIKEkatta-kichik harflarga sezgir, agar siz katta-kichik harflarni sezgirsiz qidirishni xohlasangiz, ILIKEuning o'rniga operatordan foydalaning.



-- Bu yerda esa qanday boshlangan va _ bu chiziq  ta harf va qanday tugagan
SELECT * FROM customers
WHERE city LIKE 'L_nd__'; 

-- Operator IN WHERE bandida mumkin bo'lgan qiymatlar ro'yxatini belgilash imkonini beradi.
-- Operator IN bir nechta shartlarning qisqartmasi hisoblanadi OR.
SELECT * FROM customers
WHERE country IN ('Germany', 'France', 'UK');


SELECT * FROM customers
WHERE customer_id IN (SELECT customer_id FROM orders);

-- Yuqoridagi misoldagi natija 89 ta yozuvni qaytardi, ya'ni 2 ta mijoz buyurtma bermagan.
SELECT * FROM customers
WHERE customer_id NOT IN (SELECT customer_id FROM orders);


-- Operator BETWEEN o'z ichiga oladi: boshlang'ich va tugatish qiymatlari kiritilgan.
SELECT * FROM Products
WHERE Price BETWEEN 10 AND 15;



-- Bu yerda u alifbo tartibida p dan t gacha bolganni oladi
SELECT * FROM Products
WHERE product_name BETWEEN 'Pavlova' AND 'Tofu'
ORDER BY product_name;     



-- Kalit AS so'z ko'pincha ikki yoki undan ortiq maydonlar bittaga birlashtirilganda ishlatiladi.
-- Ikki maydonni birlashtirish uchun dan foydalaning || ' ' || qoshish va Bosh joy uchun
select product_name || ' ' || unit AS product
from products;


-- JOINIkki yoki undan ortiq jadvallar qatorlarini ular orasidagi tegishli ustun asosida birlashtirish uchun band ishlatiladi .
SELECT product_id, product_name, category_name
FROM products
INNER JOIN categories ON products.category_id = categories.category_id;


-- Kalit LEFT JOINso'z "chap" jadvaldan HAMMA yozuvlarni va "o'ng" jadvaldan mos yozuvlarni tanlaydi. Natija, agar mos kelmasa, o'ng tomondan 0 ta yozuv.
SELECT testproduct_id, product_name, category_name
FROM testproducts
LEFT JOIN categories ON testproducts.category_id = categories.category_id;


-- Kalit RIGHT JOINso'z "o'ng" jadvaldan HAMMA yozuvlarni va "chap" jadvaldan mos yozuvlarni tanlaydi. Natija, agar mos kelmasa, chap tomondan 0 ta yozuv.
SELECT testproduct_id, product_name, category_name
FROM testproducts
RIGHT JOIN categories ON testproducts.category_id = categories.category_id;   


-- Kalit FULL JOINso'z har ikkala jadvaldagi BARCHA yozuvlarni tanlaydi, hatto mos kelmasa ham. Mos keladigan satrlar uchun ikkala jadvaldagi qiymatlar mavjud, agar mos kelmasa, bo'sh maydonlar qiymatni oladi NULL.
SELECT testproduct_id, product_name, category_name
FROM testproducts
FULL JOIN categories ON testproducts.category_id = categories.category_id;


-- Bu shuni anglatadiki, "o'ng" jadvaldagi barcha yozuvlar "chap" jadvaldagi har bir yozuv uchun qaytariladi.
SELECT testproduct_id, product_name, category_name
FROM testproducts
CROSS JOIN categories;








