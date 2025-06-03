from collections import defaultdict

def minWindow(self, s: str, t: str) -> str:
    if len(t) > len(s) or t == "": return ""

    char_needed = defaultdict(int)
    for char in t:
        char_needed[char] += 1
    
    need = len(t)
    min_window = [0, float("inf")]
    start_index = 0

    for end_index, char in enumerate(s):
        if char_needed[char] > 0:
            need -= 1
        char_needed[char] -= 1

        # if all `t` characters in 
        if need == 0:
            # we want to try to shrink
            while True:
                if char_needed[s[start_index]] == 0:
                    break
                char_needed[s[start_index]] += 1
                start_index += 1
            
            if min_window[1] - min_window[0] > end_index - start_index:
                min_window = [start_index, end_index]
            
            char_needed[s[start_index]] += 1
            need += 1
            start_index += 1
    
    return "" if min_window[1] > len(s) else s[min_window[0]:min_window[1]+1]
