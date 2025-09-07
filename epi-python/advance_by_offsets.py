from typing import List
def can_reach_end(A: List[int]) -> bool:
    goal = len(A) - 1
    for i in reversed(range(len(A))):
        if i + A[i] >= goal:
            goal = i
    return goal == 0
