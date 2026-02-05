def repeatedCharacter(s: str) -> str:
    chars = set()

    for char in s:
        if char not in chars:
            chars.add(char)
        else:
            return char


def repeatedCharacter(s: str) -> str:
    seen = set()

    for char in s:
        if char in seen:
            return char
        seen.add(char)
