// Bu yerda endi webpack js ni ozi kanfiguratsiya qilib beradi
module.exports = {
	mode: 'development',
	entry: './src/js/script.js',
	output: {
		path: path.resolve(__dirname, 'dist/js'), // Bu esa ochiladigan fayillarni nomi va joylashishi
		filename: 'bundle.js', // Bu hammasini toplaydigan fayl nomi
	},
	watch: true,
	devtool: 'source-map',
	module: {}
};

// Bu larni js ni hammasini src degan papkaga joylashtiramz
// Keyin yana modules degan papka ochamiz u yerda modullar joylashadi
