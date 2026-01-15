def characterReplacement(s: str, k: int) -> int:
    left = max_len = max_freq = 0
    count = {}

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_freq = max(max_freq, count[s[right]])

        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

    # AABABBA

"""
2nd try:
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = max_freq = max_len = 0
        counter = {}

        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1
            max_freq = max(max_freq, counter[s[right]])

            while (right - left + 1) - max_freq > k:
                counter[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
        
"""