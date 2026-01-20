from collections import List


def findRepeatedDnaSequences(s: str) -> List[str]:
    res, my_set = [], set()
    left = 0

    for right in range(10, len(s) + 1):
        # print(s[left:right])
        if s[left:right] in my_set and s[left:right] not in res:
            res.append(s[left:right])
        else:
            my_set.add(s[left:right])
        left += 1

    return res


def findRepeatedDnaSequences(s: str) -> List[str]:
    res, my_set = [], set()
    L, n = 10, len(s)

    for start in range(n - L + 1):
        curr = s[start : start + L]
        if curr in my_set and curr not in res:
            res.append(curr)
        my_set.add(curr)

    return res
