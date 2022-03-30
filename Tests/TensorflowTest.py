import keras
import tensorflow as tf
from tensorflow.python.keras import layers, optimizers
import keras.datasets.mnist as datasets
import os


(xs, ys), _ = datasets.load_data()
print('datasets:', xs.shape, ys.shape)

xs = tf.convert_to_tensor(xs, dtype=tf.float32) / 255
db = tf.data.Dataset.from_tensor_slices((xs, ys))

for step, (x, y) in enumerate(db):
    print(step, x.shape, y, y.shape)


model = keras.Sequential([
    layers.Dense(512, activation='relu'),
    layers.Dense(256, activation='relu'),
    layers.Dense(10)
])

with tf.GradientTape() as tape:
    x = tf.reshape(x, (-1, 28*28))
    out = model(x)

    loss = tf.reduce_sum(tf.square(out - y)) / x.shape[0]

grads = tape.gradient(loss, model.trainable_variables)
optimizers = optimizers.gradient_descent_v2(zip(grads, model.trainable_variables))