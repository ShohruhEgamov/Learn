'use strict'

// const btns = document.querySelectorAll('button');

// btns[0].addEventListener('click', () => {
// if (!btns[1].classList.contains('red')) {
// 	btns[1].classList.add('red');
// }
// else {
// 	btns[1].classList.remove('red');
// }

// 	btns[1].classList.toggle('red');
// })




//                                                   Delegatsiya

const wrapper = document.querySelector('.btn-block'),
	btns = document.querySelectorAll('button');

btns[0].addEventListener('click', () => {
	btns[1].classList.toggle('red')
});

wrapper.addEventListener('click', (event) => {
	if (event.target && event.target.matches('button.red')) {
		console.log('btn click');

	}
});



// btns.forEach((item) => {
// 	item.addEventListener('click', () => {
// 		console.log('cliked')
// 	})
// });

const btn = document.createElement('button')
btn.classList.add('blue')
wrapper.append(btn)