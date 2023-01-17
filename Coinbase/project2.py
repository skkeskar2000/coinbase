import time, threading
import websocket, json

def on_open(ws):
    ws.send(json.dumps({
        "type": "subscribe",
        "product_ids": [
            "BTC-USD"
        ],
        "channels": [
            "level2",
            "ticker"
        ]
    }))
    
def on_message(ws,message):
    data = json.loads(message)
    if "type" in data:
        if data["type"] == "l2update":
            store_level2_data(data)
        elif data["type"] == "ticker":
            store_ticker_data(data)
 
 
#Store market_data_level2
file1 = open("market_data_level2.csv","a")
file1.write("Type,ProductId,Changes,,,Timestamp\n")
def store_level2_data(data):
    file1.write(f"{data['type']},{data['product_id']},{data['changes']},{data['time']}\n")


#Store ticker data
file2 = open("market_data_ticker.csv","a")
file2.write("Type,Sequence,Product_ID,Price,Open_24h,Volume_24h,Low_24h,High_24h,Volume_30d,Best_bid,Best_bid_size,Best_ask,Best_ask_size,Side,Trade_ID,Last_size,Time\n")
def store_ticker_data(data):
    print(data)
    file2.write(f"{data['type']},{data['sequence']},{data['product_id']},{data['price']},{data['open_24h']},{data['volume_24h']},{data['low_24h']},{data['high_24h']},{data['volume_30d']},{data['best_bid']},{data['best_bid_size']},{data['best_ask']},{data['best_ask_size']},{data['side']},{data['trade_id']},{data['last_size']},{data['time']}\n")

    
socket = 'wss://ws-feed.pro.coinbase.com'

#ws = websocket.WebSocketApp(socket,on_open=on_open,on_message=on_message)
def run_ws():
    ws.run_forever()

ws = websocket.WebSocketApp(socket,on_open=on_open,on_message=on_message)
t = threading.Thread(target=run_ws)
t.start()

timer = threading.Timer(30, ws.close) # close the connection after 300 seconds (5 minutes)
timer.start()





# import ccxt
# import csv
# ex = ccxt.exchanges

# cbex = ccxt.coinbase()
# coinbaseFile1 = open("coinbase_market_data_(level2).csv","a")
# coinbaseFile1.write("Symbol,Bids,,Asks,,Timestamp,Datetime\n")

# coinbase_level2_data = ccxt.cex().fetch_l2_order_book('BTC/USDT', limit = 1)
# print(coinbase_level2_data)
# coinbaseFile1.write(f"{coinbase_level2_data['symbol']},{coinbase_level2_data['bids']},{coinbase_level2_data['asks']},{coinbase_level2_data['timestamp']},{coinbase_level2_data['datetime']}\n")
    

# coinbaseFile2 = open("coinbase_tiker_data.csv","a")
# #coinbaseFile2.write("Symbol,bids,asks,Timestamp,Datetime\n")
# coinbase_ticker_data =ccxt.cex().fetch_tickers(['BTC/USDT'])
# # isHead2 = True
# #dictKey = ""
# # if isHead2:
# #     for key in coinbase_ticker_data.keys():
# #         for key1 in key.keys():
# #             dictKey += str(key1)+","
# # coinbaseFile2.write(dictKey+"\n")
# # isHead2 = False

# dictValue = ""
# dictKey = ""
# for key,value in coinbase_ticker_data.items():
#     for key1,value1 in value.items():
#         dictKey += str(key1)+","
#         if not(type(value1) is dict):
#             dictValue += str(value1)+","

# coinbaseFile2.write(dictKey+"\n")            
# coinbaseFile2.write(dictValue+"\n")
# print(coinbase_ticker_data)






