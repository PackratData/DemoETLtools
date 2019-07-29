

def check_longitude(value):
    if value <= -180 and value >= 180:
        raise ValueError("must be between -180 and 180")

def check_latitude(value):
    if value <= -90 and value >= 90:
        raise ValueError("must be between -90 and 90")