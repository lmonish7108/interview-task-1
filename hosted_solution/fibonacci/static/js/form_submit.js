$("document").ready(function(){
	var _initial_suggestion= true;
	$("#fib-form input[name='position']").focus(function(){
		if (_initial_suggestion){
			let _suggestions = '';
			$.ajax({
				type: "GET",
				url: "/get/latest/searches/",
				success: function(data){
					$.each(data, function(index, value){
						_suggestions += "<li>Instance at Position "+ value['fields']['instance_position'] + " is "+ value['fields']['instance_value'] +".";
					});
					$(".suggestions ol").html(_suggestions);
					$("#fib-form button").removeAttr("disabled");
				}
			});	
		}
		_initial_suggestion=false;
	});
});