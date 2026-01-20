# First try

def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    hashmap = [0] * 26

    for i in range(len(s1)):
        hashmap[ord(s1[i]) - ord("a")] += 1
        # print(hashmap)
        hashmap[ord(s2[i]) - ord("a")] -= 1
        # print(hashmap)

    left = 0
    for right in range(len(s1), len(s2)):
        # print(hashmap)
        if all(j == 0 for j in hashmap):
            return True
        hashmap[ord(s2[right]) - ord("a")] -= 1
        hashmap[ord(s2[left]) - ord("a")] += 1
        left += 1

    return all(j == 0 for j in hashmap)
