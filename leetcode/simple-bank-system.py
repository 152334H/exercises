from typing import List
class Bank:
    def __init__(self, balance: List[int]):
        self.account = [None] + balance
        self.n = len(balance)
    def valid(self, acc: int) -> bool: return acc in range(1,self.n+1)
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if any(not self.valid(acc) for acc in (account1,account2)): return False
        if self.account[account1] < money: return False
        self.account[account2] += money
        self.account[account1] -= money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self.valid(account): return False
        self.account[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.valid(account): return False
        if self.account[account] < money: return False
        self.account[account] -= money
        return True


bank = Bank([10, 100, 20, 50, 30]);
assert bank.withdraw(3, 10);    
assert bank.transfer(5, 1, 20); 
assert bank.deposit(5, 20);     
assert not bank.transfer(3, 4, 15); 
assert not bank.withdraw(10, 50); 
