from typing import List

A = [-5, 3, 3, 2, -1, 0, 9, 8, 4, -4]

# Time: O(n^2)
# Space: O(1)

def selection_sort(arr: List[int]) -> None:
    for i in range(len(arr)):
        minn = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minn]:
                minn = j 
        arr[i], arr[minn] = arr[minn], arr[i]
        
selection_sort(A)
print(A)