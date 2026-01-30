def reverseWords(s: str) -> str:
    res = s.split(" ")
    for w in range(len(res)):
        nw = ""
        for i in reversed(range(len(res[w]))):
            nw += res[w][i]
        res[w] = nw

    return " ".join(res)


def reverseWords(s: str) -> str:
    return " ".join(s.split()[::-1])[::-1]


def reverseWords(s: str) -> str:
    words = s.split()
    reversed_str = ""
    for word in words:
        reversed_str += word[::-1] + " "
    return reversed_str.strip()
