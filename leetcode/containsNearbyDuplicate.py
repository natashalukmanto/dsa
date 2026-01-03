from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    window = set()

    for i in range(len(nums)):
        if i > k:
            window.remove(nums[i - k - 1])

        # print(nums[i], window)

        if nums[i] in window:
            return True

        window.add(nums[i])

        # print(nums[i])

    return False
