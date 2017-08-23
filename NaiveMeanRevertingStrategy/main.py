
import sys
import os

# Complete the function below.

def  calculate_pl(prices):
    base_price, trades, pnl, trade_happened = prices[0], [], 0, False
    for price in prices[1:]:

        # check to enter new trades
        pcnt_change = int(price / base_price - 1)
        if price > base_price: # sell
            while price >= base_price * 1.01:
                trades.append((-1, base_price * 1.01))
                base_price = base_price * 1.01
                trade_happened = True
        elif price < base_price:# buy
            while price <= base_price * 0.99:
                trades.append((1, base_price * 0.99))
                base_price = base_price * 0.99
                trade_happened = True

        # check to exit existing trades
        ongoing_trades = []
        for direction, trade_price in trades:
            if direction == 1: # bought initially
                if price >= trade_price * 1.01: # take profit
                    pnl += trade_price * 1.01 - trade_price
                elif price <= trade_price * 0.97: # take loss
                    pnl += trade_price * 0.97 - trade_price
                else: # don't close trade yet
                    ongoing_trades.append((direction, trade_price))
            elif direction == -1: # sold initially
                if price <= trade_price * 0.99: # take profit
                    pnl += trade_price - trade_price * 0.99
                elif price >= trade_price * 1.03: # take loss
                    pnl += trade_price - trade_price * 1.03
                else: # don't close trade yet
                    ongoing_trades.append((direction, trade_price))
        trades = ongoing_trades

    # exit all positions at market close
    for direction, trade_price in trades:
        pnl += direction * (prices[-1] - trade_price)

    return '{:.2f}'.format(pnl) if trade_happened else 'No Action'

if __name__ == "__main__":

    _ = int(sys.stdin.readline())

    prices = []
    for line in sys.stdin:
        prices.append(float(line))

    res = calculate_pl(prices)
    print(res + "\n")

