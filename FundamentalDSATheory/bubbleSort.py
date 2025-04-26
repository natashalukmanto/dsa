from typing import List

A = [-5, 3, 3, 2, -1, 0, 9, 8, 4, -4]

# Time: O(n^2)
# Space: O(1)

def bubble_sort(arr: List[int]) -> None:
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]: # just flip this > to be < if you want descending order
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True

bubble_sort(A)
print(A)
