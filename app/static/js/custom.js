$('#searchflight').click(function (e) {
    $('html,body').animate({
            scrollTop: $("#fh5co-tours").offset().top
        },
        'slow');
    $('#searchresponse').bootstrapTable({
        method: 'get',
        url: '/api/flights',
        cache: false,
        striped: false,
        queryParams: function (params) {
            return {
                from: $("#from-place").val(),
                to: $("#to-place").val(),
                starttime: $('#date-start').val(),
                endtime: $('#date-end').val(),
                count: $('#adultcount').val() + $('#childcount').val()
            }
        },
        clickToSelect: true,
        columns: [{
            field: 'radio',
            radio: 'true'
        },
            {
                field: 'id',
                title: 'ID',
                align: 'center',
                visible: false
            }, {
                field: 'airlines',
                title: 'AIRLINES'

            }, {
                field: 'flight_no',
                title: 'FLIGHT NUMBER'
            }, {
                field: 'source',
                title: 'SOURCE'
            }, {
                field: 'destination',
                title: 'DESTINATION'
            }, {
                field: 'starttime',
                title: 'STARTTIME'
            }, {
                field: 'endtime',
                title: 'ENDTIME'
            }, {
                field: 'amount',
                title: 'AMOUNT'
            }],
        rowStyle: function rowStyle(row, index) {
            return {
                classes: 'text-nowrap another-class',
                css: {"color": "#4E443C", "font-size": "25px","font-family":"Georgia,serif"}
            };
        },
        onLoadSuccess: function () {
            console.log($('#searchresponse').html());
        }
    });

    var table_template = `
            <div class="col-xs-12 col-xs-2">
                <input type="submit" id="selectflight" class="btn btn-primary btn-block" value="Book Flight">
            </div>
        `;
    $('#bookflightplaceholder').html(table_template);
    // console.log($('#searchresponse').html());
    $('#selectflight').click(function () {
        console.log($('#searchresponse').bootstrapTable('getSelections')[0]);
    });

});

