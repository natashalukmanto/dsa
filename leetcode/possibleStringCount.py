def possibleStringCount(word: str) -> int:
    # "aaaa" -> "aaaa", "aaa", "aa", "a"
    # "abbcccc" -> "abbcccc",

    index, res = 0, 1
    while index < len(word) - 1:
        if word[index] == word[index + 1]:
            res += 1
        index += 1
    return res
