from collections import defaultdict
from typing import List


def maxSubarrayLength(nums: List[int], k: int) -> int:
    freq = defaultdict(int)
    left = max_len = 0

    for right in range(len(nums)):
        freq[nums[right]] += 1

        while freq[nums[right]] > k:
            freq[nums[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
