from typing import List
from collections import Counter


def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    res = []
    perm = []
    count = Counter(nums)

    def dfs():
        if len(nums) == len(perm):
            res.append(perm[:])
            return

        for i in count:
            if count[i] > 0:
                count[i] -= 1
                perm.append(i)
                dfs()
                perm.pop()
                count[i] += 1

    dfs()
    return res
