class BankAccount:
    def __init__(self,initial_balance = 0):
        self.balance = initial_balance
        self.transaction = []
    def deposit(self,amount):
        if amount > 0 :
            self.balance += amount
            self.transaction.append(f"Deposit {amount}")
        return self.balance

    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction.append(f"Withdraw {amount}")
        return  self.balance
    def get_balance(self):
        return self.balance