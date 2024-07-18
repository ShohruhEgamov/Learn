# 1. Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya
import unittest
from juftTop import juft_sonlar

class TestJuftSonlar(unittest.TestCase):
    def test_juft_sonlar(self):
        self.assertEqual(juft_sonlar([1, 2, 3, 4, 5]), [2, 4])
        self.assertEqual(juft_sonlar([10, 15, 20, 25]), [10, 20])
        self.assertEqual(juft_sonlar([0, -2, -3, -4]), [0, -2, -4])
        self.assertEqual(juft_sonlar([]), [])

if __name__ == "__main__":
    unittest.main()
