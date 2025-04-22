def dailyTemperatures(self, temperatures: list) -> list:
    res = [0 for _ in range(len(temperatures))]
    stack = [] # stores (temperature, index)

    for index, temperature in enumerate(temperatures):
        while stack and stack[-1][0] < temperature:
            popped_value = stack.pop()
            res[popped_value[1]] = index - popped_value[1]
        stack.append((temperature, index))
    return res
    