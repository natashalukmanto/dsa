from typing import List
import random

# Use randint in Python to generate random index
def random_sampling(k: int, A: List[int]) -> None:
    for i in range(k):
        r = random.randint(0, len(A) - 1) # Generate a random index
        A[r], A[i] = A[i], A[r] # Swap it with the random index
    # Pick the first k elements
    
# range(k) instead of range(len(A)) so the time complexity is O(k) instead of O(n)

    