from collections import List


def findMaxLength(self, nums: List[int]) -> int:
    count = {0: -1}
    max_len = bal = 0

    for i, x in enumerate(nums):
        bal += 1 if x == 1 else -1

        if bal in count:
            max_len = max(max_len, i - count[bal])
        else:
            count[bal] = i

    return max_len
