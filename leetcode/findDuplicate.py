from typing import List

def findDuplicate(self, nums: List[int]) -> int:
    while nums[0] != nums[nums[0]]:
        nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
    return nums[0]

    # 1 -> 3 -> 4 -> 2 -> 2

    # nums.sort()
    # for i in range(len(nums) - 1):
    #     if nums[i] == nums[i+1]:
    #         return nums[i]

    # [1,3,4,2,2]
    #      ^

def findDuplicate(self, nums: List[int]) -> int:
    low, high = 1, len(nums) - 1

    while low <= high:
        middle = low + (high - low) // 2

        count = sum(num <= middle for num in nums)
        if count > middle:
            duplicate = middle
            high = middle - 1
        else:
            low = middle + 1
    
    return duplicate