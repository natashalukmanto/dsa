from typing import List


class Bank:
    # [30,100,10,50,10]
    def __init__(self, balance: List[int]):
        self.account = []
        self.n = len(balance)
        for b in balance:
            self.account.append(b)

    def isValidAccount(self, account: int) -> bool:
        return 1 <= account <= self.n

    def isValidAmount(self, account: int, money: int) -> bool:
        return money <= self.account[account - 1]

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        valid = (
            self.isValidAccount(account1)
            and self.isValidAccount(account2)
            and self.isValidAmount(account1, money)
        )
        if valid:
            self.account[account1 - 1] -= money
            self.account[account2 - 1] += money
        return valid

    def deposit(self, account: int, money: int) -> bool:
        valid = self.isValidAccount(account)
        if valid:
            self.account[account - 1] += money
        return valid

    def withdraw(self, account: int, money: int) -> bool:
        valid = self.isValidAccount(account) and self.isValidAmount(account, money)
        # print(self.account[account - 1], money, valid)
        if valid:
            self.account[account - 1] -= money
        return valid


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = [0] + balance

    def isValidAccount(self, account: int) -> bool:
        return 1 <= account < len(self.balance)

    def isValidTransaction(self, account: int, money: int) -> bool:
        return self.balance[account] >= money

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (
            self.isValidAccount(account1)
            and self.isValidAccount(account2)
            and self.isValidTransaction(account1, money)
        ):
            self.balance[account1] -= money
            self.balance[account2] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self.isValidAccount(account):
            self.balance[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.isValidAccount(account) and self.isValidTransaction(account, money):
            self.balance[account] -= money
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
