class Transaction:
    def __init__(self, merchant_id: str, payment_amount: int, customer_id: str, hour: int):
        self.merchant_id = merchant_id
        self.payment_amount = payment_amount
        self.customer_id = customer_id
        self.hour = hour
    
class Rules:
    def __init__(self, min_transaction_amount: int, multiplicative_factor: int, additive_factor: int, penalty: int):
        self.min_transaction_amount = min_transaction_amount
        self.multiplicative_factor = multiplicative_factor
        self.additive_factor = additive_factor
        self.penalty = penalty
    
class Merchant:
    def __init__(self, merchant_id: str, base_score: int):
        self.merchant_id = merchant_id
        self.score = base_score
        