from typing import List

def compress(chars: List[str]) -> int:
    i, res, n = 0, 0, len(chars)

    while i < n:
        group_len = 0
        while (i + group_len < n) and chars[i + group_len] == chars[i]:
            group_len += 1
        chars[res] = chars[i]
        res += 1
        if group_len > 1:
            length = len(str(group_len))
            chars[res : res + length] = list(str(group_len))
            res += length
        i += group_len

    return res
