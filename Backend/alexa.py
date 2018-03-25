import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session, audio
# from keras.models import load_model
from keras.models import model_from_json
import json
from keras.preprocessing import image
# from keras.optimizers import Adadelta
import numpy as np
import cv2
import sys
import os
from constants import *
import time
import requests
import _thread as thread
# import datetime

def facechop(image):
    facedata = "/Users/KrishnanRam/Downloads/opencv/data/haarcascades/haarcascade_frontalface_default.xml"
    cascade = cv2.CascadeClassifier(facedata)

    img = cv2.imread(image)

    minisize = (img.shape[1],img.shape[0])
    miniframe = cv2.resize(img, minisize)

    faces = cascade.detectMultiScale(miniframe)

    with faces[0] as f:
        x, y, w, h = [ v for v in f ]
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,255))

        sub_face = img[y:y+h, x:x+w]
        face_file_name = "c3.jpg"
        cv2.imwrite(face_file_name, sub_face)
    image_1 = cv2.imread('c3.jpg')
    image_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)
    image_1 = cv2.resize(image_1, (48, 48), interpolation=cv2.INTER_CUBIC) / 255.
    cv2.imwrite("c4.jpg",image_1)

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch

def new_game():

    welcome_msg = render_template('welcome')

    return question(welcome_msg).reprompt(welcome_msg)


#
# def last_round():
#     return statement("Hi.")


