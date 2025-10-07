"""
SOFTWARE QUALITY ASSURANCE ACTIVITY
Topic: Errors vs. Defects

INSTRUCTIONS FOR STUDENTS:
1. This program contains ERRORS (prevent execution) and DEFECTS (wrong logic/results)
2. Identify each issue and classify it as ERROR or DEFECT
3. Fix all issues to make the program work correctly
4. Test with the provided test cases at the bottom

SCENARIO:
A simple banking system that allows deposits, withdrawals, and balance checks.

REQUIREMENTS:
- Initial balance should be $1000
- Deposits must be positive amounts
- Withdrawals cannot exceed current balance
- Interest calculation: 5% annual interest on balance
- Transaction history should track all operations
"""

class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
        self.interest_rate = 0.05
    
    def deposit(self, amount):
        if amount > 0
            self.balance += amount
            self.transaction_history.append(f"Deposit: ${amount}")
            return True
        else:
            print("Deposit amount must be positive")
            return False
    
    def withdraw(self, amount):
        if amount >= 0 and amount < self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: ${amount}")
            return True
        else:
            print("Insufficient funds or invalid amount")
            return False
    
    def calculate_interest(self):
        interest = self.balanse * self.interest_rate
        self.balance += interest
        self.transaction_history.append(f"Interest earned: ${interest:.2f}")
        return interest
    
    def get_balance(self):
        return f"${self.balance}"
    
    def display_transactions(self):
        print(f"\n=== Transaction History for {self.account_holder} ===")
       for transaction in self.transaction_history:
            print(transaction)
    
    def transfer(self, other_account, amount):
        if self.withdraw():
            other_account.deposit(amount)
            self.transaction_history.append(f"Transfer to {other_account.account_holder}: ${amount}")
            return True
        return False


def calculate_total_balance(accounts:
    total = 0
    for account in accounts:
        total += account.balance
    return total


def find_high_balance_accounts(accounts, threshold=5000):
    """Find accounts with balance above threshold"""
    high_balance = []
    for account in accounts:
        if account.balance < threshold:
            high_balance.append(account)
    return high_balance


if __name__ == '__main__':
    # Crear cuentas de ejemplo
    account1 = BankAccount("Alice", 1000)
    account2 = BankAccount("Bob", 2000)
    account3 = BankAccount("Charlie", 3000)

    # Realizar algunas operaciones
    account1.deposit(500)
    account1.withdraw(200)
    account1.calculate_interest()
    print(account1.get_balance())
    account1.display_transactions()


    account2.deposit(1000)
    account2.withdraw(2500)
    account2.calculate_interest()
    print(account2.get_balance())
    account2.display_transactions()


    account3.deposit(1500)
    account3.withdraw(1000)
    account3.calculate_interest()
    print(account3.get_balance())
    account3.display_transactions()