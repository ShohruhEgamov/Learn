import unittest
from cars import Car
class CarTest(unittest.TestCase):
    def setUp(self):
        make = "GM"
        self.model = "Malibu"
        year = 2020
        self.price = 40000
        self.km = 10000
        self.avto1 = Car(make, self.model, year)
        self.avto2 = Car(make, self.model, year, price=self.price)

    def test_create(self):
        # Qiymatlar mavjudligini assertIsNotNone metodi bilan tekshiramiz
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertEqual(self.model, self.avto1.model)
        self.assertIsNotNone(self.avto1.year)
        # Qiymat mavjud emasligini assertIsNone metodi bilan tekshiramiz
        self.assertIsNone(self.avto1.price)
        # Qiymat tengligini assertEquals metodi bilan tekshiramiz
        self.assertEqual(0, self.avto1.get_km())
        # avto2 narhini tekshiramiz
        self.assertEqual(self.price, self.avto2.price)

    def test_set_price(self):
        new_price = 45000
        self.avto2.set_price(new_price)
        self.assertEqual(new_price, self.avto2.price)

    def test_add_km(self):
        # 1 Musbat qiymat berib ko'ramiz
        self.avto1.add_km(self.km)
        self.assertEqual(self.km, self.avto1.get_km())
        self.avto1.add_km(5000)
        self.assertEqual(15000, self.avto1.get_km())
        # 2 Manfiy qiymat berib ko'ramiz
        new_km = 5000
        try:
            self.avto1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)
            
    def test_get_info(self):
        avto1_info = 'GM Malibu, 2020-yil, 0km yurgan.'
        self.assertEqual(avto1_info,self.avto1.get_info())
        # avto1 narhi va km o'zgartiramiz
        self.avto1.set_price(50000)
        self.avto1.add_km(20000)
        avto1_info = 'GM Malibu, 2020-yil, 20000km yurgan. Narhi: 50000'
        self.assertEqual(avto1_info,self.avto1.get_info())
unittest.main