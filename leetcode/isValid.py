def isValid(self, s: str) -> bool:
    parentheses = {"(": ")", "[": "]", "{": "}"}
    stack = []

    for char in s:
        if char in parentheses:
            stack.append(char)
        elif not stack or parentheses[stack.pop()] != char:
            return False

    return not stack


def isValid(self, s: str) -> bool:
    parentheses = {"(": ")", "[": "]", "{": "}"}
    stack = []

    for char in s:
        if char in parentheses:
            stack.append(char)
        elif not stack or parentheses[stack.pop()] != char:
            return False

    return not stack
