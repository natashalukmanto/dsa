from typing import List


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
