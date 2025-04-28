def lengthOfLongestSubstring(s: str) -> int:
    max_length = 0
    left, right = 0, 0
    set_s = set()

    while right < len(s):
        while s[right] in set_s:
            set_s.remove(s[left])
            left += 1
        set_s.add(s[right])
        max_length = max(max_length, len(set_s))
        right += 1

    return max_length


    """
    z   x   y   z   x   y   z
    ^
    """

