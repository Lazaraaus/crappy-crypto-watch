from flask import Flask, render_template, request, flash, redirect, jsonify
from flask_cors import CORS, cross_origin
import config, csv, datetime
from binance.client import Client
from binance.enums import *

app = Flask(__name__)
cors = CORS(app)

app.secret_key = b'8a9fh9afahf3a08fhha'

client = Client(config.API_KEY, config.API_SECRET, tld='us')


@app.route('/')
@cross_origin()
def index():
    title = 'Crappy Crypto Watch'

    account = client.get_account()

    balances = account['balances']

    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']

    return render_template('index.html', title=title, my_balances=balances, symbols=symbols)


@app.route('/buy', methods=['POST'])
def buy():
    print(request.form)
    try:
        order = client.create_order(symbol=request.form['symbol'], 
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            quantity=request.form['quantity'])
    except Exception as e:
        flash(e.message, "error")

    return redirect('/')


@app.route('/sell')
def sell():
    return 'sell'


@app.route('/settings')
def settings():
    return 'settings'

@app.route('/history')
# Function history() returns historical data to the browser
def history():
    '''Call to binance API for historical candlestick''' 
    candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "25 Jan, 2021", "27 Jan, 2021")
    # List to hold parsed candlesticks
    processed_candlesticks = []
    # Loop to parse candlesticks for relevant data: open, high, low, close, timestamp
    for data in candlesticks:
        candlestick = { 
            "time": data[0] / 1000, 
            "open": data[1],
            "high": data[2], 
            "low": data[3], 
            "close": data[4]
        }
        # Append processed candlestick
        processed_candlesticks.append(candlestick)
    # Jsonify Python dict and return
    return jsonify(processed_candlesticks)
