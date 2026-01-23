from collections import List


def maxProfit(prices: List[int]) -> int:
    buy = sell = prices[0]
    max_profit = 0

    for price in prices:
        if buy > price:
            buy = price
            sell = price
        elif sell < price:
            sell = price

        max_profit = max(max_profit, sell - buy)

    return max_profit
