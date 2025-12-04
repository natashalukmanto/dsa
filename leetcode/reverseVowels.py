def reverseVowels(self, s: str) -> str:
    vowels = set("aeiouAEIOU")
    left, right = 0, len(s) - 1
    s = list(s)

    while left < right:
        if s[left] in vowels and s[right] in vowels:
            s[right], s[left] = s[left], s[right]
            right -= 1
            left += 1
        else:
            if s[left] not in vowels:
                left += 1
            if s[right] not in vowels:
                right -= 1

    return "".join(s)
