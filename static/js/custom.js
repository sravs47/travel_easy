$('#searchflight').click(function(e) {
    e.preventDefault();
    $.ajax({
        type: "GET",
        url: "/api/flights",
        data: {
            from: $("#from-place").val(), // < note use of 'this' here

        },
        success: function(result) {

            console.log(result)
        },

        error: function(result) {
            alert('error');
        }
    });
});
