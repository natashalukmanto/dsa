from collections import Counter

def frequencySort(s: str) -> str:
    freq = Counter(s)

    freq = dict(sorted(freq.items(), key=lambda items: items[1], reverse=True))
    # print(freq)
    res = []
    for key, val in freq.items():
        # print(key, val)
        res.append(val * key)

    return "".join(res)
