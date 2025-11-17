def mergeAlternately(word1: str, word2: str) -> str:
    len_word1, len_word2 = len(word1), len(word2)
    pointer1, pointer2 = 0, 0

    res = []
    while pointer1 < len_word1 or pointer2 < len_word2:
        if pointer1 < len_word1:
            res.append(word1[pointer1])
            pointer1 += 1
        if pointer2 < len_word2:
            res.append(word2[pointer2])
            pointer2 += 1

    return "".join(res)


def mergeAlternately(word1: str, word2: str) -> str:
    result = []

    n = max(len(word1), len(word2))
    for i in range(n):
        if i < len(word1):
            result.append(word1[i])
        if i < len(word2):
            result.append(word2[i])

    return "".join(result)


def mergeAlternately(word1: str, word2: str) -> str:
    pointer1, pointer2 = 0, 0
    word1, word2 = list(word1), list(word2)

    res = []
    while pointer1 < len(word1) and pointer2 < len(word2):
        res.append(word1[pointer1])
        res.append(word2[pointer2])
        pointer1 += 1
        pointer2 += 1

    while pointer1 < len(word1):
        res.append(word1[pointer1])
        pointer1 += 1

    while pointer2 < len(word2):
        res.append(word2[pointer2])
        pointer2 += 1

    return "".join(res)
