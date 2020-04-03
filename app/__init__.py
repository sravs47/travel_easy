import datetime
import json
import os
import sys

from flask import Flask
from flask import render_template, session, request, redirect, url_for, flash
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from jinja2 import Markup

from app.helpers import utils
from app.helpers.loginHelper import is_logged_in
from app.helpers.registerHelper import RegisterForm
from app.helpers import checkoutHelper
from app.helpers.checkoutHelper import hotel_li_block, flight_li_block

template_folder = (os.path.dirname(sys.modules['__main__'].__file__))
print('********************************' + template_folder)
# app = Flask(__name__, template_folder=template_folder)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'

# config mySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rootroot'
app.config['MYSQL_DB'] = 'traveleasy'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rootroot@localhost/traveleasy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.dbModels.flight_listings import flight_listings
from app.dbModels.hotel_listings import hotel_listings
from app.dbModels.order_history import order_history
from app.dbModels.persons import persons
from app.dbModels.promocode import promocode
from app.dbModels.testimonals import testimonals
from app.dbModels.users import users


@app.route('/')
def default():
    return render_template('index.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/blog', methods=['GET', 'POST'])
@is_logged_in
def blog():
    if request.method == 'POST':
        a = request
        feedback_result = testimonals(session['username'], request.form['comment'], request.form['rate'],
                                      datetime.datetime.now())
        db.session.add(feedback_result)
        db.session.commit()
    return render_template('blog.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    print(request)
    a = request
    if request.method == 'POST':
        if form.validate():
            result = users(request.form['firstname'], request.form['lastname'], request.form['rusername'],
                           request.form['rpassword'], request.form['email'], datetime.datetime.now())
            db.session.add(result)
            db.session.commit()
            session['logged_in'] = True
            session['username'] = request.form['rusername']
            session['miles'] = 0
            flash('You are now registered and can log in', 'success')
            return redirect(url_for('index'))
        else:
            flash('Verify all the fields properly', 'danger')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_candidate = request.form['password']
        user: users = users.query.filter_by(username=username, password=password_candidate).first()
        if user is not None:
            session['logged_in'] = True
            session['username'] = username
            session['miles'] = user.miles
            flash('You are now logged in', 'success')
            return redirect(url_for('index'))
        else:
            error = 'Invalid login'
            return render_template('register.html', error=error)
    else:
        error = 'Username not found'
        return render_template('register.html', error)
    return render_template('register.html')


@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('index'))


@app.route('/pastorders')
@is_logged_in
def pastorders():
    orderblock = ''
    flight_ids = {}
    hotel_ids = {}
    orders: order_history = order_history.query.filter_by(username=session['username'], order_status='complete')
    for order in orders:
        flight: flight_listings = flight_listings.query.filter_by(id=order.flight_id).first()
        hotel: hotel_listings = hotel_listings.query.filter_by(id=order.hotel_id).first()

        orderblock = orderblock + """ <tr>
                                         <th scope="row">{}</th>
                                         <td>{}</td>
                                         <td>{}</td>
                                        <td>{}</td>
                                        <td>{}</td>
                                        <td>{}</td>
                                        <td>${}</td>
                                        </tr>""".format(order.id, order.purchase_date, order.username,
                                                        flight.flight_no if flight is not None else '',
                                                        hotel.hname if hotel is not None else '', order.total_persons,
                                                        order.total_price)
    print(orderblock)
    return render_template('pastorders.html', orderblock=Markup(orderblock))


