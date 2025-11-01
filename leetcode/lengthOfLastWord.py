def lengthOfLastWord(s: str) -> int:
    end = len(s) - 1

    while end >= 0 and s[end] == " ":
        end -= 1

    start = end
    while start >= 0 and s[start] != " ":
        start -= 1

    return end - start


def lengthOfLastWord(s: str) -> int:
    p, length = len(s) - 1, 0

    while p >= 0:
        if s[p] != " ":
            length += 1

        elif length > 0:
            return length
        p -= 1

    return length
