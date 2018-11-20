$('#searchflight').click(function (e) {
    e.preventDefault();
    $.ajax({
        type: "GET",
        url: "/api/flights",
        data: {
            from: $("#from-place").val(), // < note use of 'this' here

        },
        success: function (result) {

            console.log(result);
            var table_template = `
                <table id="searchtable" class="table" align="center">
                    <thead class="black white-text">
                        <tr>
                            <th scope="col" data-field="id">id</th>
                            <th scope="col" data-field="airlines">airlines</th>
                            <th scope="col" data-field="flight_no" >flight_no</th>
                            <th scope="col" data-field="source" >source</th>
                            <th scope="col" data-field="destination" >destination</th>
                            <th scope="col" data-field="starttime" >starttime </th>
                            <th scope="col" data-field="endtime" >   endtime   </th>
                            <th scope="col" data-field="amount"> amount </th>
                        </tr>
                    </thead>
                </table>`;
            console.log("loading of thead heheh")
            console.log(typeof result)
            $('#searchresponse').html(table_template);

            // var obj = JSON.parse(result);
            $('#searchtable').bootstrapTable({
                result: JSON.parse(result)
            });

        },

        error: function (result) {
            console.log("error")
        }
    });
});
