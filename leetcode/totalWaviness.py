def totalWaviness(self, num1: int, num2: int) -> int:
    def waviness(n: int):
        s = str(n)
        return sum((a < b > c) or (a > b < c) for a, b, c in zip(s, s[1:], s[2:]))

    return sum(waviness(n) for n in range(num1, num2 + 1))

def totalWaviness0(num1: int, num2: int) -> int:
    waviness = 0
    for num in range(num1, num2 + 1):
        # building the array of digits
        num_array = []
        while num:
            num_array.append(num % 10)
            num //= 10
        num_array = num_array[::-1]

        # if len(num) < 3, waviness is 0
        if len(num_array) < 3:
            continue

        # checking if it's a valley/peak
        for i in range(1, len(num_array) - 1):
            if (num_array[i - 1] < num_array[i] > num_array[i + 1]) or (
                num_array[i - 1] > num_array[i] < num_array[i + 1]
            ):
                waviness += 1

        # print(num_array)

    return waviness
