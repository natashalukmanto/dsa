from collections import Counter, defaultdict


def areOccurrencesEqual(self, s: str) -> bool:
    return len(set(Counter(s).values())) == 1


def areOccurrencesEqual(s: str) -> bool:
    dictionary = {}

    for char in s:
        dictionary[char] = dictionary.get(char, 0) + 1

    for val in dictionary.values():
        if dictionary[s[0]] != val:
            return False
    return True


def areOccurrencesEqual(self, s: str) -> bool:
    dictionary = defaultdict(int)
    for c in s:
        dictionary[c] += 1

    frequencies = dictionary.values()
    return len(set(frequencies)) == 1
