from typing import List

def triangleType(self, nums: List[int]) -> str:
    if len(set(nums)) == 1: return "equilateral"
    summ = sum(nums)

    for i in range(3):
        if summ - nums[i] <= nums[i]:
            return "none"

    return "scalene" if len(set(nums)) == len(nums) else "isosceles"

'''

Intuition
First, we have to know about the Triangle Inequality Theorem that states for any triangle, the sum of the lengths of any two sides must be greater than the third side (this is illustrated from the Example 2 in the problem description).

Then we intuitively think that there's 4 different answers to this problem:

equilateral if the triangle are of 3 sides with the same length, i.e. the elements in nums are all equal.
none if nums violates the Triangle Inequality Theorem.
scalene if nums did not violate the Triangle Inequality Theorem and the elements in nums are all unique.
isosceles otherwise.
The next thing to do is to formulate how to do the above.

Approach
Step One
First, tackle the easiest problem: if the elements in nums are all equal, then it's an equilateral triangle. We can do this simply with

if len(set(nums)) == 1: return "equilateral"
Step Two
Then, check if nums violates the Triangle Inequality Theorem. If yes, return none. We can check this by using a for loop and subtracting the sum of nums by each element at index i. Then we check if sum-current_element is >= currrent_element.

for i in range(3):
            if summ - nums[i] <= nums[i]:
                return "none"
Step Three
Finally, if it passes the for loop, we know it follows the Triangle Inequality Theorem and therefore we just need to decide whether if we should return scalene or isosceles which can be done by check if the length of nums is equal to length of set(nums).

return "scalene" if len(set(nums)) == len(nums) else "isosceles"
Complexity
Time complexity: O(1). The input array nums is always of size 3. A triangle has exactly 3 sides, so any loop or operation on nums is constant-time.

Space complexity: O(1). We're creating at most one set of 3 elements from set(nums), and storing a few integers. No extra space grows with input.

Code
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if len(set(nums)) == 1: return "equilateral"
        summ = sum(nums)

        for i in range(3):
            if summ - nums[i] <= nums[i]:
                return "none"

        return "scalene" if len(set(nums)) == len(nums) else "isosceles"
'''