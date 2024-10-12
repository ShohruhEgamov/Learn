'use script'
function firstModule() {
	this.sayHello = function () {
		console.log('Hello World');
	}

	this.sayBy = function () {
		console.log('Bye World');
	}
}

module.exports = firstModule //Bu yerda modulni boshqalarga exsport qilamiz

// Exsport qilishning turlari

// 1 - usul
export { firstModule }

// 2 - usul
export const secconDar = 'Hello world'

// 3 - usul
export default firstModule()
// Bu usul orqali faqat bir marta qollansa bo'ladi bitta faylda

// Hamma funksiyalar quydagicha yoziladi
function slider({
	// Bu yerga hamma funksiyalarni nomlarini kiritish kerak
	container,
	slide,
	next,
	prev,
}) {
	// va bu funksiyalar yozilgan yerlarga buni yozib chiqish kerak
	// yana bu yerdagi classlar olingan const obyektlardan olishni unutmang
}


// Misol biron bir funksiyani import qilganda eng ustiga shunday qilinadi
import { slider } from './slider.js' // Bu yerda import qilish kerak
// Shunda bu funksiya bu yerda ham ishlashni boshlaydi

