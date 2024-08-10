-- Bu yerda table yaratish
CREATE TABLE cars (
  brand VARCHAR(255),
  model VARCHAR(255),
  year INT
);

-- Bu yerda jadvalni chiqarish uchun
SELECT * FROM cars;

-- Bu yerda qo'shish uchun
INSERT INTO cars (brand, model, year)
VALUES
  ('Chevralet', 'Lasetti', 2020),
  ('Chevralet', 'Cobalt', 2017),
  ('Toyota', 'Celica', 1975);

-- Bu yerda o'chirish uchun
DELETE FROM cars
WHERE brand = 'Ford' or brand = 'Chevralet';

-- Bu yerda o'zgartirish uchun
UPDATE cars
SET year = '1980', color = 'mokriy'
WHERE  id = 2;

-- Ustun nomlarini belgilash orqali biz qaysi ustunlarni tanlashni tanlashimiz mumkin:
SELECT brand, year FROM cars;

-- Bu yerda jadvalga o'zgazish kiritamiz
ALTER TABLE cars
ADD id SERIAL PRIMARY KEY;

ALTER TABLE cars
ADD mator VARCHAR(20);

-- Bu yerda tartiblash
SELECT * FROM cars ORDER BY id;


-- Bu yerda cheklov va shartlarni o'zgartiramiz
ALTER TABLE cars
ALTER COLUMN year TYPE VARCHAR(4);

-- Bu yerda esa olib tashlash
ALTER TABLE cars
DROP COLUMN mator;


-- Jadvaldagi barcha yozuvlarni o'chiring cars:
TRUNCATE TABLE cars;

-- Bu hammasini ochirib yuboradi
DROP TABLE cars;