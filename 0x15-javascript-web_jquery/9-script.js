url = 'https://hellosalut.stefanbohacek.dev/?lang=fr'
$.get(url, function(data) {
	const divEle = $('DIV#hello');
	divEle.text(data.hello);
});
