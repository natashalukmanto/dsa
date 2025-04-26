from typing import List

def plus_one(A: List[int]) -> List[int]:
    A[-1] += 1
    
    for i in reversed(range(1, len(A))):
        if A[i] != 10: return A
        A[i - 1] += 1
        A[i] = 0
        
    if A[0] == 10:
        A[0] = 1
        A.append(0)
        
    return A

A = [1, 2, 9]
print(plus_one(A)) # [1, 3, 0]
B = [9, 9, 9, 9]
print(plus_one(B)) # [1, 0, 0, 0, 0]
C = [0, 0, 0, 0]
print(plus_one(C)) # [0, 0, 0, 1]

