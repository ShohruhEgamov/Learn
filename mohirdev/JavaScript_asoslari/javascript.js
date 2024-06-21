'use strict';
function Salomlashish() {
	document.getElementById("salom").innerHTML = "Salom bu yerda nima qilayapsan"
}

function Alikolish() {
	document.getElementById("salom").style.display = 'none'
}

// window.alert(5 + 6)
// alert(5 + 10)

{
	let x, y, z;
	x = 6;
	y = 6;
	z = x + y;
	document.getElementById("bayonot").innerHTML = "The value of z is " + z + ".";
}

function yana_Ismla() {
	document.getElementById("demo1").innerHTML = "Salom Shohruh!";
	document.getElementById("demo2").innerHTML = "Yaxshimisiz";
}

document.getElementById("raqam").innerHTML = 10.50;
document.getElementById("son").innerHTML = (5 + 6) * 10;

/* The code below will change
the heading with id = "myH"
and the paragraph with id = "myP"
in my web page:*/


{
	x = 10;
	y = 6;
	z = x + y;
	document.getElementById('ozgaruvchi').innerHTML = "Bu yerdan ozgaruvchi: " + z;
}


{
	var x = 2;
	// Here x is 2
	var x = 10;
	// Here x is 10

	// Here x is 2
	document.getElementById("elon").innerHTML = x;
}

//                                                                JavaScript Const

{
	const cars = [" Saab", " Volvo ", " BMW"];
	cars[1] = " Tayotta";
	cars.push(" Lasetti");
	document.getElementById("moshina").innerHTML = cars;


	const car = { type: "Lasetti", model: "500", color: "white" }
	// car.color = "black";
	car.owner = "Johnson";
	document.getElementById("ranglar").innerHTML = "Bu o'zgargan " + car.color;
}


//                                                                JavaScript operatorlari

{
	let harf = 5;
	let harf2 = 8;
	let natija = harf > harf2;
	let harf4 = "G";
	let harf3 = "J";
	let natija2 = harf < harf2;
	document.getElementById("operator").innerHTML = "Bu yerda A harf B dan katta " + natija;
	document.getElementById("harflar").innerHTML = "Bu yer'da A harf B dan katta " + natija2;
}


//                                                                 JavaScript arifmetikasi

{

	x = 11;
	document.getElementById("arifmet").innerHTML = x ** 2;
	x = 5;
	document.getElementById("arifmet1").innerHTML = Math.pow(x, 2);
}


//                                                                 JavaScript Data Types
let b = BigInt("123456789012345678901234567890");
document.getElementById("bigint").innerHTML = b;

const cars = ["Saab", "Volvo", "BMW"];

document.getElementById("massiv").innerHTML = cars[1];

const person = {
	firstName: "Shohruh",
	lastName: "Egamov",
	yosh: 23,
	kozRangi: "black"
};

document.getElementById("objekt").innerHTML = person.firstName + " u " + person.yosh +
	" yoshga kirdi. Familyasi " + person.lastName;

// document.getElementById("taypeof").innerHTML =
// 	typeof "" +
// 	typeof "Shoh" +
// 	typeof "Egamov";

document.getElementById("taypeof").innerHTML =
	typeof "" + "<br>" +
	typeof "John" + "<br>" +
	typeof "John Doe" + "<br>" +
	typeof 0 + "<br>" +
	typeof 314 + "<br>" +
	typeof 3.14 + "<br>" +
	typeof (3) + "<br>" +
	typeof (3 + 4);

let car;
document.getElementById("undefn").innerHTML = typeof car;

//                                                                 JavaScript Functions

// function name(parameter1, parameter2, parameter3) {
// 	// code to be executed
//   }

function myFunction(p1, p2) {
	return p1 ** p2;
}

let natija = myFunction(4, 5);
document.getElementById("function").innerHTML = natija;

function buCelsius(f) {
	return (f - 32) * 5 / 9;
}


let lakal = "Malumot: " + typeof masNomi;
document.getElementById("lokal").innerHTML = lakal;

function mashinaNomi() {
	let masNomi = "Lasetti";
	let lakal = "Ichidagi: " + typeof masNomi + " " + masNomi;
	document.getElementById("lokal1").innerHTML = lakal.length;
	document.getElementById("lokal1").innerHTML = lakal;
}
mashinaNomi();


//                                                                 JavaScript ob'ektlari

const shaxs = {
	ism: "Shohruh",
	familya: "Egamov",
	id: 1221,
	toliqIsm: function () {
		return this.ism + " " + this.familya;
	}
}

document.getElementById("thisUsuli").innerHTML = shaxs.toliqIsm() + " Bu odam " +
	shaxs.ism + " Uning Familyasi " + shaxs.familya + " ID raqami " + shaxs.id;
document.getElementById("thisUsuli1").innerHTML = "Bu odam " + shaxs.ism;


//                                                                 JavaScript Events

let s = "John";
let c = new String("John");

document.getElementById("stri").innerHTML = typeof s + "<br>" + typeof c;


//                                                                 JavaScript string usullari

// var stringj = "HELLO WORD";
// document.getElementById("strd").innerHTML = stringj.charAt(1);

// var textar = "HELLO WORLD";
// document.getElementById("strd").innerHTML = textar.charAt(0);

// let codee = "SHOHRUH";
// document.getElementById("strd1").innerHTML = textar.charCodeAt(0);

// const codee = "SHOHRUH";
// let leter = codee.at(2);
// document.getElementById("strd1").innerHTML = leter;

// const text = "salom dunyo";
// let salom = text.at(6);
// document.getElementById("header").innerHTML = salom;
// console.log(text)

// let text = "salom dunyo";
// document.getElementById("header").innerHTML = text[1];
// console.log(text)

// let text = "olma, banan, anor";
// let part = text.slice(6,12);
// document.getElementById("header").innerHTML = part;               //slice()satrning bir qismini chiqaradi va chiqarilgan qismini yangi qatorga qaytaradi.
// console.log(text)

// let str = "Apple, Banana, Kiwi";
// document.getElementById("header").innerHTML = str.substring(7,13);
// console.log(text)

// let str = "Apple, Banana, Kiwi";
// document.getElementById("header").innerHTML = str.substr(7,7);
// console.log(text)

// function myFunction() {
// 	let text = document.getElementById("header").innerHTML;
//   document.getElementById("header").innerHTML = text.toUpperCase();
//   }
//   console.log(text)

// function myFunction() {
// 	let text = document.getElementById("header").innerHTML;
// 	document.getElementById("header").innerHTML = text.toLowerCase();
//   }
//   console.log(text)

// let text1 = "Shoxrux";
// let text2 = "Egamov";
// let text3 = "Shuxraat o'g'li";
// let text4 = text1.concat(" ",text2," ",text3)
// document.getElementById("header").innerHTML = text4;

// console.log(text)


// let text1 = "    Shoxrux    ";
// let text2 = text1.trim();

// document.getElementById("header").innerHTML = "Boshlangiz uzunlik: " +
// text1.length + "<br>Keyingi uzunlik: " + text2.length;

// console.log(text)

// let text = "1236";
// text = text.padStart(4,"X")
// document.getElementById("header").innerHTML = text;

// console.log(text)

// let num = 5;
// let text = num.toString();
// document.getElementById("header").innerHTML = text.padStart(4,"x");
// document.getElementById("header").innerHTML = text.padEnd(4,"x");

// console.log(text)

// let text = "SALOM ";
// let natija = text.repeat(2);

// document.getElementById("header").innerHTML = natija;

