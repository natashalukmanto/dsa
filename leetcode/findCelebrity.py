def findCelebrity(self, n: int) -> int:
        def is_celeb(i):
            for j in range(n):
                if i == j: continue
                if knows(i, j) or not knows(j, i):
                    return False
            return True

        candidate = 0
        for i in range(n):
            if knows(candidate, i):
                candidate = i
        
        if is_celeb(candidate):
            return candidate
        
        return -1