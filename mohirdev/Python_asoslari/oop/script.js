// function hisoblash(ism, tugilganKun, tugilganOy, tugilganYil) {
// 	// Joriy sanani olish
// 	var joriySana = new Date();

// 	// Tug'ilgan sanani olish
// 	var tugilganSanasi = new Date(tugilganYil, tugilganOy - 1, tugilganKun); // Oy indeksi 0 dan boshlanadi (Yanvar = 0)

// 	// Yoshni hisoblash
// 	var yosh = joriySana.getFullYear() - tugilganSanasi.getFullYear();

// 	// Tug'ilgan sanadan oldingi tug'ilgan kunlarni hisoblash
// 	if ((joriySana.getMonth() < tugilganSanasi.getMonth()) ||
// 		(joriySana.getMonth() === tugilganSanasi.getMonth() && joriySana.getDate() < tugilganSanasi.getDate())) {
// 		yosh--;
// 	}

// 	// Natijani chiqarish
// 	console.log(`${ism} ${tugilganKun}-${tugilganOy}-${tugilganYil} tug'ilgan, ${yosh} yoshda`);
// }

// // Test qilish
// hisoblash("Shohruh", 21, 12, 2000);



function hisoblash_tugilgan_va_joriy(ism, tugilganKun, tugilganOy, tugilganYil) {
	// Joriy sana va tug'ilgan sana obyektlari
	var joriySana = new Date();
	var tugilganSana = new Date(tugilganYil, tugilganOy - 1, tugilganKun); // Oy indeksi 0 dan boshlanadi (Yanvar = 0)

	// Yosh, oy va kunlarni hisoblash
	var yosh = joriySana.getFullYear() - tugilganSana.getFullYear();
	var oy = joriySana.getMonth() - tugilganSana.getMonth();
	var kun = joriySana.getDate() - tugilganSana.getDate();

	// Oy va kun uchun qondirilishi
	if (kun < 0) {
		oy--;
		kun += new Date(joriySana.getFullYear(), joriySana.getMonth(), 0).getDate(); // Oyning oxirgi kuni
	}
	if (oy < 0) {
		yosh--;
		oy += 12; // To'g'ri oylar soni
	}

	// Natija chiqarish
	console.log(`${ism} ${yosh} yil, ${oy} oy, ${kun} kun`);
}

// Test qilish
hisoblash_tugilgan_va_joriy("Shohruh", 21, 12, 2000);
hisoblash_tugilgan_va_joriy("Farrux", 15, 11, 1998);
hisoblash_tugilgan_va_joriy("Bekmirza", 21, 11, 1996);
hisoblash_tugilgan_va_joriy("Diyorbek", 14, 4, 1994);
hisoblash_tugilgan_va_joriy("Shuxrat", 25, 8, 1968);
hisoblash_tugilgan_va_joriy("Bekposhsha", 1, 2, 1975);

