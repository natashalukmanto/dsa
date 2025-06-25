"""
My initial solution was something like this:
- Find the denominator, call it x
- Make a list of size x, call it `pool`
- If the num_list is [3, 5, 7, 9] and the probability is [1/8, 4/8, 2/8, 1/8] then pool = [3, 5, 5, 5, 5, 7, 7, 9]
- Pick a random number from pool

But I couldn't figure out how to translate that into code, without making a big mess (and also pass the testcase).

So, I decided to not pursue it further.
"""

def nonuniform_random_number_generation(values: List[int], probabilities: List[float]) -> int:
    prefix_probabilities = list(itertools.accumulate(probabilities)) # creates the interval
    random_index = bisect.bisect(prefix_probabilities, random.random()) # pick a random number 
    # The random() method returns a random floating number between 0 and 1. 
    # Syntax: random.random() 
    # Parameter Values: No parameters.
    return values[random_index]