from typing import List

# O(n^2)
def longestOnes(nums: List[int], k: int) -> int:
    zeroes = max_len = 0

    for left in range(len(nums)):
        zeroes = 0
        for right in range(left, len(nums)):
            if nums[right] == 0:
                zeroes += 1

            if zeroes > k:
                break

        max_len = max(max_len, right - left + 1)

    return max_len

# O(n); Sliding Window
def longestOnes(nums: List[int], k: int) -> int:
    left = zeroes = max_length = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeroes += 1

        while zeroes > k:
            if nums[left] == 0:
                zeroes -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length
