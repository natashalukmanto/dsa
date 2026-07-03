from collections import List


def numRescueBoats(people: List[int], limit: int) -> int:
    people.sort()
    left, right = 0, len(people) - 1
    num_boats = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        num_boats += 1
        right -= 1

    return num_boats