// console.log(text)

// function myFunction() {
// 	let text = document.getElementById("demo").innerHTML;
// 	document.getElementById("demo").innerHTML =
// 	text.replace(/Microsoft/g,"W3Schools");
//   }

// function myFunction() {
// 	let text = document.getElementById("demo").innerHTML;
// 	document.getElementById("demo").innerHTML =
// 	text.replace(/MICROSOFT/i,"W3Schools");
//   }

// let text = "I love cats. Cats are very easy to love. Cats are very popular."
// text = text.replaceAll("Cats","Dogs");
// text = text.replaceAll("cats","dogs");
// document.getElementById("demo").innerHTML = text;
// console.log(text)


// let text = "a,b,s,d,e,f";
// const menHaq = text.split("s");

// document.getElementById("demo").innerHTML = menHaq[0];
// console.log(text)


//                                                                 JavaScript string qidiruvi

// let text = "Salom shohruh men dasturchiman";
// let index = text.indexOf("dasturchiman");

// document.getElementById('header').innerHTML = index;
// console.log(text)

// let text = "Salom shohruh men dasturchiman men";
// let index = text.lastIndexOf("men");

// document.getElementById('header').innerHTML = index;
// console.log(text)

// let text = "Please locate where 'locate' occurs!";
// let index = text.lastIndexOf("locate", 15);

// document.getElementById('header').innerHTML = index;
// console.log(text)

// let text = "Please locate where 'locate' occurs!";
// let index = text.search("where");

// document.getElementById('header').innerHTML = index;
// console.log(text)

// let text = "The rain in SPAIN stays mainly in the plain";
// const myArr = text.match("in");

// document.getElementById('header').innerHTML = myArr.length + " " + myArr;
// console.log(text)

// let text = "The rain in  stays mainly in the plain";
// const myArr = text.match(/ain/gi);

// document.getElementById('header').innerHTML = myArr.length + " " + myArr;
// console.log(text)

// let text = "I love cats. Cats are very easy to love. Cats are very";
// const iterator = text.matchAll("Cats");

// document.getElementById('header').innerHTML = Array.from(iterator);
// console.log(text)

// let text = "I love cats. Cats are very easy to love. Catsd are very popular.";
// const iterator = text.matchAll(/Cats/gi);

// document.getElementById('header').innerHTML = Array.from(iterator);
// console.log(text)

// let text = "Hello world, welcome to the universe.";
// document.getElementById('header').innerHTML = text.includes("welcom");
// console.log(text)

// let text = "Hello world, welcome to the universe.";
// document.getElementById('header').innerHTML = text.startsWith("Hello");
// console.log(text)

// let text = "Hello world, welcome to the universe.";
// document.getElementById('header').innerHTML = text.endsWith("universe.");
// console.log(text)

//                                                                 JavaScript shablon satrlari

// let ism = "Shohruh";
// let familya = "Egamov";

// let text = `Salom ${ism} ${familya} yaxshimisiz.`
// document.getElementById('header').innerHTML = text.endsWith(".");
// console.log(text)

// let son = 10;
// let kurs = 0.25;

// let text = `Summa ${(son * (1 + kurs)).toFixed(2)}`
// document.getElementById('header').innerHTML = text.endsWith(".");
// console.log(text)


// let header = "Shohruhbek";
// let tags = ["Birinchi", "Ikkinchi", "Uchinchi"];

// let html = `<h2>${header}<h2><ul>`;
// for (const x of tags) {
// 	html += `<<li>${x}</li>`
// }

// html += `</ul>`;
// document.getElementById('header').innerHTML = html;
// console.log(text)

// let myNumber = 2;
// let txt = "";
// while (myNumber != Infinity) {
//    myNumber = myNumber * myNumber;
//    txt = txt + myNumber + "<br>";
// }
// document.getElementById("header").innerHTML = txt;
// console.log(header)


//                                                                 JavaScript BigInt

// let x = Number.MIN_SAFE_INTEGER;

// document.getElementById('header').innerHTML = x


// console.log(header)


// document.getElementById('header').innerHTML = Number.isInteger(10) + "<br>" + Number.isInteger(10.5)


// console.log(header)


//                                                                 JavaScript raqamlari usullari

// let x = 123;
// document.getElementById("header").innerHTML =
// 	x.toPrecision() + "<br>" +
// 	(123).toString() + "<br>" +
// 	(100 + 23).toString();

// console.log(header)

// let x = 9.656;
// document.getElementById("header").innerHTML =
// 	x.toExponential() + "<br>" +
// 	x.toExponential(2) + "<br>" +
// 	x.toExponential(6);

// console.log(header)

// let x = 9.656;
// document.getElementById("header").innerHTML =
// 	x.toFixed(0) + "<br>" +
// 	x.toFixed(2) + "<br>" +
// 	x.toFixed(4) + "<br>" +
// 	x.toFixed(6);

// console.log(header)

// let x = 9.656;
// document.getElementById("header").innerHTML =
// 	x.toPrecision() + "<br>" +
// 	x.toPrecision(2) + "<br>" +
// 	x.toPrecision(4) + "<br>" +
// 	x.toPrecision(6);


// console.log(header)

// let x = 9.656;
// document.getElementById("header").innerHTML =
// 	x.valueOf() + "<br>" +
// 	(123).valueOf() + "<br>" +
// 	(100 + 23).valueOf();


// console.log(header)

// document.getElementById("header").innerHTML =
//   parseInt("-10") + "<br>" +
//   parseInt("-10.33") + "<br>" +
//   parseInt("10") + "<br>" +
//   parseInt("10.33") + "<br>" +
//   parseInt("10 6") + "<br>" +
//   parseInt("10 years") + "<br>" +
//   parseInt("years 10");

// console.log(header)
// -10
// -10
// 10
// 10
// 10
// 10
// NaN


//                                                                 JavaScript massivlar va sanalar xususiyatlari

// const mevalar = ["Olma", "Nok", "Anor", "Behi"];
// let meUzunlik = mevalar.length;

// let text = "<ul>";
// for (let i = 0; i < meUzunlik; i++) {
//   text += "<li>" + mevalar[i] + "</li>";
// }
// text += "</ul>";

// document.getElementById("header").innerHTML = text;
// console.log(header)




// const mevalar = ["Olma", "Nok", "Anor", "Behi"];

// let text = "<ul>";
// mevalar.forEach(myFunks);
// text += "</ul>";

// document.getElementById("header").innerHTML = text;

// function myFunks(value){
//   text += "<li>" + value + "</li>";
// }
// console.log(header)




// const fruits = ["Banana", "Orange", "Apple"];
// fruits[6] = "Lemon";

// let fLen = fruits.length;
// let text = "";
// for (i = 0; i < fLen; i++) {
//   text += fruits[i] + "<br>";
// }

// document.getElementById("header").innerHTML = text;
// console.log(header)


// var fruits = ["Banana", "Orange", "Apple"];
// document.getElementById("demo").innerHTML = fruits instanceof Array;

// const fruits = ["Banana", "Orange", "Apple"];
// document.getElementById("demo").innerHTML = Array.isArray(fruits);

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// document.getElementById("header").innerHTML = fruits.join(" * ");

// // Log to console
// console.log(fruits)


// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// fruits.push("Kivi")
// document.getElementById("header").innerHTML = fruits;

// // Log to console
// console.log(fruits)

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// document.getElementById("header").innerHTML = fruits;
// document.getElementById("header").innerHTML = fruits.pop();
// // Log to console
// console.log(fruits)

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// document.getElementById("header").innerHTML = fruits;
// document.getElementById("header").innerHTML = fruits.shift();
// // Log to console
// console.log(fruits)


