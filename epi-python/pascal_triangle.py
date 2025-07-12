from typing import List

# This problem is pretty trivial to solve, right
# My idea is:
# 1. take the last value in our final answer
# 2. Make a new list that will represent the next pascla triangle sequence
# 3. Populate that new sequence by looping through the index 1 element all the way to n-1
# 4. sum up the two values in previous to get the value in the new sequence
# 5. Append the new sequence to you final list
# Done
def generate_pascal_triangle0(n: int) -> List[List[int]]:
    if n == 0: return []
    if n == 1: return [[1]]
    if n == 2: return [[1], [1, 1]]
    
    res = [[1], [1, 1]]
    
    for i in range(2, n):
        previous = res[-1] # [1, 1]
        next = [1] * (i + 1)
        for j in range(1, len(next)-1):
            next[j] = previous[j-1] + previous[j]
        res.append(next)

    return res

# However, the textbook solution is cleaner, but practically uses the same idea.
def generate_pascal_triangle(n: int) -> List[List[int]]:
    result = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            result[i][j] = result[i-1][j-1] + result[i-1][j]
    return result