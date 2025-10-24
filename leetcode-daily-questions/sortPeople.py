from typing import List


def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
    pairs = list(zip(names, heights))
    pairs.sort(key=lambda p: p[1], reverse=True)

    return [pair[0] for pair in pairs]