// const meva = ["Banana", "Orange", "Apple", "Mango"]
// // Log to console
// console.log(meva)


// let arr = [];

// console.log(arr instanceof Array); // true
// console.log(arr instanceof Object); // true
// console.log(Array.isArray(arr)); // true
// console.log(Object.prototype.toString.call(arr) === '[object Array]');

// const meva = ["apple", "banana", "cherry"];
// meva.forEach(function(narsa, son){
// 	console.log(son, narsa)
// })

// function Mosh(raqam, rusum) {
// 	this.raqam = raqam;
// 	this.rusum = rusum;
// }
// let myCar = new Mosh('Toyota', 'Corolla');

// console.log(myCar instanceof Mosh)

// let arr = [];

// console.log(arr instanceof Array); // true
// console.log(arr instanceof Number); // false
// console.log(Array.isArray(arr)); // true
// console.log(Object.prototype.toString.call(arr) === '[object Array]'); // true

// const user = {
// 	name: "ali",
// 	sayName: function(){
// 		const inner = () => {
// 			console.log(this.name);
// 		};
// 		inner();
// 	}
// };
// user.sayName();

// let fruits = ["Olma", "Banan", "Apelsin"];
// let result = fruits.join(", ");
// console.log(result); // "Olma, Banan, Apelsin"

// let numbers = [1, 2, 3, 4, 5];
// let result = numbers.join(" ");
// console.log(result); // "12345"


// let params = ["name=John", "age=30", "city=NewYork"];
// let queryString = params.join(" ");
// console.log(queryString); // "name=John&age=30&city=NewYork"

// let stack = [3, 4, 5, 1, 2,];
// while (stack.length > 2) {
//   let item = stack.pop();
//   console.log(item);
// }
// 5
// 4
// 3
// 2
// 1

// let sonlar = ["Birinchi"];
// sonlar.unshift("Ikkinchi");
// sonlar.unshift("Uchinchi");
// console.log(sonlar); // ["Uchinchi", "Ikkinchi", "Birinchi"]


// const myObj = {
// 	name: "John",
// 	age: 30,
// 	myCars: {
// 	  car1: "Ford",
// 	  car2: "BMW",
// 	  car3: "Fiat"
// 	}
//   }
//   let a = myObj.myCars.car2;
//   console.log(a)

// const fruits = ["Apple", "Orange", "Apple", "Mango"];
// let position = fruits.indexOf("Orange") + 1;

// let meva = "Apple is found in position " + position;
// console.log(meva)

// const numbers = [4, 9, 16, 25, 29];
// let first = numbers.find(myFunction);

// function myFunction(value, index, array) {
// 	return value > 18;
// }

// const meva = ["Banana", "Orange", "Apple", "Mango"]
// meva.sort()
// console.log(meva)

// const meva = ["Banana", "Orange", "Apple", "Mango"];
// meva.reverse()
// console.log(meva)

// const meva = ["Banana", "Orange", "Apple", "Mango"];
// meva.sort()
// meva.reverse()

// console.log(meva)

// const months = ["Jan", "Feb", "Mar", "Apr"];
// const reversed = months.toReversed();
// console.log(reversed);
// console.log(months);

// const points = [40, 100, 1, 5, 25, 10];
// points.sort(function(a, b){return a - b});
// console.log(points);

// const points = [40, 100, 1, 5, 25, 10];
// points.sort(function (a, b) {
// 	return a - b;
// });
// console.log(points);

// const numbers1 = [45, 4, 9, 16, 25];
// const numbers2 = numbers1.map(myFunction);

// console.log(numbers1);
// console.log(numbers2);

// function myFunction(value) {
// 	return value * 2;
// }

// const numbers = [45, 4, 9, 16, 25];

// let txt = "";
// numbers.forEach(myFunction);

// console.log(txt);

// function myFunction(value) {
// 	txt += value + "<br>";
// }

// const numbers = [1, 2, 3, 4];
// const squares = numbers.map(function(num) {
//   return num * num;
// });

// console.log(squares); // [1, 4, 9, 16]

// const users = [
// 	{ name: 'Alice', age: 25 },
// 	{ name: 'Bob', age: 30 },
// 	{ name: 'Charlie', age: 35 }
// ];

// const names = users.map(user => user.age);

// console.log(names); // ['Alice', 'Bob', 'Charlie']


// const numbers = [1, 2, 3, 4];
// const result = numbers.flatMap(num => [num, num * 2]);

// console.log(result);


// const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// const oddNumbers = numbers.filter(function(number) {
//   return number % 2 !== 0;
// });

// console.log(oddNumbers);

// const words = ["spray", "limit", "elite", "exuberant", "destruction", "present"];

// const longWords = words.filter(word => word.length > 6);

// console.log(longWords);
// // ["exuberant", "destruction", "present"]

// const numbers = [1, 2, 5, 4, 5];

// const sum = numbers.reduce(function(a, b) {
//   return a + b;
// }, 0);

// console.log(sum);
// // 15


// const numbers = [1, 2, 3, 4, 5];

// const sum = numbers.reduceRight(function(accumulator, currentValue) {
//   return accumulator + currentValue;
// }, 0);

// console.log(sum);
// // 15

// const words = ["hello", "world", "from", "reduceRight"];

// const sentence = words.reduceRight(function (accumulator, currentValue) {
// 	return accumulator + " " + currentValue;
// });

// console.log(sentence);
// "reduceRight from world hello"


// const numbers = [45, 4, 9, 16, 25];
// let allOver18 = numbers.every(myFunction);

// console.log(allOver18)

// function myFunction(value) {
// 	return value > 1
// }

// const numbers = [45, 4, 9, 16, 25];
// let allOver18 = numbers.some(myFunction);

// console.log(allOver18)

// function myFunction(value) {
// 	return value > 40
// }

// const myArr = Array.from("ABCDEFG");
// console.log(myArr); // ["A", "B", "C", "D", "E", "F", "G"]

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// const keys = fruits.keys();

// let text = "";
// for (let x of keys) {
//   text += x + "<br>";
// }

// console.log(text)

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// const f = fruits.entries();

// for (let x of f) {
// 	console.log(x);
// }

// const months = ["Januar", "Februar", "Mar", "April"];
// const myMonths = months.with(2, "March");
// console.log(myMonths); // ["Januar", "Februar", "March", "April"]assistant

// const q1 = ["Jan", "Feb", "Mar"];
// const q2 = ["Apr", "May", "Jun"];
// const q3 = ["Jul", "Aug", "Sep"];
// const q4 = ["Oct", "Nov", "May"];

// const year = [...q1, ...q2, ...q3, ...q4];
// console.log(year)

// const d = new Date();
// const n = d.toDateString();
// console.log(n)

// const msec = Date.parse("dec 21, 2000");
// console.log(msec)

// const d = new Date("2000-12-21")
// console.log(d.getFullYear())

// const months = ["January","February","March","April","May","June","July","August","September","October","November","December"];
// const d = new Date();
// let month = months[d.getMonth()];
// console.log(month);

// const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

// const d = new Date();
// let day = days[d.getDay()];
// console.log(day)

// const d = new Date();                           //Usul getTimezoneOffset()mahalliy vaqt va UTC vaqti o'rtasidagi farqni (daqiqalarda) qaytaradi:
// let year = d.getTimezoneOffset();
// console.log(year)


