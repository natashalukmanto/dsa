# Time: O(nlogn)
# Space: O(N), can be O(log n), but that's more complex

from typing import List

A = [-5, 3, 3, 2, -1, 0, 9, 8, 4, -4]

def mergeSort(arr: List[int]) -> List[int]:
    n = len(arr)
    
    if n == 1: return arr
    
    m = len(arr) // 2
    left, right = arr[:m], arr[m:]
    
    left = mergeSort(left)
    right = mergeSort(right)
    l, r = 0, 0
    l_len, r_len = len(left), len(right)
    
    i = 0
    sortedArray = [0] * n
    
    while l < l_len and r < r_len:
        if left[l] < right[r]:
            sortedArray[i] = left[l]
            l += 1
        else:
            sortedArray[i] = right[r]
            r += 1
        i += 1
        
    while l < l_len:
        sortedArray[i] = left[l]
        l += 1
        i += 1
        
    while r < r_len:
        sortedArray[i] = right[r]
        r += 1
        i += 1
        
    return sortedArray

print(mergeSort(A))