from typing import List


def findPeakElement(self, nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        middle = left + (right - left) // 2
        if nums[middle] > nums[middle + 1]:
            right = middle
        else:
            left = middle + 1

    return left
