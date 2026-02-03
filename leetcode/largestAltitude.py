from typing import List


def largestAltitude(self, gain: List[int]) -> int:
    prefix_sum = [0]
    for num in gain:
        prefix_sum.append(prefix_sum[-1] + num)

    return max(prefix_sum)
