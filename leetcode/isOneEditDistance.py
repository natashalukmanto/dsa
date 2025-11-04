from collections import Counter

def isOneEditDistance(self, s: str, t: str) -> bool:
    if len(s) > len(t):
        return self.isOneEditDistance(t, s)
    
    if len(t) - len(s) > 1:
        return False
    
    for i in range(len(s)):
        if s[i] != t[i]:
            if len(s) == len(t):
                return s[i+1:] == t[i+1:]
            else:
                return s[i:] == t[i+1:]
        
    return s != t

def isOneEditDistance0(s: str, t: str) -> bool:
    if s == t or abs(len(s) - len(t)) > 1: return False
    
    pointer_s, pointer_t, tolerance = 0, 0, 1

    while pointer_s < len(s) and pointer_t < len(t):
        if s[pointer_s] == t[pointer_t]:
            pointer_s += 1
            pointer_t += 1
        else:
            if len(t) > len(s): # insert something to s
                pointer_t += 1
            elif len(s) > len(t): # delete something in s
                pointer_s += 1
            else: # replace something in s
                pointer_s += 1
                pointer_t += 1
            tolerance -= 1
        if tolerance == 0:
            return s[pointer_s:] == t[pointer_t:]
        if tolerance < 0:
            return False

    return pointer_s == len(s) or pointer_t == len(t)
        
print(isOneEditDistance("ab", "acd"))