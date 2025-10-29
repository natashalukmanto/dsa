# Initial
def bestClosingTime0(customers: str) -> int:
    penalties = [0] * (len(customers) + 1)

    last_penalty = 0
    for customer in customers:
        if customer == "N":
            last_penalty += 1
    if last_penalty == len(customers):
        return 0
    if last_penalty == 0:
        return len(customers)

    penalties[-1] = last_penalty

    for i in reversed(range(len(customers))):
        # print(i)
        if customers[i] == "Y":
            penalties[i] = penalties[i + 1] + 1
        else:
            penalties[i] = penalties[i + 1] - 1
        # print(penalties)

    res = min(penalties)
    for i in range(len(penalties)):
        if penalties[i] == res:
            return i

def bestClosingTime(customers: str) -> int:
    curr_penalty = sum(customer == "Y" for customer in customers)

    min_penalty = curr_penalty
    hour = 0

    for index, customer in enumerate(customers):
        if customer == "Y":
            curr_penalty -= 1
        else:
            curr_penalty += 1

        if curr_penalty < min_penalty:
            min_penalty = curr_penalty
            hour = index + 1

    return hour


def bestClosingTime(customers: str) -> int:
    curr_penalty = 0
    min_penalty = curr_penalty
    hour = 0

    for index, customer in enumerate(customers):
        if customer == "Y":
            curr_penalty -= 1
        else:
            curr_penalty += 1

        if curr_penalty < min_penalty:
            min_penalty = curr_penalty
            hour = index + 1

    return hour
