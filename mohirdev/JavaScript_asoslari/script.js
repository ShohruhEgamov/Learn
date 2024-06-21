const tasodifiy = [40, 100, 1, 5, 25, 10, 42, 15, 18, 54, 95, 13]

document.getElementById("demo").innerHTML = tasodifiy;

function myFunction() {
	for (let i = tasodifiy.length - 1; i > 0; i--) {
		let j = Math.floor(Math.random() * (i + 1));
		let k = tasodifiy[i];
		tasodifiy[i] = tasodifiy[j];
		tasodifiy[j] = k;
	}
	document.getElementById("demo").innerHTML = tasodifiy;
}


const cars = [
	{ type: "Volvo", year: 2016 },
	{ type: "Saab", year: 2001 },
	{ type: "BMW", year: 2010 }
];

displayCars();

function myFunction() {
	cars.sort(function (a, b) {
		let x = a.type.toLowerCase();
		let y = b.type.toLowerCase();
		if (x < y) { return -1; }
		if (x > y) { return 1; }
		return 0;
	});
	displayCars();
}

function displayCars() {
	document.getElementById("demo").innerHTML =
		cars[0].type + " " + cars[0].year + "<br>" +
		cars[1].type + " " + cars[1].year + "<br>" +
		cars[2].type + " " + cars[2].year;
}

function myFunction() {
	let age = document.getElementById("age").value;
	let voteable = (age < 18) ? "Too young" : "Old enough";
	document.getElementById("demo").innerHTML = voteable + " to vote.";
}



const rang = confirm("bu yerga kirit")

const meva = [];

meva[0] = (prompt("meva kirit"));
meva[1] = (prompt("meva kirit"));
meva[2] = (prompt("meva kirit"));

console.log(meva);


function juftSon(number) {
	if (number % 2 == 0) {
		console.log(`${number} juft son`);
	}
	else {
		console.log(`${number} toq son`);
	}
}
juftSon(prompt('Son kirit'))

function juftSon(number) {
	if (number % 2 == 0) {
		console.log(`${number} juft son`);
	}
	else {
		console.log(`${number} toq son`);
	}
}

juftSon(Number(prompt('Son kirit')));

const juftTop = function (number) {
	if (number % 2 == 0) {
		console.log(`${number} Juft son`);
	}
	else {
		console.log(`${number} Toq son`);
	}
	// document.getElementById("demo").innerHTML = voteable + " to vote";
}

juftTop(Number(prompt('Son kirit')));

function juftSon(number) {
	const numberstr = String(number);
	const reverstr = numberstr.split('').reverse().join('');
	return Number(reverstr)
}
console.log(juftSon(prompt("Son kiriting")));



const inRange = (min, max, number) => {
	if (number >= min && number <= max) {
		console.log(`Berilgan ${number} soni ${min} va ${max} orasida`);
	}
	else {
		console.log(`Berilgan ${number} soni ${min} va ${max} orasida emas`);
	}
}

const minRange = prompt('Minimal son kirit:');
const maxRange = prompt('Maximal son kirit:');
const givenNumber = prompt('Son kirit:');

inRange(minRange, maxRange, givenNumber)


const simCalculyator = (num1, oper, num2) => {
	switch (oper) {
		case "+":
			console.log(`Yig'indisi: ${num1 + num2}`);
			break;
		case "-":
			console.log(`Ayirmasi: ${num1 - num2}`);
			break;
		case "*":
			console.log(`Ko'paytmasi: ${num1 * num2}`);
			break;
		case "/":
			console.log(`Bo'linmasi ${num1 / num2}`)
			break
		default:
			console.log("Operatsiya noto'g'ri");
	}
}

const a = +prompt('Son kirit:');
const operation = prompt('Amal kirit:');
const b = +prompt('Son kirit:');


console.log(simCalculyator(a, operation, b));


const getElemen = (array) => {
	let largest = array[0];
	for (let i = 1; i < array.length; i++) {
		if (array[i] > largest) {
			largest = array[i];
		}
	}
	return largest
}

const arr = [1, 2, 3, 4, 50, 6, 7, 8, 9,]
const result = (getElemen(arr))
console.log(`Eng katta element: ${result}`);

const heading1 = document.getElementById('demo');
console.log(heading1);
heading1.remove();

const inputEls = document.getElementsByName('deko');
const inputEl = inputEls[0];
console.log(inputEl);
inputEl.value = 'Salom';
inputEl.disabled = true;
inputEl.remove();

const hedings1 = document.getElementsByClassName('dede');
console.log(hedings1);

const hedings = document.getElementsByTagName('h1');
console.log(hedings);

const headings = document.getElementById('sarlovha');
headings.textContent = "Salom"

const peragraph = document.createElement('p');
console.log(peragraph);

const text = document.createTextNode('Bu yerda habar');
console.log(text);

peragraph.appendChild(text);

const box = document.getElementById('box');
box.appendChild(peragraph);

console.log(box.parentElement);
console.log(box.childNodes);



const changeHeading = () => {
	const heading = document.getElementById('heading');
	heading.textContent = 'Yangi sarlovha';
}

const btn = document.getElementById('changeHeading');
btn.addEventListener('click', changeHeading);