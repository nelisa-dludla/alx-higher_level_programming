$(document).ready( function() {
	const divEle = $('DIV#red_header');
	divEle.click(
		function() {
			$('header').addClass('red');
		}
	);
});
