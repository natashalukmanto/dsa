from typing import List
from functools import cmp_to_key


def largestNumber(nums: List[int]) -> str:
    res = []

    def custom_compare(int1: int, int2: int) -> int:
        int1_str, int2_str = str(int1) + str(int2), str(int2) + str(int1)
        # -1 for int1 first before int2;
        if (int1_str) > (int2_str):
            return -1
        elif (int1_str) < (int2_str):
            return 1
        else:
            return 0

    res = sorted(nums, key=cmp_to_key(custom_compare))
    return "".join(map(str, res)) if res[0] != 0 else "0"


"""
Python compares strings lexicographically, character by character (using Unicode code points). The first position where they differ decides: the one with the larger character there is greater.

If all characters are identical up to the length of the shorter, then the shorter string is considered smaller (so the longer string is greater) because the shorter is a prefix of the longer.
"""
