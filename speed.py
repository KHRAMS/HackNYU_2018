
#Finds Speed
import requests
import json
import googlemaps
import time
from math import sin, cos, sqrt, atan2, radians

from datetime import datetime

def freegeoip_lat_long():
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat1 = j['latitude']
    lon1 = j['longitude']
    time.sleep(0.25)
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat2 = j['latitude']
    lon2 = j['longitude']
    return lat1,lon1,lat2,lon2
def calculate_speed():
    radius_of_earth=3963.0
    x = freegeoip_lat_long()
    rad_lat_1=radians(x[0])
    rad_lon_1=radians(x[1])
    rad_lat_2=radians(x[0])
    rad_lon_2=radians(x[1])
    dlon = rad_lon_2 - rad_lon_1
    dlat = rad_lat_2 - rad_lat_1

    a = sin(dlat / 2)**2 + cos(rad_lat_1) * cos(rad_lat_2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = radius_of_earth * c
    return distance/0.25
print(calculate_speed())
