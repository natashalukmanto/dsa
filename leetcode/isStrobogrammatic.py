def isStrobogrammatic(self, num: str) -> bool:
    new_digits = ["0", "1", "", "", "", "", "9", "", "8", "6"]
    res = []

    for n in reversed(num):
        res.append(new_digits[int(n)])

    return num == "".join(res)


def isStrobogrammatic(num: str) -> bool:
    strobogrammatic_nums = {
        "0": "0",
        "1": "1",
        "8": "8",
        "6": "9",
        "9": "6",
    }

    left, right = 0, len(num) - 1

    while left <= right:
        if (
            num[left] not in strobogrammatic_nums
            or strobogrammatic_nums[num[left]] != num[right]
        ):
            return False
        left += 1
        right -= 1
    return True
