def lengthOfLongestSubstring(s: str) -> int:
    left = max_len = 0
    s_set = set()

    for right in range(len(s)):
        while s[right] in s_set:
            s_set.remove(s[left])
            left += 1

        s_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len
