from collections import Counter


def numJewelsInStones(self, jewels: str, stones: str) -> int:
    stones_freq = Counter(stones)
    res = 0

    for jewel in jewels:
        res += stones_freq.get(jewel, 0)

    return res
