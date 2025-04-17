def countPairs(nums: list, k: int) -> int:
        pairs = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    pairs += 1
        return pairs