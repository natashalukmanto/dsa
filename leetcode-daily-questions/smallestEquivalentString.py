def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
    # This is a Union Find problem.
    # Intuition -> For each letters in s1 and s2, we want to map each character to the smallest equivalent character.
    # For example, given s1 = "abc" and s2 = "cde"
    # we know that c is equivalent to e, therefore if baseStr has the character 'e' in it,
    # we can "upgrade" it to its smaller equivalent 'c', but wait!
    # we also know that 'a' and 'c' is equivalent from
    # s1 = "a b c"
    # s2 = "c d e" -> shows c = e and a = c, so by transitivity implies e = a!
    # this is a better upgrade!

    # Once we know what is the smallest equivalent of each character from s1 & s2
    # All we need to do is to construct baseStr based on the mapping

    # Let's start with a structure to keep all the possible smallest character
    parents = [i for i in range(26)] # this list will keep track of the smallest equivalent of
    # each character

    def find(x):
        if parents[x] != x: # i.e. there could be a smaller equivalent
            return find(parents[x])
        return parents[x]

    def union(x, y):
        px, py = find(x), find(y) # find the smallest equivalent
        if px == py:
            return 
        elif px < py:
            parents[py] = px
        else:
            parents[px] = py
        
    # Let's find all the unions from s1 and s2
    for a, b in zip(s1, s2):
        union(ord(a) - 97, ord(b) - 97)

    # easy part is to just create the answer
    ans = []
    for char in baseStr:
        smallest = find(ord(char) - 97)
        ans.append(chr(smallest + 97))

    return ''.join(ans)