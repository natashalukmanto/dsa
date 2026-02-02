def reversePrefix(word: str, ch: str) -> str:
    if ch not in word:
        return word

    # finding the first index
    index = -1
    for i, char in enumerate(word):
        if char == ch:
            index = i
            break
    res = word[index::-1] + word[index + 1 :]

    return res
