from typing import List


def findDuplicates(nums: List[int]) -> List[int]:
    res = []

    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            res.append(abs(num))
        else:
            nums[index] *= -1

    return res


def findDuplicates0(nums: List[int]) -> List[int]:
    res, seen = [], set()

    for num in nums:
        if num not in seen:
            seen.add(num)
        else:
            res.append(num)
    return res
