# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

def maxProfit(prices):
    if len(prices) < 2:
        return 0
    sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
    for price in prices:
        prev_buy = buy
        buy = max(prev_sell - price, prev_buy)
        prev_sell = sell
        sell = max(prev_buy + price, prev_sell)
    return sell

x = maxProfit([1,2,3,4,0,2])
print(x)