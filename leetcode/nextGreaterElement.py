from typing import List


def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    stack = []
    hashmap = {}

    for num2 in nums2:
        while stack and num2 > stack[-1]:
            hashmap[stack.pop()] = num2
        stack.append(num2)

    return [hashmap.get(i, -1) for i in nums1]


def nextGreaterElement0(nums1: List[int], nums2: List[int]) -> List[int]:
    res = [-1] * len(nums1)
    for idx1, num in enumerate(nums1):
        start = nums2.index(num)

        for idx2 in range(start + 1, len(nums2)):
            if nums2[idx2] > num:
                res[idx1] = nums2[idx2]
                break

    return res
