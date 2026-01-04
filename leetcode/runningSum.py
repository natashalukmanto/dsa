from typing import List


def runningSum(self, nums: List[int]) -> List[int]:
    prefix_sum = [nums[0]]
    for i in range(1, len(nums)):
        prefix_sum.append(nums[i] + prefix_sum[i - 1])

    return prefix_sum
