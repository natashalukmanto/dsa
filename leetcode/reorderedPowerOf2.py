from collections import Counter

def reorderedPowerOf2(n: int) -> bool:
    n = list(str(n))
    n.sort()

    for i in range(30):
        x = list(str((1 << i)))
        x.sort()
        if x == n:
            return True

    return False


def reorderedPowerOf2(n: int) -> bool:
    count = Counter(str(n))

    for i in range(30):
        if count == Counter(str(1 << i)):
            return True

    return False
