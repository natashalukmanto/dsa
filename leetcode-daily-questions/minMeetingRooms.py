from typing import List
import heapq


def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[0])
    res = 0

    ends = []
    for start, end in intervals:
        while ends and start >= ends[0]:
            heapq.heappop(ends)

        heapq.heappush(ends, end)
        res = max(res, len(ends))

    return res
