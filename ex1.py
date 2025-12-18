import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

y_input_array=input("enter the number separate by comma (,):")
y_input_array=np.array([int(x) for x in y_input_array.split(",")])
x=np.array(y_input_array,dtype=float)
y=3*x+2
model=keras.Sequential([keras.layers.Dense(1,input_shape=[1])])
model.compile(
    optimizer='adam',
    loss='mse'
    )
print('training the model...')
history=model.fit(x,y,epochs=500,verbose=0)
weights=model.layers[0].get_weights()
print('\n learned weight (slope):',weights[0][0][0])
print('learned bias:',weights[1][0])
test_value=np.array([10],dtype=float)
prediction=model.predict(test_value)[0][0]

#matplotlib
print(f"\n prediction for x=10:{prediction}")
plt.plot(history.history['loss'])
plt.xlabel('Epochs')
plt.ylabel("loss")
plt.title("Training Loss curve")
plt.show()










































