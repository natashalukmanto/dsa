from collections import Counter

def maxNumberOfBalloons(text: str) -> int:
    alphabets = Counter(text)
    return min(
        list(alphabets.get(c, 0) // Counter("balloon")[c] for c in set("balloon"))
    )
