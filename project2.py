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
# isHead2 = True
file2.write("Type,Sequence,Product_ID,Price,Open_24h,Volume_24h,Low_24h,High_24h,Volume_30d,Best_bid,Best_bid_size,Best_ask,Best_ask_size,Side,Trade_ID,Last_size,Time\n")
def store_ticker_data(data):
    print(data)
    file2.write(f"{data['type']},{data['sequence']},{data['product_id']},{data['price']},{data['open_24h']},{data['volume_24h']},{data['low_24h']},{data['high_24h']},{data['volume_30d']},{data['best_bid']},{data['best_bid_size']},{data['best_ask']},{data['best_ask_size']},{data['side']},{data['trade_id']},{data['last_size']},{data['time']}\n")

     # ws = wb.active
    # ws.append([data["time"], data["price"], data["last_size"], data["best_bid"], data["best_ask"]])
    # wb.save(filename = "market_data_ticker.xlsx")
    # wb.close()
    # print(data)
    # dictKey = ""
    # if isHead2:
    #     for key in data.keys():
    #         dictKey += str(key)+","   
    #     print(dictKey)
    #     file2.write(dictKey+"\n")
    # # isHead2 = False
            
    # dictValue = ""
    # for value in data.values():
    #     dictValue += str(value)+","
    # file2.write(dictValue+"\n")
    
socket = 'wss://ws-feed.pro.coinbase.com'

ws = websocket.WebSocketApp(socket,on_open=on_open,on_message=on_message)
def run_ws():
    ws.run_forever()

t = threading.Thread(target=run_ws)
t.start()

timer = threading.Timer(30, ws.close) # close the connection after 300 seconds (5 minutes)
timer.start()