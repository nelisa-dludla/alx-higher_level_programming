url = 'https://swapi-api.alx-tools.com/api/films/?format=json'
$.get(url, function(data) {
	const listEle = $('UL#list_movies');
	movieObjs = data.results
	movieObjs.forEach(movie => {
		listEle.append(`<li>${movie.title}</li>`);
	});
});
