from typing import List

def delete_duplicates(A: List[int]) -> int:
    if not A: return 0
    
    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index

    # i = 1
    # next_place = 0
    # while i < len(A):
    #     if A[i - 1] == A[i]:
    #         next_place += 1
    #         duplicate = A[i]
    #         while A[i] == duplicate:
    #             i += 1     
    #         A[next_place] = A[i]
    #     i += 1
    #     next_place = i - 1
    #     print(A)
    # return next_place + 1