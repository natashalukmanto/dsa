from typing import List

def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()

        for i in range(len(nums)):
            low = i + 1
            high = len(nums) - 1
            while low < high:
                if abs(nums[i] + nums[low] + nums[high] - target) < abs(diff - target):
                    diff = nums[i] + nums[low] + nums[high]

                
                if nums[i] + nums[low] + nums[high] > target:
                    high -= 1
                elif nums[i] + nums[low] + nums[high] < target:
                    low += 1
                
                if abs(target - diff) == 0:
                    break

        return diff

        # #sliding window w/ fixed size of 3, three pointers?

        # # THE THREE INTEGERS DONT HAVE TO BE CONTIGUOUS

        # current_sum = 0
        # closest = float('inf')
        # answer = current_sum
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             # print(nums[i], nums[j], nums[k])
        #             current_sum = nums[i] + nums[j] + nums[k]
        #             # print(current_sum, abs(current_sum - target), closest)
        #             if abs(current_sum - target) < closest: # if found a closer distance
        #                 closest = abs(current_sum - target)
        #                 answer = current_sum
        # return answer

        # # [4,0,5,-5,3,3,0,-4,-5]
        # """
        # Hashmap: shows you the exact match
        # triplet? => 
        
        # """




        # #ex: [4,0,5,-5,3,3,0,-4,-5] -> -5, 3, 0, target = -2,
        # # sum = 4 + 0, when further -> drop the elem (greedy?) X bcs there might be -100, 100 in the end
        # # 
        # # current_sum = sum(nums[:3]) # current_sum = sum([1,1,1]) = 3, target = -100
        # # closest = abs(target - current_sum) # closest = 3
        # # answer = current_sum
        
        # # for i in range(3, len(nums)): # slide the window
        # #     current_sum -= nums[i - 3] 
        # #     current_sum += nums[i]
        # #     if closest > abs(target - current_sum): #if found a closer
        # #         closest = abs(target - current_sum)
        # #         answer = current_sum
        # # return answer
        