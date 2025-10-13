from typing import List


def permute(self, nums: List[int]) -> List[List[int]]:
    res, subarray = [], []

    def backtrack() -> None:
        if len(subarray) == len(nums):
            res.append(subarray[:])
            return

        for i in range(len(nums)):
            if nums[i] not in subarray:
                subarray.append(nums[i])
                backtrack()
                subarray.pop()

    backtrack()

    return res
