import itertools


# using stack
def backspaceCompare0(self, s: str, t: str) -> bool:
    stack_s, stack_t = [], []

    # s is the longer one
    if len(s) < len(t):
        s, t = t, s

    for i in range(len(t)):
        if s[i] != "#":
            stack_s.append(s[i])
        elif stack_s:
            stack_s.pop()

        if t[i] != "#":
            stack_t.append(t[i])
        elif stack_t:
            stack_t.pop()

    if len(s) > len(t):
        for i in range(len(t), len(s)):
            if s[i] != "#":
                stack_s.append(s[i])
            elif stack_s:
                stack_s.pop()

    # print(stack_s, stack_t)
    return stack_s == stack_t


# O(1) space
def backspaceCompare(s: str, t: str) -> bool:
    def F(S):
        skip = 0
        for char in reversed(S):
            if char == "#":
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield char

    return all(x == y for x, y in itertools.zip_longest(F(s), F(t)))
