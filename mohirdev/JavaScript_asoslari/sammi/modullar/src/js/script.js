'use script'
const module = require('./main')    // Bu yerda maindan modulni import qilamiz

const myModules = new module()
myModules.sayHello()               // Bu yerda modulni ishga tushiramiz
myModules.sayBy()                  // Bu seyby boduluni qaytaradi


// Avvalambor webpack ni yuklab lishimiz kerak
// npm i webpack webpack-cli -D

// Keyin webpack fayl ochiladi
// keyin bu yerda const orqali modullarga nom berib yukordagidey qilib import qilinidai
// keyin bu yerda modulni ishga tushiramiz
module()
// bunday qilib hammasini qilib chiqaningizdan keyin
// har bir modulga qayerda joylashgan bolsa shu klaslarni yoki funksiyalarni ichiga
// kiritib ketish kerak misol 'module('form', modalTimer, '[data-modal]')'

// misol bu yerga sliderni bunday beriladi
slider({
	container: '.offer__slider',
	wrapper: '.offer__slider-wrapper',
	inner: '.offer__slider-inner',
	prevArrow: '.offer__slider-prev',
	nextArrow: '.offer__slider-next',
	slidesToShow: 3,
	slidesToScroll: 1,
})
//Shunday hammasini chaqirib chiqaiz

// Keyin terminalga 'npx webpack' deb ishga tushiramiz

// import qilishning usullari
// 1 va 2 import qilish
import { firstModule } from './main'

// 3 usulni import qilish
import firstModule from './main'
//Bu yerda to'g'ridan to'gri import qilinadi

// Hamma exsportlarni yuklab olish
import * as main from './main'
console.log(main);


// try and catch bular xatoliklarni boshqarish

try {
	console.log('work');
	console.log(a);
	console.log('pracktic');
} catch (error) {
	console.log('error');
}
console.log('done');


//error.name bu qaytaradi
//error.message bu qaytaradi hatolik nima uchun ekanligini
//error.stack bu qaytaradi hatolik nima uchun ekanligini va qaysi qatorda ekanini
