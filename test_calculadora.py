
import unittest
from calculadora import suma, resta, multiplicacion, division

class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
    
    def test_resta(self):
        self.assertEqual(resta(5, 3), 2)
    
    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(4, 3), 12)
    
    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(10, 0), "Error: División por cero")

if __name__ == '__main__':
    unittest.main()
