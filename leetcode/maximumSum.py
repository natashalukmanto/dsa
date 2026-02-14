from typing import List
from collections import defaultdict


def maximumSum(nums: List[int]) -> int:
    groups = defaultdict(list)
    # {9: 0, 7: 1, 9: 2, 4: 3, 7: 4}

    for i, num in enumerate(nums):
        num_sum = 0
        while num:
            num_sum += num % 10
            num //= 10
        groups[num_sum].append(nums[i])

    if len(nums) == len(groups):
        return -1

    ans = -1
    for arr in groups.values():
        if len(arr) >= 2:
            arr.sort()
            ans = max(ans, arr[-1] + arr[-2])
    return ans


def maximumSum(nums: List[int]) -> int:

    def get_digit_sum(num):
        digit_sum = 0
        while num:
            digit_sum += num % 10
            num //= 10
        return digit_sum

    dic = defaultdict(int)
    res = -1

    for num in nums:
        digit_sum = get_digit_sum(num)
        if digit_sum in dic:
            res = max(res, num + dic[digit_sum])
        dic[digit_sum] = max(dic[digit_sum], num)

    return res
