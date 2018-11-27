import datetime
import json
import os
import sys

from flask import Flask
from flask import render_template, session, request, redirect, url_for, flash
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, func

from app.helpers import utils
from app.helpers.loginHelper import is_logged_in
from app.helpers.registerHelper import RegisterForm

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


# MODELS#


class flight_listings(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    airlines = db.Column('airlines', db.String(20))
    flight_no = db.Column('flight_no', db.String(10))
    source = db.Column('source', db.String(20))
    destination = db.Column('destination', db.String(20))
    starttime = db.Column('starttime', db.DateTime)
    endtime = db.Column('endtime', db.DateTime)
    seatcount = db.Column('seatcount', db.Integer)
    amount = db.Column('amount', db.Integer)
    miles = db.Column('miles',db.Integer)

    def __init__(self, airlines, flight_no, source, destination, starttime, endtime, seatcount, amount,miles):
        self.airlines = airlines
        self.flight_no = flight_no
        self.source = source
        self.destination = destination
        self.starttime = starttime
        self.endtime = endtime
        self.seatcount = seatcount
        self.amount = amount
        self.miles = miles

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# class hotel_listings(db.Model):

class hotel_listings(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    city = db.Column('city', db.String(20))
    hname = db.Column('hname', db.String(20))
    address = db.Column('address', db.String(50))
    rooms = db.Column('rooms', db.Integer)
    hprice = db.Column('hprice', db.Integer)
    fromdate = db.Column('fromdate', db.DateTime)
    todate = db.Column('todate', db.DateTime)

    def __init__(self, city, hname, address, rooms, hprice, fromdate, todate):
        self.city = city
        self.hname = hname
        self.address = address
        self.rooms = rooms
        self.hprice = hprice
        self.fromdate = fromdate
        self.todate = todate

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class users(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    firstname = db.Column('firstname', db.String(20))
    lastname = db.Column('lastname', db.String(20))
    username = db.Column('username', db.String(30), unique=True)
    password = db.Column('password', db.String(100))
    email = db.Column('email', db.String(100))
    register_date = db.Column('register_date', db.DateTime)
    miles = db.Column('miles', db.Integer)
    phoneno = db.Column('phoneno',db.String(20))


    def __init__(self, firstname, lastname, username, password, email, register_date,miles,phoneno):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.email = email
        self.register_date = register_date
        self.miles = miles
        self.phoneno = phoneno

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class testimonals(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(30), ForeignKey("users.username"))
    comment = db.Column('comment', db.String(250))
    rating = db.Column('rating', db.Integer)
    c_date = db.Column('c_date', db.DateTime, default=func.sysdate())

    def __init__(self, username, comment, rating, c_date):
        self.username = username
        self.comment = comment
        self.rating = rating
        self.c_date = c_date

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

@app.route('/')
def default():
    return render_template('index.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/blog',methods=['GET','POST'])
@is_logged_in
def blog():
    if request.method == 'POST':
        a = request
        # print(request.form.get['comment'])
        feedback_result=testimonals(session['username'],request.form['comment'],5,datetime.datetime.now())
        db.session.add(feedback_result)
        db.session.commit()
        return redirect(url_for('index'))
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
        if users.query.filter_by(username=username, password=password_candidate).first() is not None:
            session['logged_in'] = True
            session['username'] = username
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


@app.route('/checkout')
@is_logged_in
def checkout():
    return render_template('checkout.html')

@app.route('/api/flights')
def getflights():
    args = request.args
    print(args)
    return json.dumps([r.as_dict() for r in flight_listings.query.filter(
        flight_listings.starttime == datetime.datetime.strptime(args['starttime'], '%m/%d/%Y'),
        flight_listings.source == args['from'], flight_listings.destination == args['to'])],
                      default=utils.datetimeconverter)


@app.route('/api/hotels')
def gethotels():
    datas = request.data
    return json.dumps([r.as_dict() for r in hotel_listings.query.filter(
        hotel_listings.fromdate == datetime.datetime.strptime(datas['fromdate'], '%m/%d,%Y'),
        hotel_listings.city == datas['city'])],
                      default=utils.datetimeconverter)
    # return json.dumps(r.as_dict() for r in hotel_listings.query.filter(
    #     hotel_listings.fromdate>datetime.datetime.strptime(datas['checkin'],'%m/%d,%Y'),
    #     hotel_listings.
    # ))

@app.route('/api/comments')
def getcomments():
    resp = testimonals.query.order_by(testimonals.c_date).limit(10);
    return json.dumps([r.as_dict() for r in testimonals.query.order_by(testimonals.c_date).limit(10)],default=utils.datetimeconverter)

# @app.route('/api/checkout', methods=['POST'])
# def checkout():



if __name__ == '__main__':
    app.run(debug=True)
