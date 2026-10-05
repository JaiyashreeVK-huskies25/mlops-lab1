import pytest
from src.calculator import fun1, fun2, fun3, fun4, fun5


@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_fun1(x, y, expected):
    """Test addition with positive, negative and zero values"""
    assert fun1(x, y) == expected


def test_fun2():
    """Test subtraction"""
    assert fun2(5, 3) == 2
    assert fun2(0, 4) == -4


def test_fun3():
    """Test multiplication, including by zero and negatives"""
    assert fun3(2, 3) == 6
    assert fun3(-2, 3) == -6
    assert fun3(7, 0) == 0


def test_fun4():
    """Test combined function: (2+3) + (2-3) + (2*3) = 10"""
    assert fun4(2, 3) == 10
    assert fun4(0, 5) == 0


def test_fun5():
    """Test division"""
    assert fun5(6, 3) == 2
    assert fun5(1, 4) == 0.25


def test_fun5_divide_by_zero():
    """Division by zero should raise an error"""
    with pytest.raises(ZeroDivisionError):
        fun5(1, 0)


def test_float_addition():
    """0.1 + 0.2 is not exactly 0.3 in Python, so use approx"""
    assert fun1(0.1, 0.2) == pytest.approx(0.3)