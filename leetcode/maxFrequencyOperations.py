from typing import List
from collections import Counter


def maxFrequency(nums: List[int], k: int, numOperations: int) -> int:
    nums.sort()
    n = len(nums)
    res = left = right = 0
    freq = Counter()

    for num in nums:

        while right < n and nums[right] <= num + k:
            freq[nums[right]] += 1
            right += 1

        while left < n and nums[left] < num - k:
            freq[nums[left]] += 1
            left += 1

        curr = min(right - left, freq[num] + numOperations)
        res = max(res, curr)

    left = 0
    for right in range(n):
        while nums[left] + 2 * k < nums[right]:
            left += 1
        res = max(res, min(right - left + 1, numOperations))

    return res
