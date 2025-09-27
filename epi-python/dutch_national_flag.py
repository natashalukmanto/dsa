"""
Obviously this is a very trivial question if you just do A.sort().
    - Time complexity: O(n logn)
    - Space complexity: O(1)
But we can do better, let's aproach this question with a Two Pointer algorithm.
"""

def dutch_flag_partition(pivot_index: int, A) -> None:
    # A.sort()
    # === Own try ===
    
    s, e, b = 0, 0, len(A) - 1
    
    original = A[pivot_index]
    while e <= b:
        if A[e] < original:
            A[e], A[s] = A[s], A[e]
            s += 1
            e += 1
        elif A[e] > original:
            A[e], A[b] = A[b], A[e]
            b -= 1
        else:
            e += 1
                 
    # ==== Textbook Solution ===
    # left, equal, right = 0, 0, len(A) - 1
    # pivot = A[pivot_index]
    # while equal <= right:
    #     if A[equal] > pivot:
    #         A[equal], A[right] = A[right], A[equal]
    #         right -= 1
    #     elif A[equal] == pivot:
    #         equal += 1
    #     else:
    #         A[equal], A[left] = A[left], A[equal]
    #         left += 1
    #         equal += 1