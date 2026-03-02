def isIsomorphic(s: str, t: str) -> bool:
    sdic, tdic = {}, {}

    for i in range(len(s)):
        if (s[i] in sdic and sdic[s[i]] != t[i]) or (
            t[i] in tdic and tdic[t[i]] != s[i]
        ):
            return False
        sdic[s[i]] = t[i]
        tdic[t[i]] = s[i]

    return True
