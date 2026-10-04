import pytest
from src.calculator import fun1, fun2, fun3, fun4

def test_fun1():
    assert fun1(2, 3) == 5
    assert fun1(-1, 1) == 0

def test_fun2():
    assert fun2(5, 3) == 2
    assert fun2(0, 4) == -4

def test_fun3():
    assert fun3(2, 3) == 6
    assert fun3(-2, 3) == -6

def test_fun4():
    assert fun4(2, 3) == 10

@pytest.mark.parametrize("x, y, expected", [
    (1, 1, 2),
    (0, 0, 0),
    (-5, 5, 0),
])
def test_fun1_param(x, y, expected):
    assert fun1(x, y) == expected