from collections import List


def getAverages(nums: List[int], k: int) -> List[int]:
    if len(nums) < k:
        return [-1] * len(nums)
    if k == 0:
        return nums

    res = [-1] * len(nums)
    curr_sum = sum(nums[: k * 2 + 1])
    for i in range(k, len(nums) - k):
        res[i] = curr_sum // (k * 2 + 1)
        if i < len(nums) - k - 1:
            curr_sum -= nums[i - k]
            curr_sum += nums[i + k + 1]

    return res


def getAverages(nums: List[int], k: int) -> List[int]:
    if (k * 2 + 1) > len(nums):
        return [-1] * len(nums)
    if k == 0:
        return nums

    res = [-1] * len(nums)
    curr_sum = sum(nums[: k * 2 + 1])
    res[k] = curr_sum // (k * 2 + 1)

    for i in range(k * 2 + 1, len(nums)):
        curr_sum = curr_sum - nums[i - (k * 2 + 1)] + nums[i]
        res[i - k] = curr_sum // (k * 2 + 1)

    return res


def getAverages(nums: List[int], k: int) -> List[int]:
    if (k * 2 + 1) > len(nums):
        return [-1] * len(nums)
    if k == 0:
        return nums

    prefix_sum = [nums[0]]
    for i in range(1, len(nums)):
        prefix_sum.append(prefix_sum[i - 1] + nums[i])

    res = [-1] * len(nums)
    for i in range(k, len(nums) - k):
        left, right = i - k, i + k
        curr_sum = prefix_sum[right] - (prefix_sum[left - 1] if left > 0 else 0)
        res[i] = curr_sum // (k * 2 + 1)

    return res
