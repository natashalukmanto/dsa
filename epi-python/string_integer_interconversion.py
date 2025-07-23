# The problem specifically said not to use any python functions. So one solution I thought of is to create a dictionary of all the digits we have from 0 to 9. 
# For each digit in x/character in s, we map that digit/character to the correct character/digit. Build up res. Return res
# The textbook solution, I think, is less readable but fancier and shorter. It's good if you have good understanding of advanced python modules like functools
# Still, I think it's worth to study because I think it's impressive to whip that solution in an interview
import functools

def int_to_string0(x: int) -> str:
    is_positive = True
    if x < 0: 
        is_positive = False
        x *= -1
        
    if x == 0: return '0'
    
    # 314 to '314'
    digits = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    res = ''
    while x:
        digit = digits[x % 10]
        res = digit + res
        x //= 10
    return res if is_positive else '-' + res

def string_to_int0(s: str) -> int:
    is_positive = True
    if s[0] == '-':
        is_positive = False
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    res = 0
    for digit in s:
        res = res * 10 + digits[digit] 
    return res if is_positive else res * -1

print(int_to_string0(-134))
print(string_to_int0('-134'))

# Textbook solution

def int_to_string(x: int) -> str:
    is_positive = True
    if x < 0: 
        is_positive = False
        x *= -1
        
    s = []
    
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0: break
    
    return ('' if is_positive else '-') + ''.join(reversed(s))
    
def string_to_int(s: str) -> int:
    return functools.reduce(lambda res, c: res * 10 + (ord(c) - ord('0')), 
                            s[s[0] in '-+':], 0) * (-1 if s[0] == '-' else 1)