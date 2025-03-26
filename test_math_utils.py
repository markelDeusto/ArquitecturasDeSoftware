import unittest
import math_utils

class TestUtils(unittest.TestCase):
    def test_es_primo(self):
        self.assertFalse(math_utils.es_primo(4)) #falso
        self.assertTrue(math_utils.es_primo(5)) #true
        self.assertEqual(math_utils.es_primo(-5), "No es posible devolver números primos.")
        
if __name__ == "__main__":
    unittest.main()