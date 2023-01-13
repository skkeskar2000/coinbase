import ccxt
import csv
ex = ccxt.exchanges

cbex = ccxt.coinbase()
coinbaseFile1 = open("coinbase_market_data_(level2).csv","a")
coinbaseFile1.write("Symbol,Bids,Asks,Timestamp,Datetime\n")

coinbase_level2_data = ccxt.cex().fetch_l2_order_book('BTC/USDT', limit = 1)
#print(coinbase_level2_data)
coinbaseFile1.write(f"{coinbase_level2_data['symbol']},{coinbase_level2_data['bids']},{coinbase_level2_data['asks']},{coinbase_level2_data['timestamp']},{coinbase_level2_data['datetime']}\n")
    

coinbaseFile2 = open("coinbase_tiker_data.csv","a")
#coinbaseFile2.write("Symbol,bids,asks,Timestamp,Datetime\n")
coinbase_ticker_data =ccxt.cex().fetch_tickers(['BTC/USDT'])
# isHead2 = True
#dictKey = ""
# if isHead2:
#     for key in coinbase_ticker_data.keys():
#         for key1 in key.keys():
#             dictKey += str(key1)+","
# coinbaseFile2.write(dictKey+"\n")
# isHead2 = False

dictValue = ""
dictKey = ""
for key,value in coinbase_ticker_data.items():
    for key1,value1 in value.items():
        dictKey += str(key1)+","
        if not(type(value1) is dict):
            dictValue += str(value1)+","

coinbaseFile2.write(dictKey+"\n")            
coinbaseFile2.write(dictValue+"\n")
print(coinbase_ticker_data)






