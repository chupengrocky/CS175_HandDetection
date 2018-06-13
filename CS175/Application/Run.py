# import tensorflow as tf
# import json
# import vgg16
# hello = tf.constant('Hello, TensorFlow!')
# sess = tf.Session()
# print(sess.run(hello))
# vgg = vgg16.Vgg16()
# vgg.build(3)



from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
import numpy as np
import matplotlib.pyplot as plt
import os
print(os.getcwd())

# Xdata = np.load('test_data/Sign-language-digits-dataset 2/X.npy')
# test_imge = Xdata[0]
# plt.imshow(test_imge, cmap='gray')
# plt.show()


model = VGG16(weights='imagenet',
                  include_top=False,
                  input_shape=(224, 224, 3))
print(model.summary())







# Test a single image in and show the percentage
# load the model
#

# model = VGG16()
# # load an image from file
# image = load_img('test_data/RaisedHand.png', target_size=(224, 224))
# plt.imshow(image,origin='upper')
# plt.show()
# # convert the image pixels to a numpy array
# image = img_to_array(image)
#
# print(image.shape)
# # reshape data for the model
# image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
# # prepare the image for the VGG model
# image = preprocess_input(image)
# # predict the probability across all output classes
# yhat = model.predict(image)
# # convert the probabilities to class labels
# label = decode_predictions(yhat)
# # retrieve the most likely result, e.g. highest probability
# label = label[0][0]
# # print the classification
# print('%s (%.2f%%)' % (label[1], label[2]*100))

