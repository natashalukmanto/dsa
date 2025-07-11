import itertools, random
from typing import List, Iterator 

# Assumption: there are at least k elements in the stream.
def online_random_sample(stream: Iterator[int], k: int) -> List[int]:
    initial_sample = list(itertools.islice(stream, k))
    seen_so_far = k
    
    for packet in stream:
        seen_so_far += 1
        r = random.randrange(seen_so_far)
        if r < k:
            initial_sample[r] = packet
    
    return initial_sample