@app.route('/checkout', methods=["POST", "GET"])
@is_logged_in
def checkout():
    args = request.args
    hotelselection = args.get("hotelselection", None)
    flightselection = args.get("flightselection", None)
    totalcount = args.get("ppl", 0)
    flightdata = None
    hoteldata = None
    if request.method == "POST":
        orders = order_history(username=session['username'],
                               flight_id=flightselection, hotel_id=hotelselection,
                               order_status='incomplete', total_persons=totalcount)
        db.session.add(orders)
        db.session.commit()

    orderblock = ''
    order: order_history = order_history.query.filter_by(username=session['username'],
                                                         order_status='incomplete').order_by(
        order_history.id.desc()).first()
    flight_ids = []
    hotel_ids = []
    amount = 0
    if order is not None and order.flight_id is not None:
        flight_ids.append(order.flight_id)
    if order is not None and order.hotel_id is not None:
        hotel_ids.append(order.hotel_id)

    for flight_id in flight_ids:  # write for loop for orders. get flight listings and hotel listings in a list
        flightlisting: flight_listings = flight_listings.query.filter_by(id=flight_id).first()
        print((flightlisting.starttime).strftime('%m/%d/%Y'))
        print(str(flightlisting.amount))
        orderblock = orderblock + flight_li_block.format(flightlisting.airlines,
                                                         flightlisting.flight_no, flightlisting.source,
                                                         flightlisting.destination, flightlisting.begins,
                                                         flightlisting.ends,
                                                         (flightlisting.starttime).strftime('%m/%d/%Y'),
                                                         str(flightlisting.amount))

        amount = amount + flightlisting.amount * order.total_persons

    for hotel_id in hotel_ids:
        hotellisting: hotel_listings = hotel_listings.query.filter_by(id=hotel_id).first()

        orderblock = orderblock + hotel_li_block.format(hotellisting.hname, hotellisting.city, hotellisting.fromdate,
                                                        hotellisting.todate, hotellisting.hprice)

        amount = amount + hotellisting.hprice * order.total_persons
    orderblock = orderblock + """<li class="list-group-item d-flex justify-content-between lh-condensed">
                        <div>
                            <h6 class="my-0"> Summary:  </h6>
                            <small class="text-muted">Total Persons: {}</small>
                        </div>
                        <span class="text-muted">Total Amount: ${}</span>
                    </li>""".format(order.total_persons if order is not None else 0, amount)

    return render_template('checkout.html', orderblock=Markup(orderblock),
                           amount=round(float(amount) * float(0.8)) if len(flight_ids) > 0 and len(
                               hotel_ids) > 0 else amount)


@app.route('/order', methods=['POST', 'GET'])
def placeOrder():
    if request.method == 'POST':
        form = request.form
        order: order_history = order_history.query.filter_by(username=session['username'],
                                                             order_status='incomplete').order_by(
            order_history.id.desc()).first()
        order.email = request.form['email']
        order.address = request.form['address'] + request.form['address2'] + request.form['country'] + request.form[
            'state'] + request.form['zip']
        order.total_price = int(request.form['Amount'][1:])
        order.card_name = request.form.get('cc-name', None)
        order.card_type = request.form.get('paymentMethod', None)
        order.card_number = request.form.get('cc-number', None)
        order.cvv_no = request.form.get('cc-cvv', None)
        order.order_status = 'complete'
        order.purchase_date = datetime.datetime.now()

        user: users = users.query.filter_by(username=order.username).first()

        if order.card_number is not None and order.card_number == '' and user.miles < 25000:
            return render_template('ordersummaryerror.html', miles=user.miles)

        if order.flight_id is not None:
            flightlisting: flight_listings = flight_listings.query.filter_by(id=order.flight_id).first()

            if order.card_number is None and order.card_number == '' and flightlisting.type == 'International' and user.miles < 50000:
                return render_template('ordersummaryerror.html', miles=user.miles)
            flightlisting.seatcount = flightlisting.seatcount - order.total_persons
            user.miles = user.miles + flightlisting.miles

        if order.hotel_id is not None:
            hotellisting: hotel_listings = hotel_listings.query.filter_by(id=order.hotel_id).first()
            hotellisting.rooms = hotellisting.rooms - 1

        db.session.commit()

        if order.card_number is not None and order.card_number == '':
            user.miles = user.miles - 25000 if flightlisting.type == 'Domestic' else user.miles - 50000
            session['miles'] = user.miles

        db.session.commit()
        return render_template('ordersummary.html', orderid=order.id)
    return render_template('index.html')


@app.route('/flightStatus')
def flightstatus():
    return render_template('flightStatus.html')



@app.route('/api/hotels')
def gethotels():
    datas = request.args
    output = json.dumps([r.as_dict() for r in hotel_listings.query.filter(
        hotel_listings.fromdate == datetime.datetime.strptime(datas['fromdate'], '%m/%d/%Y'),
        hotel_listings.rooms >= 1,
        hotel_listings.city == datas['city'])], default=utils.datetimeconverter)
    print(output)
    return output


@app.route('/api/comments')
def getcomments():
    return json.dumps([r.as_dict() for r in testimonals.query.order_by(testimonals.c_date).limit(20)],
                      default=utils.datetimeconverter)


@app.route('/api/flightstatus/<flightno>')
def get_flight_status(flightno):
    response = json.dumps(
        [r.as_dict() for r in flight_listings.query.filter(flight_listings.flight_no == flightno,
                                                           flight_listings.starttime == datetime.datetime.strptime(
                                                               request.args['date'], '%m/%d/%Y'))],
        default=utils.datetimeconverter);
    return response


if __name__ == '__main__':
    app.run(debug=True)
