"""
Test suite para el sistema bancario BankAccount

Este archivo contiene todas las pruebas para verificar el comportamiento
correcto de la clase BankAccount y las funciones auxiliares.
"""

import pytest
import sys
import os

# Agregar el directorio padre al path para importar BankAccount
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from BankAccount import BankAccount, calculate_total_balance, find_high_balance_accounts


class TestBankAccount:
    """Clase de pruebas para la clase BankAccount"""
    
    @pytest.fixture
    def sample_account(self):
        """Fixture que crea una cuenta de ejemplo para las pruebas"""
        return BankAccount("Test User", 1000)
    
    @pytest.fixture
    def multiple_accounts(self):
        """Fixture que crea múltiples cuentas para pruebas complejas"""
        return [
            BankAccount("Alice Johnson", 1000),
            BankAccount("Bob Smith", 2000),
            BankAccount("Charlie Brown", 1500),
            BankAccount("Diana Prince", 3000)
        ]
    
    def test_account_initialization(self):
        """Prueba la inicialización correcta de una cuenta bancaria"""
        account = BankAccount("John Doe", 500)
        
        assert account.account_holder == "John Doe"
        assert account.balance == 500
        assert account.transaction_history == []
        assert account.interest_rate == 0.05
    
    def test_successful_deposit(self, sample_account):
        """Prueba que los depósitos válidos funcionen correctamente"""
        initial_balance = sample_account.balance
        deposit_amount = 500
        
        result = sample_account.deposit(deposit_amount)
        
        assert result is True
        assert sample_account.balance == initial_balance + deposit_amount
        assert f"Deposit: ${deposit_amount}" in sample_account.transaction_history
    
    def test_invalid_deposit(self, sample_account):
        """Prueba que los depósitos inválidos sean rechazados"""
        initial_balance = sample_account.balance
        
        # Prueba con cantidad negativa
        result = sample_account.deposit(-100)
        assert result is False
        assert sample_account.balance == initial_balance
        
        # Prueba con cantidad cero
        result = sample_account.deposit(0)
        assert result is False
        assert sample_account.balance == initial_balance
    
    def test_successful_withdrawal(self, sample_account):
        """Prueba que los retiros válidos funcionen correctamente"""
        initial_balance = sample_account.balance
        withdrawal_amount = 300
        
        result = sample_account.withdraw(withdrawal_amount)
        
        assert result is True
        assert sample_account.balance == initial_balance - withdrawal_amount
        assert f"Withdrawal: ${withdrawal_amount}" in sample_account.transaction_history
    
    def test_withdrawal_full_balance(self, sample_account):
        """Prueba que se pueda retirar todo el balance"""
        initial_balance = sample_account.balance
        
        result = sample_account.withdraw(initial_balance)
        
        assert result is True
        assert sample_account.balance == 0
    
    def test_insufficient_funds_withdrawal(self, sample_account):
        """Prueba que no se pueda retirar más del balance disponible"""
        initial_balance = sample_account.balance
        
        result = sample_account.withdraw(initial_balance + 100)
        
        assert result is False
        assert sample_account.balance == initial_balance
    
    def test_negative_withdrawal(self, sample_account):
        """Prueba que no se permitan retiros negativos"""
        initial_balance = sample_account.balance
        
        result = sample_account.withdraw(-50)
        
        assert result is False
        assert sample_account.balance == initial_balance
    
    def test_interest_calculation(self, sample_account):
        """Prueba el cálculo correcto de intereses"""
        initial_balance = sample_account.balance
        expected_interest = initial_balance * 0.05
        
        calculated_interest = sample_account.calculate_interest()
        
        assert calculated_interest == expected_interest
        assert sample_account.balance == initial_balance + expected_interest
        assert f"Interest earned: ${expected_interest:.2f}" in sample_account.transaction_history
    
    def test_get_balance_returns_number(self, sample_account):
        """Prueba que get_balance retorne un número, no una cadena"""
        balance = sample_account.get_balance()
        
        assert isinstance(balance, (int, float))
        assert balance == sample_account.balance
    
    def test_successful_transfer(self, multiple_accounts):
        """Prueba que las transferencias entre cuentas funcionen correctamente"""
        source_account = multiple_accounts[0]  # Alice
        target_account = multiple_accounts[1]  # Bob
        
        initial_source_balance = source_account.balance
        initial_target_balance = target_account.balance
        transfer_amount = 300
        
        result = source_account.transfer(target_account, transfer_amount)
        
        assert result is True
        assert source_account.balance == initial_source_balance - transfer_amount
        assert target_account.balance == initial_target_balance + transfer_amount
        assert f"Transfer to {target_account.account_holder}: ${transfer_amount}" in source_account.transaction_history
    
    def test_failed_transfer_insufficient_funds(self, multiple_accounts):
        """Prueba que las transferencias fallen cuando no hay fondos suficientes"""
        source_account = multiple_accounts[0]  # Alice
        target_account = multiple_accounts[1]  # Bob
        
        initial_source_balance = source_account.balance
        initial_target_balance = target_account.balance
        transfer_amount = initial_source_balance + 100  # Más del balance disponible
        
        result = source_account.transfer(target_account, transfer_amount)
        
        assert result is False
        assert source_account.balance == initial_source_balance
        assert target_account.balance == initial_target_balance
    
    def test_transaction_history_tracking(self, sample_account):
        """Prueba que el historial de transacciones se registre correctamente"""
        # Realizar varias operaciones
        sample_account.deposit(200)
        sample_account.withdraw(50)
        sample_account.calculate_interest()
        
        # Verificar que todas las transacciones estén registradas
        history = sample_account.transaction_history
        assert len(history) == 3
        assert "Deposit: $200" in history
        assert "Withdrawal: $50" in history
        assert "Interest earned:" in history[2]  # El tercer elemento contiene el interés


