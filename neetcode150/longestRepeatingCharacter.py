from typing import List

def characterReplacement(self, s: str, k: int) -> int:
    substring_max_freq, longest_substring, left = 0, 0, 0
    substring_freq_count = {}

    for right in range(len(s)):
        substring_freq_count[s[right]] = 1 + substring_freq_count.get(s[right], 0)
        substring_max_freq = max(substring_max_freq, substring_freq_count[s[right]])

        while (right - left + 1) - substring_max_freq > k:
            substring_freq_count[s[left]] -= 1
            left += 1
        
        longest_substring = max(longest_substring, right - left + 1)
    
    return longest_substring