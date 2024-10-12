const canvas = document.querySelector('canvas'),
	toolBtns = document.querySelectorAll('.tool'),
	fillColor = document.querySelector('#fill-color'), // Bu yerda hamma yerini to'ldirish uchun
	sizeSlider = document.querySelector('#size-slider'), // Bu yerda sizeni oldik
	colorPicker = document.querySelector('#color-picker'), //Bu yerda biz rang tanlashni oldik
	clearCanvasBtn = document.querySelector('.clear-canvas'),
	colorBtns = document.querySelectorAll('.colors .option'), //bU YERDA COLORNI VA ICHIDAGI OPTIONNI OLAMIZ
	saveImageBtn = document.querySelector('.save-img')
// Bu yerda chizish funksiyasin
let ctx = canvas.getContext('2d'),
	isDrowing = false,                // Bu chizilmasligi uchun
	brushWidth = 5,                   // Bu chiziqning qalinligi
	selectedTool = 'brush',
	selectedColor = '#000',
	prevMouseX,
	prevMouseY,
	snapshot

// Bu yerda yuklangan faylni orqa foni
const setCannvasBackground = () => {
	ctx.fillStyle = '#fff'
	ctx.fillRect(0, 0, canvas.width, canvas.height) // Buni vazifasi shu rasm kengligi va balandligini boyaydi
	ctx.fillStyle = selectedColor
}

// Buni vazifasi canvas faqat ozini ichida ishlashi uchun
window.addEventListener('load', () => {
	canvas.width = canvas.offsetWidth         // Faqat ozini enida
	canvas.height = canvas.offsetHeight       //faqat ozini uzunligida
	setCannvasBackground()
})

//Bu esa bosganda chizish uchun
const stastDrow = e => {
	isDrowing = true                  // Bu esa true bolganda chizilishi uchun
	prevMouseX = e.offsetX       // Bu yerda mousni yonalishlarini olamiz
	prevMouseY = e.offsetY
	ctx.beginPath()                   // Bu esa chizishni boshlagandan keyin tugatadi
	ctx.lineWidth = brushWidth       // Bu esa chiziqning qalinligini o'zi
	snapshot = ctx.getImageData(0, 0, canvas.width, canvas.height)
	ctx.strokeStyle = selectedColor
	ctx.fillStyle = selectedColor
}

// Bu yerga tortburchakni chizish uchun funksiya
const drowRectangle = e => {
	//Agar 'rangni to'ldirish' yopiq turgan bolsa
	if (!fillColor.checked) {
		ctx.strokeRect(e.offsetX, e.offsetY, prevMouseX - e.offsetX, prevMouseY - e.offsetY)
	}
	//Agar 'rangni to'ldirish' yoniq turgan bolsa
	else {
		ctx.fillRect(e.offsetX, e.offsetY, prevMouseX - e.offsetX, prevMouseY - e.offsetY)
	}
	// // Yukoridagini biz qisqartirib yozishimiz mumkin
	// fillColor.checked

	// 	? ctx.fillRect(e.offsetX, e.offsetY, prevMouseX - e.offsetX)
	// 	: ctx.strokeRect(e.offsetX, e.offsetY, prevMouseX - e.offsetX)
}

// Bu yerda Doira chizish uchun
const drawCircle = e => {
	ctx.beginPath()
	const radius =
		Math.sqrt(Math.pow(prevMouseX - e.offsetX, 2)) + Math.pow(prevMouseY - e.offsetY, 2)
	ctx.arc(prevMouseX, prevMouseY, radius, 0, 2 * Math.PI)
	ctx.stroke()
	fillColor.checked ? ctx.fill() : ctx.stroke()
}
// Bu yerda uchburchak chizamiz
const drawTriangle = e => {
	ctx.beginPath()                      // Chizishni boshlaydi
	ctx.moveTo(prevMouseX, prevMouseY)   // Bu 1 tarafini uzun chizadi
	ctx.lineTo(e.offsetX, e.offsetY)
	ctx.lineTo(prevMouseX * 2 - e.offsetX, e.offsetY)  // Bu esa pas qismini uzun chizadi
	ctx.closePath()                                     // Bu esa ochiq tarafini yopadi
	fillColor.checked
		? ctx.fill()
		: ctx.stroke()
}

// Bu chizish uchun
const drawing = e => {
	if (!isDrowing) return           // Bu esa false bolganda hech narsa qaytarmasligi uchun
	ctx.putImageData(snapshot, 0, 0)
	//Bu yerda hamma shakillarni chizish uchun
	switch (selectedTool) {
		case 'brush':
			ctx.lineTo(e.offsetX, e.offsetY)
			ctx.stroke()                     // Bu metod chizish uchun
			break;
		case 'rectangle':
			drowRectangle(e)
			break
		case 'circle':
			drawCircle(e)
			break
		case 'triangle':
			drawTriangle(e)
			break
		case 'eraser':
			ctx.strokeStyle = '#fff'
			ctx.lineTo(e.offsetX, e.offsetY)  // Bu yerda ochirgich bolsilganda oq rangda ochiradi
			ctx.stroke()
			break
		default:
			break;
	}
}

// Bu yerda esa shakillarni yasaymiz
toolBtns.forEach(btn => {
	btn.addEventListener('click', () => {
		document.querySelector('.options .active').classList.remove("active") // Bu yerda hamma activelarni o'chiramiz
		btn.classList.add('active')              //Bu yerda esa bosganda yonadigan qilamiz
		selectedTool = btn.id                   // Bu yerda biz chizgishlarni hammasini bitta ozgaruvchiga oldik
	})
})

//bu yerda biz sizeni funksiyasini yozamiz
sizeSlider.addEventListener('change', () => (brushWidth = sizeSlider.value))
//Bu yerda mishkani yuborganda to'xtashi uchun
const stopDraw = () => {
	isDrowing = false
}

//Bu yerga biz rang tanlaydiganni funksiyasini olamiz
colorPicker.addEventListener('change', () => {
	colorPicker.parentElement.style.background = colorPicker.value
	colorPicker.parentElement.click()
})


// Buyerda colorlarni funksiyasi
colorBtns.forEach(btn => {
	btn.addEventListener('click', e => {
		document.querySelector('.options .selected').classList.remove('selected')     // Bu yerda activni otkzish uchun
		btn.classList.add('selected')             // Bu yerda qaysini bossa sunga bu classs otisi uchun
		const bgColor = window.getComputedStyle(btn).getPropertyValue('background-color')  // Bu yerda rangni css dan olayapmiz
		selectedColor = bgColor
	})
})

// Bu yerda ochirib yuborisjh
clearCanvasBtn.addEventListener('click', () => {
	ctx.clearRect(0, 0, canvas.width, canvas.height)
	setCannvasBackground()
})

// Bu yerda saqlash uchun funcsiya
saveImageBtn.addEventListener('click', () => {
	const link = document.createElement('a')
	link.download = `paint${Date.now()}.jpg`
	link.href = canvas.toDataURL()
	link.click()
})

canvas.addEventListener('mousedown', stastDrow)
canvas.addEventListener('mousemove', drawing)
canvas.addEventListener('mouseup', stopDraw)