// const d = new Date();
// // d.setFullYear(2000);
// // d.setFullYear(2020, 11, 3);
// // d.setMonth(11);
// // d.setDate(15);
// // d.setDate(d.getDate() + 100);
// d.setHours(22);
// console.log(d)

// let text;
// const today = new Date();
// const someday = new Date();
// someday.setFullYear(2000, 11, 21);

// if (someday > today) {
// 	text = "Today is before December 21, 2000.";
//   } else {
// 	text = "Today is after December 21, 2000.";
//   }
// console.log(text)

//                                                                 JavaScript matematika xususiyatlari

// let a = "Math.E:  " + Math.E +
// "Math.PI:" + Math.PI +
// "Math.SQRT2: " + Math.SQRT2 +
// "Math.SQRT1_2:  " + Math.SQRT1_2 +
// "Math.LN2:  " + Math.LN2 +
// "Math.LN10:  " + Math.LN10 +
// "Math.LOG2E:  " + Math.LOG2E +
// "Math.Log10E:  " + Math.LOG10E;

// console.log(a)

// console.log(Math.round(4.4))
// console.log(Math.ceil(4.2))
// console.log(Math.floor(4.6))
// console.log(Math.trunc(4.6))
// console.log(Math.sign(4.6))
// console.log(Math.pow(8, 2))
// console.log(Math.sqrt(16))
// console.log(Math.abs(-4.6))
// console.log("The sine value of 90 degrees is " + Math.sin(90 * Math.PI / 180))
// console.log("The sine value of 90 degrees is " + Math.cos(0 * Math.PI / 180))
// console.log(Math.min(0, 150, 30, 20, -8, -200))
// console.log(Math.max(0, 150, 30, 20, -8, -200))
// console.log(Math.random())

// console.log(Math.log(-1)) // NaN
// console.log(Math.log(-0)) // -Infinity
// console.log(Math.log(0)) // -Infinity
// console.log(Math.log(1)) // 0
// console.log(Math.log(10)) // 2.302585092994046
// console.log(Math.log(Infinity))// Infinity

// function buYerda(x, y) {
// 	return Math.log(y) / Math.log(x);
// }

// console.log(buYerda(2, 8));     // 2 x 2 x 2 = 8 Expected output: 3


// console.log(buYerda(5, 625));    // 5 x 5 x 5 x 5 = 625 Expected output: 4


// console.log(Math.log2(16))

//                                                                 JavaScript random xususiyatlari

// const ism = ['shoh', 'far', 'bek', 'diy']
// const f = ism.keys();
// console.log(Math.floor(Math.random() * f))

// console.log(Math.floor(Math.random() * 10))

// function getRndInteger(min, max) {
// 	return Math.floor(Math.random() * (max - min)) + min;
//   }

// function getRndInteger(min, max) {
// 	return Math.floor(Math.random() * (max - min + 1) ) + min;
//   }

//                                                                 JavaScript random xususiyatlari

// const booolen = ["100 is " + Boolean(100) +
// 	"3.14 is " + Boolean(3.14) +
// 	"-15 is " + Boolean(-15) +
// 	"Any (not empty) string is " + Boolean("Hello") +
// 	"Even the string 'false' is " + Boolean('false') +
// 	"Any expression (except zero) is " + Boolean(1 + 7 + 3.14)]

// console.log(booolen)

// let name = null;
// let text = "missing";
// let result = name ?? text;
// console.log(result); // "missing"assistant

//                                                                        JavaScript if else xossalari

// if (new Date().getHours() < 8) {
// 	console.log("Good day!");
// }

// else (
// 	console.log("Good morning!")
// )

// const time = new Date('March 13, 08 24:20').getHours();
// let greeting;
// if (time < 10) {
// 	greeting = "Good morning";
// }

// else if (time < 20) {
// 	greeting = "Good day";
// }

// else if (time < 24) {
// 	greeting = "Good ningt";
// }
// else {
// 	greeting = "Good evening";
// }

// console.log(greeting)



// function taqqoslash(a) {
// 	let result;
// 	if (a > 0) {
// 		result = "Musbat son";
// 	}
// 	else if (a < 0) {
// 		result = "Manfiy son";
// 	}
// 	else {
// 		result = "Manfiy son";
// 	}
// 	return result;
// }
// console.log(taqqoslash(5))


// let day;
// switch (new Date().getDay()) {
// 	case 0:
// 		day = "Yakshanba";
// 		break;
// 	case 1:
// 		day = "Dushanba";
// 		break;
// 	case 2:
// 		day = "Seshanba";
// 		break;
// 	case 3:
// 		day = "Chorshanba";
// 		break;
// 	case 4:
// 		day = "Payshanba";
// 		break;
// 	case 5:
// 		day = "Juma";
// 		break;
// 	case 6:
// 		day = "Shanba";
// 		break;
// }
// console.log(day)

// let text;
// switch (new Date().getDay()) {
// 	case 6:
// 		text = "Today is Saturday";
// 		break
// 	case 0:
// 		text = "Today is Sunday";
// 		break;
// 	default:
// 		text = "Looking forward to the Weekend";
// }
// console.log(text)


// let text;
// switch (new Date().getDay()) {
// 	case 4:
// 	case 5:
// 		text = "Bugun ish kuni"
// 		break;
// 	case 0:
// 	case 6:
// 		text = "Bugun dam olish"
// 		break;
// 	default:
// 		text = "Bugun ish vaqtida"
// }
// console.log(text)

// let x = "1";

// switch (x) {
// 	case "0":
// 		text = "Off"
// 		break;
// 	case "1":
// 		text = "On"
// 		break;
// 	default:
// 		text = "No value found"
// }
// console.log(text)


//                                                                        JavaScript loop for xossalari

// const carss = ["BMW", "Volvo", "Saab", "Ford", "Fiat", "Audi"];
// let = text = "";

// for (let i = 0; i < carss.length; i++){
// 	text += carss[i];
// }
// console.log(text)

// let text = "";

// for (let i = 0; i < 5; i++) {
//   text += " The number is " + i;
// }

// for (let i = 0, len = carss.length, text = ""; i < len; i++) {
// 	text += carss[i]";
//   }

// const carss = ["BMW", "Volvo", "Saab", "Ford"];
// let i = 2;
// let len = carss.length;
// let text = "";

// for (; i < len; i++) {
//   text += carss[i];
// }
// console.log(text)

// const carss = ["BMW", "Volvo", "Saab", "Ford"];

// let i = 0;
// let len = carss.length;
// let text = " ";

// for (; i < len;) {
//   text += carss[i] + ' ';
//   i++;
// }
// console.log(text)

// const foo = 5;
// let output = "Output: ";
// switch (foo) {
//   case 0:
//     output += "So ";
//   case 1:
//     output += "What ";
//     output += "Is ";
//   case 2:
//     output += "Your ";
//   case 3:
//     output += "Name";
//   case 4:
//     output += "?";
//     console.log(output);
//     break;
//   case 5:
//     output += "!";
//     console.log(output);
//     break;
//   default:
//     console.log("Please pick a number from 0 to 5!");
// }

// const Animal = "Giraffe";
// switch (Animal) {
//   case "Cow":
//   case "Giraffe":
//   case "Dog":
//   case "Pig":
//     console.log("This animal is not extinct.");
//     break;
//   case "Dinosaur":
//   default:
//     console.log("This animal is extinct.");
// }

