from typing import List


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    if num1 == [0] or num2 == [0]: return [0]
    
    answer = [0] * (len(num1) + len(num2))
    
    signed = (num1[0] < 0) ^ (num2[0] < 0)
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    
    # multiplying
    for i in reversed(range(len(num1))): # 0
        for j in reversed(range(len(num2))): # 0,1,2,3
            answer[i + j + 1] += num1[i] * num2[j]
            answer[i + j] += answer[i + j + 1] // 10
            answer[i + j + 1] %= 10
    
    # # carry
    # carry = 0
    # for i in reversed(range(len(answer))):
    #     answer[i] += carry
    #     carry = answer[i] // 10
    #     answer[i] %= 10
        
    # remove leading zeros
    index = 0
    while answer[index] == 0:
        index += 1     
    answer = answer[index:]
    
    # add back the negative sign (if necessary)
    if signed:
        answer[0] *= -1
    
    return answer