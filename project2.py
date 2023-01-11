# API Key: n9SUxKiHZSknrFI9
# API Secret: vxjRTdrfqJ3ws6qylg20m9mhLzkXD2m5

# 9f0711b08a39934d06b27e748104b84c
# Y5DJVIELYVP8VxIbeI6moVaiHijJ0d8TE1B4KG5HVfiHzTpL2VHgteCtqnGpT/lw9hOU0ImmxodCPX5ndWEz2A==

import websocket, json
from openpyxl import Workbook

def on_open(ws):
    ws.send(json.dumps({
        "type": "subscribe",
        "product_ids": [
            "BTC-USD"
        ],
        "channels": [
            "level2",
            # "ticker"
        ]
    }))
    
def on_message(ws,message):
    data = json.loads(message)
    if "type" in data:
        if data["type"] == "level2":
            print(data)
            store_level2_data(data)
        elif data["type"] == "ticker":
            store_ticker_data(data)
 
def store_level2_data(data):
    wb2 = Workbook()
    ws = wb2.active
    ws.append(["timestamp", "bids", "asks"])
    print(data)
    for level in data["bids"]:
        ws.append([data["timestamp"], level[0], level[1]])

    for level in data["asks"]:
        ws.append([data["timestamp"], level[0], level[1]])

    wb2.save("market_data_level2.xlsx")

wb = Workbook()
ws = wb.active
ws.append(["timestamp", "price", "last_size", "bid", "ask"])

def store_ticker_data(data):
    ws = wb.active
    ws.append([data["time"], data["price"], data["last_size"], data["best_bid"], data["best_ask"]])
    wb.save(filename = "market_data.xlsx")
    # file = open("market_data.csv","w")
    # file.write("timestamp, price, last_size, bid, ask")
    # print(data["time"] +","+data["price"] +","+ data["last_size"]+ ","+data["best_bid"]+"," +data["best_ask"])
    # file.write(data["time"] +","+data["price"] +","+ data["last_size"]+ ","+data["best_bid"]+"," +data["best_ask"])
    # file.close()
       
socket = 'wss://ws-feed.pro.coinbase.com'

ws = websocket.WebSocketApp(socket,on_open=on_open,on_message=on_message)
ws.run_forever()



