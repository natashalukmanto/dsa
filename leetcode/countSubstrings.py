def countSubstrings(s: str) -> int:
    def max_palindromes(left, right):
        count = 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

        return count

    res = 0
    for i in range(len(s)):
        res += max_palindromes(i, i)
        res += max_palindromes(i, i + 1)

    return res
