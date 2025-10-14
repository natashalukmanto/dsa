from typing import List
from collections import defaultdict


def subarraySum(self, nums: List[int], k: int) -> int:
    res, prefix_sum = 0, 0
    count_freq = defaultdict(int)
    count_freq[0] = 1

    for i in range(len(nums)):
        prefix_sum += nums[i]
        res += count_freq[prefix_sum - k]
        count_freq[prefix_sum] += 1

    return res


# def subarraySum(nums: List[int], k: int) -> int:
#     prefix_sum = [0] * (len(nums) + 1)
#     res = 0

#     for i in range(len(nums)):
#         prefix_sum[i + 1] = prefix_sum[i] + nums[i]

#     count = defaultdict(int)

#     for i in range(len(prefix_sum)):
#         res += count.get(prefix_sum[i] - k, 0)
#         count[prefix_sum[i]] += 1

#     return res

print(subarraySum([-1, -1, 1], 0))
