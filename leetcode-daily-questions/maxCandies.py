from collections import deque
from typing import List

def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
    seen = set() # for a list of boxes that we already visit, reduce repeating
    queue = deque() # for a list of boxes that we need to check either we can open later or not

    def dfs(box):
        if box in seen: return 0
        if status[box] == 0: 
            queue.append(box)
            return 0
        
        seen.add(box)
        total = candies[box]

        # Check if we can get any candies from the contained boxes inside `box`
        for next_box in containedBoxes[box]:
            total += dfs(next_box)

        # Check if we can open any boxes with keys
        for next_box in keys[box]:
            status[next_box] = 1
            if next_box in queue:
                total += dfs(next_box)
        
        return total
    
    return sum([dfs(box) for box in initialBoxes])