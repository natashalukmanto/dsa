from typing import List

def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, current_sum = 0, sum(nums[:k])
        max_sum = current_sum
        # print(current_sum)

        for right in range(left + k, len(nums)):
            current_sum = current_sum - nums[left] + nums[right]
            # print(current_sum)
            max_sum = max(max_sum, current_sum)
            left += 1
            # print(left, right, max_sum)
        
        return max_sum / k