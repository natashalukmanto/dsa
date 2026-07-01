from typing import List

def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    i = 0
    res = []

    def get_words(i: int):
        current_line = []
        curr_length = 0

        while i < len(words) and curr_length + len(words[i]) <= maxWidth:
            current_line.append(words[i])
            curr_length += len(words[i]) + 1
            i += 1

        return current_line

    def create_line(line: List[str], i: int):
        base_length = -1

        for word in line:
            base_length += len(word) + 1

        extra_spaces = maxWidth - base_length

        if len(line) == 1 or i == len(words):
            return " ".join(line) + " " * extra_spaces

        word_count = len(line) - 1
        spaces_between_words = extra_spaces // word_count
        additional_spaces_left = extra_spaces % word_count

        for j in range(additional_spaces_left):
            line[j] += " "

        for j in range(word_count):
            line[j] += " " * spaces_between_words

        return " ".join(line)

    while i < len(words):
        current_line = get_words(i)
        i += len(current_line)
        res.append(create_line(current_line, i))

    return res
