from typing import List


def calculateTax0(brackets: List[List[int]], income: int) -> float:
    if income == 0:
        return 0.0

    tax, prev = 0.0, 0
    for upper_bound, percentage in brackets:
        tax += (min(upper_bound, income) - prev) * (percentage / 100)
        prev = upper_bound
        if income < upper_bound:
            break

    return tax


def calculateTax(self, brackets: List[List[int]], income: int) -> float:
    tax, prev = 0.0, 0

    for upper_bound, percentage in brackets:
        if income >= upper_bound:
            tax += (upper_bound - prev) * (percentage / 100)
            prev = upper_bound
        else:
            tax += (income - prev) * (percentage / 100)
            break

    return tax
