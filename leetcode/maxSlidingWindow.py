from typing import List
from collections import deque


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    res = []
    dq = deque()

    for i in range(k):
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()
        dq.append(i)

    res.append(nums[dq[0]])

    for i in range(k, len(nums)):
        if dq and dq[0] == i - k:
            dq.popleft()

        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()

        dq.append(i)
        res.append(nums[dq[0]])

    return res


# TLE
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    res = []
    window = deque(nums[:k])

    res.append(max(window))

    for i in range(k, len(nums)):
        window.popleft()
        window.append(nums[i])
        # print(window)

        res.append(max(window))
        # print(res)

    return res
