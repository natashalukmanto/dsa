from collections import List


def totalFruit(fruits: List[int]) -> int:
    basket = {}
    left = max_fruits = 0

    for right in range(len(fruits)):
        basket[fruits[right]] = basket.get(fruits[right], 0) + 1

        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            left += 1

        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits


def totalFruit(fruits: List[int]) -> int:
    basket = {}
    left = 0

    for right in range(len(fruits)):
        basket[fruits[right]] = basket.get(fruits[right], 0) + 1

        if len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            left += 1

    return right - left + 1
