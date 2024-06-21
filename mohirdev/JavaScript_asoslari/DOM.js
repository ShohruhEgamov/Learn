'use strict';

const x1 = document.getElementsByClassName("intro");
document.getElementById("demo").innerHTML = 'Birinchi paragraf (0 indeksi 0) sinf = "intro":' + x1[0].innerHTML;

const x2 = document.querySelectorAll("p.intro");
document.getElementById("demo").innerHTML = 'Birinchi paragraf (0 indeksi 0) sinf = "intro": ' + x2[1].innerHTML;

const x3 = document.forms["frm1"];
let text = "";
for (let i = 0; i < x3.length; i++) {
	text += x3[i].value + "<br>";
}
document.getElementById("demo").innerHTML = text;

document.getElementById('demo1').innerHTML = "Bu yerda titleda " + document.title;


const x4 = document.querySelectorAll('p.intro');
document.getElementById('demo').innerHTML = "bu yerda css selektorariga qarab chiqariladi " + x4[1].innerHTML;

function validateForm() {
	let x4 = document.forms["myForm"]["fname"].value;
	if (x4 == "") {
		alert("Iltimos ismni kiriting");
		return false;
	}
}

function myFunksion() {
	let x = document.getElementById("numb").value;
	let text;
	if (isNaN(x) || x < 1 || x > 10) {
		text = "Bu raqam emas";
	}
	else {
		text = "Ha bu son";
	}
	document.getElementById("demo").innerHTML = text;

}


function myMove() {
	let id = null;
	const elem = document.getElementById("animate");
	let pos = 0;
	clearInterval(id);
	id = setInterval(frame, 10);
	function frame() {
		if (pos == 350) {
			clearInterval(id);
		}
		else {
			pos++;
			elem.style.top = pos + "px";
			elem.style.right = pos + "px";
		}
	}
}


document.getElementById('but').onclick = changeText;
function changeText() {
	document.getElementById('demo').innerHTML = "Ooooops!";
}


function mOver(obj) {
	obj.innerHTML = "Thank You";
}

function mOut(obj) {
	obj.innerHTML = "Mouse Over Me";
}

function mDown(obj) {
	obj.style.backgroundColor = "#1ec5e5";
	obj.style.color = "#ffffff";
	obj.innerHTML = "Va aleykum assalom";
}

function mUp(obj) {
	obj.backgroundColor = "green";
	obj.color = "#000000";
	obj.innerHTML = "Yaxshimisiz";
}

var x = document.getElementById('myBtn');
x.addEventListener("click", myFum);
x.addEventListener("click", someFum);

function myFum() {
	alert("Hello World!");
}
function someFum() {
	alert("Salom Shohruh");
}




var x = document.getElementById("myBtn");
x.addEventListener("mouseover", myFunction);
x.addEventListener("click", mySecondFunction);
x.addEventListener("mouseout", myThirdFunction);

function myFunction() {
	document.getElementById("demo").innerHTML += "Salom Shohruh!<br>";
}
function mySecondFunction() {
	document.getElementById("demo").innerHTML += "Juda zo'r!<br>";
}
function myThirdFunction() {
	document.getElementById("demo").innerHTML += "Hafa bo'ldim!<br>";
}





let p1 = 5;
let p2 = 7;
var x = document.getElementById("myBtn");
x.addEventListener("click", function () {
	myFunction(p1, p2);
});
x.addEventListener("mouseover", mySecondFunction);
x.addEventListener("mouseout", myThirdFunction);

function myFunction(a, b) {
	document.getElementById("demo").innerHTML = a * b + "<br>";
}
function mySecondFunction() {
	document.getElementById("demo").innerHTML = "Bosing!<br>"; // agar bu yerda += qilinsa har safar yangini qoshadi
}
function myThirdFunction() {
	document.getElementById("demo").innerHTML = "Boshmadingiz!<br>";
}





document.getElementById("myDIV").addEventListener("mousemove", myFunction);

function myFunction() {
	document.getElementById("demo").innerHTML = Math.random();
}

function removeHandler() {
	document.getElementById("myDIV").removeEventListener("mousemove", myFunction);
}

document.getElementById("child").innerHTML = document.body.innerHTML;



const para = document.createElement("p");
const node = document.createTextNode("This is new.");
para.appendChild(node);
const element = document.getElementById("div1");
const child = document.getElementById("p1");
element.insertBefore(para, child);



function myFunction() {
	var txt;
	if (confirm("Bu buttonni bos")) {
		txt = "Siz bunga rozisiz!";
	} else {
		txt = "Siz bunga norozisiz!";
	}
	document.getElementById("demo").innerHTML = txt;
}

function myFunction() {
	let text;
	let person = prompt("Please enter your name:", "Shohruh Egamov");
	if (person == null || person == "") {
		text = "User cancelled the prompt.";
	} else {
		text = "Hello " + person + "! How are you today?";
	}
	document.getElementById("demo").innerHTML = text;
}