def look_and_say(n: int) -> str:
    def next_number(res):
        i, s = 0, ""
        while i < len(res):
            count = 1
            while i + 1 < len(res) and res[i] == res[i + 1]:
                i += 1
                count += 1
            s += str(count) + res[i]
            i += 1
        return s
    
    res = "1"
    for _ in range(1, n):
        res = next_number(res)
    return res