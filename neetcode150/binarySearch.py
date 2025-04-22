def search(nums: list, target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = left + (right - left) // 2 # avoid integer overflow
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1
