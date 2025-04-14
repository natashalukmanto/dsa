"""
Obviously this is a very trivial question if you just do A.sort().
    - Time complexity: O(n logn)
    - Space complexity: O(1)
But we can do better, let's aproach this question with a Two Pointer algorithm.
"""

def dutch_flag_partition(pivot_index: int, A) -> None:
    # A.sort()
    left, equal, right = 0, 0, len(A) - 1
    pivot = A[pivot_index]
    while equal <= right:
        if A[equal] > pivot:
            A[equal], A[right] = A[right], A[equal]
            right -= 1
        elif A[equal] == pivot:
            equal += 1
        else:
            A[equal], A[left] = A[left], A[equal]
            left += 1
            equal += 1