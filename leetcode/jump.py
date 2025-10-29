from typing import List

def jump(self, nums: List[int]) -> int:
    curr_farthest = curr_end = answer = 0

    for i in range(len(nums) - 1):
        curr_farthest = max(curr_farthest, nums[i] + i)

        if i == curr_end:
            curr_end = curr_farthest
            answer += 1

    return answer