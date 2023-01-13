# import time, threading
# import websocket, json

# def on_open(ws):
#     ws.send(json.dumps({
#         "event": "addChannel",
#         "channel": "ok_sub_spot_btc_usdt_depth"
#     }))
#     ws.send(json.dumps({
#         "event": "addChannel",
#         "channel": "ok_sub_spot_btc_usdt_trade"
#     }))
    
# def on_message(ws, message):
#     data = json.loads(message)
#     if "channel" in data:
#         if data["channel"] == "ok_sub_spot_btc_usdt_depth":
#             store_level2_data(data)
#         elif data["channel"] == "ok_sub_spot_btc_usdt_trade":
#             store_trade_data(data)
 
 
# #Store market_data_level2
# file1 = open("okx_market_data_level2.csv","a")
# file1.write("Channel,Timestamp,Asks,Bids\n")
# def store_level2_data(data):
#     file1.write(f"{data['channel']},{data['timestamp']},{data['asks']},{data['bids']}\n")

# #Store trade data
# file2 = open("okx_market_data_trade.csv","a")
# file2.write("Channel,Timestamp,Trade_ID,Price,Size,Side\n")
# def store_trade_data(data):
#     print(data)
#     file2.write(f"{data['channel']},{data['timestamp']},{data['data'][0]['tid']},{data['data'][0]['price']},{data['data'][0]['amount']},{data['data'][0]['type']}\n")

# socket = 'wss://real.okex.com:10441/websocket'

# ws = websocket.WebSocketApp(socket,on_open=on_open,on_message=on_message)
# def run_ws():
#     ws.run_forever()

# t = threading.Thread(target=run_ws)
# t.start()

# timer = threading.Timer(30, ws.close) # close the connection after 30 seconds
# timer.start()
import ccxt
import csv

# Initialize the exchange object
okex = ccxt.okex()

# Fetch level-2 order book
# level2_data = okex.fetch_order_book('BTC/USDT', limit=1)
for x in range(1,30):
  level2_data = okex.fetch_order_book('BTC/USDT', limit=1)
  print(level2_data)

# Fetch trade history
trade_data = okex.fetch_trades('BTC/USDT',limit=30)

# Save level-2 data to a CSV file
with open('okx_level2_data.csv', mode='w') as level2_file:
    fieldnames = ['bids', 'asks']
    writer = csv.DictWriter(level2_file, fieldnames=fieldnames)
    writer.writeheader()
    for bid, ask in zip(level2_data['bids'], level2_data['asks']):
        writer.writerow({'bids': bid, 'asks': ask})

# Save trade data to a CSV file
with open('okx_trade_data.csv', mode='w') as trade_file:
    fieldnames = ['timestamp', 'symbol', 'side', 'amount', 'price']
    writer = csv.DictWriter(trade_file, fieldnames=fieldnames)
    writer.writeheader()
    for trade in trade_data:
        writer.writerow({'timestamp': trade['timestamp'], 'symbol': trade['symbol'], 'side': trade['side'], 'amount': trade['amount'], 'price': trade['price']})