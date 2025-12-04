# tests/unit/test_operations.py
import pytest
from src.calculator.operations import add, subtract, multiply, divide

def test_add_positive_numbers():
    assert add(1, 2) == 3

def test_add_negative_numbers():
    assert add(-1, -2) == -3

def test_add_positive_and_negative_numbers():
    assert add(1, -2) == -1

def test_add_zero():
    assert add(0, 0) == 0

def test_add_float_numbers():
    assert add(0.1, 0.2) == pytest.approx(0.3)

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2

def test_subtract_positive_and_negative_numbers():
    assert subtract(5, -3) == 8

def test_subtract_zero():
    assert subtract(0, 0) == 0

def test_subtract_float_numbers():
    assert subtract(0.5, 0.2) == pytest.approx(0.3)

def test_multiply_positive_numbers():
    assert multiply(2, 3) == 6

def test_multiply_negative_numbers():
    assert multiply(-2, -3) == 6

def test_multiply_positive_and_negative_numbers():
    assert multiply(2, -3) == -6

def test_multiply_by_zero():
    assert multiply(5, 0) == 0

def test_multiply_float_numbers():
    assert multiply(2.5, 2) == 5.0

def test_divide_positive_numbers():
    assert divide(6, 3) == 2.0

def test_divide_negative_numbers():
    assert divide(-6, -3) == 2.0

def test_divide_positive_by_negative_numbers():
    assert divide(6, -3) == -2.0

def test_divide_float_numbers():
    assert divide(7.5, 2.5) == 3.0

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        divide(5, 0)
