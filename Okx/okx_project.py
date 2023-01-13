import ccxt
import csv

okex = ccxt.okex()

level2_data = okex.fetch_order_book('BTC/USDT', limit=1)

trade_data = okex.fetch_trades('BTC/USDT',limit=1)

# Save okx level2 data to a CSV file
okxFile1 = open("okx_level2_data.csv","a")
okxlevel2_value = ""
okxlevel2_key = ""
# print(level2_data)
for key,value in level2_data.items():
  okxlevel2_key+= key+","
  okxlevel2_value+= str(value)+","

okxFile1.write(okxlevel2_key+"\n")            
okxFile1.write(okxlevel2_value+"\n")

# Save trade data to a CSV file
okxFile2 = open("okx_trade_data.csv","a")
dictValue = ""
dictKey = ""

#print(type(trade_data[0]))
data = trade_data[0]
for key,value in data.items():
  dictKey+= key+","
  dictValue+= str(value)+","

okxFile2.write(dictKey+"\n")            
okxFile2.write(dictValue+"\n")
#print(trade_data)
