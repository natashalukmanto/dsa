from typing import List
def sumOfUnique(nums: List[int]) -> int:
    unique = {}

    for num in nums:
        unique[num] = unique.get(num, 0) + 1

    total_sum = 0
    for key, value in unique.items():
        if value == 1:
            total_sum += key

    return total_sum