// const expr = "Bananas";
// switch (expr) {
// 	case "Oranges":
// 		console.log("Oranges are $0.59 a pound.");
// 		break;
// 	case "Apples":
// 		console.log("Apples are $0.32 a pound.");
// 		break;
// 	case "Bananas":
// 		console.log("Bananas are $0.48 a pound.");
// 		break;
// 	case "Cherries":
// 		console.log("Cherries are $3.00 a pound.");
// 		break;
// 	case "Mangoes":
// 	case "Papayas":
// 		console.log("Mangoes and papayas are $2.79 a pound.");
// 		break;
// 	default:
// 		console.log(`Sorry, we are out of ${expr}.`);
// }

// console.log("Is there anything else you'd like?");

// const action = "say_hello";
// switch (action) {
//   case "say_hello": {
//     const message = "hello";
//     console.log(message);
//     break;
//   }
//   case "say_hi": {
//     const message = "hi";
//     console.log(message);
//     break;
//   }
//   default: {
//     console.log("Empty action received.");
//   }
// }


// let str = '';

// for (let i = 0; i < 9; i++) {
//   str = str + i;
// }

// console.log(str);
// // Expected output: "012345678"


//                                                                        JavaScript loop for in xossalari

const persons = {
	fname: 'Shohruh',
	lname: 'Egamov',
};
persons.fname = "Farrux";
let txt = "";
for (let x in persons) {
	txt += persons[x] + " ";
}
console.log(`Salom janob ${txt}sizni tabriklayman`);



const numberss = [45, 4, 9, 16, 25];

let txtt = "";
numberss.forEach(meFunksiyam);
console.log(txtt);

function meFunksiyam(value, index, array) {
	txtt += value + " ";
}


const carsr = ["BMW", "Volvo", "Mini"];

let text0 = "";
for (let x of carsr) {
	text0 += x + " ";
}

console.log(text0);


//                                                       bu yerda shifirlangan matinni topish
let language = "JavaScript";

let matn = "";
for (let x of language) {
	matn += x + "edSCFVCvvnsSjdFV215Cenj";
}
let ol = matn;
ol = ol.replaceAll(/edSCFVCvvnsSjdFV215Cenj/ig, "");

console.log(ol);
console.log(matn);




//                                             bu yerda whileni topish
let son = "";
let i = 0;
while (i < 10) {
	son += "Bu son: " + i + " ";
	i++;
}

console.log(son);


let soz = "";
let d = 0;

do {
	soz += "Bu soz: " + d + " ";
	d++;
}
while (d > 10);
console.log(soz);


const moshina = ["BMW", "Volvo", "Saab", "Ford"];

let m = 0;
let rusum = "";
for (; moshina[m];) {
	rusum += moshina[m] + " ";
	m++;
}

console.log(moshina);


const moshinaWhile = ["BMW", "Volvo", "Saab", "Ford"];

let mWh = 0;
let rusumWh = "";
while (moshinaWhile[mWh]) {
	rusumWh += moshinaWhile[mWh] + " ";
	mWh++;
}

console.log(moshinaWhile);


//                                                                        JavaScript break xossalari
let br = "";
for (let j = 0; j < 10; j++) {
	if (j === 3)
		break;
	br += j + " ";
}
console.log(br);

let brc = "";
for (let c = 0; c < 10; c++) {
	if (c === 3)
		continue;
	else if (c === 8)
		break;
	brc += c + " ";
}
console.log(brc);


const cars2 = ["BMW", "Volvo", "Saab", "Ford"];
let text8 = "";

list: {
	text8 += cars2[0] + "<br>";
	text8 += cars2[1] + "<br>";
	break list;
	text8 += cars2[2] + "<br>";
	text8 += cars2[3] + "<br>";
}

console.log(text8);

//                                                                        JavaScript iterator xossalari

function menRaqamim() {
	let n = 0;
	return {
		next: function () {
			n += 100;
			return { value: n, done: true };
		}
	};
}

const n = menRaqamim();
n.next();
n.next();
n.next();
n.next();

console.log(n.next().value);



buRaqam = {};

buRaqam[Symbol.iterator] = function () {
	let g = 0;
	let done = false;
	return {
		next() {
			g += 10;
			if (g === 100) {
				done = true;
			}
			return { value: g, done: done };
		}
	};
};

let yangi = "";
for (let i of buRaqam) {
	yangi += i + " ";
}

console.log(yangi);


//                                                                        JavaScript set xossalari
let set = new Set([1, 2, 31, 40, 5]);
console.log(`Bu yerda ${set.size} bor`);


const letters1 = new Set();
letters1.add("a");
letters1.add("b");
letters1.add("c");

console.log(letters1.size);

const letters2 = new Set(["a", "b", "c"]);

let text2 = "";
for (const x of letters2) {
	text2 += x + " ";
}

console.log(text2);

// usul has() ichidagi belgi setda bo'lsa true bo'lmasa false chiqaradi
const letters3 = new Set(["a", "b", "c"]);
answers = letters3.has("b");
console.log(answers);


const letters4 = new Set(["a", "b", "c"]);
let text4 = "";
letters4.forEach(function (value) {
	text4 += value + " ";
})

console.log(text4);

// usul entries
const entr = new Set(["a", "b", "c"]);

const iterator = entr.entries();

let mat = "";
for (let entry of iterator) {
	mat += entry + " ";
}

console.log(mat);


//                                                                        JavaScript Map() xossalari
//Usul get()Xaritadagi kalitning qiymatini oladi:
//Xaritaga elementlarni quyidagi set()usul bilan qo'shishingiz mumkin:
//Usul set()mavjud Xarita qiymatlarini o'zgartirish uchun ham ishlatilishi mumkin:
//Xususiyat size xaritadagi elementlar sonini qaytaradi:
//Usul delete()xarita elementini olib tashlaydi:
//Usul clear()xaritadan barcha elementlarni olib tashlaydi:
//has()Agar kalit xaritada mavjud bo'lsa, usul true ni qaytaradi :

const fruk = new Map([
	["olma", 500],
	["banan", 600],
	["shaftoli", 700]
]);
fruk.set("nok", 800)
fruk.set("olma", 1800)
let nur = fruk.get("olma");
console.log(nur);
console.log(fruk.get("banan"));
console.log(fruk.delete("shaftoli"));
console.log(fruk.size);

const frukt = new Map([
	["olma", 500],
	["banan", 600],
	["shaftoli", 700]
]);

//Usul forEach()xaritadagi har bir kalit/qiymat juftligi uchun qayta qo'ng'iroqni chaqiradi:
let yana = "";
frukt.forEach(function (value, key) {
	yana += key + ": " + value + " ";
})
console.log(yana);

//Usul entries()xaritadagi [kalit, qiymatlar] bilan iterator ob'ektini qaytaradi:
let entre = "";
for (let entry of frukt.entries()) {
	entre += entry + " ";
}
console.log(entre);

//Usul keys()xaritadagi kalitlarga ega iterator ob'ektini qaytaradi:
//Usul values()xaritadagi qiymatlar bilan iterator ob'ektini qaytaradi:
let keyse = "";
for (const x of frukt.keys()) {
	keyse += x + " ";
}
console.log(keyse);


const apples = { name: 'Apples' };
const bananas = { name: 'Bananas' };
const oranges = { name: 'Oranges' };


const fruits5 = new Map();


fruits5.set(apples, 500);
fruits5.set(bananas, 300);
fruits5.set(oranges, 200);

console.log(fruits5.get(apples));

//JavaScript Map.groupBy()

const fruits = [
	{ name: "apples", quantity: 300 },
	{ name: "bananas", quantity: 500 },
	{ name: "oranges", quantity: 200 },
	{ name: "kiwi", quantity: 150 }
];

