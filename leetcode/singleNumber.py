from typing import List

def singleNumber(self, nums: List[int]) -> int:
    res = 0
    for num in nums:
        res ^= num
    return res

    # DOESNT WORK BCS THE 2ND ELEM MIGHT NOT BE PLACED IN THAT SEQUENCE, ex: [4,1,2,1,2]
    # res = nums[0]

    # for i in range(1, len(nums)):
    #     if i % 2 == 0:
    #         res += nums[i]
    #     else:
    #         res -= nums[i]
    #     print(res)

    # return res
