from typing import List
from collections import defaultdict
from functools import cache


def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
    # building the graph
    graph = defaultdict(list)

    for prev_course, next_course in relations:
        graph[next_course - 1].append(prev_course - 1)

    months = 0

    @cache
    def dfs(course: int):
        if not graph[course]:
            return time[course]

        res = 0
        for neighbor in graph[course]:
            res = max(res, dfs(neighbor))

        return time[course] + res

    for course in range(n):
        months = max(months, dfs(course))

    return months
