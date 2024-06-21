'use strict'

// const car = {
// 	mator: "X",
// 	color: "red",
// 	isAirbag: true,
// 	isSpeed: function () {
// 		console.log(320);

// 	}
// }

// const gm = {
// 	isAirbag: false,
// }

// gm.__proto__ = car;
// console.log(gm)

// Object.setPrototypeOf(gm, car)
// console.log(gm);

//                                                                              Amaliy mashgulotlar u bilan ishlash

const seriesDB = {
	count: 0,
	series: {},
	aktior: {},
	genres: [],
	private: false,
	start: function () {
		seriesDB.count = +prompt("Nechi serial ko'rgansiz?", '');

		while (
			seriesDB.count == '' ||
			seriesDB.count == null ||
			isNaN(seriesDB.count)
		) {
			seriesDB.count = +prompt("Nechi serial ko'rgansiz?", '');
		}
	},
	rememberMySeries: function () {
		for (let i = 0; i < 2; i++) {
			const a = prompt("Oxirgi ko'rgan serialingiz?", ''),
				b = prompt("Ushbu serial nechta qismdan iborat?", '');

			if (a != null && b != null && a != "" && b != "") {
				seriesDB.series[a] = b;
				console.log('done');
			}
			else {
				console.log('error');
				i--
			}
		}
	},
	detextLevelSeries: function () {
		if (seriesDB.count < 5) {
			console.log("Siz seriallarni kam ko'rgan ekansiz", '');
		}
		else if (seriesDB.count >= 5 && seriesDB.count < 10) {
			console.log("Siz seriallarni o'rtacha ko'rgan ekansi", '')
		}
		else if (seriesDB.count > 10) {
			console.log("Siz seriallarni juda ko'p ko'rgan ekansiz", '')
		}
		else {
			console.log('Error');
		}
	},

	visibleDB: function () {
		if (seriesDB.private) {
			seriesDB.private = false
		}
		else {
			seriesDB.private = true
		}
	},

	showDb: function () {
		if (!seriesDB.private) {
			console.log(seriesDB);
		}
	},
	writeGenres: function () {
		// for (let i = 0; i < 3; i++) {
		// 	const a = prompt(`Oxirgi ko'rgan serialingiz janri? ${i + 1}`);
		// 	if (a === "" || a === null) {
		// 		console.log('Siz notogri kiritingiz')
		// 		i--
		// 	}
		// 	else {
		// 		seriesDB.genres[i] = a;
		// 	}
		// }

		let genres = prompt("Yaxsi ko'rgan filimingi vergul bilan yoz").toLowerCase()
		if (genres === '' || genres === null) {
			console.log('Siz noto`ri malumot kiritingiz')
			i--

		}
		else {
			seriesDB.genres = genres.split(',')
			seriesDB.genres.sort()
		}

		seriesDB.genres.forEach((item, index) => {
			console.log(`Sizni yaxshi ko'rgan janringiz ${index + 1} nomi ${item}`);
		})
	}
}



//                                     dinamic typing

//   to string
console.log(typeof String(4));
