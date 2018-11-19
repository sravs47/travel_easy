import os
import sys
import json

from flask import Flask, render_template, session, request, redirect, url_for, flash
from flask_mysqldb import MySQL

from app.helpers.registerHelper import RegisterForm
from app.helpers.loginHelper import is_logged_in

app=Flask(__name__,template_folder=os.path.dirname(sys.modules['__main__'].__file__))
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'

# my_loader = jinja2.ChoiceLoader([app.jinja_loader,jinja2.FileSystemLoader(os.path.dirname(sys.modules['__main__'].__file__))])
# app.jinja_loader = my_loader

#config mySQL
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='rootroot'
app.config['MYSQL_DB']='traveleasy'
app.config['MYSQL_CURSORCLASS']='DictCursor'

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
    payload = {
        'flight_no':'A1',
        'source':'san antonio',
        'destination':'austin'
    }
    return json.dumps(payload)




if __name__=='__main__':
    app.run(debug=True)

