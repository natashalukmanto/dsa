from typing import Iterator, List
import itertools, heapq


def sort_approximately_sorted_array0(sequence: Iterator[int], k: int) -> List[int]:
    res, min_heap = [], []

    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)

    for x in sequence:
        val = heapq.heappushpop(min_heap, x)
        res.append(val)

    while min_heap:
        res.append(heapq.heappop(min_heap))

    return res

def sort_approximately_sorted_array0(sequence: Iterator[int], k: int) -> List[int]:
    res, min_heap = [], []

    for _ in range(k + 1):
        try:
            item = next(sequence)
            heapq.heappush(min_heap, item)
        except StopIteration:
            break

    while True:
        res.append(heapq.heappop(min_heap))
        try:
            item = next(sequence)
            heapq.heappush(min_heap, item)
        except StopIteration:
            break

    while min_heap:
        res.append(heapq.heappop(min_heap))

    return res
