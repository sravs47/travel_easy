import json

from flask import render_template, session, request, redirect, url_for, flash
from flask_mysqldb import MySQL

from app import app, flight_listings
from app.helpers import utils
from app.helpers.loginHelper import is_logged_in
from app.helpers.registerHelper import RegisterForm

#initialize MYSQL
mysql=MySQL(app)

@app.route('/')
def default():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST':

        firstname = form.firstname.data
        lastname = form.lastname.data
        username = form.rusername.data
        email = form.email.data
        password = form.rpassword.data

        if form.validate():
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)",( f'{firstname} {lastname}', email, username, password))
            mysql.connection.commit()
            cur.close()
            flash('You are now registered and can log in', 'success')
            return redirect(url_for('login'))
        else:
            flash('Verify all the fields properly','danger')
    return render_template('register.html')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username = request.form['username']
        password_candidate=request.form['password']
        cur = mysql.connection.cursor()
        result = cur.execute("select * from users where username= %s",[username])
        if result >0:
            data = cur.fetchone()
            password=data['password']
            session['logged_in']=True
            session['username']=username
            flash('You are now logged in','success')
            return redirect(url_for('index'))
        else:
            error='Invalid login'
            return render_template('register.html',error=error)
        cur.close()

    else:
        error='Username not found'
        return render_template('register.html',error)
    return render_template('register.html')



@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out','success')
    return redirect(url_for('index'))

@app.route('/api/flights')
def getflights():
    return json.dumps([r.as_dict()for r in flight_listings.query.all()],default = utils.datetimeconverter)

if __name__=='__main__':
    app.run(debug=True)

