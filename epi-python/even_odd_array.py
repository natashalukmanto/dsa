from typing import List

def even_odd(A: List[int]) -> None:
    i, write_idx = 0, len(A) - 1
    while i < len(A) and i < write_idx:
        if A[i] % 2 != 0:
            A[i], A[write_idx] = A[write_idx], A[i]
            write_idx -= 1
        else: 
            i += 1
    return None