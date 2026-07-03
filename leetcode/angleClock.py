def angleClock(hour: int, minutes: int) -> float:
    return min(abs(30 * hour - 5.5 * minutes), 360 - abs(30 * hour - 5.5 * minutes))
