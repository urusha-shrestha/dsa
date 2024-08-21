# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit(prices):
    l,r=0,1
    maxProfit=0

    while r<len(prices):
        if prices[l]<prices[r]:
            profit = prices[r]-prices[l]
            maxProfit = max(maxProfit,profit)
        else:
            l = r

        r +=1
    return maxProfit

prices = [2,4,1]

print(maxProfit(prices))