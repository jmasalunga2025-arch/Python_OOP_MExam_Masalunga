class BankAccount:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self._balance = initial_balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
         
        if amount > self._balance:
            raise ValueError("Withdrawal amount cannot exceed balance.")
        self._balance -= amount
        return self._balance


account = BankAccount(100)
account.deposit(50)
account.withdraw(20)
print(account.get_balance())