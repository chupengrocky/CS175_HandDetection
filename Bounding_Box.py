import tensorflow as tf
import json
import vgg16
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
vgg = vgg16.Vgg16()

