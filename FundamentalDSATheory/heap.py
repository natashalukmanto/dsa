# Build a Min Heap (Heapify)
# Time: O(n), Space: O(1)

A = [-4, 3, 1, 0, 2, 5, 10, 8 , 12, 9]

import heapq
heapq.heapify(A) # A = [-4, 0, 1, 3, 2, 5, 10, 8, 12, 9], notice it is not totally sorted in ascending order.

# Heap push (Insert element)
# Time: O(log n)
heapq.heappush(A, 4) # A = [-4, 0, 1, 3, 2, 5, 10, 8, 12, 9, 4]

R""" It actually looks like this:
           -4
         /    \
        0      1
       / \    / \
      3   2  5  10
     / \   \   \
    8  12  9    4
"""

# Heap pop (extract min value)
# Time: O(log n)

minn = heapq.heappop(A) # A = [0, 2, 1, 3, 4, 5, 10, 8, 12, 9], minn = -4

# Peek at min heap, time: O(1)
print(A[0])

# Heap sort
# Time: O(nlogn), Space = O(n)
# Space complexity of O(1) is possible, but it's just rather complex to do

def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0] * n
    
    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn
    
    return new_list
    
print(heapsort(A)) # [0, 1, 2, 3, 4, 5, 8, 9, 10, 12]

# Heap Push Pop
# Time: O(log n)

heapq.heappushpop(A, 99)

# Max Heap
# There's no implementation of max heap in heapq, so what we need to do is to negate the values of the tree

B = [0, 2, 1, 3, 4, 5, 10, 8, 12, 9]

for i in range(len(B)):
    B[i] = -B[i]

heapq.heapify(B) # [-12, -9, -10, -8, -4, -5, -1, -2, -3, 0]

largest = -heapq.heappop(B) # 12

heapq.heappush(B, -7) # insert value 7 into the max heap

# Build from scratch, Time: O(n log n); slower than heapify. 
C = [-5, 4, 2, 1, 7, 0, 3]
heap = []
for num in C:
    heapq.heappush(heap, num)
    print(heap)
    
print(len(heap))

# Putting tuples of items on the heap

D = [5, 4, 3, 5, 4, 3, 5, 5, 4]

from collections import Counter

counter = Counter(D) # Counter({5: 4, 4: 3, 3: 2})

heap1 = []

for key, val in counter.items():
    heapq.heappush(heap1, (val, key)) # sorts by val first, but in any ties, sort by key then

print(heap1)