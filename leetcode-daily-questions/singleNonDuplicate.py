from typing import List

def singleNonDuplicate(nums: List[int]) -> int:
    # binary? 
    # [1,1,2,3,3,4,4,8,8], len = 9, middle = 4
    # all elements appears twice, except 1 element -> length has to be odd
    if len(nums) == 1: return nums[0]
    if nums[-1] != nums[-2]: return nums[-1]
    if nums[0] != nums[1]: return nums[0]

    left, right = 0, len(nums) - 1
    while left < right:
        middle = left + (right - left) // 2
        if middle-1 == -1:
            break
        print(middle)
        print("going left", nums[middle], nums[middle - 1])
        if nums[middle] != nums[middle - 1] and nums[middle] != nums[middle + 1]:
            return nums[middle]
        else:
            right = middle 
            
    left, right = 0, len(nums) - 1
    while left < right:
        middle = left + (right - left) // 2
        if middle-1 == -1:
            break
        print(middle)
        print("going right: ", nums[middle], nums[middle + 1])
        if nums[middle] != nums[middle + 1] and nums[middle] != nums[middle - 1]:
            return nums[middle]
        else:
            left = middle
            
print(singleNonDuplicate([7,7,10,11,11,12,12]))