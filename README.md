# Banking System - Testing

This project contains a simple banking system with professional tests using pytest.

## Project Structure

```
├── BankAccount.py          # Main banking system code
├── test/
│   └── test_bank_account.py # Complete test suite
├── requirements.txt        # Project dependencies
├── pytest.ini              # Pytest configuration
└── README.md               # This file
```

## Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

### Basic Commands

```bash
# Run all tests
pytest

# Run with more detailed output
pytest -v

# Run a specific test class
pytest test/test_bank_account.py::TestBankAccount

# Run a specific test method
pytest test/test_bank_account.py::TestBankAccount::test_successful_deposit
```

### Coverage Reports

```bash
# Generate coverage report in terminal
pytest --cov=BankAccount

# Generate HTML coverage report
pytest --cov=BankAccount --cov-report=html

# View the HTML report (created at htmlcov/index.html)
open htmlcov/index.html
```

### HTML Reports

```bash
# Generate HTML test report
pytest --html=report.html --self-contained-html
```

### Parallel Execution

```bash
# Run tests in parallel (faster for large suites)
pytest -n auto
```

## Types of Tests Included

### 1. **Unit Tests** (`TestBankAccount`)
- Account initialization
- Valid and invalid deposits
- Valid and invalid withdrawals
- Interest calculation
- Transfers between accounts
- Transaction history

### 2. **Helper Function Tests** (`TestUtilityFunctions`)
- Total balance calculation
- Find accounts with high balance
- Handling edge cases (empty lists, no matches)

### 3. **Integration Tests** (`TestIntegrationScenarios`)
- Complete banking operation scenarios
- Multiple transfers between accounts
- Data consistency verification

## Test Features

- **Fixtures**: Reusable test data
- **Parametrization**: Tests with multiple input data
- **Clear assertions**: Specific and descriptive checks
- **Full coverage**: Tests for normal and edge cases
- **Documentation**: Each test is documented with its purpose

## Useful Development Commands

```bash
# Run only tests that failed in the last run
pytest --lf

# Stop after the first failure
pytest -x

# Watch mode (requires pytest-watch)
pytest-watch

# Run with profiling to identify slow tests
pytest --durations=10
```

## Best Practices Implemented

1. **Clear separation**: Production code separated from tests
2. **Descriptive naming**: Method names explain what is being tested
3. **Reusable fixtures**: Shared setup between tests
4. **Specific assertions**: Clear and precise checks
5. **Edge cases**: Tests for limit and error cases
6. **Documentation**: Each class and method is documented

## Example Output

```bash
$ pytest -v
========================= test session starts ==========================
collected 20 items

test/test_bank_account.py::TestBankAccount::test_account_initialization PASSED     [ 5%]
test/test_bank_account.py::TestBankAccount::test_successful_deposit PASSED        [10%]
test/test_bank_account.py::TestBankAccount::test_invalid_deposit PASSED          [15%]
test/test_bank_account.py::TestBankAccount::test_successful_withdrawal PASSED    [20%]
test/test_bank_account.py::TestBankAccount::test_withdrawal_full_balance PASSED  [25%]
test/test_bank_account.py::TestBankAccount::test_insufficient_funds_withdrawal PASSED [30%]
test/test_bank_account.py::TestBankAccount::test_negative_withdrawal PASSED      [35%]
test/test_bank_account.py::TestBankAccount::test_interest_calculation PASSED     [40%]
test/test_bank_account.py::TestBankAccount::test_get_balance_returns_number PASSED [45%]
test/test_bank_account.py::TestBankAccount::test_successful_transfer PASSED      [50%]
test/test_bank_account.py::TestBankAccount::test_failed_transfer_insufficient_funds PASSED [55%]
test/test_bank_account.py::TestBankAccount::test_transaction_history_tracking PASSED [60%]
test/test_bank_account.py::TestUtilityFunctions::test_calculate_total_balance PASSED [65%]
test/test_bank_account.py::TestUtilityFunctions::test_calculate_total_balance_empty_list PASSED [70%]
test/test_bank_account.py::TestUtilityFunctions::test_find_high_balance_accounts PASSED [75%]
test/test_bank_account.py::TestUtilityFunctions::test_find_high_balance_accounts_custom_threshold PASSED [80%]
test/test_bank_account.py::TestUtilityFunctions::test_find_high_balance_accounts_no_matches PASSED [85%]
test/test_bank_account.py::TestIntegrationScenarios::test_complete_banking_scenario PASSED [90%]
test/test_bank_account.py::TestIntegrationScenarios::test_multiple_transfers_scenario PASSED [95%]

========================= 20 passed in 0.12s =========================
```