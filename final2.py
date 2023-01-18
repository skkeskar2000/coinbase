import ccxt
import time, datetime

# Initialize the exchange objects
cbex = ccxt.coinbase()
okx = ccxt.okex()

# Set the interval for data fetches (in seconds)
#interval = 60 #600 sec 10 min
endTime = datetime.datetime.now() + datetime.timedelta(seconds=20)

# initialize counters
bid_count_cbex = 0
ask_count_cbex = 0
bid_count_okx = 0
ask_count_okx = 0

# initialize variables
best_bid_cbex = float('-inf')
best_ask_cbex = float('inf')
best_bid_okx = float('-inf')
best_ask_okx = float('inf')

# Fetch bids from Coinbase and find the best bid
while True:
    if datetime.datetime.now() >= endTime:
        break

    # Fetch bids and asks from Coinbase
    market_data_cbex = ccxt.cex().fetch_l2_order_book('BTC/USDT')
    print("market data cbex: ",market_data_cbex)
    bids_cbex = market_data_cbex['bids']
    asks_cbex = market_data_cbex['asks']
    for bid in bids_cbex:
        bid_count_cbex+=1
        #print("bids_cbex: ",bids_cbex)
        if bid[0] > best_bid_cbex:
            best_bid_cbex = bid[0]
    print("bids_cbex",bids_cbex)

    for ask in asks_cbex:
        ask_count_cbex+=1
        #print("asks_cbex: ",asks_cbex)
        if ask[0] < best_ask_cbex:
            best_ask_cbex = ask[0]

    # Fetch bids and asks from OKEx
    market_data_okx = okx.fetch_order_book('BTC/USDT')
    print("market data okx: ",market_data_okx)
    bids_okx = market_data_okx['bids']
    asks_okx = market_data_okx['asks']
    for bid in bids_okx:
        bid_count_okx+=1
        #print("bids_okx: ",bids_okx)
        if bid[0] > best_bid_okx:
            best_bid_okx = bid[0]

    for ask in asks_okx:
        ask_count_okx+=1
       #print("asks_okx: ",asks_okx)
        if ask[0] < best_ask_okx:
            best_ask_okx = ask[0]


print("-----------------------------------------------")
#Print best bid and best ask from both for 1min
print("best_bid_cbex in 1min: ",best_bid_cbex)
print("best_ask_cbex in 1min: ",best_ask_cbex)
print("best_bid_okx in 1min: ",best_bid_okx)
print("best_ask_okx in 1min: ",best_ask_okx)

print("-----------------------------------------------")

# Compare the best bid and best ask from Coinbase and OKEx
if best_bid_cbex > best_bid_okx:
    print("Coinbase has the best bid")
    bid_diff = ((best_bid_cbex - best_bid_okx) / best_bid_okx) * 100
    print("Coinbase has a better bid by: ", bid_diff, "%")
else:
    print("OKEx has the best bid")
    bid_diff = ((best_bid_okx - best_bid_cbex) / best_bid_cbex) * 100
    print("OKEx has a better bid by: ", abs(bid_diff), "%")

if best_ask_cbex < best_ask_okx:
    print("Coinbase has the best ask")
    ask_diff = ((best_ask_cbex - best_ask_okx) / best_ask_okx) * 100
    print("Coinbase has a better ask by: ", ask_diff, "%")
else:
    print("OKEx has the best ask")
    ask_diff = ((best_ask_okx - best_ask_cbex) / best_ask_cbex) * 100
    print("OKEx has a better ask by: ", abs(ask_diff), "%")

print("-----------------------------------------------")

# Calculate the percentage difference between best bid and ask from Coinbase and OKEx
#bid_diff = ((best_bid_cbex - best_bid_okx) / best_bid_cbex) * 100
#ask_diff = ((best_ask_cbex - best_ask_okx) / best_ask_cbex) * 100

# if bid_diff > 0:
#     print("Coinbase has a better bid by: ", bid_diff, "%")
# else:
#     print("OKEx has a better bid by: ", abs(bid_diff), "%")

# if ask_diff > 0:
#     print("Coinbase has a better ask by: ", ask_diff, "%")
# else:
#     print("OKEx has a better ask by: ", abs(ask_diff), "%")

# print("-----------------------------------------------")

print("bid_count_cbex: ",bid_count_cbex)
print("Ask_count_cbex: ",ask_count_cbex)
print("bid_count_okx: ",bid_count_okx)
print("Ask_count_okx: ",ask_count_okx)

print("-----------------------------------------------")



# while True:
#     if datetime.datetime.now() >= endTime:
#         break
#     # Subscribe to market data
#     market_data_cbex = ccxt.cex().fetch_l2_order_book('BTC/USDT')
#     market_data_okx = okx.fetch_order_book('BTC/USDT')

#     # Subscribe to ticker data
#     ticker_data_cbex = ccxt.cex().fetch_tickers(['BTC/USDT'])
#     ticker_data_okx = okx.fetch_ticker('BTC/USDT')

#     # Subscribe to trade data
#     trade_data_cbex = ccxt.cex().fetch_trades('BTC/USDT')
#     trade_data_okx = okx.fetch_trades('BTC/USDT')

#     # Find the best bid and offer for Coinbase
#     best_bid_cbex = market_data_cbex['bids'][0][0]
#     best_offer_cbex = market_data_cbex['asks'][0][0]
#     bid_count_cbex += len(market_data_cbex['bids'])
#     ask_count_cbex += len(market_data_cbex['asks'])

#     print("best_bid_cbex: ",best_bid_cbex)
#     print("best_offer_cbex: ",best_offer_cbex)

#     # Find the best bid and offer for OKEx
#     best_bid_okx = market_data_okx['bids'][0][0]
#     best_offer_okx = market_data_okx['asks'][0][0]
#     bid_count_okx += len(market_data_okx['bids'])
#     ask_count_okx += len(market_data_okx['asks'])

#     print("best_bid_okx: ",best_bid_okx)
#     print("best_offer_okx: ",best_offer_okx)

#     # Compare the best bid and offer between Coinbase and OKEx
#     if best_bid_cbex > best_bid_okx:
#         print("Coinbase has the best bid.")
#     else:
#         print("OKEx has the best bid.")
#     if best_offer_cbex < best_offer_okx:
#         print("Coinbase has the best ask.")
#     else:
#         print("OKEx has the best ask.")

# # Print the number of bids and asks fetched from Coinbase and OKEx respectively
# print("Number of bids fetched from Coinbase: ", bid_count_cbex)
# print("Number of asks fetched from Coinbase: ", ask_count_cbex)
# print("Number of bids fetched from OKEx: ", bid_count_okx)
# print("Number of asks fetched from OKEx: ", ask_count_okx)
