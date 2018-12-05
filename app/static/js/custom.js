
//search flights
$('#searchflight').click(function (e) {
// animate for slide down
    $('html,body').animate({
            scrollTop: $("#fh5co-tours").offset().top
        },
        'slow');

    console.log('_________________________-')
    console.log($('#adultcount').val())
    console.log($('#childcount').val())
    console.log(Number($('#adultcount').val()) + Number($('#childcount').val()))

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
                count: (Number($('#adultcount').val()) + Number($('#childcount').val()))
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
                title: 'Starttime'
            }, {
                field: 'endtime',
                title: 'Endtime'
            },{
                field: 'count',
                title: 'People'
            }, {
                field: 'amount',
                title: 'Amount(each)'
            }],
        rowStyle: function rowStyle(row, index) {
            return {
                classes: 'text-nowrap another-class',
                css: {"color": "#4E443C", "font-size": "20px","font-family":"Georgia,serif"}
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
        console.log($('#searchresponse').bootstrapTable('getSelections')[0].id);
        path = "/checkout?ppl="+(Number($('#adultcount').val()) + Number($('#childcount').val()))+"&flightselection="+$('#searchresponse').bootstrapTable('getSelections')[0].id;
        $.post(path,function(data){
           window.location="http://localhost:5000/checkout"
        });

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
                todate: $('#hotels').find('#date-end').val(),
                count: (Number($('#hadultscount').val()) + Number($('#hchildrencount').val())),
                rooms: $('#hotels').find('#hrooms').val()

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
                field: 'fromdate',
                title: 'Checkin'
            }, {
                field: 'todate',
                title: 'Checkout'
            },{
                field: 'count',
                title: 'People'
            }, {
                field: 'rooms',
                title: 'Rooms'
            },{
                field: 'hprice',
                title: 'Price(each)'
            } ],
        rowStyle: function rowStyle(row, index) {
            return {
                classes: 'text-nowrap another-class',
                css: {"color": "#4E443C", "font-size": "20px","font-family":"Georgia,serif"}
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
        console.log($('#searchresponse').bootstrapTable('getSelections')[0].id);
        path = "/checkout?ppl="+(Number($('#hadultscount').val()) + Number($('#hchildrencount').val()))+"&hotelselection="+$('#searchresponse').bootstrapTable('getSelections')[0].id;
        $.post(path,function(data){
           window.location="http://localhost:5000/checkout"
        });

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
                todate: $('#packages').find('#date-end').val(),
                count: $('#padultscount').val() + $('#pchildcount').val(),
                rooms:$('#packages').find('#prooms').val()
            }
           }
            else{
               return{
                city: $('#packages').find("#to-place").val(),
                fromdate: $("#showdates").find("#date-start").val(),
                todate: $("#showdates").find('#date-end').val(),
                count: $('#padultscount').val() + $('#pchildcount').val(),
                rooms:$('#prooms').val()
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
                align: 'center'
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
            },{
                field: 'count',
                title: 'People'
            }, {
                field: 'rooms',
                title: 'Rooms'
            }, {
                field: 'todate',
                title: 'Checkout',
            }],
            rowStyle: function rowStyle(row, index) {
                return {
                    classes: 'text-nowrap another-class',
                    css: {"color": "#4E443C", "font-size": "20px","font-family":"Georgia,serif"}
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
                align: 'center'
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
            },{
                field: 'count',
                title: 'People'
            }, {
                field: 'amount',
                title: 'Price'
            }],
            rowStyle: function rowStyle(row, index) {
                return {
                    classes: 'text-nowrap another-class',
                    css: {"color": "#4E443C", "font-size": "20px","font-family":"Georgia,serif"}
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
        var hotelselection = $('input[name=btSelectItem1]:checked').closest("tr").find("td").slice(1,2).text();
        var flightselection = $('input[name=btSelectItem]:checked').closest("tr").find("td").slice(1,2).text();

        console.log(hotelselection)
        console.log(Number($('#padultscount').val())+Number($('#pchildcount').val()))
        console.log(Number($('#pchildcount').val()))
        path = "/checkout?ppl="+(Number($('#padultscount').val()) + Number($('#pchildcount').val()))+"&hotelselection="+hotelselection+"&flightselection="+flightselection;
        $.post(path,function(data){
           window.location="http://localhost:5000/checkout"
        });

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
    $('#showdates').toggle('slow');
});

$('#miles').click(function(){
    $('#paymentblock').toggle('slow');
});
