insert into flight_listings(airlines,flight_no,source,destination,starttime,endtime,seatcount,amount,miles,status,type)
values('American Airlines','AA330','San Antonio','Dallas',sysdate(),sysdate()+2000,100,150,5000,'On Time','Domestic');
insert into flight_listings(airlines,flight_no,source,destination,starttime,endtime,seatcount,amount,miles,status,type)
values('United Airlines','UA170','San Antonio','Chicago',sysdate(),sysdate()+2000,100,250,15000,'On Time','Domestic');

insert into hotel_listings(city,hname,address,rooms,hprice,fromdate,todate)
values('Dallas','Hilton Grand','101 South parkway',25,150,'2018-12-01 18:36:40','2018-12-01 18:56:40')
insert into hotel_listings(city,hname,address,rooms,hprice,fromdate,todate)
values('Chicago','Marriot hotels','102 North parkway',25,130,'2018-12-01 18:37:44','2018-12-01 18:57:44')

