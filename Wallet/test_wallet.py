import pytest
from wallet import Wallet, InsufficientAmount

"""
fixture functions are created by marking them with the @pytest.fixture decorator.
Test functions that require fixtures should accept them as arguments.
For example, for a test to receive a fixture called wallet, it should have an argument with the fixture name, wallet.
"""
@pytest.fixture
def empty_wallet():
    ''' Returns a testes instance with a zero balance'''
    return Wallet()

@pytest.fixture
def wallet():
    '''Returns a testes instance with a balance of 20'''
    return Wallet(20)

def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet):
    assert wallet.balance == 100

def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance == 100

def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)