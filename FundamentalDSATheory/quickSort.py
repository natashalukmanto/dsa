# Time: O(nlogn)
# Space: O(N), can be O(log n), but that's more complex

from typing import List

A = [-5, 3, 3, 2, -1, 0, 9, 8, 4, -4]

def quickSort(arr: List[int]) -> List[int]:
    if len(arr) <= 1: return arr
    
    p = arr[-1]
    
    left = [x for x in arr[:-1] if x <= p]
    right = [x for x in arr[:-1] if x > p]
    
    left = quickSort(left)
    right = quickSort(right)
    
    return left + [p] + right

print(quickSort(A))