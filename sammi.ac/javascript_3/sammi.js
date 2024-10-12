'use strict'

// const car = {
// 	mator: "X",
// 	color: "red",
// 	isAirbag: true,
// 	isSpeed: function () {
// 		console.log(320);

// 	}
// }

// const gm = {
// 	isAirbag: false,
// }

// gm.__proto__ = car;
// console.log(gm)

// Object.setPrototypeOf(gm, car)
// console.log(gm);

//                                                                              Amaliy mashgulotlar u bilan ishlash

const seriesDB = {
	count: 0,
	series: {},
	aktior: {},
	genres: [],
	private: false,
	start: function () {
		seriesDB.count = +prompt("Nechi serial ko'rgansiz?", '');

		while (
			seriesDB.count == '' ||
			seriesDB.count == null ||
			isNaN(seriesDB.count)
		) {
			seriesDB.count = +prompt("Nechi serial ko'rgansiz?", '');
		}
	},
	rememberMySeries: function () {
		for (let i = 0; i < 2; i++) {
			const a = prompt("Oxirgi ko'rgan serialingiz?", ''),
				b = prompt("Ushbu serial nechta qismdan iborat?", '');

			if (a != null && b != null && a != "" && b != "") {
				seriesDB.series[a] = b;
				console.log('done');
			}
			else {
				console.log('error');
				i--
			}
		}
	},
	detextLevelSeries: function () {
		if (seriesDB.count < 5) {
			console.log("Siz seriallarni kam ko'rgan ekansiz", '');
		}
		else if (seriesDB.count >= 5 && seriesDB.count < 10) {
			console.log("Siz seriallarni o'rtacha ko'rgan ekansi", '')
		}
		else if (seriesDB.count > 10) {
			console.log("Siz seriallarni juda ko'p ko'rgan ekansiz", '')
		}
		else {
			console.log('Error');
		}
	},

	visibleDB: function () {
		if (seriesDB.private) {
			seriesDB.private = false
		}
		else {
			seriesDB.private = true
		}
	},

	showDb: function () {
		if (!seriesDB.private) {
			console.log(seriesDB);
		}
	},
	writeGenres: function () {
		// for (let i = 0; i < 3; i++) {
		// 	const a = prompt(`Oxirgi ko'rgan serialingiz janri? ${i + 1}`);
		// 	if (a === "" || a === null) {
		// 		console.log('Siz notogri kiritingiz')
		// 		i--
		// 	}
		// 	else {
		// 		seriesDB.genres[i] = a;
		// 	}
		// }

		let genres = prompt("Yaxsi ko'rgan filimingi vergul bilan yoz").toLowerCase()
		if (genres === '' || genres === null) {
			console.log('Siz noto`ri malumot kiritingiz')
			i--

		}
		else {
			seriesDB.genres = genres.split(',')
			seriesDB.genres.sort()
		}

		seriesDB.genres.forEach((item, index) => {
			console.log(`Sizni yaxshi ko'rgan janringiz ${index + 1} nomi ${item}`);
		})
	}
}



//                                     dinamic typing

//   to string
console.log(typeof String(4));




// funksiyani obyektga aylantirish
function Car(name, color, mph) {
	this.name = name;
	this.color = color;
	this.airbag = true;
	this.mph = mph;
	this.speed = function () {
		console.log(`Speed of car ${this.name} is ${this.mph}`);

	}
}

Car.prototype.sayHello = function () {
	console.log(`Hello ${this.name}!`);
}

const bmw = new Car('bmw', 'red', 350);
const mers = new Car('mers', 'width', 300);

bmw.sayHello()
mers.sayHello()

bmw.speed();
mers.speed();



// context this - xar doim nimagadur qaram(osiladi)

function logger() {
	console.log(this);
}

logger()

// 1) Oddiy functionni cantenti this bo'sa xar doim windovga osiladi agar qattiq rejim yoniq bolsa undifaynedga teng

// Closure bu ozgaruvchini yuqoridan qidiradi

const a = 4;

function log() {
	const a = 5
	console.log(a);
}

log()

// 2) this obyektlarda nimaga osiladi. Bu cantext ni ichidagi metotda obyektning o'ziga teng

const obj = {
	x: 10,
	y: 20,
	sum: function () {
		console.log(this);

	}
}

obj.sum()


// bu yerda biz endi thisni boshqa obyektga call qilishini o`rganamiz

function lager() {
	console.log(this),
		console.log(this.nomi);

}

const mashina = {
	nomi: 'BMW',
	speed: 200,
}

// Usul call 
lager.call(mashina)

// usul apply
lager.apply(mashina)

// lager()

// uslul bind
function calc(number) {
	return this * number
}

const calcBind = calc.bind(5)
console.log(calcBind(10)) // 50


const btn = document.querySelector('button')

btn.addEventListener('click', function () {
	this.style.backgroundColor = 'red';  // yna bir yo'li (e) => {e.target usuli}
})

const object = {
	x: 10,
	y: 20,
	sem: function () {
		const bagger = () => {
			console.log(this.x);
		}
		bagger()
	}
}

object.sem() // 10

// Strelkali funksiya hech qanday contextga ega emas, u har doim tepasidagi contextga bog'liq qoladi...

// qisqa strelkali funksiya usuli

const abr = (a) => a + 16
console.log(abr(10)) // 26


//                                                                                       Classlar xaqida
class Car {
	constructor(name, year, speed) {
		this.name = name
		this.year = year
		this.speed = speed
	}

	calcSpeed() {
		return this.speed * 100
	}
}

const germni = new Car('BMW', 'Black', 200)
console.log(germni);


// Bu yerda Car dan avlodi obyekt oladi
class Lasetti extends Car {
	constructor(name, year, speed, color) {
		super(name, year, speed)   // Bu ichidagi obyektlarni otasidan meros olishi uchun
		this.color = color
	}

	ballon() {
		console.log(`Bu moshinaning ismi ${this.name} uning yili ${this.year} tezligi ${this.speed} rangi ${this.color}.`);
	}
}

const myCar = new Lasetti('Jentra', 2020, 220, 'white')
myCar.ballon()
//Bu moshinaning ismi Jentra uning yili 2020 tezligi 220 rangi white.

console.log(myCar.calcSpeed()); //22000


//                                                                                        Reast operatoer
// bu ...rest operatori qolgan qiymatlarni bir joyga massiv qilib yig'ib beradi 
function magger(a, b, ...rest) {
	console.log(a);
	console.log(b);
	console.log(rest);
}

magger(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

// Bu yerda def sukut boyicha aylanadi va agar qiymat berilmasa 10 ga teng bo'ladi
function sas(number, def = 10) {
	console.log(number + def);
}
sas(5) //15
sas(5, 5) //10



