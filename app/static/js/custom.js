$('#searchflight').click(function (e) {
    e.preventDefault();

    var table_template = `
                <table id="searchtable" class="table" align="center">
                    <thead class="table table-hover table-striped ">
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

    $('#searchresponse').html(table_template);


    // var obj = JSON.parse(result);
    $.get("/api/flights", function (data, status) {
        console.log(data)
        $('#searchtable').bootstrapTable({
            data: JSON.parse(data)
        });
    });
});
