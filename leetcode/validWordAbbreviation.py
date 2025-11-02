from collections import deque


def validWordAbbreviation(self, word: str, abbr: str) -> bool:
    if len(abbr) > len(word):
        return False

    word_pointer, abbr_pointer, queue = 0, 0, deque()

    while abbr_pointer < len(abbr):
        if abbr[abbr_pointer].isdigit():
            digit = ""
            while abbr_pointer < len(abbr) and abbr[abbr_pointer].isdigit():
                digit += abbr[abbr_pointer]
                abbr_pointer += 1
            queue.append(digit)
        else:
            queue.append(abbr[abbr_pointer])
            abbr_pointer += 1
    print(list(queue))

    while word_pointer < len(word):
        if queue:
            val = queue.popleft()
            if val[0] == "0":
                return False
            if val.isdigit():
                if int(val) > len(word) - word_pointer:
                    return False
                else:
                    word_pointer += int(val)
            else:
                if val != word[word_pointer]:
                    return False
                word_pointer += 1
        else:
            return False

    return not queue and word_pointer == len(word)


def validWordAbbreviation(self, word: str, abbr: str) -> bool:
    if len(abbr) > len(word):
        return False

    word_pointer, abbr_pointer = 0, 0

    while word_pointer < len(word) and abbr_pointer < len(abbr):
        ch = abbr[abbr_pointer]
        if ch.isdigit():
            if ch == "0":
                return False

            val = 0
            while abbr_pointer < len(abbr) and abbr[abbr_pointer].isdigit():
                val = val * 10 + int(abbr[abbr_pointer])
                abbr_pointer += 1

            word_pointer += val

            if word_pointer > len(word):
                return False

        else:
            if word[word_pointer] != abbr[abbr_pointer]:
                return False

            word_pointer += 1
            abbr_pointer += 1

    return word_pointer == len(word) and abbr_pointer == len(abbr)
