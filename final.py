import ccxt
import time

# Initialize exchange objects
cbex = ccxt.coinbase()
okx = ccxt.okex()

# Set the interval for data fetches (in seconds)
interval = 600  #600 sec 10 min

while True:

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

    print("--------------------------------------------")
    # Check which exchange has the best bid and offer
    if best_bid_cbex > best_bid_okx:
        print("cbex has the best bid")
        print("--------------------------------------------")
    else:
        print("OKEx has the best bid")
        print("--------------------------------------------")

    if best_offer_cbex < best_offer_okx:
        print("cbex has the best offer")
        print("--------------------------------------------")
    else:
        print("OKEx has the best offer")
        print("--------------------------------------------")

    # Wait for the specified interval before fetching data again
    time.sleep(interval)
