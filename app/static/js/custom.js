
//search flights
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


//search hotels
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
                fromdate: $('#hotels').find("#date-start").val(),
                todate: $('#hotels').find('#date-end').val()
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
                title: 'Checkin'
            }, {
                field: 'todate',
                title: 'Checkout'
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
        var selection = $('#searchresponse').bootstrapTable('getSelections')[0];

    });
 });


//search packages

$('#searchpackage').click(function (e) {
    $('html,body').animate({
        scrollTop: $("#fh5co-tours").offset().top
     },'slow');
    searchresponseblock = `
        <div id="searchresponse1" class="table table-striped table-dark table-responsive" align="center"/>
        <div id="searchresponse2" class="table table-striped table-dark table-responsive" align="center"/>`;
    $("#searchcontainer").html(searchresponseblock);

    $('#searchresponse1').bootstrapTable({
        method: 'get',
        url: '/api/hotels',
        cache: false,
        striped: false,
        queryParams: function (params) {
           if($('#showdates').find("#date-start").val() == ''){
            return {
                city: $('#packages').find("#to-place").val(),
                fromdate: $('#packages').find('#date-start').val(),
                todate: $('#packages').find('#date-end').val()
            }
           }
            else{
               return{
                city: $('#packages').find("#to-place").val(),
                fromdate: $("#showdates").find("#date-start").val(),
                todate: $("#showdates").find('#date-end').val()
              }
            }
        },
        clickToSelect: true,
        columns:[{
            field:'radio',
            radio: 'true'
            },
            {
                field: 'id',
                title: 'ID',
                align: 'center',
                visible: false,
            }, {
                field: 'hname',
                title: 'HotelName',


            }, {
                field: 'address',
                title: 'Address',

            }, {
                field: 'hprice',
                title: 'Price',

            }, {
                field: 'fromdate',
                title: 'Checkin',

            }, {
                field: 'todate',
                title: 'Checkout',

            }],
            rowStyle: function rowStyle(row, index) {
                return {
                    classes: 'text-nowrap another-class',
                    css: {"color": "#4E443C", "font-size": "25px","font-family":"Georgia,serif"}
                };
            },
        onLoadSuccess: function () {

           $('#searchresponse1').find("tbody").find(".bs-checkbox").each(function(i, obj) {
                $(this).html('<input data-index="'+i+'" name="btSelectItem1" type="radio">');
           });

        }

    });
    $('#searchresponse2').bootstrapTable({
        method: 'get',
        url: '/api/flights',
        cache: false,
        striped: false,
        queryParams: function (params) {
            return {
                from: $('#packages').find("#from-place").val(),
                to: $('#packages').find("#to-place").val(),
                starttime: $('#packages').find('#date-start').val(),
                endtime: $('#packages').find('#date-end').val(),
                count: $('#padultscount').val() + $('#pchildcount').val()
            }
        },
        clickToSelect: true,
        columns:[{
            field:'radio',
            radio: 'true'
            },
            {
                field: 'id',
                title: 'Id',
                align: 'center',
                visible: false
            }, {
                field: 'airlines',
                title: 'Airlines'

            }, {
                field: 'flight_no',
                title: 'Flight Number'
            }, {
                field: 'source',
                title: 'Source'
            }, {
                field: 'destination',
                title: 'Destination'
            }, {
                field: 'starttime',
                title: 'Start-time'
            }, {
                field: 'endtime',
                title: 'Endtime'
            }, {
                field: 'amount',
                title: 'Price'
            }],
            rowStyle: function rowStyle(row, index) {
                return {
                    classes: 'text-nowrap another-class',
                    css: {"color": "#4E443C", "font-size": "25px","font-family":"Georgia,serif"}
                };
            },
        onLoadSuccess: function () {
//            console.log($('#searchresponse2').html());
        }

    });
    $("#searchcontainer").append(`
        <div class="col-xs-12 col-xs-2">
            <input type="submit" id="selectPackage" class="btn btn-primary btn-block" value="Select Package">
        </div>
    `);
    $('#selectPackage').click(function () {
        console.log($('#searchresponse1').bootstrapTable('getSelections')[0]);
        var hotelselection = $('input[name=btSelectItem1]:checked').closest("tr").get(0);
        var flightselection = $('input[name=btSelectItem]:checked').closest("tr").get(0);
        console.log(hotelselection)
        console.log(flightselection)

    });
 });


//blog- comments
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


// flight status
$('#getFlightStatus').click(function(e) {
//$('html,body').animate({
//            scrollTop: $("#fh5co-tours").offset().top
//        },
//        'slow');
      e.preventDefault();
      path="/api/flightstatus/"+$('#fno').val()
      $.get(path,function(data) {
          response = jQuery.parseJSON(data)
          var showdata = `
                     <div class="col-md-12">
						<div class="car">
							<div class="one-4">
								<h3>Flight Status</h3>
								<span class="price" id="selectflight">${response[0].status}</span>
							</div>
						</div>
					</div>
          `;
          $('#flightstatusresponse').html(showdata)
      });
});


//for packages advanced option
$('#flightadvanced').click(function() {
$('#showdates').toggle('slow',function(){
});
});




//<div class="col-md-4 table-responsive">
//                <table class="table">
//                <tr>
//                <th>
//                <img src="/static/images/flight.jpg" alt="flightdelayimage"
//                </th>
//                <th>
//                <input type="submit" id="selectflight"  value="${response[0].status}">
//                </th>
//                </tr>
//                </table>
//            </div>