import string

def is_palindrome(s: str) -> bool:
    s = s.translate(str.maketrans('', '', string.punctuation)).lower().replace(" ", "")
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]: return False 
        left += 1
        right -= 1
    return True