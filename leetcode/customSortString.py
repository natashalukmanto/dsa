from collections import Counter


def customSortString(self, order: str, s: str) -> str:
    s_counter = Counter(s)
    res = []

    for char in order:
        if char in s_counter:
            res.append(char * s_counter[char])
            del s_counter[char]

    for char, freq in s_counter.items():
        res.append(char * freq)

    return "".join(res)
