const tasodifiySon = (min, max) => {
	return Math.floor(Math.random() * (max - min + 1)) + min;
}

const generator = () => {
	const minEl = document.getElementById('min');
	const maxEl = document.getElementById('max');
	const min = Number(minEl.value);
	const max = Number(maxEl.value);

	if (minEl.value === '' || maxEl.value === '') {
		alert('Iltimos son kiriting')
		return
	}

	if (min > max) {
		alert('Min son katta bo\'lishi mumkin emas')
	}

	const placeholderEl = document.querySelector('#placeholder');
	placeholderEl.textContent = tasodifiySon(min, max);

}
const btnEl = document.getElementById('generator');
btnEl.addEventListener('click', generator);
