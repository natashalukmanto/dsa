def minRemoveToMakeValid0(s: str) -> str:
    res = ""

    # going forward
    points = 0  # +1 for '(' and -1 for ')'
    for i in range(len(s)):
        if s[i] != "(" and s[i] != ")":
            res += s[i]
            continue

        if s[i] == ")":
            points -= 1
        elif s[i] == "(":
            points += 1

        if points < 0:
            points = 0
            continue
        else:
            res += s[i]

    ans = ""
    # going backward
    points = 0  # -1 for '(' and +1 for ')'
    for i in reversed(range(len(res))):
        if res[i] != "(" and res[i] != ")":
            ans = res[i] + ans
            continue

        if res[i] == ")":
            points += 1
        elif res[i] == "(":
            points -= 1

        if points < 0:
            points = 0
            continue
        else:
            ans = res[i] + ans

    return ans

def minRemoveToMakeValidStack(s: str) -> str:
        s = list(s)
        stack = []

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        
        while stack:
            s[stack.pop()] = ''
        
        return ''.join(s)


def minRemoveToMakeValid(s: str) -> str:
        
        def removeInvalidParentheses(string: str, open_symbol: str, close_symbol: str) -> str:
            sb = []

            balance = 0
            for c in string:
                if c == open_symbol:
                    balance += 1
                elif c == close_symbol:
                    if balance == 0:
                        continue
                    balance -= 1
                sb.append(c)
            return "".join(sb)
        
        s = removeInvalidParentheses(s, '(', ')')
        # print(s)
        s = removeInvalidParentheses(s[::-1], ')', '(')
        # print(s)

        return s[::-1]
