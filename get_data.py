import config, csv
from binance.client import Client

# Establish Connection with Client
client = Client(config.API_KEY, config.API_SECRET)

# Create CSV object to create data file and write to it
csvfile = open('coinview/2020_15minutes.csv', 'w', newline='') 
candlestick_writer = csv.writer(csvfile, delimiter=',')

# Grab Historical Data with API call
candlesticks = client.get_historical_klines("XLMUSDT", Client.KLINE_INTERVAL_1DAY, "01 Dec, 2020", "27 Jan, 2021")
#candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2020", "12 Jul, 2020")
#candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2017", "12 Jul, 2020")

# Write rows 
for candlestick in  candlesticks:
    candlestick[0] = candlestick[0] / 1000
    candlestick_writer.writerow(candlestick)

# Close file 
csvfile.close()
