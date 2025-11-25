import heapq
from typing import Iterator


def online_median(sequence: Iterator[int]) -> List[float]:
    min_heap, max_heap = [], []

    res = []
    for x in sequence:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        res.append(
            0.5 * (min_heap[0] + -max_heap[0])
            if len(min_heap) == len(max_heap)
            else min_heap[0]
        )

    return res
