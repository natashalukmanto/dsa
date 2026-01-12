from typing import List
def longestSubarray(self, nums: List[int]) -> int:
    left = max_len = zero = 0  # zero counts the number of 0 in the curr window

    for right in range(len(nums)):
        if nums[right] == 0:
            zero += 1

        while zero > 1:
            if nums[left] == 0:
                zero -= 1
            left += 1

        max_len = max(max_len, right - left)

    return max_len
