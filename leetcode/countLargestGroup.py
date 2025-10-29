def countLargestGroup(self, n: int) -> int:
    if n == 0: return 0
    if n == 1: return 1

    digit_sum = {}
    for num in range(1, n + 1):
        _sum = 0
        while num:
            _sum += num % 10
            num //= 10
        if _sum in digit_sum:
            digit_sum[_sum] += 1
        else:
            digit_sum[_sum] = 1

    max_group = max(digit_sum.values())
    return sum(value == max_group for value in digit_sum.values())
