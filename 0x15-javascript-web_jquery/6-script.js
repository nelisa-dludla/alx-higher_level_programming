$(document).ready( function() {
	const divEle = $('DIV#update_header');
	divEle.click(
		function() {
			const headerEle = $('header');
			headerEle.text('New Header!!!');
		}
	);
});
