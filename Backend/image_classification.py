# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Conv2D, Dropout
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers.normalization import BatchNormalization
from keras.layers import Dense
import keras
import h5py
import numpy as np

import boto3
import json
import cv2

# Camera 0 is the integrated web cam on my netbook
# camera_port = 0
#
# #Number of frames to throw away while the camera adjusts to light levels
# ramp_frames = 30
#
# # Now we can initialize the camera capture object with the cv2.VideoCapture class.
# # All it needs is the index to a camera port.
# camera = cv2.VideoCapture(camera_port)
#
# # Captures a single image from the camera and returns it in PIL format
# def get_image():
#  # read is the easiest way to get a full image out of a VideoCapture object.
#  retval, im = camera.read()
#  return im
#
# # Ramp the camera - these frames will be discarded and are only used to allow v4l2
# # to adjust light levels, if necessary
# for i in xrange(ramp_frames):
#  temp = get_image()
# # Take the actual image we want to keep
# camera_capture = get_image()
# file = "/home/katchu11/Pictures/user.jpg"
# # A nice feature of the imwrite method is that it will automatically choose the
# # correct format based on the file extension you provide. Convenient!
# cv2.imwrite(file, camera_capture)
#
# # You'll want to release the camera, otherwise you won't be able to create a new
# # capture object until your script exits
# del(camera)


# Initialziing the CNN

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape = (48, 48, 3), padding='valid',activation = 'relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), input_shape = (48, 48, 3), activation = 'relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.35))

model.add(Conv2D(256, (3, 3), input_shape = (48, 48, 3), activation = 'relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))

# model.add(Conv2D(512, (3, 3)))
# model.add(BatchNormalization())
# model.add(Activation('relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Dropout(0.5))


model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))

model.add(Dense(512, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))

model.add(Dense(7, activation='softmax'))

print(model.summary())
adam = keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=True )
model.compile(optimizer = adam, loss = 'categorical_crossentropy', metrics = ['accuracy'])
# Part 2 - Fitting the CNN to the images
from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale = 1./255, shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True)
test_datagen = ImageDataGenerator(rescale = 1./255)
training_set = train_datagen.flow_from_directory('/home/katchu11/HackNYU_2018/dataset/test_set',
target_size = (48, 48),
batch_size = 32,
class_mode = 'categorical')
test_set = test_datagen.flow_from_directory('/home/katchu11/HackNYU_2018/dataset/training_set',
target_size = (48, 48),
batch_size = 32,
class_mode = 'categorical')
model.fit_generator(training_set,
steps_per_epoch = 8000,
epochs   = 7,
validation_data = test_set,
validation_steps = 2000,verbose=1)
model.save('test2_model.h5')
from keras.preprocessing import image
test_image = image.load_img('/home/katchu11/HackNYU_2018/dataset/training_set/angry5513.jpg', target_size = (48, 48))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = model.predict(test_image)
print(result)
