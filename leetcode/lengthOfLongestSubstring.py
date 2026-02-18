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


def lengthOfLongestSubstring(s: str) -> int:
    left = 0
    max_len = 0
    my_set = set()

    for right in range(len(s)):
        while s[right] in my_set:
            my_set.remove(s[left])
            left += 1
        my_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


def lengthOfLongestSubstring(s: str) -> int:
    dic = {}
    left = max_len = 0

    for right in range(len(s)):
        if s[right] in dic:
            left = max(left, dic[s[right]])

        max_len = max(max_len, right - left + 1)
        dic[s[right]] = right + 1

    return max_len
