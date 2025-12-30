from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    left = 0
    curr_sum = max_sum = sum(nums[:k])

    for right in range(left + k, len(nums)):
        curr_sum = curr_sum - nums[left] + nums[right]
        if curr_sum > max_sum:
            max_sum = curr_sum
        left += 1

    return max_sum / k