function myCallback({ quantity }) {
	return quantity > 200 ? "ok" : "low";
}

const groupBy = (array, callback) => {
	const map = new Map();
	array.forEach(item => {
		const key = callback(item);
		if (!map.has(key)) {
			map.set(key, []);
		}
		map.get(key).push(item);
	});
	return map;
};

const result = groupBy(fruits, myCallback);

let text = "These fruits are Ok:    ";
for (let x of result.get("ok")) {
	text += x.name + " " + x.quantity + " ";
}

text += "  These fruits are low:   ";
for (let x of result.get("low")) {
	text += x.name + " " + x.quantity + "  ";
}
console.log(text);

console.log(result.get("ok"));




const person8 = {
	firstName: "Shohruh",
	lastName: "Egamov",
	age: 50
};

let { firstName: name, lastName: familya, country = "UZ" } = person8;

console.log(familya + " " + name + " " + country);
console.log(person8);

const fruits7 = ["Bananas", "Oranges", "Apples", "Mangos"];

const { [0]: m1, [1]: m2 } = fruits7;
console.log(m1 + " " + m2);


const numbers = [10, 20, 30, 40, 50, 60, 70];


const a = numbers.find(num => num < 30);
const b5 = numbers.find(num => num >= 30 && num < 50);
const rest = numbers.filter(num => num >= 50);

console.log(a);  // 10
console.log(b5);  // 30
console.log(rest);  // [50, 60, 70]

let firstName = "John";
let lastName = "Doe";
[firstName, lastName] = [lastName, firstName];
console.log(firstName + " " + lastName);


let qidiru = "Salom men Shohruh";
let n8 = qidiru.search(/shohruh/i)
console.log(n8);


let almashtir = "Salom Shohruh Egamov men Asad man";
let javoblari = almashtir.replace(/asad/i, "Diyor");
console.log(javoblari);


let regext = "Salom men Shohruh dasturchiman";
const pattern = /j/;
console.log(pattern.test(regext));


const obj = /e/.exec("The best things in life are free!");
let xs = `U ${obj[0]} yerda va ${obj.index} pozitsionda matni esa: ${obj.input}`;
console.log(xs);


function myFunction() {
	let age = 15;
	let voteable = (age < 18) ? "Too young" : "Old enough";
	console.log(voteable + " to vote.");
}

try {
	aflet("Salom mehmon");
}
catch (err) {
	err.message;
}





//Raqam yozganda uning raqam yoki son ligini tekshirib hato malumotni chiqaradi
{/* <h2>JavaScript try catch</h2>

<p>Please input a number between 5 and 10:</p>

<input id="demo" type="text">
<button type="button" onclick="myFunction()">Test Input</button>
<p id="p01"></p> */}

function myFunction() {
	const message = document.getElementById("p01");
	message.innerHTML = "";
	let x = document.getElementById("demo").value;
	try {
		if (x.trim() == "") throw "empty";
		if (isNaN(x)) throw "not a number";
		x = Number(x);
		if (x < 5) throw "too low";
		if (x > 10) throw "too high";
	}
	catch (err) {
		message.innerHTML = "Input is " + err;
	}
}



let num = 123.456;

// toFixed() ga 100 argumenti berilganda
try {
	console.log(num.toFixed(100));
} catch (e) {
	console.log(e.name + ": " + e.message);  // RangeError: toFixed() digits argument must be between 0 and 100
}

try {
	let arr = new Array(-1);
} catch (e) {
	console.log(e.name + ": " + e.message);  // RangeError: Invalid array length
}


function recursive() {
	try {
		return recursive();
	} catch (e) {
		console.log(e.name + ": " + e.message);  // RangeError: Maximum call stack size exceeded
	}
}

recursive();


try {
	let num = 1;
	num.toFixed(101);  // noto'g'ri argument
} catch (e) {
	if (e instanceof RangeError) {
		console.log("RangeError qo'lga olindi: " + e.message);
	} else {
		console.log("Boshqa xato: " + e.message);
	}
}


try {
	let result = someFunction();
} catch (error) {
	console.error("Xato qo'lga olindi:", error.message);
}

try {
	// Xatolik bo'lishi mumkin bo'lgan kod
	let result = someFunction();
} catch (error) {
	// Xato qo'lga olinadi va qayta ishlanadi
	console.error(error);
}

try {
	let result = someFunction();
} catch (error) {
	console.error("Xato qo'lga olindi:", error.message);
} finally {
	console.log("Bu har doim bajariladi.");
}


try {
	// Xato bo'lishi mumkin bo'lgan kod
	let result = someFunction();

	// Sun'iy xato yaratish
	if (result < 0) {
		throw new Error("Natija manfiy bo'lishi mumkin emas.");
	}

} catch (error) {
	// Xato qo'lga olinadi va qayta ishlanadi
	console.error("Xato qo'lga olindi:", error.message);
} finally {
	// Bu blok har doim bajariladi
	console.log("Bu har doim bajariladi.");
}

try {
	eval('foo bar');
} catch (e) {
	if (e instanceof EvalError) {
		console.error("EvalError qo'lga olindi:", e.message);
	} else {
		console.error("Boshqa xato qo'lga olindi:", e.message);
	}
}


try {
	eval('var x = ;');  // Sintaksis xatosi
} catch (e) {
	console.log(e.name);     // SyntaxError
	console.log(e.message);  // Unexpected token ;
	console.log(e.stack);    // Xato stack izi
}


try {
	// Bu yerda xato bo'lishi mumkin bo'lgan kod
	let result = someFunction();
} catch (e) {
	if (e instanceof RangeError) {
		console.error("RangeError qo'lga olindi:", e.message);
	} else if (e instanceof ReferenceError) {
		console.error("ReferenceError qo'lga olindi:", e.message);
	} else if (e instanceof TypeError) {
		console.error("TypeError qo'lga olindi:", e.message);
	} else if (e instanceof URIError) {
		console.error("URIError qo'lga olindi:", e.message);
	} else {
		console.error("Boshqa xato qo'lga olindi:", e.message);
	}


}

let salom = "";
salom = function () {
	return "Salom Dunyo"
}
console.log(hello());


let hello5 = "";

hello5 = () => {
	return "Salom Dunyo"
}

console.log(hello5());


let hello = "";
hello1 = (val, alik) => "Salom " + val + " " + alik;
console.log(hello1("Dunyo", "Shohruh"));

//hello = val => "Hello " + val;
let x89 = "";
salom1 = () => {
	console.log(x89 += this);
}

window.addEventListener("load", salom1)

console.log(salom1("Salom").addEventListener("clik", salom1));


class myCarf {
	constructor(brand, year, color) {
		this.brand = brand;
		this.year = year;
		this.color = color;
	}
}

const myyCar1 = new Car("BMW", 2014, "black");
const myyCar2 = new Car("Lasetti", 2019, "width");
const myyCar3 = new Car("Tico", 2018, "red");

console.log(myyCar1.brand + " " + myyCar2.brand);


let textjson = '{ "employees" : [' +
	'{ "firstName":"Shohruh" , "lastName":"Egamov" },' +
	'{ "firstName":"Farrux" , "lastName":"Egamov" },' +
	'{ "firstName":"Diyorbek" , "lastName":"Egamov" },' +
	'{ "firstName":"Bekmirza" , "lastName":"Egamov" } ]}';

const objeckt = JSON.parse(textjson);
console.log(objeckt.employees[2].firstName + " " + objeckt.employees[1].lastName);

