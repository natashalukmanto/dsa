from typing import List


def minTransfers(self, transactions: List[List[int]]) -> int:
    wallet = [0] * 12

    for f, t, amt in transactions:
        wallet[f] -= amt
        wallet[t] += amt

    wallet = [w for w in wallet if w != 0]
    n = len(wallet)

    def dfs(i: int) -> int:
        while i < n and wallet[i] == 0:
            i += 1

        if i == n:
            return 0

        cost = float("inf")
        for k in range(i + 1, n):
            if wallet[k] * wallet[i] < 0:
                wallet[k] += wallet[i]
                cost = min(cost, 1 + dfs(i + 1))
                wallet[k] -= wallet[i]

        return cost

    return dfs(0)
