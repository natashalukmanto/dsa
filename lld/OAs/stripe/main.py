from collections import defaultdict
from typing import List
from classes import Transaction, Rules, Merchant


def calculate_fraud_score(
    transaction_list: List[str], rules_list: List[str], merchant_list: List[int]
):
    transactions, rules, merchants = [], [], {}

    # storing the input
    for t in transaction_list:
        t = t.split(",")
        transactions.append(Transaction(t[0], int(t[1]), t[2], int(t[3])))

    for r in rules_list:
        r = r.split(",")
        rules.append(Rules(int(r[0]), int(r[1]), int(r[2]), int(r[3])))

    pairs = list(zip(transactions, rules))
    pairs.sort(key=lambda p: p[0].hour)

    for m in merchant_list:
        m = m.split(",")
        merchants[m[0]] = Merchant(m[0], int(m[1]))

    # case 1: payment_amount > min_transaction_amount
    for transaction, rule in pairs:
        if transaction.payment_amount > rule.min_transaction_amount:
            merchants[transaction.merchant_id].score *= rule.multiplicative_factor

    # storing the frequency of transactions between customer & merchant
    freq = defaultdict(int)  # (cust, merch) -> count
    additive_factors_map = defaultdict(
        list
    )  # (cust, merch) -> list of additive_factors seen
    hour_map = defaultdict(int)  # (cust, merch, hour) -> count in that hour
    penalty_map = defaultdict(list)  # (cust, merch, hour) -> penalties in that hour

    for transaction, rule in pairs:
        customer = transaction.customer_id
        merchant = transaction.merchant_id
        hour = transaction.hour

        # case 2: the same customer_id had made ≥ 3 transaction to a merchant_id
        freq[(customer, merchant)] += 1
        additive_factors_map[(customer, merchant)].append(rule.additive_factor)

        if freq[(customer, merchant)] == 3:
            merchants[merchant].score += sum(additive_factors_map[(customer, merchant)])
        elif freq[(customer, merchant)] > 3:
            merchants[merchant].score += rule.additive_factor

        # case 3: a transaction is the ≥ 3rd from the same custoemr_id in the same hour for the same merchant_id
        hour_map[(customer, merchant, hour)] += 1
        penalty_map[(customer, merchant, hour)].append(rule.penalty)

        apply_amt = 0
        if hour_map[(customer, merchant, hour)] == 3:
            apply_amt = sum(penalty_map[(customer, merchant, hour)])
        elif hour_map[(customer, merchant, hour)] > 3:
            apply_amt = rule.penalty

        if apply_amt:
            if 12 <= hour <= 17:
                merchants[merchant].score += apply_amt
            elif (9 <= hour <= 11) or (18 <= hour <= 21):
                merchants[merchant].score -= apply_amt

    res = [
        f"{merchant_id},{merchant.score}" for merchant_id, merchant in merchants.items()
    ]
    return res


transactions_list = [
    "merchant1,1200,customer1,10",
    "merchant1,500,customer1,10",
    "merchant2,2400,customer1,15",
    "merchant1,800,customer1,16",
    "merchant1,1000,customer2,17",
    "merchant1,1400,customer1,10",
]

rules_list = [
    "1000,2,8,15",
    "1400,5,3,19",
    "2300,3,17,34",
    "1800,2,9,6",
    "1000,4,8,2",
    "1200,3,11,7",
]

merchants_list = [
    "merchant1,10",
    "merchant2,20",
]

print(calculate_fraud_score(transactions_list, rules_list, merchants_list))
