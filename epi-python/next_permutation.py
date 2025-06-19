from typing import List

def next_permutation(perm: List[int]) -> List[int]:
    # Find `e`, the element that appears right before the longest decreasing suffix
    e = -1
    for i in reversed(range(len(perm) - 1)):
        if perm[i] < perm[i + 1]:
            e = i
            break

    # Swap perm[e] with perm[i]
    for i in reversed(range(len(perm))):
        if perm[e] < perm[i]:
            perm[e], perm[i] = perm[i],  perm[e]
            break;
        
    # Finally 'sort' the longest dec suffix in perm by reversing it
    perm[e+1:] = reversed(perm[e+1:])
    
    return [] if e == -1 else perm