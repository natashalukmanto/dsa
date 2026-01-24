from collections import List

def buy_and_sell_stock_twice(prices: List[float]) -> float:
    first_buy, first_profit, second_buy, second_profit = prices[0], 0, prices[0], 0

    for price in prices:
        if price < first_buy:
            first_buy = price

        if price - first_buy > first_profit:
            first_profit = price - first_buy

        if price - first_profit < second_buy:
            second_buy = price - first_profit

        if price - second_buy > second_profit:
            second_profit = price - second_buy

    return second_profit
