from multiprocessing import Process
import ccxt
import datetime
#import matplotlib.pyplot as plt

# Initialize the exchange objects
cbex = ccxt.coinbase()
okx = ccxt.okex()

# Set time
endTime = datetime.datetime.now() + datetime.timedelta(seconds=10)

class JointClass:
        
        def __init__(self):
            self.best_bid_cbex = float('-inf')
            self.best_ask_cbex = float('inf')
            self.best_bid_okx = float('-inf')
            self.best_ask_okx = float('inf')

        def fetch_data_cbex(self):
            while True:
                if datetime.datetime.now() >= endTime:
                    break

                # Fetch bids and asks from Coinbase
                market_data_cbex = ccxt.cex().fetch_l2_order_book('BTC/USDT')
                bids_cbex = market_data_cbex['bids']
                asks_cbex = market_data_cbex['asks']
                for bid in bids_cbex:
                    # print("bids_cbex : ",bids_cbex)
                    if bid[0] > self.best_bid_cbex:
                        self.best_bid_cbex = bid[0]

                for ask in asks_cbex:
                    # print("Asks_cbex: ",asks_cbex)
                    if ask[0] < self.best_ask_cbex:
                        self.best_ask_cbex = ask[0]
                        
        
        def fetch_data_okx(self):
            while True:
                if datetime.datetime.now() >= endTime:
                    break

                # Fetch bids and asks from OKEx
                market_data_okx = okx.fetch_order_book('BTC/USDT')
                bids_okx = market_data_okx['bids']
                asks_okx = market_data_okx['asks']
                for bid in bids_okx:
                    # print("bids_okx: ",bids_okx)
                    if bid[0] > self.best_bid_okx:
                        self.best_bid_okx = bid[0]

                for ask in asks_okx:
                    # print("asks_okx: ",asks_okx)
                    if ask[0] < self.best_ask_okx:
                        self.best_ask_okx = ask[0]
            
        def run(self):
            cbex_process = Process(target=self.fetch_data_cbex)
            okx_process = Process(target=self.fetch_data_okx)

            cbex_process.start()
            okx_process.start()
            cbex_process.join()
            okx_process.join()

            print("------------------------------------------------------------")
            print("best_bid_cbex: ",self.best_bid_cbex)
            print("best_ask_cbex: ",self.best_ask_cbex)
            print("best_bid_okx: ",self.best_bid_okx)
            print("best_ask_okx: ",self.best_ask_okx)
            print("------------------------------------------------------------")

            # Compare the best bid and best ask from Coinbase and OKEx
            if self.best_bid_cbex > self.best_bid_okx:
                print("Coinbase has the best bid")
                bid_diff = ((self.best_bid_cbex - self.best_bid_okx) / self.best_bid_okx) * 100
                print("Coinbase has a better bid by: ", bid_diff, "%")
            else:
                print("OKEx has the best bid")
                bid_diff = ((self.best_bid_okx - self.best_bid_cbex) / self.best_bid_cbex) * 100
                print("OKEx has a better bid by: ", abs(bid_diff), "%")

            if self.best_ask_cbex < self.best_ask_okx:
                print("Coinbase has the best ask")
                ask_diff = ((self.best_ask_cbex - self.best_ask_okx) / self.best_ask_okx) * 100
                print("Coinbase has a better ask by: ", ask_diff, "%")
            else:
                print("OKEx has the best ask")
                ask_diff = ((self.best_ask_okx - self.best_ask_cbex) / self.best_ask_cbex) * 100
                print("OKEx has a better ask by: ", abs(ask_diff), "%")

            print("------------------------------------------------------------")

if __name__ == '__main__':
    obj = JointClass()
    obj.run()
