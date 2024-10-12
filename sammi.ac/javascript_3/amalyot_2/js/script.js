'use strict'

document.addEventListener('DOMContentLoaded', () => {
	const adv = document.querySelectorAll('.promo__adv img'),
		wrapper = document.querySelector('.promo__bg'),
		genre = wrapper.querySelector('.promo__genre'),
		seriesList = document.querySelector('.promo__interactive-list'),
		addForm = document.querySelector('form.add'),
		inputVal = addForm.querySelector('.adding__input'),
		checkbox = addForm.querySelector("[type='checkbox']");



	// console.log(adv);

	const seriesDB = {
		series: [
			'Omar',
			'Ertugrul',
			'Kurulus Osman',
			'Barbaros',
			'Fatih',
			'Kosem Sultan',
			'Payitaht Abdülhamid',
			'Alparslan',
			'Uyanis Buyuk Selcuklu',
			'Kurulus Osman 2',
			'Salohiddin ayyubi'
		]
	}

	addForm.addEventListener('submit', (event) => {
		event.preventDefault()

		let newSeries = inputVal.value;
		const favorit = checkbox.checked;

		// console.log(newSeries);
		// console.log(favorit);

		if (newSeries) {
			if (newSeries.length > 18) {
				newSeries = `${newSeries.substring(0, 18)}...`
			}


			seriesDB.series.push(newSeries);
			sortEr(seriesDB.series)
			createSeriesList(seriesDB.series, seriesList)
			event.target.reset()
		}
		if (favorit) {
			console.log("Sevimli serial qo'shildi");
		}

	});

	const deleteAdv = (arr) => {
		adv.forEach(item => {
			item.remove()
		});
	}

	const makeChanges = () => {
		genre.textContent = 'Comedi';

		wrapper.style.backgroundImage = 'url("img/1.jpg")';

	}

	const sortEr = (arr) => {
		arr.sort();
	}

	function createSeriesList(series, perent) {

		perent.innerHTML = '';
		sortEr(series)

		series.forEach((item, index) => {
			perent.innerHTML += `
		<li class="promo__interactive-item">
			${index + 1}) ${item}
			<div class="delete"></div>
		</li>`
		})

		document.querySelectorAll('.delete').forEach((trash, idx) => {
			trash.addEventListener('click', () => {
				trash.parentElement.remove()
				seriesDB.series.splice(idx, 1)

				createSeriesList(series, perent)
			})
		})
	}

	sortEr(seriesDB.series)
	makeChanges()
	deleteAdv(adv)
	createSeriesList(seriesDB.series, seriesList)
});

