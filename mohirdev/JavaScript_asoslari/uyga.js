
function uyIPaddress(address) {
	return address.replace(/\./g, '[.]');
}

// Misol:
const address = "1.1.1.1";
console.log(uyIPaddress(address));
// Javobi:
// "1[.]1[.]1[.]1"


function uySozUzunligi(s) {
	if (!s) return 0;
	const words = s.trim().split(' ');
	return words[words.length - 1].length;
}

// Misol:
const sentence = "Salom Dunyo";
console.log(uySozUzunligi(sentence));
// Javob: 5

let regext = "Salom men Shohruh dasturchiman";
const pattern = /j/;
console.log(pattern.test(regext));


const obj = /e/.exec("The best things in life are free!");