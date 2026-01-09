from typing import List

def maxFrequency(nums: List[int], k: int) -> int:
    nums.sort()
    left = window_sum = max_freq = 0

    for right in range(len(nums)):
        window_sum += nums[right]

        while nums[right] * (right - left + 1) - window_sum > k:
            window_sum -= nums[left]
            left += 1

        max_freq = max(max_freq, right - left + 1)
        # print(nums[left], nums[right], operations, max_freq)

    return max_freq
