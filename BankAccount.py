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
        # Issue 1: Missing colon (ERROR - Syntax)
        if amount > 0
            self.balance += amount
            self.transaction_history.append(f"Deposit: ${amount}")
            return True
        else:
            print("Deposit amount must be positive")
            return False
    
    def withdraw(self, amount):
        # Issue 2: Wrong comparison operator (DEFECT - Logic)
        if amount >= 0 and amount < self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: ${amount}")
            return True
        else:
            print("Insufficient funds or invalid amount")
            return False
    
    def calculate_interest(self):
        # Issue 3: Wrong variable name (ERROR - NameError)
        interest = self.balanse * self.interest_rate
        self.balance += interest
        self.transaction_history.append(f"Interest earned: ${interest:.2f}")
        return interest
    
    def get_balance(self):
        # Issue 4: Wrong return type (DEFECT - Returns string instead of number)
        return f"${self.balance}"
    
    def display_transactions(self):
        # Issue 5: Wrong indentation (ERROR - IndentationError)
        print(f"\n=== Transaction History for {self.account_holder} ===")
       for transaction in self.transaction_history:
            print(transaction)
    
    def transfer(self, other_account, amount):
        # Issue 6: Missing parameter in method call (DEFECT - Logic)
        if self.withdraw():
            other_account.deposit(amount)
            self.transaction_history.append(f"Transfer to {other_account.account_holder}: ${amount}")
            return True
        return False


# Issue 7: Missing closing parenthesis (ERROR - Syntax)
def calculate_total_balance(accounts:
    total = 0
    for account in accounts:
        total += account.balance
    return total


# Issue 8: Wrong comparison in function (DEFECT - Logic)
def find_high_balance_accounts(accounts, threshold=5000):
    """Find accounts with balance above threshold"""
    high_balance = []
    for account in accounts:
        # This should find accounts >= threshold, but uses >
        if account.balance < threshold:
            high_balance.append(account)
    return high_balance





"""
ANSWER KEY FOR INSTRUCTORS:

ERRORS (Prevent Execution):
1. Line 20: Missing colon after if statement
2. Line 35: Typo in variable name 'balanse' → 'balance'
3. Line 45: Wrong indentation before 'for' loop
4. Line 54: Missing closing parenthesis in function definition

DEFECTS (Allow Execution but Wrong Behavior):
5. Line 27: Wrong comparison (should be <=) to allow withdrawal of full balance
6. Line 40: Returns string instead of numeric value for balance
7. Line 51: Missing 'amount' parameter in withdraw() call
8. Line 68: Wrong comparison operator (< should be >=)

Total Issues: 8 (4 Errors + 4 Defects)
"""