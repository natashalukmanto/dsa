def reverse_words(s):
    # Reverses the whole string
    def reverse(start, finish):
        while start < finish:
            s[start], s[finish] = s[finish], s[start]
            start += 1
            finish -= 1
    reverse(0, len(s) - 1)
    
    # Reverses each word
    start = 0
    finish = start
    while finish < len(s):
        if s[finish] == ' ':
            reverse(start, finish - 1)
            start = finish + 1
            finish = start
        else:
            finish += 1
    
    reverse(start, finish - 1)
    
    return s