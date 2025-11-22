from typing import List


def intervalIntersection(
    self, firstList: List[List[int]], secondList: List[List[int]]
) -> List[List[int]]:
    if not firstList or not secondList:
        return []
    res = []

    f, s = 0, 0
    while f < len(firstList) and s < len(secondList):
        startf, endf = firstList[f]
        starts, ends = secondList[s]

        if startf > ends:
            s += 1
        elif starts > endf:
            f += 1
        else:
            res.append([max(startf, starts), min(endf, ends)])
            if endf > ends:
                s += 1
            elif ends > endf:
                f += 1
            else:
                s += 1
                f += 1

    return res


# [[8,15]] and [[2,6],[8,10],[12,20]],
#    ^                           ^

# [[0,2],[5,10],[13,23],[24,25]] and [[1,5],[8,12],[15,24],[25,26]]
#         ^                            ^
# res = [[1, 2], []]
