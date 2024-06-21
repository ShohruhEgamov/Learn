'use strict'

const box = document.querySelector('#box')
// console.dir(box);
// box.style.backgroundColor = "red"
// box.style.cssText = 'background-color: red; width: 100px; height:100px'
const buttons = document.querySelectorAll('button')
buttons[0].style.width = '100px'

const circles = document.querySelectorAll('.circle')
const circle = document.querySelector('.circle')
const hearts = document.querySelectorAll('.heart')
const circleWrapper = document.querySelector('.circle__wrapper')

box.style.cssText = 'background-color: red; width: 100px; height: 100px'

buttons[0].style.width = '100px'
circles[1].style.backgroundColor = 'yellow'
circle.style.backgroundColor = 'yellow'

// for (let i = 0; i < hearts.length; i++) {
// 	hearts[i].style.backgroundColor = 'green'
// }

// hearts.forEach((item, index, arr) => {
// 	item.style.backgroundColor = 'gray'
// })

const btn = document.createElement('button')
// const text = document.createTextNode('I am text')

document.body.append(btn)

const myCircle = document.createElement('div')

myCircle.classList.add('circle')

circleWrapper.append(myCircle)
// circleWrapper.before(myCircle)
// circleWrapper.after(myCircle)
// circles[0].after(myCircle)
circles[1].remove()
circles[1].replaceWith(myCircle)
circleWrapper.append(myCircle)
// myCircle.innerHTML = '<pre>E</pre>'
myCircle.textContent = 'E'
// circleWrapper.insertAdjacentHTML('beforeend', '<pre>E</pre>')




//                                                        Bu yerda faqat o'rganish uchun

// Old way
// const box = document.getElementById('box')
// console.log(box);

// const button = document.getElementsByTagName('button')
// console.log(button);

// const circle = document.getElementsByClassName('circle')
// console.log(circle);

//New way
// const heart = document.querySelector('heart')
// console.log(heart);


// const hearts = document.querySelectorAll('.heart')
// console.log(hearts);

// hearts.forEach(item => {
// 	console.log(item);
// })
