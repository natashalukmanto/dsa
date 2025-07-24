# Tried to be fancy this time and learn from my mistakes in 6.2 :D
import functools, string

# This problem is similar to 6.2 Base Conversion, the base conversion is base 26 to base 10
# With that recognized, it's trivial to solve this problem
# With solving 6.2, you should be familiar with how to represent numbers to base 10 or from base 10
def ss_decode_col_id0(col: str) -> int:
    return functools.reduce(
        lambda running_sum, c: running_sum * 26 + (string.ascii_uppercase.index(c.upper()) + 1),
        # string.ascii_uppercase is the string 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. Refer to https://docs.python.org/3/library/string.html
        # I put +1 because A is actually column 1 not column 0. 
        col,
        0)

# The textbook solution is very similar to the above. The only difference is that it uses ord() instead of string.ascii_uppercase
# Honestly they're similar approach with the same logic, I don't think any has a advantage.
def ss_decode_col_id(col: str) -> int:
    return functools.reduce(
        lambda running_sum, c: running_sum * 26 + ord(c) - ord('A') + 1,
        col,
        0)
    
print(ss_decode_col_id("AA"))