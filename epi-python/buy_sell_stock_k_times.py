from typing import List

def buy_and_sell_stock_k_times(prices: List[float], k: int) -> float:
    if k == 0: 
        return 0.0
    elif 2 * k >= len(prices):
        return sum([max(0, b - a) for a, b in zip(prices[:-1], prices[1:])])
    else:
        max_profit = [0.0] * k
        min_prices = [float('inf')] * k
        for price in prices:
            for i in reversed(range(k)):
                max_profit[i] = max(max_profit[i], price - min_prices[i])
                min_prices[i] = min(min_prices[i], price - (0 if i == 0 else max_profit[i - 1]))
        return max_profit[-1]