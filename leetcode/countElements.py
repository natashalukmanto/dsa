from typing import List

def countElements(arr: List[int]) -> int:
    arr_set = set(arr)
    res = 0
    
    for num in arr:
        if num + 1 in arr_set:
            res += 1
    
    return res