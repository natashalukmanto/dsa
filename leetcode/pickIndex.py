import bisect, random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.cumulative = []
        cumulative_sum = 0
        for num in w:
            cumulative_sum += num
            self.cumulative.append(cumulative_sum)

    def pickIndex(self) -> int:
        val = random.randint(0, self.cumulative[-1] - 1)
        return bisect.bisect_right(self.cumulative, val)


# class Solution:

#     def __init__(self, w: List[int]):
#         self.w = w
#         self.sum_w = sum(self.w)
#         self.probability = [self.w[0] / self.sum_w]

#         for i in range(1, len(self.w)):
#             self.probability.append(self.probability[i - 1] + (self.w[i] / self.sum_w))

#     def pickIndex(self) -> int:
#         value, index = random.random(), 0
#         for i in range(len(self.probability)):
#             if self.probability[i] > value:
#                 index = i
#                 break
#         return index
