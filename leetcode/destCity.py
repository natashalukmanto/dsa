from typing import List


def destCity(paths: List[List[str]]) -> str:
    outgoing_city = set()

    for path in paths:
        outgoing_city.add(path[0])

    for path in paths:
        if path[1] not in outgoing_city:
            return path[1]
