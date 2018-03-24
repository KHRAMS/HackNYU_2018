from __future__ import print_function
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.optimizers import Adadelta
from keras.utils import np_utils
import numpy
import csv
import scipy.misc
import scipy
from scipy import ndimage
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint


img_rows, img_cols = 48, 48
classifier = Sequential()
classifier.add(Convolution2D(64, 5, 5, border_mode='valid',
                        input_shape=(48, 48, 3)))
classifier.add(keras.layers.advanced_activations.PReLU(init='zero', weights=None))
classifier.add(keras.layers.convolutional.ZeroPadding2D(padding=(2, 2), dim_ordering='th'))
classifier.add(MaxPooling2D(pool_size=(5, 5), strides=(2, 2)))

classifier.add(keras.layers.convolutional.ZeroPadding2D(padding=(1, 1), dim_ordering='th'))
classifier.add(Convolution2D(64, 3, 3))
classifier.add(keras.layers.advanced_activations.PReLU(init='zero', weights=None))
classifier.add(keras.layers.convolutional.ZeroPadding2D(padding=(1, 1), dim_ordering='th'))
classifier.add(Convolution2D(64, 3, 3))
classifier.add(keras.layers.advanced_activations.PReLU(init='zero', weights=None))
classifier.add(keras.layers.convolutional.AveragePooling2D(pool_size=(3, 3), strides=(2, 2)))

classifier.add(keras.layers.convolutional.ZeroPadding2D(padding=(1, 1), dim_ordering='th'))
classifier.add(Convolution2D(128, 3, 3))
classifier.add(keras.layers.advanced_activations.PReLU(init='zero', weights=None))
classifier.add(keras.layers.convolutional.ZeroPadding2D(padding=(1, 1), dim_ordering='th'))
classifier.add(Convolution2D(128, 3, 3))
classifier.add(keras.layers.advanced_activations.PReLU(init='zero', weights=None))

classifier.add(keras.layers.convolutional.ZeroPadding2D(padding=(1, 1), dim_ordering='th'))
classifier.add(keras.layers.convolutional.AveragePooling2D(pool_size=(3, 3), strides=(2, 2)))

classifier.add(Flatten())
classifier.add(Dense(1024))
classifier.add(keras.layers.advanced_activations.PReLU(init='zero', weights=None))
classifier.add(Dropout(0.2))
classifier.add(Dense(1024))
classifier.add(keras.layers.advanced_activations.PReLU(init='zero', weights=None))
classifier.add(Dropout(0.2))

classifier.add(Dense(7))

classifier.add(Activation('softmax'))

ada = Adadelta(lr=0.1, rho=0.95, epsilon=1e-08)
classifier.compile(loss='categorical_crossentropy',
              optimizer=ada,
              metrics=['accuracy'])

filepath="weights-improvement-{epoch:02d}-{val_acc:.2f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
callbacks_list = [checkpoint]

from keras.preprocessing.image import ImageDataGenerator

# generates more images by transforming images slightly based on previous images
train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)


training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                 target_size = (48, 48),
                                                 batch_size = 32,
                                                 class_mode = 'categorical')

test_set = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size = (48, 48),
                                            batch_size = 32,
                                            class_mode = 'categorical')

classifier.fit_generator(training_set,
                         steps_per_epoch = 3000,
                         epochs = 12,
                         validation_data = test_set,
                         callbacks= callbacks_list,
                         validation_steps = 2000)


classifier.save('my_model_1.hdf5')