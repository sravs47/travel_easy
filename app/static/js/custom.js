$('#searchflight').click(function(e) {
//Innerhtml to replace with flight thead
    e.preventDefault();
    $.ajax({
        type: "GET",
        url: "/api/flights",
//        data: {
//            from: $("#from-place").val(), // < note use of 'this' here
//
//        },
        success: function(result) {

            console.log(result)
            var obj = JSON.parse(result)
        },

        error: function(result) {
            console.log("error")
        }
    });
});
