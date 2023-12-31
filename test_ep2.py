# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 17:02:54 2023

@author: bruno
"""
from tensorflow.keras.utils import load_img
#from keras.preprocessing.image import load_img
#from keras.preprocessing.image import img_to_array
from tensorflow.keras.utils import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
 
# load and prepare the image
def load_image(filename):
 # load the image
 img = load_img(filename, grayscale=True, target_size=(28, 28))
 # convert to array
 img = img_to_array(img)
 # reshape into a single sample with 1 channel
 img = img.reshape(1, 28, 28, 1)
 # prepare pixel data
 img = img.astype('float32')
 img = img / 255.0
 return img
 
# load an image and predict the class
def run_example():
 # load the image
 img = load_image('sample_image.png')
 # load model
 model = load_model('final_model.h5')
 # predict the class
 result = np.argmax(model.predict(img), axis=-1)
 print(result[0])
 
# entry point, run the example
run_example()