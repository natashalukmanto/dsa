import functools

def roman_to_integer(s: str) -> int:
    roman_numerals_map = {"I": 1, "V": 5,  "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    
    return functools.reduce(
        lambda x, i: x + (roman_numerals_map[s[i]] if roman_numerals_map[s[i]] >= roman_numerals_map[s[i + 1]] else -roman_numerals_map[s[i]]), 
        range(len(s) - 1), 
        roman_numerals_map[s[-1]]
    ) 
    
    # if s in roman_numerals_map: return roman_numerals_map[s]
    
    # sum, i = 0, 0
    # while i  < len(s):
    #     if i + 1 < len(s) and roman_numerals_map[s[i]] < roman_numerals_map[s[i + 1]]:
    #         sum -= roman_numerals_map[s[i]]
    #     else:
    #         sum += roman_numerals_map[s[i]]
    #     i += 1
        
    # return sum