from typing import List

def minimumOperations(nums: List[int]) -> int:
    dp1 = dp2 = dp3 = 0

    for num in nums:
        new_dp1 = dp1 + (num != 1)
        new_dp2 = min(dp1, dp2) + (num != 2)
        new_dp3 = min(dp1, dp2, dp3) + (num != 3)
        dp1, dp2, dp3 = new_dp1, new_dp2, new_dp3  
    
    return min(dp1, dp2, dp3)

def minimumOperations0(nums: List[int]) -> int:
    res = len(nums)

    pre1 = [0] * (len(nums) + 1)
    pre2 = [0] * (len(nums) + 1)
    pre3 = [0] * (len(nums) + 1)

    for i in range(len(nums)):
        pre1[i+1] = (nums[i] == 1) + pre1[i]
        pre2[i+1] = (nums[i] == 2) + pre2[i]
        pre3[i+1] = (nums[i] == 3) + pre3[i]
    
    # print(pre1, pre2, pre3)

    for i in range(-1, len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                keep = 0

                keep += pre1[i+1]
                keep += pre2[j+1]-pre2[i+1]
                keep += pre3[k+1]-pre3[j+1]

                res = min(res, len(nums)-keep)

    return res

    # # 3 nested for loops. -> brute force. The indexes of the for loops denotes the ends of 1s, 2,s and 3s

    # # [2,1,3,2,1]
    # #  ^       ^
    # # [0,1,2,3,4] -> []
    # # [4,1,0,3,2]
    # nums2 = nums[:]
    # s, e, b = 0, 0, len(nums) - 1
    # while e <= b:
    #     if nums2[e] == 2:
    #         e += 1
    #     elif nums2[e] < 2:
    #         nums2[e], nums2[s] = nums2[s], nums2[e]
    #         e += 1
    #         s += 1
    #     else:
    #         nums2[e], nums2[b] = nums2[b], nums2[e]
    #         b -= 1
    
    # print(nums2)

    # return sum([1 for i in range(len(nums)) if nums[i] != nums2[i]])

    # # non_dec_sequence = []
    # # start, end = 0, 0
    # # res = 0

    # # while end < len(nums)-1:
    # #     if nums[end] > nums[end+1]:
    # #         if start != 0 and end != 0:
    # #             non_dec_sequence.append([start, end])
    # #         start = end + 1
            
    # #     end += 1

    # # return non_dec_sequence