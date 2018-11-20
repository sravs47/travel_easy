import datetime

def datetimeconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
