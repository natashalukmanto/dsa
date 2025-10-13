from typing import List


def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []

    for i in range(len(nums)):
        if i > 0 and nums[i - 1] == nums[i]:
            continue
        low, high = i + 1, len(nums) - 1
        while low < high:
            current_sum = nums[i] + nums[low] + nums[high]
            if current_sum == 0:
                res.append([nums[i], nums[low], nums[high]])
                while low < high and nums[low] == nums[low + 1]:
                    low += 1
                while low < high and nums[high] == nums[high - 1]:
                    high -= 1
                low += 1
                high -= 1
            elif current_sum < 0:
                low += 1
            else:
                high -= 1

    return res
