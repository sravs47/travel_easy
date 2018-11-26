$('#searchflight').click(function (e) {
// animate for slide down
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
        $('#bookplaceholder').html(table_template);
        $('#selectflight').click(function () {
        console.log($('#searchresponse').bootstrapTable('getSelections')[0]);
    });
});

$('#SearchHotel').click(function (e) {
    $('html,body').animate({
            scrollTop: $("#fh5co-tours").offset().top
        },
        'slow');
    $('#searchresponse').bootstrapTable({
        method: 'get',
        url: '/api/hotels',
        cache: false,
        striped: false,
        queryParams: function (params) {
            return {
                city: $("#hcity").val(),
                fromdate: $('#date-end').val(),
                todate: $('#adultcount').val()
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
                field: 'hname',
                title: 'HotelName'

            }, {
                field: 'address',
                title: 'Address'
            }, {
                field: 'hprice',
                title: 'Price'
            }, {
                field: 'fromdate',
                title: 'From'
            }, {
                field: 'todate',
                title: 'todate'
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
                <input type="submit" id="selectHotel" class="btn btn-primary btn-block" value="Book Hotel">
            </div>
        `;
    $('#bookplaceholder').html(table_template);
    // console.log($('#searchresponse').html());
    $('#selectHotel').click(function () {
        console.log($('#searchresponse').bootstrapTable('getSelections')[0]);
    });
 });


$(document).ready(function() {
    $.get( "/api/comments", function(data) {
    response = jQuery.parseJSON(data)
    var innerhtml = "";
    for(var i in response){
        innerhtml = innerhtml + `
                    <div class="col-md-4">
                        <div class="box-testimony">
                            <blockquote>
                                <span class="quote"><span><i class="icon-quotes-right"></i></span></span>
                                <p>&ldquo;${response[i].comment}&rdquo;</p>
                            </blockquote>
                         <p class="author">${response[i].username}</p>
                        </div>
                    </div>`;
    }
    $('#loadcomments').html(innerhtml);
    });
});







