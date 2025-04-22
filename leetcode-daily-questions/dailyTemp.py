def dailyTemperatures(self, temperatures: list) -> list:
    stack = [] # stack hold the highest temperature seen and its index, i.e. stack = (index, temperature)
    res = [0 for _ in range(len(temperatures))] # [0 0 0 ...]

    #     Index:           0  1  2  3  4  5  6 
    # Ex: temperatures = [30,38,30,36,35,40,28], length = 7
    # stack = [40, 28]
    # res = [1, 4, 1, 2, 1, 0, 0]

    for index, temperature in enumerate(temperatures):
        while stack and temperature > stack[-1][1]:
            val = stack.pop() # stack = (index, temperature)
            res[val[0]] = index - val[0]
        stack.append((index, temperature))
    return res
