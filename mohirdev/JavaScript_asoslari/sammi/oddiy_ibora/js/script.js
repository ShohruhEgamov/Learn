'use strict'

// Bu yerda oddiy iboralar yani bizga kerak bolmagan
// narsalarni o'chirish

new RegExp()

const firsName = prompt('Wat is your name', '')
const regex1 = /a/ig

console.log(firsName.search(regex1));
console.log(firsName.match(regex1));

const password = prompt('your password')
console.log(password.replace(/\|/g, '*'));


const num1 = '12-34-56-78-90'
console.log(num1.replace(/-/g, ':'));


const num2 = '100px'
console.log(num2.replace(/px/g, ''));


// Bu yerda agar men togri yozsam qabul qiladi blmasa qabul qilmaydi
const name3 = prompt('Name', '')
const regex2 = /egamov/gi

//d Bu faqat sonlarni qidiradi agar D bolsa not num
//w Bu faqat so'zlarni qidiradi agar W bolsa not world
//s Bu spaselarni qidiradi agar S bolsa not spese

if (regex2.test(name3)) {
	console.log('Salom boshliq')
} else {
	console.log('Boshliq emas')
}

const name = prompt('Yozing', '')
const regex3 = /\D/gi
console.log(name3.match(regex3));


// OOP ning getter va setter hususiyatlari

function Car(name, color, bonus) {
	this.name = name;    // Buni this va let qilishdan maqsad agar this bilan olinsa hamma yerda o'zgaradi
	this.color = color;
	let extraBonus = bonus; // let bilan olinsa bitta joda o'zgaradi

	this.info = function () {
		console.log(`Name of car: ${this.name}: color is ${this.color}. There is sam bons ${bonus}`);
	}
	// Bu getter
	this.getBonus = function () {
		return extraBonus;
	}
	// Bu setter
	//Bu yerda quydagi shartlar bajarilsa ishlatiladi bolmasa bermaydi
	this.setBonus = function (bonus) {
		if (typeof bonus == 'number' && bonus > 0 && bonus < 100) {
			extraBonus = bonus
		} else {
			console.log('Bonus not correct');
		}
	}
}

const bmw = new Car('bmw', 'black', 10)

console.log(bmw.getBonus());
bmw.setBonus(30)

bmw.info();