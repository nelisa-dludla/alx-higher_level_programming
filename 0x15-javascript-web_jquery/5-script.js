$(document).ready( function() {
	const divEle = $('DIV#add_item');
	divEle.click(
		function() {
			const listEle = $('UL.my_list');
			listEle.append('<li>Item</li>');
		}
	);
});
