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
 
wb2 = Workbook()
ws2 = wb2.active
ws2.append(["ProductId","timestamp","changes"])
def store_level2_data(data):
    ws2 = wb2.active
    print(data)
    # ws2.append(data['product_id'],data["time"],data["changes"])
    # for level in data["bids"]:
    #     ws.append([data["time"], level[0], level[1]])

    # for level in data["asks"]:
    #     ws.append([data["time"], level[0], level[1]])

    wb2.save(filename = "market_data_level.xlsx")

wb = Workbook()
ws = wb.active
ws.append(["timestamp", "price", "last_size", "bid", "ask"])

def store_ticker_data(data):
    ws = wb.active
    ws.append([data["time"], data["price"], data["last_size"], data["best_bid"], data["best_ask"]])
    wb.save(filename = "market_data_ticker.xlsx")
    
socket = 'wss://ws-feed.pro.coinbase.com'

ws = websocket.WebSocketApp(socket,on_open=on_open,on_message=on_message)
   
ws.run_forever()
# import threading
# import time

# def check_timeout():
#     start_time = time.time()
#     while True:
#         if time.time() - start_time > 5:
#             ws.close()
#             break

# timeout_thread = threading.Thread(target=check_timeout)
# timeout_thread.start()



