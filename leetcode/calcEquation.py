from typing import List
from collections import defaultdict


def calcEquation0(
    equations: List[List[str]], values: List[float], queries: List[List[str]]
) -> List[float]:
    res, var = [-1.0] * len(queries), set()
    connections = {}

    for i in range(len(equations)):
        connections[tuple(equations[i])] = values[i]
        set.add(equations[i][0])
        set.add(equations[i][0])

    for i in range(len(queries)):
        query, query_reverse = tuple(queries[i]), tuple(queries[i][1], queries[i][0])

        if query in connections and query[0] == query[1]:
            res[i] = 1.0
        elif query_reverse in connections:
            res[i] = 1 / connections[query_reverse]
        elif query[0] in var and query[1] in var:
            # how do i do this one?? stuck
            pass

    # print(connections)

    return res

def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    connections = defaultdict(defaultdict)
    res = []

    for equation, value in zip(equations, values):
        connections[equation[0]][equation[1]] = value
        connections[equation[1]][equation[0]] = 1/value

    def backtrack(source_node, target_node, acc_score, visited):
        visited.add(source_node)
        ret = -1.0
        neighbors = connections[source_node]

        if target_node in neighbors:
            ret = acc_score * connections[source_node][target_node]
        else:
            for neighbor, value in neighbors.items():
                if neighbor in visited:
                    continue
                ret = backtrack(neighbor, target_node, acc_score * value, visited)
                if ret != -1.0:
                    break
                    
        visited.remove(source_node)
        return ret

    for dividend, divisor in queries:
        if dividend not in connections or divisor not in connections:
            ret = -1.0
        elif dividend == divisor:
            ret = 1.0
        else:
            visited = set()
            ret = backtrack(dividend, divisor, 1.0, visited)
        res.append(ret)

    return res
