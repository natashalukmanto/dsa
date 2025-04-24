from typing import List

def plus_one(A: List[int]) -> List[int]:
    carry = 0
    A[-1] += 1
    for i in reversed(range(len(A))):
        A[i] = A[i] + carry
        carry = 0
        if A[i] == 10:
            carry = 1
            A[i] = 0
    
    if A[0] == 0:
        A[0] = 1
        A.append(0)
            
    return A
