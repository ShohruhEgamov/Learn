import unittest # Test qilish uchun 
from name import get_full_name # Kerak funksiyani import qilaasiz


class NameTest(unittest.TestCase): # Doim shunday yoziladi
    def test_toliq_ism(self): # Bu har doim test bolib boshlanishi kerak
        formatted_name = get_full_name("alijon", "valiyev") # bu qaysi malumotni berish
        self.assertEqual(formatted_name, "Alijon Valiyev") # Bu yerda kutayotgan javobimiz

    def test_toliq_ism_otasi(self):
        name = get_full_name("hasan", "husanov", "olimovich")
        self.assertEqual(name, "Hasan Olimovich Husanov")


# if __name__ == '__main__':
# unittest.main()
unittest.main() # Bu esa ishlatish uchun beriladi