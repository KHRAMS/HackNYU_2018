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
    image_1 = cv2.resize(image_1, (48, 48), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite("c4.jpg",image_1)

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch

def new_game():

    welcome_msg = render_template('welcome')

    return question(welcome_msg).reprompt(welcome_msg)


# @ask.intent("YesIntent")
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
        return audio('playing song').play('https://www.youtube.com/watch?time_continue=1&v=dQw4w9WgXcQ')
    else:
        return statement(render_template('drowsy_not'))



if __name__ == '__main__':

    app.run(debug=True)