let x = 0.1;
let y = 0.2;
// let z = x + y;  // bu yerda hazo beradi 0.30000000000000004
let z = (x * 10 + y * 10) / 10; // bu yerda to'ri beradi 0.3
console.log(z);


let y5 = "hello \
word";            //Agar buzishni hohlasangiz bunday \ usuldan foydalaning

console.log(y5);

if (typeof myObj !== "undefined" && myObj !== null);



function Personn(ism, familya, yosh) {
	this.firstName = ism;
	this.lastName = familya;
	this.age = yosh;
}

const meningOtam = new Personn("Shuhrat", "Egamov", 56);
const meningOnam = new Personn("Shuhrat", "Egamov", 56);



function Person2(first, last, age, eye) {
	this.firstName = first;
	this.lastName = last;
	this.age = age;
	this.eyeColor = eye;
}

Person2.prototype.natsional = "English";
const myFather = new Person2("John", "Doe", 50, "blue");
console.log(myFather.natsional);

/*Object.entries() metodi JavaScript-da obyektning o'ziga tegishli sanab o'tiladigan 
xossalari (enumerable properties) va xususiyatlarining [key, value] juftliklari ko'rinishidagi 
massivlarni qaytaradi. Bu metod obyektning barcha sanab 
o'tiladigan xossalarini o'z ichiga olgan massivni hosil qiladi.*/
const person10 = {
	firstName: "Shohruh",
	lastName: "Egamov",
	age: 23,
	eyeColor: "Qora"
};

const person20 = { firstName: "Shuhrat", lastName: "Ortikov" };
Object.assign(person10, person20);

let texttt = Object.entries(person10);
console.log(texttt);


const objg = { a: 1, b: 2, c: 3 };

const entries = Object.entries(objg);

console.log(entries); // [ ['a', 1], ['b', 2], ['c', 3] ]


const objh = { a: 1, b: 2, c: 3 };

for (const [key, value] of Object.entries(objh)) {
	console.log(`${key}: ${value}`);
}

// Natija:
// a: 1
// b: 2
// c: 3


const fruitsh = { Bananas: 300, Oranges: 200, Apples: 500 };

let texth = "";

for (let [fruit, amount] of Object.entries(fruitsh)) {
	texth += fruit + ": " + amount + " ";
}

console.log(texth);


const fruitsb = { Bananas: 300, Oranges: 200, Apples: 500 };
const myMap = new Map(Object.entries(fruitsb));
console.log(myMap);

/*Object.fromEntries() metodi JavaScript-da Object.entries() ning teskarisi bo'lib, 
[key, value] juftliklari ko'rinishidagi massivdan ob'ekt hosil qiladi. Bu metod massivlar yoki xaritalar (maps) 
ko'rinishidagi ma'lumotlarni ob'ekt sifatida qayta shakllantirish uchun ishlatiladi.*/

const objk = { a: 1, b: 2, c: 3 };

const transformed = Object.entries(objk).map(([key, value]) => [key, value * 2]);

const newObj = Object.fromEntries(transformed);

console.log(newObj); // { a: 2, b: 4, c: 6 }


const entiress = [
	['a', 1],
	['b', 2],
	['c', 3]
];

const objektlar = Object.fromEntries(entiress);
console.log(objektlar);

/*Object.values() metodi JavaScript-da ob'ektning o'ziga tegishli barcha sanab o'tiladigan 
(enumerable) xossalarining qiymatlarini massiv ko'rinishida qaytaradi. Bu metod kalitlarga 
e'tibor bermay, faqat qiymatlarni oladi.*/

const obdj = { a: 1, b: 2, c: 3 };
const valuesdj = Object.values(obdj);
console.log(valuesdj);


const nestedObj = {
	a: 1,
	b: { nested: 2 },
	c: 3
};

const values = Object.values(nestedObj);
console.log(values); // [1, { nested: 2 }, 3]



const scores = { Alice: 550, Bob: 70, Charlie: 90 };

const totalScore = Object.values(scores).reduce((acc, score) => acc + score, 0);

console.log(totalScore);

const objfl = { a: 1, b: 2, c: 3, d: 4 };

const filteredValues = Object.values(objfl).filter(value => value > 2);

console.log(filteredValues); // [3, 4]


// groupBy funksiyasi
function groupBy(array, key) {
	return array.reduce((result, currentValue) => {
		// Kalit qiymatini oling
		const groupKey = currentValue[key];
		// Agar guruh mavjud bo'lmasa, yangi guruh yarating
		if (!result[groupKey]) {
			result[groupKey] = [];
		}
		// Hozirgi qiymatni tegishli guruhga qo'shing
		result[groupKey].push(currentValue);
		return result;
	}, {});
}

// Misol massiv
const fruitst = [
	{ name: "apples", quantity: 300 },
	{ name: "bananas", quantity: 500 },
	{ name: "oranges", quantity: 200 },
	{ name: "kiwi", quantity: 150 }
];

// Guruplash
const groupedFruitsf = groupBy(fruitst, "name");

console.log(groupedFruitsf);
/*
{
  apples: [ { name: 'apples', quantity: 300 } ],
  bananas: [ { name: 'bananas', quantity: 500 } ],
  oranges: [ { name: 'oranges', quantity: 200 } ],
  kiwi: [ { name: 'kiwi', quantity: 150 } ]
}
*/


// groupBy funksiyasi
function groupBy(array, fn) {
	return array.reduce((result, currentValue) => {
		// Kalit qiymatini funksiya yordamida oling
		const groupKey = fn(currentValue);
		// Agar guruh mavjud bo'lmasa, yangi guruh yarating
		if (!result[groupKey]) {
			result[groupKey] = [];
		}
		// Hozirgi qiymatni tegishli guruhga qo'shing
		result[groupKey].push(currentValue);
		return result;
	}, {});
}

// Misol massiv
const fruitsj = [
	{ name: "apples", quantity: 300 },
	{ name: "bananas", quantity: 500 },
	{ name: "oranges", quantity: 200 },
	{ name: "kiwi", quantity: 150 }
];

// Guruplash funksiyasi
function quantityCategory(fruit) {
	return fruit.quantity > 200 ? 'ok' : 'low';
}

// Guruplash
const groupedFruits = groupBy(fruitsj, quantityCategory);

console.log(groupedFruits);
/*
{
  ok: [
	{ name: 'apples', quantity: 300 },
	{ name: 'bananas', quantity: 500 }
  ],
  low: [
	{ name: 'oranges', quantity: 200 },
	{ name: 'kiwi', quantity: 150 }
  ]
}
*/


const person45 = {
	fname: "John",
	lname: "Doe",
	age: 25
};

let txtTY = "";
for (let x in person45) {
	txtTY += person45[x] + " ";
}

console.log(txtTY);


const person90 = {
	firstName: "John",
	lastName: "Doe",
	language: "EN"
};

Object.defineProperty(person90, "year", { value: "2000" })
// O'zgartirish
Object.defineProperty(person90, "language", { value: "NO" })

console.log(`Mijozning tug'ilgan kuni ${person90.year}`);
console.log(`Mijozning Tili ${person90.language}`);


const person55 = {
	firstName: "John",
	lastName: "Doe",
	language: "en",
	get bang() {
		return this.firstName.toUpperCase();
	}
};
console.log(person55.bang);


const personSet = {
	firstName: "John",
	lastName: "Doe",
	language: "en",
	set lang(lang) {
		this.language = lang.toUpperCase();
	}
};
personSet.lang = "ru";

