from typing import List
import heapq


def findKthLargest(nums: List[int], k: int) -> int:
    res = []

    for num in nums:
        heapq.heappush(res, num)
        if len(res) > k:
            heapq.heappop(res)
        # print(res)

    return res[0]


print(findKthLargest([1, 2, 3, 4, 4, 5, 6], 7))
