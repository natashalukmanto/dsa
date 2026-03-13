from typing import List
from collections import deque


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        The result is undefined if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        The result is undefined if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """

# DFS
def depthSum(self, nestedList: List[NestedInteger]) -> int:
    def unpackList(nestedList: List[NestedInteger], curr_sum: int, depth: int) -> int:
        for item in nestedList:
            if item.isInteger():
                curr_sum += depth * item.getInteger()
            else:
                curr_sum += unpackList(item.getList(), 0, depth + 1)
        return curr_sum

    res = unpackList(nestedList, 0, 1)
    return res

# BFS
def depthSum(self, nestedList: List[NestedInteger]) -> int:
    queue = deque(nestedList)

    depth, res = 1, 0

    while len(queue) > 0:
        for _ in range(len(queue)):
            item = queue.pop()
            if item.isInteger():
                res += item.getInteger() * depth
            else:
                queue.extendleft(item.getList())
        depth += 1

    return res
