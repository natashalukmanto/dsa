class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        
        def next_number(s):
            result, i = [], 0
            while i < len(s):
                count = 1
                while i+1 < len(s) and s[i] == s[i+1]:
                    count += 1
                    i += 1
                result.append(str(count) + s[i])
                i += 1
            return "".join(result)
        
        s = "1"
        for i in range(1, n):
            s = next_number(s)
        return s
        