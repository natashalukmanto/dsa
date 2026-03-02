from collections import Counter

def closeStrings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False

    word1_counter, word2_counter = Counter(word1), Counter(word2)

    return sorted(word1_counter.values()) == sorted(word2_counter.values()) and set(
        word1_counter
    ) == set(word2_counter)
