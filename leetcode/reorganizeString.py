from collections import Counter
import heapq

def reorganizeStringHeap(s: str) -> str:
    ans = []
    pq = []
    heapq.heapify(pq)
    count = Counter(s)

    for char, value in count.items():
        heapq.heappush(pq, (-value, char))

    while pq:
        count_first, char_first = heapq.heappop(pq)
        if not ans or char_first != ans[-1]:
            ans.append(char_first)
            if count_first + 1 != 0:
                heapq.heappush(pq, (count_first + 1, char_first))
        else:
            if not pq:
                return ""
            count_second, char_second = heapq.heappop(pq)
            ans.append(char_second)
            if count_second + 1 != 0:
                heapq.heappush(pq, (count_second + 1, char_second))
            heapq.heappush(pq, (count_first, char_first))

    return "".join(ans)

def reorganizeStringEO(self, s: str) -> str:
    count = Counter(s)
    max_freq, char = 0, ''

    for c, f in count.items():
        if f > max_freq:
            max_freq = f
            char = c
    
    n = len(s)
    
    if max_freq > ceil(n/2):
        return ''
    
    ans = [''] * n
    index = 0

    # placing the most frequent char in ans
    while count[char] != 0:
        ans[index] = char
        index += 2
        count[char] -= 1
    
    for key, value in count.items():
        while value > 0:
            if index >= n:
                index = 1

            ans[index] = key
            index += 2
            value -= 1
    
    return ''.join(ans)