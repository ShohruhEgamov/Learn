exports.myDateTime = function () {
	const bugun = new Date();
	const sana = bugun.toLocaleDateString();  // Sanani chiqarish
	const vaqt = bugun.toLocaleTimeString();  // Vaqtni chiqarish
	return `${sana} Soat esa ${vaqt}`; // Sanani va vaqtni birgalikda qaytaradi
};

// // Hafta kunining nomini chiqarish
// console.log('Bugun:', haftaKunlari[haftaKuniRaqami]);

exports.myDateTimeday = function () {
	const haftaKunlari = ['Yakshanba', 'Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba'];
	const bugun = new Date();
	const haftaKuniRaqami = bugun.getDay();
	return haftaKunlari[haftaKuniRaqami];
};
