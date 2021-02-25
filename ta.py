import numpy
import talib
from numpy import genfromtxt
import datetime
# Collect data 
my_data = genfromtxt('2020_15minutes.csv', delimiter=',')

# Collect all the closing values from my_data
close = my_data[:,4]
data_open = my_data[:,1]
data_high = my_data[:,2]
data_low = my_data[:,2]
time_stamps = my_data[:,0]
actual_time = []
for ts in time_stamps:
    actual_time.append(datetime.datetime.utcfromtimestamp(ts).strftime('%y-%m-%d %H:%M:%S'))

print(actual_time[0])

# Get RSI of closing data
rsi = talib.RSI(close, timeperiod=14)
morning_stars = talib.CDLMORNINGSTAR(data_open, data_high, data_low, close)
engulfing = talib.CDLENGULFING(data_open, data_high, data_low, close)

print(engulfing)
index = 0
for star in morning_stars:
    print(actual_time[index], data_open[index], close[index], engulfing[index], star, rsi[index])
    index += 1


string = "hello"
print(string[::-1])
