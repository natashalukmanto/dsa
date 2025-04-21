class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq_map = Counter(answers)
        total = 0
        
        for answer, count in freq_map.items():
            total += ceil(count / (answer + 1)) * (answer + 1)

        return total
        