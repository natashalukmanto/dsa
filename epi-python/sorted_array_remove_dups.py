from typing import List

# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    write_index = 1
    for i in range(len(A)):
        if A[i] != A[write_index - 1]:
            A[write_index] = A[i]
            write_index += 1
    return write_index