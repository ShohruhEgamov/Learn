window.addEventListener('DOMContentLoaded', () => {
	const tabsParent = document.querySelector('.tabheader__items'),
		tabs = document.querySelectorAll('.tabheader__item'),
		tabContent = document.querySelectorAll('.tabcontent'),
		loader = document.querySelector('.loader')

	//loader
	setTimeout(() => {
		loader.style.opacity = '0';
		setTimeout(() => {
			loader.style.display = 'none'
		}, 500)
	}, 2000);

	//Tab
	function hidetabContent() {
		tabContent.forEach(item => {
			item.classList.add('hide')
			item.classList.remove('show', 'fade')
		});
		tabs.forEach(item => {
			item.classList.remove('tabheader__item_active')
		});
	}
	function showtabContent(i = 0) {
		tabContent[i].classList.add('show', 'fade')
		tabContent[i].classList.remove('hide')
		tabs[i].classList.add('tabheader__item_active')
	}

	hidetabContent()
	showtabContent()

	tabsParent.addEventListener('click', (event) => {
		const target = event.target
		if (target && target.classList.contains('tabheader__item')) {
			tabs.forEach((item, idx) => {
				if (target === item) {
					hidetabContent()
					showtabContent(idx)
				}
			})
		}
	})


	//Timer

	const deadline = '2030-01-10';

	function getTimeRemaining(endtime) {
		let days, hours, minutes, seconds;

		const timer = Date.parse(endtime) - Date.parse(new Date());
		if (timer <= 0) {
			days = 0;
			hours = 0;
			minutes = 0;
			seconds = 0;
		}
		else {
			days = Math.floor(timer / (1000 * 60 * 60 * 24))
			hours = Math.floor((timer / (1000 * 60 * 60)) % 24)
			minutes = Math.floor((timer / 1000 / 60) % 60)
			seconds = Math.floor((timer / 1000) % 60)
		}
		return { timer, days, hours, minutes, seconds }
	}

	function getZero(num) {
		if (num >= 0 && num < 10) {
			return `0${num}`
		}
		return num
	}
	function setClock(selector, endtime) {
		const timer = document.querySelector(selector);
		days = timer.querySelector('#days'),
			hours = timer.querySelector('#hours'),
			minutes = timer.querySelector('#minutes'),
			seconds = timer.querySelector('#seconds'),
			timeInterval = setInterval(updateClock, 1000);

		updateClock()
		function updateClock() {
			const t = getTimeRemaining(endtime);

			days.innerHTML = getZero(t.days);
			hours.innerHTML = getZero(t.hours);
			minutes.innerHTML = getZero(t.minutes);
			seconds.innerHTML = getZero(t.seconds);

			if (t.timer <= 0) {
				clearInterval(timeInterval)
			}
		}
	}


	setClock('.timer', deadline)

	//Modal xxxzzz
	const modalTrigger1 = document.querySelector('[data-madal1]'),
		modalTrigger2 = document.querySelector('[data-madal2]'),
		modal = document.querySelector('.modal'),
		modalCloseBtn = document.querySelector('[data-close]');

	// Chiqish uchun funksiya
	function closeModal() {
		modal.classList.add('hide')
		modal.classList.remove('show')
		document.body.style.overflow = ''
	}

	// Kirish uchun funksiya
	function openModal() {
		modal.classList.add('show')
		modal.classList.remove('hide')
		document.body.style.overflow = 'hidden'
		clearInterval(modalTimer)
	}

	// modalTrigger.forEach((item) => {
	// 	item.addEventListener('click', openModal)
	// })

	//modal buttonlaari
	modalTrigger1.addEventListener('click', openModal)
	modalTrigger2.addEventListener('click', openModal)

	modalCloseBtn.addEventListener('click', closeModal)

	// madaldan tashqarini boshganda madaldan chiqishi uchun
	modal.addEventListener('click', (e) => {
		if (e.target === modal) {
			closeModal()
		}
	})

	// esc knopkasini boshganda modaldan chiqishi uchun
	document.addEventListener('keydown', (e) => {
		if (e.code === 'Escape' && modal.classList.contains('show')) {
			closeModal()
		}
	})

	// avtamatic sayt yuklanganda madal chiqishi uchun
	const modalTimer = setTimeout(openModal, 3000);


	//Eng pastga tushganida modal chqishi uchun
	function showModalByScroll() {
		if (window.pageYOffset + document.documentElement.clientHeight >= document.documentElement.scrollHeight - 1) {
			openModal()
			window.removeEventListener('scroll', showModalByScroll)
		}
	}
	window.addEventListener('scroll', showModalByScroll)

	//Class
	class MenuCard {
		constructor(src, alt, title, descr, price, perentSelector,) {
			this.src = src;
			this.alt = alt;
			this.title = title;
			this.descr = descr;
			this.price = price;
			// this.classes = classes;
			this.perent = document.querySelector(perentSelector);
			this.transfer = 11000;
			this.chageToUSZ()
		}

		// Bu dollrni so'mga aylantirish uchun
		chageToUSZ() {
			this.price = this.price * 11000
		}
		// Bu qartalarni almashtirish uchun
		render() {
			const element = document.createElement('div');

			// this.classes.forEach((clasname) => element.classList.add(this.clasname))

			element.innerHTML = `
			<div class="menu__item">
					<img src=${this.src} alt=${this.alt} />
					<h3 class="menu__item-subtitle">${this.title}</h3>
					<div class="menu__item-descr">${this.descr}
					</div>
					<div class="menu__item-divider"></div>
					<div class="menu__item-price">
						<div class="menu__item-cost">Price:</div>
						<div class="menu__item-total"><span>${this.price}</span> uz/month</div>
					</div>
				</div>
			`
			this.perent.append(element)
		}
	}

	// const card1 = new MenuCard()
	// card1.render()

	//Qisqa usul
	new MenuCard(
		'img/tabs/1.png',
		'vegy',
		'Plan "Usual"',
		'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Fugit nesciunt facere, sequi exercitationem praesentium ab cupiditate beatae debitis perspiciatis itaque quaerat id modi corporis delectus ratione nobis harum voluptatum in.',
		10,
		'.menu .container'
		// 'menu__item'
	).render()

	new MenuCard(
		'img/tabs/2.jpg',
		'elite',
		'Plan “Premium”',
		'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Fugit nesciunt facere, sequi exercitationem praesentium ab cupiditate beatae debitis perspiciatis itaque quaerat id modi corporis delectus ratione nobis harum voluptatum in.',
		15,
		'.menu .container'
		// 'menu__item'
	).render()

	new MenuCard(
		'img/tabs/3.jpg',
		'post',
		'Plan "VIP"',
		'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Fugit nesciunt facere, sequi exercitationem praesentium ab cupiditate beatae debitis perspiciatis itaque quaerat id modi corporis delectus ratione nobis harum voluptatum in.',
		20,
		'.menu .container'
		// 'menu__item'
	).render()
})