@ask.intent("EmotionIntent")
def next_round():
    start = time.time()
    emotion='angry'
    cap = cv2.VideoCapture(0)  # video capture source camera (Here webcam of laptop)
    ret, frame = cap.read()  # return a single frame in variable `frame`

    cv2.imwrite('c1.jpg', frame)  # display the captured image

    cap.release()

    #RASPBERRY PI 3 STUFF HERE!!!!

    # r = requests.put('https://fb81eb17.ngrok.io', data={'input': 'data'})
    # with open("c1.jpg", 'wb') as f:
    #     f.write(r.content)


    facedata = "/Users/KrishnanRam/Downloads/opencv/data/haarcascades/haarcascade_frontalface_default.xml"
    cascade = cv2.CascadeClassifier(facedata)

    img = cv2.imread('c1.jpg')

    minisize = (img.shape[1], img.shape[0])
    miniframe = cv2.resize(img, minisize)

    faces = cascade.detectMultiScale(miniframe)

    for f in faces:
        x, y, w, h = [v for v in f]
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255))

        sub_face = img[y:y + h, x:x + w]
        face_file_name = "c3.jpg"
        cv2.imwrite(face_file_name, sub_face)
    image_1 = cv2.imread('c3.jpg')
    image_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)
    image_1 = cv2.resize(image_1, (48, 48), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite("c4.jpg", image_1)

    json_file = open("model.json", 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    model.load_weights("best_weight.hdf5")
    img = image.load_img('c4.jpg', target_size=(48, 48))
    img = np.expand_dims(img, axis=0)

    classes = model.predict_classes(img)


    EMOTIONS = ['angry', 'disgusted', 'fearful', 'happy', 'neutral','sad', 'surprised']


    emotion = EMOTIONS[classes[0]]
    print(emotion)
    end = time.time()
    print(end-start)

    if classes[0] == 0:
        win = render_template('win')
        return question(win)
    else:
        lose = render_template('lose')
        return question(lose)

@ask.intent("DrowsyIntent")
def drowsy_round():


    face_cascade = cv2.CascadeClassifier(
        '/Users/KrishnanRam/Downloads/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('/Users/KrishnanRam/Downloads/opencv/data/haarcascades/haarcascade_eye.xml')
    cam = cv2.VideoCapture(0)
    count = 0
    iters = 0
    temp = 0
    count_1 = 0
    start = time.time()
    while (time.time() - start < 7.0):
        ret, cur = cam.read()
        gray = cv2.cvtColor(cur, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(10, 10))
        for (x, y, w, h) in faces:
            # cv2.rectangle(cur,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = cur[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            if len(eyes) == 0:
                print("Eyes closed")
                temp += 0
            else:
                print("Eyes open")
                temp += 1
            print(iters)
            iters += 1
            if iters == 3:
                print("Hello World")
                iters = 0
                if temp == 0:
                    print ("Drowsiness Detected!!!")
                    temp = 0
                    count_1 +=1

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    if count_1 >=  2:
        drowsy = render_template('drowsy')
        return question(drowsy)
    else:
        return question(render_template('drowsy_not'))

@ask.intent("TrafficIntent", convert={'origin': str, 'destination': str, 'departure': str, 'arrival': str})

def return_traffic_analysis(origin,destination,departure,arrival):
    import urllib.request, json, time
    endpoint = "https://maps.googleapis.com/maps/api/distancematrix/json?"
    api_key = "AIzaSyDh7AyHVeTuX5BM3gJPj5nUg0FiPEknmLo"
    origin = origin.replace(" ",",")
    print(origin,destination,departure,arrival)
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
                                                                                                                        '2018-03-25 ' + departure + ":00",
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
        return question("Within the paremeters you inputted you will not reach your destination on time.")
    else:
        return question("The best time to leave is: " + (str(best_time).replace(".", ":")))


@ask.intent("WeatherIntent",convert={'destination':str, 'origin':str})

def return_weather_analysis(destination, origin):
    import urllib.request, json, time
    destination_address = destination.replace(" ","+")
    origin_address = origin.replace(" ","+")
    endpoint = "https://maps.googleapis.com/maps/api/distancematrix/json?"
    api_key = "AIzaSyDh7AyHVeTuX5BM3gJPj5nUg0FiPEknmLo"

    nreq = 'origins={}&destinations={}&key={}'.format(origin_address, destination_address, api_key)
    req = endpoint + nreq
    resp = urllib.request.urlopen(req).read()
    dta = json.loads(resp.decode('utf-8'))

    destination_address = (dta["destination_addresses"][0]).split(",")[2].split(" ")[2]
    origin_address = (dta["origin_addresses"][0]).split(",")[2].split(" ")[2]

    origin_endpoint = "https://api.openweathermap.org/data/2.5/weather?"
    origin_key = "7487c4fa1078b870d628607a3e4e8ccb"
    origin_nav_request = 'zip={}&APPID={}'.format(origin_address,origin_key)
    origin_request = origin_endpoint + origin_nav_request
    origin_response = urllib.request.urlopen(origin_request).read()
    origin_data = json.loads(origin_response.decode('utf-8'))
    origin_weather = (origin_data["weather"][0]["id"])

    destination_endpoint = "https://api.openweathermap.org/data/2.5/weather?"
    destination_key = "7487c4fa1078b870d628607a3e4e8ccb"
    destination_nav_request = 'zip={}&APPID={}'.format(destination_address, destination_key)
    destination_request = destination_endpoint + destination_nav_request
    destination_response = urllib.request.urlopen(destination_request).read()
    destination_data = json.loads(destination_response.decode('utf-8'))
    destination_weather = (destination_data["weather"][0]["id"])

    if 781 == origin_weather or 781 == destination_weather or 900 <= origin_weather <= 902 or 900 <= destination_weather <= 902 or 905 <= origin_weather <= 906 or 905 <= destination_weather <= 906 or 957 <= origin_weather <= 962 or 957 <= destination_weather <= 962:
        return statement("Be careful of this extreme weather, I advise to definitely not drive outside.")
    elif 602 == origin_weather or 602 == destination_weather or 621 <= origin_weather <= 622 or 621 <= destination_weather <= 622:
        return statement("Be careful of the heavy snow, I recommend not driving outside currently")
    elif 600 <= origin_weather <= 601 or 600 <= destination_weather <= 601 or 611 <= origin_weather <= 620 or 611 <= destination_weather <= 620:
        return statement("Be careful of the sleet and light snow, make sure you are not speeding")
    elif 200 <= origin_weather <= 531 or 200 <= destination_weather <= 531:
        return statement("Be careful of the rain and thunder, make sure you are not speeding")
    else:
        return statement("The weather outside is safe and great to drive. Remember to buckle up and maintain control of the car")

@ask.intent("NoIntent")
def no_intent():
    return statement("Bye")


if __name__ == '__main__':

    app.run(debug=True)