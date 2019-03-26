$("document").ready(function(){
	$("#fib-form input[name='position']").change(function(){
		$(".suggestions").loadingView({
			"state": true,
		});
		$.ajax({
			type: "GET",
			url: "/get/latest/searches/",
			success: function(data){
				$.each(data, function(index, value){
					$(".suggestions ol").append("<li>Instance at Position "+ value['fields']['instance_position'] + " is "+ value['fields']['instance_value'] +".");
				})
				$("#fib-form button").removeAttr("disabled");
			}
		});
	});
});