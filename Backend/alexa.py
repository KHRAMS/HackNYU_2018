import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
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

def facechop(image):
    facedata = "/Users/KrishnanRam/Downloads/opencv/data/haarcascades/haarcascade_frontalface_default.xml"
    cascade = cv2.CascadeClassifier(facedata)

    img = cv2.imread(image)

    minisize = (img.shape[1],img.shape[0])
    miniframe = cv2.resize(img, minisize)

    faces = cascade.detectMultiScale(miniframe)

    for f in faces:
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

    return question(welcome_msg)


@ask.intent("YesIntent")

def next_round():
    start = time.time()
    cap = cv2.VideoCapture(0)  # video capture source camera (Here webcam of laptop)
    ret, frame = cap.read()  # return a single frame in variable `frame`

    cv2.imwrite('c1.jpg', frame)  # display the captured image

    cap.release()

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




if __name__ == '__main__':

    app.run(debug=True)