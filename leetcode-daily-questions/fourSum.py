from typing import List


def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    res, subarray = [], []

    def kSum(k: int, start_index: int, target: int):
        if k == 2:
            left, right = start_index, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    res.append(subarray + [nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
            return

        for i in range(start_index, len(nums) - k + 1):
            if i > start_index and nums[i] == nums[i - 1]:
                continue
            subarray.append(nums[i])
            kSum(k - 1, i + 1, target - nums[i])
            subarray.pop()

    kSum(4, 0, target)
    return res
