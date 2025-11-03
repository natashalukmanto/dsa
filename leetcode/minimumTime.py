from typing import List
from collections import defaultdict
from functools import cache


def minimumTime0(n: int, relations: List[List[int]], time: List[int]) -> int:
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


def minimumTime(n: int, relations: List[List[int]], time: List[int]) -> int:
    relations_graph = defaultdict(list)

    for prev_course, next_course in relations:
        relations_graph[next_course - 1].append(prev_course - 1)

    memo = {}

    def dfs(course: int) -> int:
        if course in memo:
            return memo[course]

        if not relations_graph[course]:
            memo[course] = time[course]
            return memo[course]

        best = 0
        for neighbor in relations_graph[course]:
            best = max(best, dfs(neighbor))
        memo[course] = time[course] + best

        return memo[course]

    res = 0
    for i in range(n):
        res = max(res, dfs(i))
    return res
