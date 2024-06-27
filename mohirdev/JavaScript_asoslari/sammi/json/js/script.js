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


// Bu yerda agar dosti kelgan bo'lsa birinchi ifni chiqaradi kelmagan bolsa else ni agar ikkalasi ham ishlamasa finally ishga tushadi
const isFrendCome = true

const meetingRequest = new Promise((resolve, reaject) => {
	if (isFrendCome) {
		const msg = "Frend I'm there"
		resolve(msg)
	}
	else {
		const arr = "I can't come there"
		reaject(arr)
	}
})

meetingRequest
	.then((msg) => console.log(msg))  // Birinchisi ishga tushsa chiqadi
	.catch((arr) => console.log(arr)) // Ikkinchisi ishga tushsa chiqadi
	.finally(() => console.log("I'm colling you")) // Har doim chiqadi



// Bu yerda ketma ket ishlashligi uchun
console.log("Request date..."); // Birinchi bu ishlaydi

const req = new Promise((resolve) => {
	setTimeout(() => {
		const praduct = {
			name: 'car',
			color: 'black'
		}
		console.log('Processing date...'); // Ikkinchi bu ishlaydi
		resolve(praduct)
	}, 2000);
})

req
	.then((data) => {
		return new Promise((resolve) => {
			setTimeout(() => {
				data.status = 'ordered'
				console.log('Get data...');
				resolve(data)
			}, 2000)
		})
	})

	.then((result) => console.log(result))
	.finally(() => console.log('Fetching end'))



// Bu yerda promise ning boshqacha turi ko'rsatilgan

const request = (time) => {
	return new Promise((resolve) => {
		setTimeout(() => resolve(), time)
	})
}

// //Oddiy ko'rinishi
// request(1000).then(() => console.log('Request 1000 ms'))
// request(2000).then(() => console.log('Request 2000 ms'))
// request(3000).then(() => console.log('Request 3000 ms'))

// //  Bu esa qisqa boshqacha yo'li
// Promise.all([request(1000), request(2000), request(3000)]).then(() => console.log('all'))

// Bu yana bir ko'rinishi
Promise.race([request(1000), request(2000), request(3000)]).then(() => console.log('all'))




