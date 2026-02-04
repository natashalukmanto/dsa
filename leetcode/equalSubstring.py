def equalSubstring(s: str, t: str, maxCost: int) -> int:
    max_length = left = cost = 0

    for right in range(len(s)):
        if s[right] != t[right]:
            cost += abs(ord(s[right]) - ord(t[right]))

        while cost > maxCost:
            cost -= abs(ord(s[left]) - ord(t[left]))
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length
