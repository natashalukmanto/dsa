# LC Daily Question - 1922. Count Good Numbers

"""
This question is a lot of math. 

Objective: A digit string of length `n` is good if:
            - even indices are even
            - odd indices are prime

Let's tackle the even part first.
    - This means the even indices has only 5 types: 0, 2, 4, 6, 8. It can't be 10 because it takes up 2 spots instead of 1.
    - Now think about how many even indices a digit string of length n would have.
        - The answer is (n + 1) / 2. Why? Say you have a digit string of length 3: there's only 2 even indices: 0 and 2. Hence why (n + 1) / 2

Okay, now let's build some intuition for the second part.
    - Similar to the even indices, the odd indices can only hold: 2,3,5,7. If you thought about "why not 9?" it's because 9 is not a prime number and 11 & above takes up two spots.
    - How many odd indices can a digit string of length n have? 
        - Answer is n / 2, why? Because think about it as slots/spots again. If a digit string is of length 3 -> there's only 1 index tha this odd (which is 1).
        - [][][]
        -  0 1 2
        -  E O E (E = even, O = odd)
        
How did the LeetCode's Editorial able to get that formula? This is a familiar concept in permutation. I like to think of it like
    - Imagine a digit string of length 4
    - We have 4 slots that we can fill like so: _ _ _ _
        - On the first slot, we can fill with 5 different integer (as discussed previously), either 0, 2, 4, 6, or 8.
        - Therefore for the first one, we put in 5
        
        - On the second slot, we can fill with 4 different integers, either 2,3,5, or 7.
        - So put in 4 in the second slot
        
        - This continues until: 
        - _ _ _ _
        - 5 4 5 4 = 5 * 4 * 5 * 4 = 5^2 * 4^2 (Now, what do you think the 2 represent here?. Ans: it's the # of odd indices and even indices in digit string of length 4.)
        
    - That's how they got the formula.
    
If we stop here, LC gives you a TLE (Time Limit Exceeded). So now we have another problem, how can we calculate it fast enough?
Ans: we use fast exponentiation.

pow(base, exponent, modulus):
Returns the result of base raised to the power of exponent, modulo modulus ((base**exponent) % modulus). 
This form is more efficient for large numbers when you only need the remainder of the division.

TLDR
- i think to best to understand fast exponentiation, you need some knowledge about modular arithmetic, or at least about the modulo operator and how does it prevent numbers from blowing up.
- you can abstract this away by using python's pow() function, it's already a fast exponentiation.

"""

def countGoodNumbers(n: int) -> int:
    mod = 10**9 + 7
    return (pow(5, (n + 1) // 2, mod) * pow(4, n // 2, mod)) % mod  
    
        
        