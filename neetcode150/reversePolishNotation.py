def evalRPN(tokens: list) -> int:
    stack = []

    for token in tokens:
        if token == '+':
            stack.append(stack.pop() + stack.pop())
        elif token == '*':
            stack.append(stack.pop() *stack.pop())
        elif token == '-':
            number2 = stack.pop()
            number1 = stack.pop()
            stack.append(number1 - number2)
        elif token == '/':
            number2 = stack.pop()
            number1 = stack.pop()
            stack.append(int(number1 / number2))
        else:
            stack.append(int(token))
    
    return stack[0]