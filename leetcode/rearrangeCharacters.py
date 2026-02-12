from collections import Counter

def rearrangeCharacters(s: str, target: str) -> int:
    count_target = Counter(target)
    count_s = Counter(s)

    return min(
        list(count_s.get(char, 0) // count_target.get(char, 0) for char in set(target))
    )
