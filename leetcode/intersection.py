from typing import List
from collections import defaultdict

def intersection(self, nums: List[List[int]]) -> List[int]:
    dictionary = defaultdict(int)
    n = len(nums)
    res = []

    for num in nums:
        for x in num:
            dictionary[x] += 1

    for key, value in dictionary.items():
        if value == n:
            res.append(key)

    return sorted(res)
