from typing import List

def can_reach_end(A: List[int]) -> bool:
    goal = len(A) - 1
    for index in reversed(range(len(A))):
        if A[index] + index >= goal:
            goal = index
        
    return goal == 0