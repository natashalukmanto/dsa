class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right: 
            current_sum = numbers[left] + numbers[right] # is faster bcs you don't need to always recalculate the current_sum
            if current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
            else: # found the pair! numbers[left] + numbers[right] == target
                return [left + 1, right + 1]
        # left, right = 0, len(numbers) - 1

        # while left < right:
        #     if numbers[left] + numbers[right] == target:
        #         return [left + 1, right + 1]
        #     elif numbers[left] + numbers[right] < target:
        #         left += 1
        #     else:
        #         right -= 1
