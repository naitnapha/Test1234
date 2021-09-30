function getdata_facebook() {
	FB.api('/me','GET',
	  {"fields":"id,name,businesses,accounts.limit(200){picture,id,engagement,fan_count,link,name,new_like_count}"},
	  function(response) {
	      console.log("data : ",response);	
	  }
	);
}