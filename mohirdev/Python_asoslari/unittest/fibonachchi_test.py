# 4. Berilgan son Fibonachchi ketma-ketligida uchraydimi (True) yoki yo'q (False) qaytaruvchi funksiya
import unittest
from fibonachchi import is_fibonacci

class TestIsFibonacci(unittest.TestCase):
    def test_is_fibonacci(self):
        self.assertTrue(is_fibonacci(0))
        self.assertTrue(is_fibonacci(1))
        self.assertTrue(is_fibonacci(5))
        self.assertTrue(is_fibonacci(13))
        self.assertFalse(is_fibonacci(4))
        self.assertFalse(is_fibonacci(10))
        self.assertFalse(is_fibonacci(20))

if __name__ == "__main__":
    unittest.main()