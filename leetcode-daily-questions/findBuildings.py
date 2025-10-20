from typing import List


def findBuildings(heights: List[int]) -> List[int]:
    max_height_so_far, res = 0, []

    for i in reversed(range(len(heights))):
        if heights[i] > max_height_so_far:
            res.append(i)
        max_height_so_far = max(max_height_so_far, heights[i])

    return res[::-1]


def findBuildings(heights: List[int]) -> List[int]:
    stack = []

    for i, height in enumerate(heights):
        while stack and height >= heights[stack[-1]]:
            stack.pop()
        stack.append(i)

    return stack
