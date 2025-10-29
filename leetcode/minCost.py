from typing import List
from collections import Counter


def minCost(basket1: List[int], basket2: List[int]) -> int:
    freq = Counter(basket1)
    freq.subtract(Counter(basket2))
    min_elem = min(basket1 + basket2)

    swap = []
    for elem, frequency in freq.items():
        if frequency % 2 != 0:
            return -1
        swap.extend([elem] * (abs(frequency) // 2))
        # print(swap)
    swap.sort()
    if not swap:
        return 0
    cost = 0
    for i in range(len(swap) // 2):
        direct_swap = swap[i]
        indirect_swap = 2 * min_elem
        cost += min(direct_swap, indirect_swap)

        return cost


# print(minCost([4, 2, 2, 2], [1, 1, 2, 4]))
