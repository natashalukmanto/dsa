import functools, string

def convert_base0(num_as_string: str, b1: int, b2: int) -> str:
    # num_as_string: a number (b1)
    # b1: original base
    # b2: destination base
    
    # Edge case 1: num_as_string is 0 -> returns 0 in any other bases
    if num_as_string == "0": return "0"
    
    # Edge case 2: handling negatives
    is_negative = False
    if num_as_string[0] in '-+':
        if num_as_string[0] == '-': is_negative = True
        num_as_string = num_as_string[1:]
    
    # approach: represent num_as_string (base b1) as (base 10)
    #           represent num_as_string (base 10) as (base b2)
    representation_b1 = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    representation_b2 = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    
    # subtask 1: represent num_as_string (base b1) as (base 10)
    num_as_string_base_10 = 0
    for char in num_as_string:
        char = representation_b1[char] if char in representation_b1 else int(char)
        # print(char)
        num_as_string_base_10 = num_as_string_base_10 * b1 + char
        # print(num_as_string_base_10)
    
    # subtask 2: represent num_as_string (base 10) as (base b2)
    num_as_string_base_b2 = []
    while True:
        if num_as_string_base_10 == 0: break
        remainder = num_as_string_base_10 % b2
        num_as_string_base_10 //= b2
        # print("num_as_string_base_10:", num_as_string_base_10, "remainder:", remainder, "\n")
        num_as_string_base_b2.append(representation_b2[remainder]) if remainder in representation_b2 else num_as_string_base_b2.append(str(remainder))
        # print(num_as_string_base_b2)
    # print("Final: ", num_as_string_base_b2)
    
    return "-" + "".join(reversed(num_as_string_base_b2)) if is_negative else "".join(reversed(num_as_string_base_b2))

# print(convert_base0("1234563143", 7, 15))

# Now, let's take a look at the textbook solution
# What really helped me to understand this question is trying to perform base conversion on a piece of paper. Give it a try
# I think that will clear up your confusion.

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
        # num_as_int is a number in base 10 as an integer type
        # Represent num_as_int as (base base).
        def construct_from_base(num_as_int, base):
            return ('' if num_as_int == 0 else
                    # string.hexdigits is the string '0123456789abcdefABCDEF'. Visit: https://docs.python.org/3/library/string.html#string.hexdigits
                    construct_from_base(num_as_int // base, base) + string.hexdigits[num_as_int % base].upper())
        # print(construct_from_base(1007, 13))
        is_negative = num_as_string[0] == '-'
        # This makes the number respresentation in base 10 
        num_as_int = functools.reduce(
            lambda running_sum, c: running_sum * b1 + string.hexdigits.index(c.lower()),
            # Take your time to understand this line above
            # Why does it uses .index? Because .index gives you back an int type, therefore you don't need to do int(c), I thought it was very clever
            # '0123456789'.upper() is just itself, '0123456789'
            num_as_string[is_negative:],
            0
        )
        return ('-' if is_negative else '') + ('0' if num_as_int == 0 else construct_from_base(num_as_int, b2))
    
# print(convert_base("1234563143", 7, 15))
