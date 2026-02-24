from typing import List
from collections import Counter


def uniqueOccurrences(arr: List[int]) -> bool:
    freq = Counter(arr)

    res = list(freq.values())
    # print(res)
    return len(set(res)) == len(res)
