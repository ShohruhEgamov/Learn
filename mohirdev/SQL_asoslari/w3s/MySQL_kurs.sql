CREATE DATABASE loyiha_db;

USE loyiha_db;

CREATE TABLE loyiha (
id INT serial default value,
ism VARCHAR(200),
familya VARCHAR(200),
yosh INT
);

INSERT INTO loyiha (ism,familya,yosh) VALUES 
('Shohruh','Egamov',23),
('Farrux','Egamov',25),
('Diyorbek','Egamov',29),
('Bekmirza','Egamov',27),
('Bekposhsha','Ro`zibayeva',18),
('Shuxrat','Ortikov',18);

SELECT * FROM loyiha;


-- Mijozlar jadvalining faqat dastlabki 3 ta yozuvini tanlang:
SELECT * FROM loyiha LIMIT 3;

SELECT * FROM loyiha
ORDER BY ism DESC
LIMIT 3;

SELECT MAX(id) FROM loyiha;


SELECT COUNT(DISTINCT ism)
FROM loyiha;


SELECT * FROM loyiha
WHERE ism LIKE 'Sh_h__h';

SELECT * FROM loyiha
WHERE ism LIKE '[S]%';


SELECT ism + ' ' + familya AS fulname,yosh From loyiha;

SELECT CONCAT(ism, ' ', familya) AS fullname, yosh 
FROM loyiha
LIMIT 1000;



CREATE TABLE xizmatchi (
id INT serial default value,
ism VARCHAR(200),
familya VARCHAR(200),
yosh INT
);

INSERT INTO xizmatchi (ism,familya,yosh) VALUES 
('as','dd',23),
('sad','ads',25),
('dsad','dsad',29),
('dasd','ff',27),
('ads','Ro`fdf',18),
('sdaf','fd',18);


-- Bu yerda agar UNION ALL bolsa takroriy qiymatlarni ham qaytaradi
select ism from loyiha
union
select ism from xizmatchi
order by ism;


SELECT ism, familya FROM loyiha
WHERE yosh = 23
UNION ALL
SELECT ism, familya FROM xizmatchi
WHERE yosh=27
ORDER BY ism;

SELECT COUNT(ism), familya
FROM loyiha
GROUP BY ism;


-- Bu yerda agar aytilgan shart togri bolsa true qaytaradi
SELECT ism
FROM loyiha
WHERE id = ANY
  (SELECT id
  FROM loyiha
  WHERE id = 1);


-- Bu yerda esa shartlar qoyiladi va birma bir tayorlanadi
SELECT ism, id,
CASE WHEN id > 3 THEN 'Bu mening akam'
	 WHEN id = 3 THEN 'Bu mening ukam'
	 ELSE 'Bu yerda mening o`zim'
END AS tofa
FROM loyiha;


-- Data beyslarni korish uchun
SHOW DATABASES;