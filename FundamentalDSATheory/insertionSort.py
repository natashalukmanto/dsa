from typing import List

A = [-5, 3, 3, 2, -1, 0, 9, 8, 4, -4]

# Time: O(n^2)
# Space: O(1)

def insertion_sort(arr: List[int]) -> None:
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]

insertion_sort(A)
print(A)