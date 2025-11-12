def isSubsequence(s: str, t: str) -> bool:
    pointer_s, pointer_t = 0, 0

    while pointer_s < len(s) and pointer_t < len(t):
        if s[pointer_s] == t[pointer_t]:
            pointer_s += 1
        pointer_t += 1
    
    return pointer_s == len(s)

def isSubsequence(s: str, t: str) -> bool:
    LEFT_BOUND, RIGHT_BOUND = len(s), len(t)
    
    def helper(left_index, right_index):
        if left_index == LEFT_BOUND:
            return True
        elif right_index == RIGHT_BOUND:
            return False
        elif s[left_index] == t[right_index]:
            return helper(left_index + 1, right_index + 1)
        else:
            return helper(left_index, right_index + 1)
    
    return helper(0, 0)

