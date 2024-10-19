from bank_account import BankAccount
import pytest

from main import balance

@pytest.fixture
def bank_account():
    balance = 100
    account = BankAccount(balance)
    return account

def test_inital_balance(bank_account):
    assert bank_account.balance == 100

def test_deposit_balance(bank_account):
    bank_account.deposit(50)
    assert  bank_account.balance == 150

def test_withdraw_balance(bank_account):
    bank_account.withdraw(30)
    assert  bank_account.balance == 70
def test_deposit_transaction(bank_account):
    bank_account.deposit(50)
    assert "Deposit 50" in bank_account.transaction
def test_withdraw_transaction(bank_account):
    bank_account.withdraw(50)
    assert "Withdraw 50" in bank_account.transaction
def test_invalid_deposit(bank_account):
    bank_account.deposit(-50)
    assert bank_account.balance == 100
def test_invalid_withdraw(bank_account):
    bank_account.withdraw(150)
    assert bank_account.balance == 100

def test_get_balance(bank_account):
    assert bank_account.get_balance() == 100
    bank_account.deposit(50)
    assert bank_account.get_balance() == 150
    bank_account.withdraw(40)
    assert bank_account.get_balance() == 110
