'use strict'
// Bu yerda locol storage dan foydalanish usullari
const email = document.querySelector('Bu yerga classs nomi'),
	firsName = document.querySelector('Bu yerga classs nomi'),
	lastName = document.querySelector('Bu yerga classs nomi'),
	formSubmit = document.querySelector('Bu yerga classs nomi')
doc = document.querySelector('Bu yerga classs nomi')


formSubmit.addEventListener('submit', (e) => {
	e.preventDefault()          // Bu qayta yuklanganda hamma yeri yangilanmasligi uchun

	const user = {
		email: email.value,
		name: firsName.value,
	}

	e.target.reset()

	localStorage.setItem('user', JSON.stringify(user))     // Bu malumotni server tushinadigan tilda yuborish uchun
})

const user = JSON.parse(localStorage.getItem('user'))     // Bu esa serverdan olish uchun

doc.textContent = `${user.name}`