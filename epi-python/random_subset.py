import random
from typing import Dict, List

# A quite straightforward solution, simulating a similar approach to 5.12 Sample Offline Data
# Time: O(n), Space: O(n) -> since we have to create the nums array first
# Approach:
# 1. create an array that stores all possible n values (think of this like a pool from which we will draw the random numbers from)
# 2. Do the below k times:
    # 2a. pick a random index from i to n-1
    # 2b. swap nums[i] and nums[r]
# 3. return the nums array (sliced up to index k-1)
def random_subset0(n: int, k: int) -> List[int]:
    nums = [i for i in range(n)]
    for i in range(k):
        r = random.randint(i, n-1)
        nums[i], nums[r] = nums[r], nums[i]
    return nums[:k]

# This is the book solution, cleverly used a dictionary to keep track of ONLY the necessary elements
# The idea is that we only use k elements of n, and the rest that were not picked by the random generator stays the same
# Furthermore, we only need to return k elements

# This is an opportunity to optimize our approach

# nums is a Dictionary that stores (index, value), e.g. (0, 28) means that at index 0, the value is 28 
def random_subset(n: int, k: int) -> List[int]:
    # 1. Create the data structure
    nums: Dict[int, int ] = {} # nums = (index, value)
    
    # 2. Do the below k times
    for i in range(k): 
        random_index = random.randint(i, n-1) # 2a. Generate a random number
        nums[random_index], nums[i] = nums.get(i, i), nums.get(random_index, random_index) # 2b. Swap the value at index `random number` with the value at index `i`     
        # But wait, the it could be the case where the random number generator picked the same random number more than once!
        # In that case, we need to find if there has been a swap that happened which is tracked in our dictionary.
        # Then we get back that value and only then we can swap.  
    
    return [nums[i] for i in range(k)] # 3. Return the appropriate subset.

    