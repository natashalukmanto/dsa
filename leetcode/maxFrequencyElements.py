from typing import List


def maxFrequencyElements(nums: List[int]) -> int:
    dic = {}
    max_freq = 0

    for num in nums:
        dic[num] = dic.get(num, 0) + 1
        max_freq = max(max_freq, dic[num])

    res = 0
    for key, value in dic.items():
        if value == max_freq:
            res += value

    return res


def maxFrequencyElements(nums: List[int]) -> int:
    dic = {}
    max_frequency = res = 0

    for num in nums:
        dic[num] = dic.get(num, 0) + 1
        frequency = dic[num]
        # print(dic)

        if frequency > max_frequency:
            max_frequency = frequency
            res = frequency
        elif max_frequency == frequency:
            res += frequency

    return res
