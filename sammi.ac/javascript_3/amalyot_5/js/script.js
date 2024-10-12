'use strict';

const btn = document.querySelector('#btn');

// let timerId;
// let i = 0;


function myAnimation() {
	const car = document.querySelector('.car');
	let pos = 0;

	const timerId = setInterval(frame, 10);

	function frame() {
		if (pos === 700) {
			clearInterval(timerId);
		} else {
			pos++;
			car.style.left
			pos + 'px';
		}
	}
}

btn.addEventListener('click', myAnimation);


// btn.addEventListener('click', () => {
// 	// timerId = setTimeout(toxtash, 1000);
// 	timerId = setInterval(toxtash, 500)
// })

// clearInterval(timerId)

// function toxtash() {
// 	if (i === 3) {
// 		clearInterval(timerId)
// 	}
// 	console.log('Salom Shohruh');
// 	i++
// }


// let id = setTimeout(function log() {
// 	console.log('Salom Shohruhbek yaxshimisiz');
// 	id = setTimeout(log, 500);
// }, 500)

