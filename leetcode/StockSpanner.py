class StockSpanner:
    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        span = 1
        while self.stock and self.stock[-1][0] <= price:
            span += self.stock.pop()[1]

        self.stock.append((price, span))
        return span
