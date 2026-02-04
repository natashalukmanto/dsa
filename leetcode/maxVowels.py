def maxVowels(s: str, k: int) -> int:
    vowel = ("a", "i", "u", "e", "o")
    num_vowels = max_vowels = 0

    for i in range(k):
        num_vowels += int(s[i] in vowel)
    max_vowels = num_vowels

    for right in range(k, len(s)):
        num_vowels += int(s[right] in vowel)
        num_vowels -= int(s[right - k] in vowel)
        max_vowels = max(max_vowels, num_vowels)

    return max_vowels


def maxVowels(s: str, k: int) -> int:
    vowel = ("a", "i", "u", "e", "o")
    num_vowels = max_vowels = left = 0

    for right in range(len(s)):
        if s[right] in vowel:
            num_vowels += 1

        while right - left + 1 > k:
            if s[left] in vowel:
                num_vowels -= 1
            left += 1

        max_vowels = max(max_vowels, num_vowels)

    return max_vowels
