from typing import List

def canReach(self, arr: List[int], start: int) -> bool:
    if 0 <= start <= len(arr) - 1 and arr[start] >= 0:
        if arr[start] == 0: return True

        arr[start] = -arr[start]

        return self.canReach(arr, start + arr[start]) or self.canReach(arr, start - arr[start])

    return False

"""
=== Cleaned ===
def canReach(self, arr: List[int], start: int) -> bool:
    visited = set()

    def dfs(index: int) -> bool:
        if (index < 0 or index >= len(arr)) or (index in visited): return False
        if arr[index] == 0: return True
        
        visited.add(index)

        return dfs(index + arr[index]) or dfs(index - arr[index])

    return dfs(start)
        
        
=== First Attempt Accepted ===
def canReach(self, arr: List[int], start: int) -> bool:
    visited = set()

    def dfs(index: int):
        if arr[index] == 0:
            return True
        
        if (arr[index], index) in visited:
            return False

        visited.add((arr[index], index))
        left, right = False, False
        if index + arr[index] < len(arr):
            left = dfs(index + arr[index])

        if index - arr[index] > -1:
            right = dfs(index - arr[index])
        
        return left or right

    return dfs(start)
"""