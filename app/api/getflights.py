from app import app
from flask import request
import json
from app.dbModels.flight_listings import flight_listings
import datetime
from app.helpers import utils

@app.route('/api/flights')
def getflights():
    args = request.args
    output = json.dumps([r.as_dict() for r in flight_listings.query.filter(
        flight_listings.starttime == datetime.datetime.strptime(args['starttime'], '%m/%d/%Y'),
        flight_listings.seatcount >= int(args['count']),
        flight_listings.source == args['from'], flight_listings.destination == args['to'])],
                        default=utils.datetimeconverter)
    print(output)
    return output
