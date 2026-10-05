# Calculator functions
def fun1(x, y):
    """Returns the sum of x and y"""
    return x + y


def fun2(x, y):
    """Returns x minus y"""
    return x - y


def fun3(x, y):
    """Returns the product of x and y"""
    return x * y


def fun4(x, y):
    """Returns the sum of fun1, fun2 and fun3"""
    return fun1(x, y) + fun2(x, y) + fun3(x, y)


def fun5(x, y):
    """Returns x divided by y, raises an error if y is 0"""
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y


if __name__ == "__main__":
    # Quick check when running this file directly
    print("fun1(2, 3) =", fun1(2, 3))
    print("fun2(2, 3) =", fun2(2, 3))
    print("fun3(2, 3) =", fun3(2, 3))
    print("fun4(2, 3) =", fun4(2, 3))
    print("fun5(6, 3) =", fun5(6, 3))