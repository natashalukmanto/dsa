from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    freq_r, freq_m = Counter(ransomNote), Counter(magazine)
    
    for char in set(ransomNote):
        if freq_r[char] > freq_m.get(char, 0): return False
    return True

def canConstruct(ransomNote: str, magazine: str) -> bool:
    freq = Counter(magazine)
    
    for char in ransomNote:
        if freq[char] <= 0: 
            return False

        freq[char] -= 1

    return True

def canConstruct(ransomNote: str, magazine: str) -> bool:
    ransomNote = sorted(ransomNote, reverse=True)
    magazine = sorted(magazine, reverse=True)

    while ransomNote and magazine:
        if ransomNote[-1] == magazine[-1]:
            ransomNote.pop()
            magazine.pop()
        elif magazine[-1] < ransomNote[-1]:
            magazine.pop()
        else:
            return False

    return not ransomNote
