# Sistema Bancario - Testing

Este proyecto contiene un sistema bancario simple con pruebas profesionales usando pytest.

## Estructura del Proyecto

```
├── BankAccount.py          # Código principal del sistema bancario
├── test/
│   └── test_bank_account.py # Suite completa de pruebas
├── requirements.txt        # Dependencias del proyecto
├── pytest.ini            # Configuración de pytest
└── README.md             # Este archivo
```

## Instalación

1. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución de Pruebas

### Comandos Básicos

```bash
# Ejecutar todas las pruebas
pytest

# Ejecutar con output más detallado
pytest -v

# Ejecutar una clase específica de pruebas
pytest test/test_bank_account.py::TestBankAccount

# Ejecutar un método específico
pytest test/test_bank_account.py::TestBankAccount::test_successful_deposit
```

### Reportes de Cobertura

```bash
# Generar reporte de cobertura en terminal
pytest --cov=BankAccount

# Generar reporte de cobertura en HTML
pytest --cov=BankAccount --cov-report=html

# Ver el reporte HTML (se crea en htmlcov/index.html)
open htmlcov/index.html
```

### Reportes HTML

```bash
# Generar reporte HTML de las pruebas
pytest --html=report.html --self-contained-html
```

### Ejecución en Paralelo

```bash
# Ejecutar pruebas en paralelo (más rápido para suites grandes)
pytest -n auto
```

## Tipos de Pruebas Incluidas

### 1. **Pruebas Unitarias** (`TestBankAccount`)
- Inicialización de cuentas
- Depósitos válidos e inválidos
- Retiros válidos e inválidos
- Cálculo de intereses
- Transferencias entre cuentas
- Historial de transacciones

### 2. **Pruebas de Funciones Auxiliares** (`TestUtilityFunctions`)
- Cálculo de balance total
- Búsqueda de cuentas con balance alto
- Manejo de casos edge (listas vacías, sin coincidencias)

### 3. **Pruebas de Integración** (`TestIntegrationScenarios`)
- Escenarios completos de operaciones bancarias
- Múltiples transferencias entre cuentas
- Verificación de consistencia de datos

## Características de las Pruebas

- **Fixtures**: Reutilización de datos de prueba
- **Parametrización**: Pruebas con múltiples datos de entrada
- **Assertions claras**: Verificaciones específicas y descriptivas
- **Cobertura completa**: Pruebas para casos normales y edge cases
- **Documentación**: Cada prueba está documentada con su propósito

## Comandos Útiles para Desarrollo

```bash
# Ejecutar solo las pruebas que fallaron en la última ejecución
pytest --lf

# Ejecutar pruebas hasta que una falle
pytest -x

# Ejecutar en modo watch (requiere pytest-watch)
pytest-watch

# Ejecutar con profiling para identificar pruebas lentas
pytest --durations=10
```

## Buenas Prácticas Implementadas

1. **Separación clara**: Código de producción separado de las pruebas
2. **Nomenclatura descriptiva**: Nombres de métodos que explican qué se prueba
3. **Fixtures reutilizables**: Configuración compartida entre pruebas
4. **Assertions específicas**: Verificaciones claras y precisas
5. **Casos edge**: Pruebas para casos límite y errores
6. **Documentación**: Cada clase y método está documentado

## Ejemplo de Salida

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