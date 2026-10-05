import unittest
from src.calculator import fun1, fun2, fun3, fun4, fun5


class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        """Test addition"""
        self.assertEqual(fun1(2, 3), 5)
        self.assertEqual(fun1(-1, 1), 0)

    def test_fun2(self):
        """Test subtraction"""
        self.assertEqual(fun2(5, 3), 2)

    def test_fun3(self):
        """Test multiplication"""
        self.assertEqual(fun3(2, 3), 6)
        self.assertEqual(fun3(7, 0), 0)

    def test_fun4(self):
        """Test combined function"""
        self.assertEqual(fun4(2, 3), 10)

    def test_fun5(self):
        """Test division"""
        self.assertEqual(fun5(6, 3), 2)

    def test_fun5_divide_by_zero(self):
        """Division by zero should raise an error"""
        with self.assertRaises(ZeroDivisionError):
            fun5(1, 0)

    def test_float_addition(self):
        """Use assertAlmostEqual for floats"""
        self.assertAlmostEqual(fun1(0.1, 0.2), 0.3)


if __name__ == "__main__":
    unittest.main()