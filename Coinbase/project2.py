import ccxt
import csv
ex = ccxt.exchanges

cbex = ccxt.coinbase()
for x in range(1,3):
    level2_data = ccxt.cex().fetch_l2_order_book('BTC/USDT', limit = 1)
    print(level2_data)

# Fetch ticker 
# ticker_data = ex.fetch_ticker(['BTC/USDT'])
# print(ticker_data)
if (cbex.has['fetchTickers']):
    ticker_data =ccxt.cex().fetch_tickers(['BTC/USDT'])
    #symbols = list(cbex.markets.keys())
    #print("ticker data")
    #print(ticker_data)

#Save level-2 data to a CSV file
with open('level2_data.csv', mode='w') as level2_file:
        fieldnames = ['bids', 'asks']
        writer = csv.DictWriter(level2_file, fieldnames=fieldnames)
        writer.writeheader()
        for bid, ask in zip(level2_data['bids'], level2_data['asks']):
            writer.writerow({'bids': bid, 'asks': ask})




