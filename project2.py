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
 
 
 
file1 = open("market_data_level.csv","a")
file1.write("Type,ProductId,Changes,,,Timestamp\n")
def store_level2_data(data):
    file1.write(f"{data['type']},{data['product_id']},{data['changes']},{data['time']}\n")
    

# wb = Workbook()
# ws = wb.active
# ws.append(["timestamp", "price", "last_size", "bid", "ask"])
# wb.save(filename = "market_data_ticker.xlsx")
file2 = open("market_data_ticker.csv","a")
file2.write("Type,Sequence,Product_ID,Price,Open_24h,Volume_24h,Low_24h,High_24h,Volume_30d,Best_bid,Best_bid_size,Best_ask,Best_ask_size,Side,Trade_ID,Last_size,Time\n")
def store_ticker_data(data):
    # ws = wb.active
    # ws.append([data["time"], data["price"], data["last_size"], data["best_bid"], data["best_ask"]])
    # wb.save(filename = "market_data_ticker.xlsx")
    # wb.close()
    print(data)
    file2.write(f"{data['type']},{data['sequence']},{data['product_id']},{data['price']},{data['open_24h']},{data['volume_24h']},{data['low_24h']},{data['high_24h']},{data['volume_30d']},{data['best_bid']},{data['best_bid_size']},{data['best_ask']},{data['best_ask_size']},{data['side']},{data['trade_id']},{data['last_size']},{data['time']}\n")

    
socket = 'wss://ws-feed.pro.coinbase.com'

ws = websocket.WebSocketApp(socket,on_open=on_open,on_message=on_message)
   
ws.run_forever()



