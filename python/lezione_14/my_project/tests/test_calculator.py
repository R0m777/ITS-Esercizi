from my_project.calculator import Calculator
import pytest


'''def test_addition():
    calculation: Calculator = Calculator(10,5)
    assert calculation.addition() == 13, 'the sum is wrong'

def test_subbtraction():
    calculation: Calculator = Calculator(10,5)
    assert calculation.subtraction() == 5, 'the sub is wrong'

def test_multiplication():
    calculation: Calculator = Calculator(10,5)
    assert calculation.multiplication() == 50, 'the multtip is wrong'

def test_division():
    calculation: Calculator = Calculator(10,5)
    assert calculation.division() == 2.00, 'the quo is wrong'
    '''
@pytest.fixture
def calculation():
    return Calculator(10,5)

def test_addition(calculation):
    assert calculation.addition() == 13, 'the sum is wrong'

def test_subbtraction(calculation):
    assert calculation.subtraction() == 5, 'the sub is wrong'

def test_multiplication(calculation):
    assert calculation.multiplication() == 50, 'the multtip is wrong'

def test_division(calculation):
    assert calculation.division() == 2.00, 'the quo is wrong'