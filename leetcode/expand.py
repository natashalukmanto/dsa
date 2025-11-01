from typing import List


def expand(self, s: str) -> List[str]:
    if "{" not in s:
        return [s]

    options, i = [], 0
    while i < len(s):
        if s[i] == "{":
            option = []
            while s[i] != "}":
                i += 1
                if s[i] != "," and s[i] != "}":
                    option.append(s[i])
            options.append(sorted(option))
        else:
            if s[i] != "}" and s[i] != "{":
                options.append(s[i])
        i += 1
    # print(options)

    res, path = [], []

    def backtrack(index: int):
        if index == len(options):
            res.append("".join(path))
            return
        else:
            for ch in options[index]:
                path.append(ch)
                backtrack(index + 1)
                path.pop()

    backtrack(0)
    return res


def expand(self, s: str) -> List[str]:
    
    def buildOptions(index: int):
        option = []
        if s[index] != "{":
            option.append(s[index])
            return option, index + 1
        else:
            while s[index] != "}":
                if "a" <= s[index] <= "z":
                    option.append(s[index])
                index += 1
            return sorted(option), index + 1

    def findWords(index: int):
        if index == len(s):
            return [""]

        option, i = buildOptions(index)
        suffix = findWords(i)
        res = []

        for ch in option:
            for w in suffix:
                res.append(ch + w)
        return res

    return findWords(0)
