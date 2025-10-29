from typing import List
def maxFrequency(nums: List[int], k: int) -> int:
    k_count = nums.count(k)
    max_gain = 0

    for repeating in range(1, 51):
        current = max_current = 0
        for num in nums:
            if repeating == k: continue
            if num == repeating: current += 1
            elif num == k: current -= 1

            current = max(current, 0)
            max_current = max(max_current, current)
        
        max_gain = max(max_gain, max_current)
    
    return k_count + max_gain

print(maxFrequency([1, 3, 3, 1, 2, 1, 3, 3, 2], 3))