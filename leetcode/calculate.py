# O(n) space complexity sol
def calculate(s: str) -> int:
    stack = []
    current_num = 0
    operation = '+'
    current_char = ""

    for i in range(len(s)):
        current_char = s[i]

        if current_char.isdigit():
            current_num = current_num * 10 + int(current_char)
        
        if (not current_char.isdigit() and not current_char.isspace()) or i == len(s) - 1:
            if operation == '+':
                stack.append(current_num)
            elif operation == '-':
                stack.append(-current_num)
            elif operation == '*':
                stackTop = stack.pop()
                stack.append(stackTop * current_num)
            else:
                stackTop = stack.pop()
                stack.append(int(stackTop / current_num))
            
            operation = current_char
            current_num = 0
        
        res = 0

    while stack:
        res += stack.pop()
    
    return res


# O(1) space complexity sol
def calculate(s: str) -> int:
    last_num = current_num = res = 0
    operation = "+"
    current_char = ""

    for i in range(len(s)):
        current_char = s[i]

        if current_char.isdigit():
            current_num = current_num * 10 + int(current_char)

        if (not current_char.isdigit() and not current_char.isspace()) or i == len(
            s
        ) - 1:
            if operation == "+" or operation == "-":
                res += last_num
                last_num = current_num if operation == "+" else -current_num
            elif operation == "*":
                last_num = last_num * current_num
            else:
                last_num = int(last_num / current_num)

            operation = current_char
            current_num = 0

    return res + last_num
