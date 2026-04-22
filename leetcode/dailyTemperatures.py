from typing import List


def dailyTemperatures0(self, temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    stack = []

    for i, temperature in enumerate(temperatures):
        while stack and stack[-1][1] < temperature:
            val = stack.pop()
            res[val[0]] = i - val[0]

        stack.append((i, temperature))

    return res


def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    hottest = 0

    for curr_day in range(len(temperatures) - 1, -1, -1):
        curr_temp = temperatures[curr_day]

        if curr_temp >= hottest:
            hottest = temperatures[curr_day]
            continue

        days = 1
        while curr_temp >= temperatures[curr_day + days]:
            days += res[curr_day + days]
        res[curr_day] = days

    return res
