import config
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET, tld='us')

account = client.get_account()

balances = account['balances']

for balance in balances:
    print(balance)

print('1')

print(balances)

print(account)
