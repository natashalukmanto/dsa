from typing import List


def numberOfSubarrays(nums: List[int], k: int) -> int:
    # prefix_sum = [0, 1, 2, 2, 3, 4]

    # {
    #   0: 1,
    #   1: 1,
    #   2: 2,
    #   3: 1,
    #   4: 1
    # }

    count = {0: 1}
    answer = curr = 0

    for num in nums:
        curr += num % 2
        answer += count.get(curr - k, 0)
        count[curr] = count.get(curr, 0) + 1

    return answer
