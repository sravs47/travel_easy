from flask import Flask,render_template,session,request,redirect,url_for,logging,flash
from flask_mysqldb import MySQL
import jinja2
import os
import sys
from app.helpers.registerHelper import RegisterForm
from functools import wraps

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

@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/register',methods=['GET','POST'])
def register():
    print('Entered register')
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
            flash('Verify all the fields properly','failure')


    return render_template('register.html')

@app.route('/register',methods=['GET',''])






if __name__=='__main__':
    app.run(debug=True)

