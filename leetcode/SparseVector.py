from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        res = 0
        for i in range(len(self.vector)):
            res = res + (vec.vector[i] * self.vector[i])
        return res


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = {}

        for i, num in enumerate(nums):
            if num != 0:
                self.vector[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for i, num in self.vector.items():
            if i in vec.vector:
                result += num * vec.vector[i]
        return result

class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = []

        for i, n in enumerate(nums):
            if n != 0:
                self.vector.append((i, n))
            
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        p, q = 0, 0

        while p < len(vec.vector) and q < len(self.vector):
            if vec.vector[p][0] == self.vector[q][0]:
                result += vec.vector[p][1] * self.vector[q][1]
                p += 1
                q += 1
            elif vec.vector[p][0] < self.vector[q][0]:
                p += 1
            else:
                q += 1
        
        return result
