def toGoatLatin(sentence: str) -> str:
    sentence = sentence.split()
    for i, word in enumerate(sentence):
        sentence[i] = list(word)

    vowels = set(("a", "e", "i", "o", "u"))
    # print(sentence)
    for i in range(len(sentence)):
        if sentence[i][0].lower() in vowels:
            sentence[i].append("ma")
        else:
            sentence[i].append(sentence[i][0])
            sentence[i].append("ma")
            sentence[i].pop(0)
        sentence[i].append("a" * (i + 1))

    return " ".join("".join(word) for word in sentence)
