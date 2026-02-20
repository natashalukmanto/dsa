from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))
