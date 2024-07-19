

class Shaxs:
    def __init__(self, ism, familya, tyil):
        self.ism = ism
        self.familya = familya
        self.tyil = tyil
    
    def get_fullname(self):
        return f"{self.ism} {self.familya}"

class Talaba(Shaxs):
    def __init__(self, ism, familya, tyil):
        super().__init__(ism, familya, tyil)

class Fan:
    def __init__(self, nomi):
        self.nomi = nomi
        self.__talabalar = []

    def add_student(self, talaba):
        self.__talabalar.append(talaba)

    def get_talabalar(self):
        return [talaba.get_fullname() for talaba in self.__talabalar]

    def get_info(self):
        talabalar = ", ".join([talaba.get_fullname() for talaba in self.__talabalar])
        return f"Fan: {self.nomi}, Talabalar: {talabalar}"


# Bu yoqida test
import unittest

class TestFan(unittest.TestCase):
    def setUp(self):
        self.fan = Fan("Matematika")
        self.talaba1 = Talaba("Shohruh", "Egamov", 2000)
        self.talaba2 = Talaba("Farrux", "Egamov", 2001)

    def test_add_student(self):
        self.fan.add_student(self.talaba1)
        self.assertIn(self.talaba1, self.fan._Fan__talabalar)  # Yashirin xususiyatga kirish
        self.assertEqual(len(self.fan._Fan__talabalar), 1)

    def test_get_talabalar(self):
        self.fan.add_student(self.talaba1)
        self.fan.add_student(self.talaba2)
        talabalar = self.fan.get_talabalar()
        self.assertEqual(talabalar, ["Shohruh Egamov", "Farrux Egamov"])

    def test_get_info(self):
        self.fan.add_student(self.talaba1)
        self.fan.add_student(self.talaba2)
        info = self.fan.get_info()
        self.assertEqual(info, "Fan: Matematika, Talabalar: Shohruh Egamov, Farrux Egamov")

if __name__ == "__main__":
    unittest.main()
