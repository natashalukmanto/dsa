from typing import List

def findMin(nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle + 1] < nums[middle]:
                return nums[middle + 1]
            elif nums[middle - 1] > nums[middle]:
                return nums[middle]
            elif nums[middle] > nums[-1]:
                left = middle + 1
            else:
                right = middle - 1