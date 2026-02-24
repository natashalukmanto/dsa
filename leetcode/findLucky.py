from typing import List

def findLucky(arr: List[int]) -> int:
    dic = {}
    res = -1

    for num in arr:
        dic[num] = dic.get(num, 0) + 1

    for key, value in dic.items():
        if key == value and value > res:
            res = value

    return res
