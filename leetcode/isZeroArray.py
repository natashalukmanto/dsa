from typing import List

def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
    diff = [0] * (len(nums) + 2)
    for query in queries:
        diff[query[0]] += 1
        diff[query[1] + 1] -= 1
    
    prefix_sum = [0] * len(diff)
    prefix_sum[0] = diff[0]
    for i in range(1, len(prefix_sum)):
        prefix_sum[i] = diff[i] + prefix_sum[i - 1]

    for i in range(len(nums)):
        if nums[i] - prefix_sum[i] > 0: return False
    return True

    '''
    # Brute Force O(len(nums) x len(queries))
    for query in queries:
        for i in range(query[0], query[1] + 1):
            if nums[i] > 0: nums[i] -= 1 
    
    # print(nums)
    return all(nums[i] == 0 for i in range(len(nums)))
    '''

'''
# Example 1:
            0 1 2
nums =      [1,0,1], queries = [[0,2]]
difference =[1,0,0,-1,0]
prefix =    [1,1,1,0,0]

# Example 2:
            0  1  2  3
nums =      [4, 3, 2, 1], queries = [[1,3],[0,2]]
difference =[1, 1, 0, -1, -1, 0]
prefix =    [1, 2, 2, 1, 0, 0]
'''
