from typing import List

def buy_and_sell_stock_once(prices: List[float]) -> float:
    buy, max_profit = 0, 0.0
    
    for sell in range(len(prices)):
        if prices[sell] < prices[buy]:
            buy = sell
        max_profit = max(max_profit, prices[sell] - prices[buy])
    
    return max_profit