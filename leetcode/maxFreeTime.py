from typing import List


def maxFreeTime(
    eventTime: int, k: int, startTime: List[int], endTime: List[int]
) -> int:
    n = len(startTime)
    res = 0
    t = 0

    for i in range(n):
        t += endTime[i] - startTime[i]
        right = eventTime if i == n - 1 else startTime[i + 1]
        left = 0 if i <= k - 1 else endTime[i - k]
        res = max(res, right - left - t)

        if i >= k - 1:
            t -= endTime[i - k + 1] - startTime[i - k + 1]

    return res
