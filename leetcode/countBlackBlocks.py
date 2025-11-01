from typing import List
from collections import defaultdict


def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
    num_block_affected = defaultdict(int)
    for x, y in coordinates:
        for r, c in ((x, y), (x - 1, y - 1), (x - 1, y), (x, y - 1)):
            if 0 <= r < m - 1 and 0 <= c < n - 1:
                num_block_affected[(r, c)] += 1
    # num_block_affected = {
    # (0, 0): 1,
    # (1, 1): 4,
    # (0, 2): 3
    # }

    # res = [0,2,2,0,0] i.e. how many submatrix have ith black blocks
    ans = [0] * 5
    for count in num_block_affected.values():
        ans[count] += 1

    total_blocks = (m - 1) * (n - 1)
    ans[0] = total_blocks - sum(ans[1:])
    return ans
