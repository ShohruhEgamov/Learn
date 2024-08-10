-- Jadval yaratish
CREATE TABLE contacts(
ism VARCHAR(50),
familya VARCHAR(50),
t_yil DATE,
kasb VARCHAR(50),
qiziqish VARCHAR(50),
id SERIAL NOT NULL PRIMARY KEY,
tel VARCHAR(60)
);

SELECT * FROM contacts;


-- Jadvalga malumot kiritish
INSERT INTO contacts (ism,familya,t_yil,kasb,qiziqish,tel) 
VALUES
	('Shohruh','Egamov','2000-12-21','Devaloper','Gaming','+79992372042'),
	('Diyorbek','Egamov','1994-04-14','Biznes','Driving','+79992372042'),
	('Bekmirza','Egamov','1996-11-21','Master','Football','+79992372042'),
	('Farruh','Egamov','1998-11-15','Transleter','Music','+79992372042'),
	('Gulmira','Egamova','1995-08-08','Quran','Quran','+79992372042'),
	('Shuhratjon','Ortikov','1996-08-25','Teacher','Music','+79992372042'),
	('Bekposhsha','Roziboyeva','1975-02-01','Quen','Quen','+79992372042');


-- Yangi qiziqish uchun jadval
CREATE TABLE qiziqish(
id SERIAL NOT NULL PRIMARY KEY,
name VARCHAR(50)
);


-- Qiziqishlarga kiritish
INSERT INTO qiziqish (name)
VALUES 
	('Gaming'),
	('Driving'),
	('Football'),
	('Music'),
	('Quran'),
	('Music'),
	('Quen');

SELECT * FROM qiziqish;

-- Bu yerda kasblarni yozamiz
CREATE TABLE kasb(
id SERIAL NOT NULL PRIMARY KEY,
name VARCHAR(50)
);

-- Bu yerda kasblarga kiritish
INSERT INTO kasb (name)
VALUES 
	('Devaloper'),
	('Biznes'),
	('Master'),
	('"Transleter"'),
	('Quran'),
	('Teacher'),
	('Quen');


SELECT * FROM contacts;