from typing import List


# Cleaned up
def maximumUniqueSubarray(self, nums: List[int]) -> int:
    # avoiding recomputation of sums
    # have a set for

    # might TLE
    subarray = set()
    left = curr_sum = max_sum = 0

    for right in range(len(nums)):
        while nums[right] in subarray:
            subarray.remove(nums[left])
            curr_sum -= nums[left]
            left += 1

        subarray.add(nums[right])
        curr_sum += nums[right]

        max_sum = max(max_sum, curr_sum)

    return max_sum


# Initial Try
def maximumUniqueSubarray(self, nums: List[int]) -> int:
    subarray = set()
    left = right = curr_sum = max_sum = 0

    while right < len(nums):
        if nums[right] not in subarray:
            subarray.add(nums[right])
            curr_sum += nums[right]
            right += 1

        else:
            while nums[right] in subarray:
                subarray.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

        max_sum = max(max_sum, curr_sum)

    return max_sum
