import random
from typing import List
from offline_sampling import random_sampling 

def compute_random_permutation0(n: int) -> List[int]:
    # This is known as the Coupon Collector's Problem
    # To solve this problem:
        # 1. Create a list of size n
        # 2. For each index in the list, we randomly pick an integer from 0 to n (inclusive)
        # 3. Narrow the range however you can
        
    if n <= 1:
        return list(range(n))
    
    pool = list(range(n))  # Available values to pick from
    res = []

    for i in range(n):
        idx = random.randrange(len(pool))
        res.append(pool[idx])            
        pool.pop(idx)                

    return res

# we can also use the offline_sampling.py solution from previously
def compute_random_permutation(n: int) -> List[int]:
    permutation = list(range(n))
    random_sampling(n, permutation)
    return permutation
