import functools

def rabin_karp(t: str, s: str) -> int:
    # t = text, s = substring
    # return -1 if s not in t else t.index(s) is faster though
    if len(s) > len(t): return -1
    
    t_hash = functools.reduce(lambda hash, char: hash * 26 + ord(char), t[:len(s)], 0)
    s_hash = functools.reduce(lambda hash, char: hash * 26 + ord(char), s, 0)
    
    for i in range(len(s), len(t)):
        if t_hash == s_hash and t[i - len(s):i] == s:
            return i - len(s)
        
        t_hash -= ord(t[i - len(s)]) * (26 ** max(len(s) - 1, 0))
        t_hash = t_hash * 26 + ord(t[i])
        
    if t_hash == s_hash and t[-len(s):] == s:
        return len(t) - len(s)
        
    return -1

