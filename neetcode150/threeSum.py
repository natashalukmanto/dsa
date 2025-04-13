def threeSum(nums: list) -> list:
    nums.sort()
    res = []

    for index in range(len(nums)):
        
        # skipping duplicates
        if index > 0 and nums[index] == nums[index - 1]:
            continue

        # same thing as twoSumii.py
        target = -nums[index]
        left, right = index + 1, len(nums) - 1


        while left < right:
            if target > nums[left] + nums[right] :
                left += 1
            elif target < nums[left] + nums[right]:
                right -= 1
            else:
                res.append([nums[index], nums[left], nums[right]])
                left += 1
                right -= 1
            
            
                # skipping duplicates
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                        
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return res