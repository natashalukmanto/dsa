def strStr(haystack: str, needle: str) -> int:
    for window_start in range(len(haystack) - len(needle) + 1):
        for i in range(len(needle)):
            if needle[i] != haystack[window_start + i]:
                break
            if i == len(needle) - 1:
                return window_start
    return -1
