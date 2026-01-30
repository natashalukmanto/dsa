def reverseOnlyLetters(s: str) -> str:
    s = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        if not s[left].isalpha():
            left += 1
        if not s[right].isalpha():
            right -= 1
        if s[left].isalpha() and s[right].isalpha():
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    return "".join(s)


def reverseOnlyLetters(s: str) -> str:
    ans = []
    right = len(s) - 1

    for left, char in enumerate(s):
        if char.isalpha():
            while not s[right].isalpha():
                right -= 1
            ans.append(s[right])
            right -= 1
        else:
            ans.append(char)

    return "".join(ans)
