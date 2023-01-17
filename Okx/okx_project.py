import ccxt
import csv, datetime

okex = ccxt.okex()

# Save okx level2 data to a CSV file
okxFile1 = open("okx_level2_data.csv","a")
okxFile1.write("Symbol,Bids,,Asks,,Timestamp,Datetime\n")

# Save trade data to a CSV file
okxFile2 = open("okx_trade_data.csv","a")
okxFile2.write("Price, Amount, Timestamp, Datetime, Side\n")

endTime = datetime.datetime.now() + datetime.timedelta(minutes=1)

while True:
  if datetime.datetime.now() >= endTime:
    break
  
  level2_data = okex.fetch_order_book('BTC/USDT')
  trade_data = okex.fetch_trades('BTC/USDT')
  
  def store_level2_data(level2_data):
    okxFile1.write(f"{level2_data['symbol']},{level2_data['bids']},{level2_data['asks']},{level2_data['timestamp']},{level2_data['datetime']}\n")

  store_level2_data(level2_data)
  # okxFile1.close()

  #okxlevel2_value = ""
  #okxlevel2_key = ""
  #print(level2_data)
  # for key,value in level2_data.items():
  #   okxlevel2_key+= key+","
  #   okxlevel2_value+= str(value)+","

  # okxFile1.write(okxlevel2_key+"\n")            
  # okxFile1.write(okxlevel2_value+"\n")

  def store_trade_data(trade_data):
      for i in trade_data:
          okxFile2.write(f"{i['price']}, {i['amount']}, {i['timestamp']}, {i['datetime']}, {i['side']}\n")

  store_trade_data(trade_data)
  #okxFile2.close()

  # dictValue = ""
  # dictKey = ""

  # #print(type(trade_data[0]))
  # data = trade_data[0]
  # for key,value in data.items():
  #   dictKey+= key+","
  #   dictValue+= str(value)+","

  # okxFile2.write(dictKey+"\n")            
  # okxFile2.write(dictValue+"\n")
  #print(trade_data)
