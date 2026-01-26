from typing import List


# This is my first approach. If you read it, you'll understand that it's basically the same thing, but without using the .sort() function
# While I think it's less readable/more verbose, I think this is easier to understand than the solutions/
def rearrange0(A: List[int]) -> None:
    interleave = True
    for i in range(len(A) - 1):
        if interleave:
            interleave = False
            if A[i] > A[i + 1]:
                temp = A[i]
                A[i] = A[i + 1]
                A[i + 1] = temp

        else:
            interleave = True
            if A[i] < A[i + 1]:
                temp = A[i]
                A[i] = A[i + 1]
                A[i + 1] = temp
    return A


# Or you can equivalently, do this approach. The only difference is that the approach below does not use the variable interleave and instead
# takes advantage of the parity of the index number (i)
def rearrange1(A: List[int]) -> None:
    for i in range(1, len(A)):
        if i % 2 == 0:
            if A[i - 1] < A[i]:
                A[i - 1], A[i] = A[i], A[i - 1]
        else:
            if A[i] < A[i - 1]:
                A[i - 1], A[i] = A[i], A[i - 1]


# Solutions:

# Remember what the question is asking: given an array of integers called A, we want to sort it so that A[0] ≤ A[1] ≥ A[2] ≤ A[3] ≥ ...
# If we have an example like:
# Original:                         [3, 5, 2, 1, 6, 4]
# Then we want the answer to be:    [3, 5, 1, 6, 2, 4]
# Notice:                            3≤ 5 ≥1 ≤6 ≥2 ≤4 (pay attention to the signs!)
# For even indices i, ensure A[i] <= A[i+1]
# For odd indices i, ensure A[i] >= A[i+1]
# The condition is local, meaning each pair only needs to satisfy its relation, regardless of what the rest of the array looks like.
# So, by ensuring the correct relation between each pair A[i] and A[i+1] as you go through the array, you create the pattern without needing full sorting.


def rearrange(A: List[int]) -> None:
    for i in range(len(A)):
        # i % 2 == 0 → even index → sort ascending → A[i] <= A[i+1]
        # i % 2 == 1 → odd index → sort descending → A[i] >= A[i+1]
        A[i : i + 2] = sorted(A[i : i + 2], reverse=i % 2)
    return A


"""
A = [3, 5, 2, 1, 6, 4]

# Steps:
i=0 (even): A[0:2] = [3, 5] → keep order
i=1 (odd): A[1:3] = [5, 2] → sort descending → [5, 2]
i=2 (even): A[2:4] = [2, 1] → sort ascending → [1, 2]
i=3 (odd): A[3:5] = [2, 6] → sort descending → [6, 2]
i=4 (even): A[4:6] = [2, 4] → sort ascending → [2, 4]

Result: [3, 5, 1, 6, 2, 4] — matches pattern

"""
