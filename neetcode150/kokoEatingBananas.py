from math import ceil
from typing import List

def minEatingSpeed(piles: List[int], h: int) -> int:
    left, right = 1, max(piles)
    while left <= right:
        middle = left + (right - left) // 2
        finish = 0
        for pile in piles:
            finish += ceil(pile/middle)
        if finish <= h:
            right = middle - 1
        else:
            left = middle + 1
    return left