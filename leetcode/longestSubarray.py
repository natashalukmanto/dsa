from typing import List
from collections import deque


def longestSubarray(nums: List[int], limit: int) -> int:
    left = res = 0
    max_deque, min_deque = deque(), deque()

    for right in range(len(nums)):
        while max_deque and max_deque[-1] < nums[right]:
            max_deque.pop()
        max_deque.append(nums[right])

        while min_deque and min_deque[-1] > nums[right]:
            min_deque.pop()
        min_deque.append(nums[right])

        while max_deque[0] - min_deque[0] > limit:
            if max_deque[0] == nums[left]:
                max_deque.popleft()
            if min_deque[0] == nums[left]:
                min_deque.popleft()
            left += 1

        res = max(res, right - left + 1)

    return res
