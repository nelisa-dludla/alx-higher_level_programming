$(document).ready( function() {
	const divEle = $('DIV#toggle_header')
	divEle.click(
		function() {
			$('header').toggleClass('green red');
		}
	);
});