console.log(personSet.language);


const objDef = {};

Object.defineProperty(objDef, "name", {
	value: "Alice",
	writable: false,
	enumerable: false,
	configurable: true
});

const descriptor = Object.getOwnPropertyDescriptor(obj, "name");

console.log(descriptor);
/*
{
  value: "Alice",
  writable: false,
  enumerable: false,
  configurable: true
}
*/

const personEx = { firstName: "John", lastName: "Doe" };
Object.preventExtensions(personEx);
let answer = Object.isExtensible(personEx);
console.log(answer);


const personSel = {
	firstName: "John",
	lastName: "Doe",
	age: 50,
	eyeColor: "blue"
};
Object.seal(personSel);
let textSel = "";
try {
	delete personSel.age;
	textSel = Object.values(personSel);
}
catch (err) {
	textSel = err.message;
}

console.log(textSel);



//                                              JavaScript funktsiyasi ta'riflari

function sum(...args) {
	let sum = 0;
	for (let a of args)
		sum += a;
	return sum;
}

let x = sum(4, 9, 16, 25, 29, 100, 66, 77);
console.log(x);


function findMax() {
	let max = -Infinity;
	for (let i = 0; i < arguments.length; i++) {
		if (arguments[i] > max) {
			max = arguments[i];
		}
	}
	return max;
}
console.log(findMax(4, 4, 74, 7, 6, 6, 8, 2, 6, 87));


class Car {
	constructor(brand, year) {
		this.brand = brand;
		this.year = year;
	}
}
const myCar1 = new Car("Ford", 2014);
const myCar2 = new Car("Audi", 2014);

console.log(myCar1.brand + " " + myCar2.brand);


class Yosh {
	constructor(name, year) {
		this.name = name;
		this.year = year;
	}
	age() {
		const date = new Date();
		return date.getFullYear() - this.year;
	}
}

const myAge = new Yosh("Shohruh", 2000);
console.log("Mening ismim " + myAge.name + " men " + myAge.age() + " yoshdaman");


class Car {
	constructor(brend) {
		this.carName = brend;
	}
	present() {
		return "Men " + this.carName + " ga egaman";
	}
}

class Model extends Car {
	constructor(brend, model) {
		super(brend);
		this.modelName = model;
	}
	show() {
		return this.present() + ", modelim " + this.modelName;
	}
}

const myCar = new Model("Toyota", "Camry");
console.log(myCar.show());
console.log(myCar.present());


class Car1 {
	constructor(brand) {
		this._carname = brand;
	}
	set carname(x) {
		this._carname = x;
	}
	get carname() {
		return this._carname;
	}
}

const myCar3 = new Car1("Ford");
myCar.carname = "Volvo";
console.log(myCar3.carname);


class Car2 {
	constructor(name) {
		this.ism = name;
	}
	static hello(x) {
		return ("Assalomu alaykum!!! ") + x.ism;
	}
}

const myCar4 = new Car2("Shohruh");
// console.log(myCar4.ism);
// console.log(Car2.hello());
console.log(Car2.hello(myCar4));


function myDispleniya(some) {
	console.log(some);
}

function myCalculyator(num1, num2) {
	let sum = num1 + num2;
	return sum;
	// myDisplayer(sum);
}

// function myFirs() {
// 	myDispleniya("Hello");
// }

// function mySecond() {
// 	myDispleniya("goodbye")
// }

// myFirs();
// mySecond();

let results = myCalculyator(5, 6);
myDispleniya(results);


function myDisplayer(something) {
	console.log(something);
}

function myCalc(num1, num2, myCalBack) {
	let sum = num1 + num2;
	myCalBack(sum);
}

myCalc(5, 8, myDisplayer);

const myNumbers = [4, 1, -20, -7, 5, 9, -6];
const posNumbers = removeNeg(myNumbers, (x) => x <= 0);
console.log(posNumbers);

function removeNeg(numbers, callback) {
	const myArray = [];
	for (const x of numbers) {
		if (callback(x)) {
			myArray.push(x);
		}
	}
	return myArray;
}


let inputDate = "2024-02-14";
let startDate = new Date(inputDate);
let tday = new Date();
let diff = tday - startDate;
let dayDiff = Math.floor(diff / (1000 * 60 * 60 * 24));
console.log(dayDiff + " kun bo'ldi");
console.log(dayDiff - 365 + " kun qoldi");

setTimeout(mySevishim, 3000);
function mySevishim() {
	console.log("Men seni sevaman");
}

setTimeout(myUylanish, 5000);
function myUylanish() {
	console.log('Menga turmushga chiqasanmi');
}

setInterval(mySoniya, 1000);
function mySoniya() {
	let d = new Date();
	console.log(d.getHours() + ":" + d.getMinutes() + ":" + d.getSeconds());

}




function myVada(some) {
	console.log(some);
}

let myPromise = new Promise(function (myResolve, myRejact) {
	let x = 1;
	if (x == 0) {
		myResolve("OK");
	}
	else {
		myRejact("Error");
	}
});

myPromise.then(
	function (value) { myVada(value); },
	function (error) { myVada(error); }
);

function myAsin(some) {
	console.log(some);
}

async function myFunkAs() { return 'Hello' };

myFunkAs().then(
	function (value) { myAsin(value); },
	function (error) { myAsin(error); }
);

async function myDist() {
	let myProm = new Promise(function (resovle) {
		setTimeout(function () {
			resovle('Hello');
		}, 3000);
	});
	console.log(await myProm);
}

function delaay(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
}

async function asyncFunction() {
	console.log("Start");

	await delaay(10000); // 2 soniya kuting

	console.log("End");
}

asyncFunction();

async function fetchData() {
	try {
		let response = await fetch('https://api.example.com/data');
		let data = await response.json();
		console.log(data);
	} catch (error) {
		console.error('Error:', error);
	}
}


function fetchData() {
	fetch('https://api.example.com/data')
		.then(response => response.json())
		.then(data => console.log(data))
		.catch(error => console.error('Error:', error));
}


const fs = require('fs');

// Mavjud JSON faylini o'qish
fs.readFile('json.json', 'utf8', (err, data) => {
	if (err) {
		console.error(err);
		return;
	}

	// JSON ma'lumotni parse qilish
	let jsonData = JSON.parse(data);

	// Yangi ma'lumotlar
	let yangiMalumot = {
		"ism": "Alisher",
		"yosh": 30,
		"kasb": "Dasturchi"
	};

	// Yangi ma'lumotlarni qo'shish
	jsonData.push(yangiMalumot);

	// Yangilangan ma'lumotlarni JSON fayliga yozish
	fs.writeFile('yangilangan_fayl.json', JSON.stringify(jsonData, null, 4), 'utf8', (err) => {
		if (err) {
			console.error(err);
			return;
		}
		console.log('JSON fayli muvaffaqiyatli yangilandi!');
	});
});


// XMLHttpRequest obyektini yaratish
const xhr = new XMLHttpRequest();

// So'rovni ochish
xhr.open('POST', 'https://example.com/api', true);

// Sarlavhalarni o'rnatish
xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
xhr.setRequestHeader('Authorization', 'Bearer token_value');

// So'rovni yuborish
xhr.send(JSON.stringify({
	name: "Alisher",
	age: 30,
	job: "Dasturchi"
}));

// Javobni olish
xhr.onreadystatechange = function () {
	if (xhr.readyState === 4 && xhr.status === 200) {
		console.log('Serverdan javob:', xhr.responseText);
	}
};
