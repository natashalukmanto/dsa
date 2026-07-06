from collections import List


def longestCommonPrefix(arr1: List[int], arr2: List[int]) -> int:
    possible_prefix_arr1 = set()

    for num in arr1:
        s = str(num)
        possible_prefix_arr1.update(int(s[:i]) for i in range(1, len(s) + 1))

    max_len = 0
    for num in arr2:
        s = str(num)
        for i in range(1, len(s) + 1):
            if int(s[:i]) in possible_prefix_arr1:
                max_len = max(max_len, i)

    return max_len
