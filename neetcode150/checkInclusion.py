from typing import List

def checkInclusion(self, s1: str, s2: str) -> bool:
    # Check if s1 can be a substring of s2, i.e. the length of s1 and s2
    # if s1 is longer than s2, then s2 does not contain a permutation of s1
    if len(s1) > len(s2): return False

    # Populate the alphabet array
    s1_count, s2_count = [0] * 26, [0] * 26
    for i in range(len(s1)):
        s1_count[ord(s1[i]) - ord('a')] += 1
        s2_count[ord(s2[i]) - ord('a')] += 1

    # check how many matches they have
    matches = 0
    for i in range(26):
        if s1_count[i] == s2_count[i]:
            matches += 1

    # check how many matches are there to start with
    left = 0
    for right in range(len(s1), len(s2)):
        if matches == 26:
            return True
        
        # expanding the window
        index = ord(s2[right]) - ord('a')
        # it was previously a match, but we're about to change it
        if s1_count[index] == s2_count[index]: matches -= 1
        s2_count[index] += 1
        # we have found a new match
        if s1_count[index] == s2_count[index]: matches += 1

        # shrinking the window
        index = ord(s2[left]) - ord('a')
        # it was previously a match, but we're about to change it
        if s1_count[index] == s2_count[index]: matches -= 1
        s2_count[index] -= 1
        # we have found a new match
        if s1_count[index] == s2_count[index]: matches += 1

        left += 1

    return matches == 26 # got to check for the last iteration