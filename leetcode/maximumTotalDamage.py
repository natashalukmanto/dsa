from collections import Counter
from bisect import bisect_left
from typing import List

def maximumTotalDamage(self, power: List[int]) -> int:
    freq = Counter(power)
    vals = sorted(freq.keys())
    dmg = [v * freq[v] for v in vals]

    m = len(vals)
    if m == 0:
        return 0

    dp = [0] * m

    for i in range(m):
        skip = dp[i - 1] if i > 0 else 0

        safe = vals[i] - 2
        j = bisect_left(vals, safe) - 1
        take = dmg[i] + (dp[j] if j >= 0 else 0)

        dp[i] = max(skip, take)

    return dp[-1]
