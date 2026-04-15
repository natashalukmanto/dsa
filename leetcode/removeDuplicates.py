def removeDuplicates(s: str) -> str:
    stack = []

    for char in s:
        stack.pop() if stack and char == stack[-1] else stack.append(char)

    return "".join(stack)
