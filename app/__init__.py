from flask import Flask
import os,sys
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

template_folder = (os.path.dirname(sys.modules['__main__'].__file__))
print('********************************'+template_folder)
app=Flask(__name__,template_folder=template_folder)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'

#config mySQL
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='rootroot'
app.config['MYSQL_DB']='traveleasy'
app.config['MYSQL_CURSORCLASS']='DictCursor'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rootroot@localhost/traveleasy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)
migrate = Migrate(app,db)


#MODELS#


class flight_listings(db.Model):
    id = db.Column('id',db.Integer,primary_key=True)
    airlines=db.Column('airlines',db.String(20))
    flight_no = db.Column('flight_no',db.String(10))
    source = db.Column('source',db.String(20))
    destination = db.Column('destination',db.String(20))
    starttime = db.Column('starttime',db.DateTime)
    endtime = db.Column('endtime', db.DateTime)
    seatcount = db.Column('seatcount',db.Integer)
    amount = db.Column('amount',db.Integer)

    def __init__(self,airlines,flight_no,source,destination,starttime,endtime,seatcount,amount):
        self.airlines = airlines
        self.flight_no = flight_no
        self.source = source
        self.destination = destination
        self.starttime = starttime
        self.endtime = endtime
        self.seatcount = seatcount
        self.amount = amount

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
# class hotel_listings(db.Model):
# db.init_app()