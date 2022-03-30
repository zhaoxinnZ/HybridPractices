import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

model = tf.keras.Sequential([
    tf.keras.Input(shape=(3,)),
    tf.keras.layers.Dense(100, activations=tf.nn.relu),
    tf.keras.layers.Dense(100, activations=tf.nn.relu),
    tf.keras.layers.Dense(100, activations=tf.nn.relu),
    tf.keras.layers.Dense(1, activations=None),
])

model.compile(loss=tf.keras.losses.mae,
              optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
              metrics=["mae"]
)

model.fit(x_train, y_train, epochs=100)

