from collections import List


def minStartValue(self, nums: List[int]) -> int:
    # [1,-2,-3] -> [1, -1, -4]
    # [1,2] -> [1,3]
    # [-3,2,-3,4,2] -> [-3,-1,-4,0,2]

    prefix_sum = [nums[0]]

    for i in range(1, len(nums)):
        prefix_sum.append(nums[i] + prefix_sum[i - 1])
    # print(prefix_sum)

    return max(1, 1 - min(prefix_sum))
