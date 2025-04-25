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