from typing import List

# Honestly this is just following instructions. I also feel like the description 
#   "You are allowed to delete any number of elements from nums without making it empty. "
# is just a distraction. 

# Here's how you can approach it:
# Because we want the maximum sum of the subarray of nums, then we do not want any negatives.
# Think if we have something like [any positive number, -1, -6, -7], then all we want to do is to ignore the negative numbers and just take the one positive number
# Same goes for [1, 2, -1, -6] -> we ignore the negative numbers and the subarray is [1, 2] with the sum of 3

# But wait! What if all of the values in nums are negative? Then the max(nums) will be the greatest sum. So just return that

# From the first explanation, we know now that we only care about the positive numbers
# An extra step is that the subarray have to be of unique elements, hence we use set()

#DONE!

def maxSum(self, nums: List[int]) -> int:
    return max(nums) if max(nums) < 0 else sum(set([num for num in nums if num > 0]))
    # if max(nums) < 0: return max(nums)
    # else:
    #     res = []
    #     for num in nums:
    #         if num not in res and num > 0:
    #             res.append(num)
    #     return sum(res)
    