from typing import List


def missingNumber(nums: List[int]) -> int:
    set_nums = set(nums)
    for i in range(len(nums) + 1):
        if i not in set_nums:
            return i


def missingNumber(nums: List[int]) -> int:
    expected_sum = int((len(nums) * (len(nums) + 1)) / 2)
    actual_sum = sum(nums)

    return expected_sum - actual_sum
