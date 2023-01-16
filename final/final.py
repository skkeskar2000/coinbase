import ccxt

# okx connected
okx = ccxt.okex()
level2_data = okx.fetch_order_book('BTC/USDT', limit=1)
trade_data = okx.fetch_trades('BTC/USDT',limit=1)

#coinbase connected

cbex = ccxt.coinbase()
coinbase_level2_data = ccxt.cex().fetch_l2_order_book('BTC/USDT', limit = 1)
coinbase_ticker_data =ccxt.cex().fetch_tickers(['BTC/USDT'])


print(level2_data["bids"][0][0])
print(coinbase_level2_data["bids"][0][0])




