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

def frequencySort(s: str) -> str:
    freq = Counter(s)
    max_freq = max(freq.values())

    buckets = [[] for _ in range(max_freq+1)]
    for key, val in freq.items():
        buckets[val-1].append(key)

    res = []
    for i in reversed(range(len(buckets))):
        for char in buckets[i]:
            res.append(char * (i+1))
        
    return "".join(res)