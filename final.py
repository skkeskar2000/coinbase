import ccxt
import time, datetime

# Initialize exchange objects
cbex = ccxt.coinbase()
okx = ccxt.okex()

# Set the interval for data fetches (in seconds)
#interval = 60 #600 sec 10 min
endTime = datetime.datetime.now() + datetime.timedelta(seconds=10)
# i=0
while True:
    if datetime.datetime.now() >= endTime:
        break
    # Subscribe to market data
    market_data_cbex = ccxt.cex().fetch_l2_order_book('BTC/USDT')
    market_data_okx = okx.fetch_order_book('BTC/USDT')

    # Subscribe to ticker data
    ticker_data_cbex = ccxt.cex().fetch_tickers(['BTC/USDT'])
    ticker_data_okx = okx.fetch_ticker('BTC/USDT')

    # Subscribe to trade data
    trade_data_cbex = ccxt.cex().fetch_trades('BTC/USDT')
    trade_data_okx = okx.fetch_trades('BTC/USDT')

    # Find the best bid and offer
    print("--------------------------------------------")
    best_bid_cbex = market_data_cbex['bids'][0][0]
    print("Best Bid Coinbase: ",best_bid_cbex)
    best_offer_cbex = market_data_cbex['asks'][0][0]
    print("Best Offer Coinbase: ",best_offer_cbex)
    best_bid_okx = market_data_okx['bids'][0][0]
    print("Best Bid Okx: ",best_bid_okx)
    best_offer_okx = market_data_okx['asks'][0][0]
    print("Best Offer Okx: ",best_offer_okx)


    okx_bid_count = 0
    cbx_bid_count = 0
    cbx_offer_count = 0
    okx_offer_count = 0
    print("--------------------------------------------")
    # Check which exchange has the best bid and offer
    if best_bid_cbex > best_bid_okx:
        cbx_bid_count+=1
    else:
        okx_bid_count+=1

    if best_offer_cbex > best_offer_okx:
        okx_offer_count+=1
    else:
        cbx_offer_count+=1

    #i+=1
    # Wait for the specified interval before fetching data again
    #time.sleep(interval)
if okx_bid_count < cbx_bid_count:
    print("cbx has best bid")
    print("--------------------------------------------")
else:
    print("okx has best bid")
    print("--------------------------------------------")

if okx_offer_count < cbx_offer_count:
    print("okx has best offer")
    print("--------------------------------------------")
else:
    print("cbx has best offer")
    print("--------------------------------------------")
