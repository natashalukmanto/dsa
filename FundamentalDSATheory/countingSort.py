# Time: O(n + k)
# Space: O(k)

from typing import List

A = [5, 3, 3, 2, 1, 0, 9, 8, 4, 4]

def quickSort(arr: List[int]) -> None:
    n = len(arr)
    maxx = max(arr)
    
    count = [0] * (maxx + 1)
    
    for x in arr:
        count[x] += 1
        
    i = 0
    for c in range(maxx + 1):
        while count[c] > 0:
            arr[i] = c
            i += 1
            count[c] -= 1
            
quickSort(A)
print("Quick sort w/o negatives:\t", A)

A = [-5, 3, 3, 2, -1, 0, 9, -8, 4, -4]

def quickSortWithNegatives(arr: List[int]) -> None:
    n = len(arr)
    minn, maxx = min(arr), max(arr)
    
    count = [0] * (maxx - minn + 1)
    
    for x in arr:
        count[x - minn] += 1
        
    i = 0
    for c in range(len(count)):
        while count[c] > 0:
            arr[i] = c + minn
            i += 1
            count[c] -= 1
            
quickSortWithNegatives(A)
print("Quick sort with negatives:\t", A)
    