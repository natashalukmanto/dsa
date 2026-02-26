from typing import List
from collections import defaultdict

def numIdenticalPairs(nums: List[int]) -> int:
    res = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                res += 1
    return res

def numIdenticalPairs(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = 0

        for num in nums:
            res += count[num]
            count[num] += 1
        
        return res