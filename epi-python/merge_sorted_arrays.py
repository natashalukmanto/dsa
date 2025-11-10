from collections import List
import heapq


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    min_heap = []

    for array_id, array in enumerate(sorted_arrays):
        if array:
            heapq.heappush(min_heap, (array[0], array_id, 0))

    result = []
    while min_heap:
        entry, array_id, index = heapq.heappop(min_heap)
        result.append(entry)

        next_idx = index + 1
        if next_idx < len(sorted_arrays[array_id]):
            next_val = sorted_arrays[array_id][next_idx]
            heapq.heappush(min_heap, (next_val, array_id, next_idx))

    return result
