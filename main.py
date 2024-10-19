from bank_account import BankAccount

balance = 100
account = BankAccount(balance)

print(f"Initial balance: {account.balance}")
print(f"Despositing 50: {account.deposit(50)}")
print(f"Withdrawing 30: {account.withdraw(30)}")