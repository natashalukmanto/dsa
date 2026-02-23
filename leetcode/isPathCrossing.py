def isPathCrossing(path: str) -> bool:
    x, y = 0, 0
    coordinates = set()
    coordinates.add((0, 0))

    for char in path:
        if char == "N":
            x += 1
        elif char == "S":
            x -= 1
        elif char == "E":
            y += 1
        else:
            y -= 1

        if (x, y) in coordinates:
            return True

        coordinates.add((x, y))

    return False
