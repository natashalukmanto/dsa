from typing import List

def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    costs.sort(key=lambda x: x[0] - x[1])

    total_costs = 0
    n = len(costs) // 2
    for i in range(n):
        total_costs += costs[i][0] + costs[i + n][1]

    return total_costs

def twoCitySchedCost0(self, costs: List[List[int]]) -> int:
    costs.sort(key=lambda x: x[0] - x[1])
    
    total_costs = 0
    for i in range(len(costs)):
        if i < len(costs) / 2:
            total_costs += costs[i][0]
        else:
            total_costs += costs[i][1]
    
    return total_costs