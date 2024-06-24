'use strict'

// const car = {
// 	brand: 'Toyota',
// 	model: 'Camry',
// 	year: {
// 		buYil: 5,
// 		kelasiYil: 10
// 	}
// }
// const objToJSON = JSON.stringify(car)
// console.log(objToJSON);

// const clone = JSON.parse(JSON.stringify(car))

//json.stringify = objectdan jsonga ogirib beradi
//json.parse = jsonni objectga ogirib beradi

// clone.year.buYil = 15

// console.log(clone);
// console.log(car);



const uzs = document.querySelector('#usz'),
	usd = document.querySelector('#usd')

uzs.addEventListener('input', (e) => {
	const request = new XMLHttpRequest()

	request.open('GET', 'json/index.json') // Bu ochib beradi
	request.setRequestHeader('Content-type', 'application/json; charset=utf-8') //Bu sarlovha joylashtiradi
	request.send() //Bu  yuboradi

	request.addEventListener('readystatechange', () => { //Agar readystatechange o'rniga load qo'yilsa "request.readyState === 4 &&" buni qo'ymasada bo'ladi
		if (request.readyState === 4 && request.status === 200) {
			console.log(request.response)
			const data = JSON.parse(request.response)
			usd.value = (+uzs.value / data.current.usd).toFixed(2)
		}
		else {
			usd.value = 'Error'
		}
	})
})