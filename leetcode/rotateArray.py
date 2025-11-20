from typing import List


def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    res = [0] * n

    for i in range(n):
        res[(i + k) % n] = nums[i]

    nums[:] = res


def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n

    start = count = 0
    while count < n:
        current, prev = start, nums[start]
        while True:
            next_index = (current + k) % n
            nums[next_index], prev = prev, nums[next_index]
            current = next_index
            count += 1

            if start == current:
                break
        start += 1


def rotate(nums: List[int], k: int) -> None:
    n = len(nums)
    k %= n

    if k == 0:
        return

    nums[:] = reversed(nums)
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])


def rotate(self, nums: List[int], k: int) -> None:
    k %= len(nums)

    for _ in range(k):
        prev = nums[-1]
        for j in range(len(nums)):
            nums[j], prev = prev, nums[j]
