import string

def decoding(s: str) -> str:
    result = []
    i = 0
    while i < len(s):
        count = 0
        while i < len(s) and s[i] in string.digits:
            count = count * 10 + int(s[i])
            i += 1
        if i < len(s):
            result.append(s[i] * count)
            i += 1
    return "".join(result)

def encoding(s: str) -> str:
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        result.append(str(count) + s[i])
        i += 1
    return "".join(result)