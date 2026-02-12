from typing import List
from collections import Counter


def largestUniqueNumber(self, nums: List[int]) -> int:
    nums_freq = Counter(nums)
    return max(list(num for num, freq in nums_freq.items() if freq == 1), default=-1)
