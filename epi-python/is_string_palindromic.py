# pretty straightforward, unlike the leetcode problem, this problem doesn't specify that there's , or . so I just assume we don't care abt that.

def is_palindromic(s: str) -> bool:
    return s[::-1] == s