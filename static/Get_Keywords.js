$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				text : $('#stackoverflow_question').val()
			},
			type : 'POST',
			url : '/get_keywords',
			success : function(data){console.log(data)}
		})

		event.preventDefault();

	});

});