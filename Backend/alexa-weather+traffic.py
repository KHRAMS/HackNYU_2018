import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import json
from keras.preprocessing import image
import numpy as np
import cv2
import urllib.request, json, time
import sys
import os
import urllib.request, json, time
import urllib.request, json, time
import time
import requests

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def new_game():
    welcome_msg = render_template('welcome')

    return question(welcome_msg).reprompt(welcome_msg)


@ask.intent("TrafficIntent", convert={'origin': str, 'destination': str, 'departure': str, 'arrival': str})

def return_traffic_analysis(origin,destination,departure,arrival):
    import urllib.request, json, time
    endpoint = "https://maps.googleapis.com/maps/api/distancematrix/json?"
    api_key = "AIzaSyBTr-wJwTkr6VUt3xboaCyZBtQk_ST_GHY"
    origin = origin.replace(" ",",")
    destination = destination.replace(" ",",")
    departure_hour = departure.split(":")[0]
    departure_minute = departure.split(":")[1]
    departure_time = float(departure_hour + "." + departure_minute)

    arrival_hour = arrival.split(":")[0]
    arrival_minute = arrival.split(":")[1]
    arrival_time = float(arrival_hour + "." + arrival_minute)
    dict_time = {}
    best_time = 0
    while departure_time < arrival_time:
        nav_request = 'origins={}&destinations={}&departure_time={}&mode={}&traffic_model={}&key={}'.format(origin,
                                                                                                            destination,
                                                                                                            int(
                                                                                                                time.mktime(
                                                                                                                    time.strptime(
                                                                                                                        '2018-03-24 ' + departure + ":00",
                                                                                                                        '%Y-%m-%d %H:%M:%S'))),
                                                                                                            "driving",
                                                                                                            "best_guess",
                                                                                                            api_key)
        request = endpoint + nav_request
        response = urllib.request.urlopen(request).read()
        data = json.loads(response.decode('utf-8'))
        output = (data['rows'][0]['elements'][0]['duration_in_traffic']["text"])
        time_hour = output.replace(" mins", "")
        time_hour = time_hour.replace(" hour ", ".")
        time_hour = time_hour.replace(" hours ", ".")
        time_hour = time_hour.replace(" min", "")
        time_hour = float(time_hour)
        num = departure_time + time_hour
        if (num - int(num)) >= 0.6:
            num += 1.0
            num = num - 0.6
            num = round(num, 2)
        if (num) < arrival_time:
            dict_time[departure_time] = time_hour
            best_time = departure_time
        departure_time += 0.25
        departure_time = round(departure_time, 2)
        if (departure_time - int(departure_time)) >= 0.6:
            departure_time += 1.0
            departure_time = departure_time - 0.6
            departure_time = round(departure_time, 2)

    if ("The best time to leave is: " + (str(best_time).replace(".", ":"))) == "The best time to leave is: 0":
        return statement("Within the paremeters you inputted you will not reach your destination on time.")
    else:
        return statement("The best time to leave is: " + (str(best_time).replace(".", ":")))


@ask.intent("NoIntent")
def no_intent():
    return statement("Bye")


@ask.intent("TimeIntent", convert={'time': str})
def time_intent(time):
    return statement("Time is", time)


if __name__ == '__main__':
    app.run(debug=True)
