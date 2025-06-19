from typing import List

# Brute Force is obvious but uses O(n) additional storage
# perm[] tells you where char[i] in A should be, hence B[perm[i]] = A[i]
def apply_permutation0(perm: List[int], A: List[int]) -> None:
    B = [0] * len(A)
    for i in range(len(perm)):
        B[perm[i]] = A[i]
    A[:] = B # we have to permute in-place, hence we copy the list B to A
    
# Solution without additional storage
def apply_permutation(perm: List[int], A: List[int]) -> None:
    for i in range(len(A)):
        while perm[i] != i:
            A[i], A[perm[i]] = A[perm[i]], A[i]
            perm[i], perm[perm[i]] = perm[perm[i]], perm[i]                                        
