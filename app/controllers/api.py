from app.run import app
from app.dao import flightsdao
import json

@app.route('/api/flights')
def getflights():

    payload = flightsdao.flight_listings.query.all()
    return json.dumps(payload)
