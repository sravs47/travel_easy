import datetime
import json

from flask import render_template, session, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from app import app, flight_listings, users, hotel_listings,testimonals
from app.helpers import utils
from app.helpers.loginHelper import is_logged_in
from app.helpers.registerHelper import RegisterForm

db = SQLAlchemy(app)


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
