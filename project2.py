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
file1.write("Type,ProductId,Changes,Timestamp\n")
def store_level2_data(data): 
    file1.write(data['type']+","+data['product_id']+","+str(data["changes"])+","+data["time"]+"\n")
    

# wb = Workbook()
# ws = wb.active
# ws.append(["timestamp", "price", "last_size", "bid", "ask"])
# wb.save(filename = "market_data_ticker.xlsx")
file2 = open("market_data_ticker.csv","a")
isHead2 = True
def store_ticker_data(data):
    # ws = wb.active
    # ws.append([data["time"], data["price"], data["last_size"], data["best_bid"], data["best_ask"]])
    # wb.save(filename = "market_data_ticker.xlsx")
    # wb.close()
    # print(data)
    dictKey = ""
    if isHead2:
        for key in data.keys():
            dictKey += str(key)+","   
        print(dictKey)
        file2.write(dictKey+"\n")
        
    dictValue = ""
    for value in data.values():
        dictValue += str(value)+","
    file2.write(dictValue+"\n")
    # file2.write(data['time']+","+data["price"]+","+data["last_size"]+","+data["best_bid"]+","+data["best_ask"]+"\n")

    
socket = 'wss://ws-feed.pro.coinbase.com'

ws = websocket.WebSocketApp(socket,on_open=on_open,on_message=on_message)
   
ws.run_forever()



