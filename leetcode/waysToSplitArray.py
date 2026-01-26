from collections import List


def waysToSplitArray(nums: List[int]) -> int:
    # prefix sum [10,4,-8,7] -> [10,14,6,13]
    #                               ^
    # prefix sum [2,3,1,0] -> [2,5,6,6]
    #                             ^     to get the 6 - 5

    prefix_sum = [0] * len(nums)
    prefix_sum[0] = nums[0]
    for i in range(1, len(prefix_sum)):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]

    res = 0
    for i in range(len(prefix_sum) - 1):
        if prefix_sum[i] >= (prefix_sum[-1] - prefix_sum[i]):
            res += 1

    return res


def waysToSplitArray(nums: List[int]) -> int:
    # prefix sum [10,4,-8,7] -> [10,14,6,13]
    #                               ^
    # prefix sum [2,3,1,0] -> [2,5,6,6]
    #                             ^     to get the 6 - 5

    left_sum, right_sum = 0, sum(nums)

    res = 0
    for i in range(len(nums) - 1):
        left_sum += nums[i]
        right_sum -= nums[i]
        if left_sum >= right_sum:
            res += 1

    return res
