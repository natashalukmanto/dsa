from collections import List


def decrypt(self, code: List[int], k: int) -> List[int]:
    result = [0] * len(code)

    if k == 0:
        return result

    start, end, window_sum = 1, k, 0

    if k < 0:
        start = len(code) - abs(k)
        end = len(code) - 1

    for i in range(start, end + 1):
        window_sum += code[i]

    for i in range(len(code)):
        result[i] = window_sum
        window_sum -= code[start % len(code)]
        window_sum += code[(end + 1) % len(code)]
        start += 1
        end += 1

    return result
