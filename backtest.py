import backtrader as bt
import datetime

#Create RSIStrategy class
class RSIStrategy(bt.Strategy):

    def __init__(self):
        # Calculate RSI for data over period
        self.rsi = bt.talib.RSI(self.data, period=14)

    def next(self):
        """Class method to let BackTrader know what to do at each data point""" 
        if self.rsi < 30 and not self.position:
            # If asset is oversold and we aren't in the market, enter market
            self.buy(size=1)
        
        if self.rsi > 70 and self.position:
            # If asset is overbought, close position
            self.close()

# Create Cerebro Object
cerebro = bt.Cerebro()
cerebro.broker.setcash(10000.0)

# Get Python data objects for date range
fromdate = datetime.datetime.strptime('2019-06-01', '%Y-%m-%d')
todate = datetime.datetime.strptime('2019-12-30', '%Y-%m-%d')

# Read data into backtrader feeds object 
data = bt.feeds.GenericCSVData(dataname='coinview/2020_15minutes.csv', dtformat=2, timeframe=bt.TimeFrame.Minutes, compression=15, fromdate=fromdate, todate=todate)#, compression=15, timeframe=bt.TimeFrame.Minutes, fromdate=fromdate, todate=todate)

# Add data to Cerebro instance
cerebro.adddata(data)
# Add strategy to Cerebro instance
cerebro.addstrategy(RSIStrategy)
# Run Cerebro instance
cerebro.run()
# Plot Cerebro instance
cerebro.plot()
