from typing import List


def findKDistantIndices(nums: List[int], key: int, k: int) -> List[int]:
    res = []

    keys = []
    for index, value in enumerate(nums):
        if value == key:
            keys.append(index)

    # print(keys)
    for i in range(len(nums)):
        # print(res)

        closest_key = 0
        while closest_key < len(keys):
            if abs(i - keys[closest_key]) <= k:
                res.append(i)
                break
            closest_key += 1

    return res
