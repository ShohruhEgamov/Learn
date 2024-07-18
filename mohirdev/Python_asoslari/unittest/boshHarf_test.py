# 2. Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya
import unittest
from boshHarf import capitalize_first_letters

class TestCapitalizeFirstLetters(unittest.TestCase):
    def test_capitalize_first_letters(self):
        self.assertEqual(capitalize_first_letters(["hello", "world"]), ["Hello", "World"])
        self.assertEqual(capitalize_first_letters(["python", "programming"]), ["Python", "Programming"])
        self.assertEqual(capitalize_first_letters(["test", "case"]), ["Test", "Case"])
        self.assertEqual(capitalize_first_letters(["capitalize", "first"]), ["Capitalize", "First"])

if __name__ == "__main__":
    unittest.main()