class TestUtilityFunctions:
    """Clase de pruebas para las funciones auxiliares"""
    
    @pytest.fixture
    def test_accounts(self):
        """Fixture con cuentas de prueba para funciones auxiliares"""
        accounts = [
            BankAccount("Low Balance", 500),
            BankAccount("Medium Balance", 2500),
            BankAccount("High Balance", 6000),
            BankAccount("Very High Balance", 10000)
        ]
        return accounts
    
    def test_calculate_total_balance(self, test_accounts):
        """Prueba el cálculo del balance total de múltiples cuentas"""
        expected_total = sum(account.balance for account in test_accounts)
        
        total = calculate_total_balance(test_accounts)
        
        assert total == expected_total
        assert total == 19000  # 500 + 2500 + 6000 + 10000
    
    def test_calculate_total_balance_empty_list(self):
        """Prueba el cálculo del balance total con lista vacía"""
        total = calculate_total_balance([])
        assert total == 0
    
    def test_find_high_balance_accounts(self, test_accounts):
        """Prueba la búsqueda de cuentas con balance alto"""
        threshold = 5000
        
        high_balance_accounts = find_high_balance_accounts(test_accounts, threshold)
        
        # Deben ser solo las cuentas con balance >= 5000
        expected_accounts = [acc for acc in test_accounts if acc.balance >= threshold]
        assert len(high_balance_accounts) == len(expected_accounts)
        
        # Verificar que todas las cuentas retornadas tengan balance >= threshold
        for account in high_balance_accounts:
            assert account.balance >= threshold
    
    def test_find_high_balance_accounts_custom_threshold(self, test_accounts):
        """Prueba la búsqueda con un umbral personalizado"""
        threshold = 2000
        
        high_balance_accounts = find_high_balance_accounts(test_accounts, threshold)
        
        # Deben ser las cuentas con balance >= 2000
        expected_count = 3  # Medium, High, Very High
        assert len(high_balance_accounts) == expected_count
    
    def test_find_high_balance_accounts_no_matches(self, test_accounts):
        """Prueba cuando ninguna cuenta cumple el umbral"""
        threshold = 20000  # Más alto que cualquier balance
        
        high_balance_accounts = find_high_balance_accounts(test_accounts, threshold)
        
        assert len(high_balance_accounts) == 0


class TestIntegrationScenarios:
    """Pruebas de integración que simulan escenarios reales"""
    
    def test_complete_banking_scenario(self):
        """Prueba un escenario completo de operaciones bancarias"""
        # Crear cuentas
        alice = BankAccount("Alice Johnson", 1000)
        bob = BankAccount("Bob Smith", 2000)
        
        # Operaciones básicas
        alice.deposit(500)
        alice.withdraw(200)
        
        # Cálculo de interés
        bob_interest = bob.calculate_interest()
        
        # Transferencia
        alice.transfer(bob, 300)
        
        # Verificaciones finales
        assert alice.balance == 1000  # 1000 + 500 - 200 - 300
        assert bob.balance == 2400  # 2000 + 100 (interés) + 300 (transferencia)
        assert bob_interest == 100  # 5% de 2000
        
        # Verificar historiales
        assert len(alice.transaction_history) == 4  # deposit, withdraw, transfer, + la del transfer
        assert len(bob.transaction_history) == 2  # interest, deposit from transfer
    
    def test_multiple_transfers_scenario(self):
        """Prueba múltiples transferencias entre varias cuentas"""
        accounts = [
            BankAccount("Account1", 1000),
            BankAccount("Account2", 1500),
            BankAccount("Account3", 2000)
        ]
        
        # Transferencias en cadena
        accounts[0].transfer(accounts[1], 200)  # Account1 -> Account2
        accounts[1].transfer(accounts[2], 300)  # Account2 -> Account3
        accounts[2].transfer(accounts[0], 100)  # Account3 -> Account1
        
        # Verificar balances finales
        assert accounts[0].balance == 900   # 1000 - 200 + 100
        assert accounts[1].balance == 1400  # 1500 + 200 - 300
        assert accounts[2].balance == 2200  # 2000 + 300 - 100
        
        # Verificar que el total se mantiene
        total_balance = calculate_total_balance(accounts)
        assert total_balance == 4500  # 1000 + 1500 + 2000


if __name__ == "__main__":
    # Ejecutar las pruebas si se ejecuta este archivo directamente
    pytest.main([__file__, "-v"])