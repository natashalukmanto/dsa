from typing import List
def search(nums: List[int], target: int) -> int:
    # The idea is a modified binary search.

    # First let's find out where is the rotation.
    front_index, back_index = 0, len(nums) - 1
    while front_index < back_index:
        # The formula should be this way to avoid interger overflow.
        middle = front_index + (back_index - front_index) // 2
        # A non-rotated sorted array should look like
        # [0, 1, 2, 4, 5, 6, 7]
        # Logically, the 1st element < middle element < back element
        # Hence, the if statement
        if nums[middle] > nums[back_index]:
            front_index = middle + 1
        else:
            back_index = middle
        # At this point, the middle should be your index for the start of rotation.

    # Now, we make use of the starting point of rotation
    # by making our search field smaller
    start = front_index
    front_index, back_index = 0, len(nums) - 1
    if target >= nums[start] and target <= nums[back_index]:
        front_index = start
    else:
        back_index = start

    # This is your typical binary search
    while front_index <= back_index:
        middle = front_index + (back_index - front_index) // 2
        if nums[middle] == target:
            return middle
        elif target > nums[middle]:
            front_index = middle + 1
        else:
            back_index = middle - 1
    
    return -1

def search2(nums: List[int], target: int) -> int:
    # First, let's find the pivot
    left, right = 0, len(nums) - 1

    while left <= right:
        middle = left + (right - left) // 2
        if middle > 0 and nums[middle - 1] >= nums[middle]:
            left = middle
        if middle < len(nums) - 1 and nums[middle + 1] < nums[middle]:
            left = middle + 1
        if nums[middle] > nums[-1]:
            left = middle + 1
        else:
            right = middle - 1

    start = left

    # Next, let's narrow down our search field by figuring out
    # which part of the array should we do Binary Search 
    left, right = 0, len(nums) - 1

    if target > nums[right]:
        right = start - 1
    else:
        left = start

    # Finally, let's do binary search on the area we have decided
    while left <= right:
        middle = left + (right - left) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    
    return -1
