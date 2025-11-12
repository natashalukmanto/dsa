
from typing import List
from merge_sorted_arrays import merge_sorted_arrays


def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    sorted_arrays = []
    direction = 1 # 1 for increasing; -1 for decreasing
    
    start = 0
    for i in range(1, len(A)+1):
        if (i == len(A) or 
            A[i-1] >= A[i] and direction == 1 or
            A[i-1] < A[i] and direction == -1):
            sorted_arrays.append(A[start:i] if direction == 1 else A[i-1:start-1:-1])
            start = i
            direction *= -1
        
    return merge_sorted_arrays(sorted_arrays)