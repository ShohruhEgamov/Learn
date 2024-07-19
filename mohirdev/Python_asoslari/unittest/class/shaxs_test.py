import unittest
from shaxs import Shaxs,Talaba,Fan

class ShaxsTest(unittest.TestCase):
	def setUp(self):
		self.ism = 'Shohruh'
		self.familya = 'Egamov'
		self.tyil = 2000
		self.bosqich = 1
		self.nomi = 'Matematika'
		self.talabalar = []
		self.inson = Shaxs(self.ism, self.familya, self.tyil)
		self.talaba = Talaba(self.ism, self.familya, self.tyil)
		self.fan = Fan(self.nomi)
		self.talaba1 = Talaba("Shohruh", "Egamov", 2000)
		self.talaba2 = Talaba("Farrux", "Egamov", 2001)
	
	# IChida shu elementlar bormi yoki yoqligini bildiradi
	def test_shaxs(self):
		self.assertIsNotNone(self.inson.ism)
		self.assertIsNotNone(self.inson.familya)
		self.assertIsNotNone(self.inson.tyil)

	# Endi Get infoni test qilamiz
	def test_info(self):
		inson_info = 'Shohruh Egamov. Tug\'ilgan yil: 2000'
		self.assertEqual(inson_info, self.inson.get_info())

	# Endi talaba clasini tekshiramiz
	def test_talaba(self):
		self.assertIsNotNone(self.talaba.ism)
		self.assertIsNotNone(self.talaba.familya)
		self.assertIsNotNone(self.talaba.tyil)

	# Endi get Full name test qilamiz
	def test_full_name(self):
		talaba_ful = "Shohruh Egamov"
		self.assertEqual(talaba_ful, self.talaba.get_fullname())

	# Talabaga qoshish
	def test_talaba_init(self):
		self.assertEqual(self.talaba.ism, self.ism)
		self.assertEqual(self.talaba.familya, self.familya)
		self.assertEqual(self.talaba.tyil, self.tyil)
		self.assertEqual(self.talaba.bosqich, 1)

	# Endi get infoni tekshiramiz
	def test_get_info(self):
		talaba_get = 'Shohruh Egamov. 1-bosqich talabasi'
		self.assertEqual(talaba_get, self.talaba.get_info())
	
	# Bu yerda kurs qoshish
	def test_talaba_update_bosqich(self):
		if self.talaba.update_bosqich():
			return self.assertEqual(self.talaba.bosqich, 2)
		
	# Bu yerda Fanni test qilamiz
	def test_fan_init(self):
		self.assertEqual(self.fan.nomi, self.nomi)
# #...................................................................#
# # 	Bu yerda talabalar royxatini shakilantiramiz					#
# 	def test_fan_add_s(self):										#
# 		new_talaba = 'Farrux Egamov'								#
# 		self.fan.add_student(new_talaba)							#
# #...................................................................#
	# Bu yerda ful name
	# def test_full_name(self):
	# 	misol = 'Fan: Matematika, Talabalar: Shohruh Egamov'
	# 	self.assertEqual(misol, self.fan.get_info())
	# Bu yerda esa tegishlimi yo'qmi aniqlaymiz

	def test_is_instance(self):
		self.assertTrue(isinstance(self.inson, Shaxs))
		self.assertTrue(isinstance(self.talaba, Shaxs))
		self.assertTrue(isinstance(self.talaba, Talaba))
		self.assertFalse(isinstance(self.fan, Talaba))

	# Bu yerda talaba qoshamiz
	def test_add_student(self):
		self.fan.add_student(self.talaba1)
		self.assertIn(self.talaba1, self.fan.talabalar)
		self.assertEqual(len(self.fan.talabalar), 1)

	# Bu yerda talabalar royhati
	def test_get_talabalar(self):
		self.fan.add_student(self.talaba1)
		self.fan.add_student(self.talaba2)
		talabalar = self.fan.get_talabalar()
		self.assertEqual(talabalar, ["Shohruh Egamov", "Farrux Egamov"])

	# Bu yerda get infoni tekshiramiz
	def test_get_info(self):
		self.fan.add_student(self.talaba1)
		self.fan.add_student(self.talaba2)
		info = self.fan.get_info()
		self.assertEqual(info, "Fan: Matematika, Talabalar: Shohruh, Farrux")
unittest.main()


