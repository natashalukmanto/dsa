def angleClock(hour: int, minutes: int) -> float:
    return min(abs(30 * hour - 5.5 * minutes), 360 - abs(30 * hour - 5.5 * minutes))


def angleClock0(self, hour: int, minutes: int) -> float:
    one_minute_angle = 6
    one_hour_angle = 30

    total_minute_angle = minutes * one_minute_angle
    total_hour_angle = (hour % 12 + minutes / 60) * one_hour_angle

    answer = abs(total_minute_angle - total_hour_angle)
    return min(answer, 360 - answer)
