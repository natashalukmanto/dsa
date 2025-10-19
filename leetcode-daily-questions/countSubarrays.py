def isValid(self, nums: List[int]) -> bool:
    return nums[0] + nums[2] == nums[1] / 2


def countSubarrays(self, nums: List[int]) -> int:
    res = 0
    for i in range(len(nums) - 2):
        res += self.isValid(nums[i : i + 3])

    return res
