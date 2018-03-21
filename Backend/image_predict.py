from keras.models import load_model
import h5py
import numpy as np
model = load_model('test2_model.h5')
print(model.summary())
from keras.preprocessing import image
test_image = image.load_img('/home/katchu11/MyPrograms/sompic.jpg', target_size = (48, 48))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = model.predict(test_image)
print(result)
