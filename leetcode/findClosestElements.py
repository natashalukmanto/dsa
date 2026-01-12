from typing import List

def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    left, right = 0, len(arr) - 1

    while right - left + 1 != k:
        # if arr[left] is closer to x:
        if abs(arr[left] - x) < abs(arr[right] - x):
            right -= 1
        # if arr[right] is closer to x:
        elif abs(arr[left] - x) > abs(arr[right] - x):
            left += 1
        # tiebreaker
        else:
            if arr[left] < arr[right]:
                right -= 1
            else:
                left += 1

    return arr[left : left + k]

    # left = start = 0
    # operations = float('inf')
    # window_sum = sum(arr[:k])
    # target_sum = sum([x] * k)

    # for right in range(k, len(arr)):
    #     print(window_sum, target_sum)
    #     curr_operations = abs(target_sum - window_sum)
    #     if operations > curr_operations:
    #         #print(operations, curr_operations)
    #         start = left
    #         operations = curr_operations

    #     window_sum -= arr[left]
    #     window_sum += arr[right]
    #     left += 1

    # return arr[start:start+k]
