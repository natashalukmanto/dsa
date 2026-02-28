from collections import defaultdict
from typing import List

def numSubarraysWithSum(nums: List[int], goal: int) -> int:
    count_ps = defaultdict(int)
    count_ps[0] = 1
    curr_sum = res = 0

    for num in nums:
        curr_sum += num
        res += count_ps[curr_sum - goal]
        count_ps[curr_sum] += 1

    return res
