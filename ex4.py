import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

time = np.arange(0, 100, 0.1)
data = np.sin(time)
df = pd.DataFrame(data, columns=['value'])
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df)

def create_sequences(data, time_step=10):
    x, y = [], []
    for i in range(len(data) - time_step):
        x.append(data[i:(i + time_step), 0])
        y.append(data[i + time_step, 0])      
    return np.array(x), np.array(y)

time_step = 10
x, y = create_sequences(scaled_data, time_step)
x = x.reshape(x.shape[0], x.shape[1], 1)
train_size = int(len(x) * 0.8)
x_train = x[:train_size]
x_test = x[train_size:]
y_train = y[:train_size]
y_test = y[train_size:]

model = Sequential()
model.add(LSTM(50, input_shape=(time_step, 1)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')

model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=50, batch_size=32, verbose=1)
train_predict = model.predict(x_train)
test_predict = model.predict(x_test)
train_predict = scaler.inverse_transform(train_predict)
y_train_actual = scaler.inverse_transform([y_train])
test_predict = scaler.inverse_transform(test_predict)
y_test_actual = scaler.inverse_transform([y_test])
train_score = np.sqrt(mean_squared_error(y_train_actual[0], train_predict[:,0]))
test_score = np.sqrt(mean_squared_error(y_test_actual[0], test_predict[:,0]))
print(f'Train Score: {train_score:.2f} RMSE')
print(f'Test Score: {test_score:.2f} RMSE')


plt.figure(figsize=(10,5))
plt.plot(df.values,label="actual data")
train_plot = np.empty_like(scaled_data)
train_plot[:] = np.nan
train_plot[time_step:train_size+time_step, :] = train_predict
test_plot = np.empty_like(scaled_data)
test_plot[:] = np.nan
test_plot[train_size+time_step:] = test_predict

plt.title('LSTM Sine Wave Prediction')
plt.plot(scaler.inverse_transform(scaled_data), label='Actual Data')
plt.plot(train_plot, label='Training Prediction')
plt.plot(test_plot, label='Testing Prediction')
plt.legend()
plt.show()
