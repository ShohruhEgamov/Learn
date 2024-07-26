import json

class Person:
	def __init__(self,name,firstname,age,email): 
		self.name = name
		self.firstname= firstname
		self.age = age
		self.email = email

# To'liq ism familyasi
	def get_info(self):
		return f"Ism sharifi {self.name} {self.firstname} yoshi {self.age} da. Elektron manzili {self.email}."

class Days(Person):
		def __init__(self,name,firstname,age,email,year, month, day,):
			super().__init__(name,firstname,age,email)
			self.year = year
			self.month = month
			self.day = day

# Tug'ilgan kuni
		def birth_day(self):
			return f"{self.year}-{self.month}-{self.day}"

# Tu'g'ilgan kunini (life_path_number) qilish
		def get_life_path_number(self):
			def t_sum(n):
				return sum(int(toplam) for toplam in str(n))

			day_sum = t_sum(self.day)
			month_sum = t_sum(self.month)
			year_sum = t_sum(self.year)

			total_sum = day_sum + month_sum + year_sum

			while total_sum >= 10:
				total_sum = t_sum(total_sum)

			return total_sum

	# Bu yerda raqamga mos hususiyatlar
		def get_info_by_number(self, data):
			life_path_number = self.get_life_path_number()
			return data.get(str(life_path_number), "Noma'lum raqam")
		
	# JSON faylni ochish
		def read_data_from_txt(file_path):
			data = {}
			with open(file_path, 'r', encoding='utf-8') as f:
				for line in f:
					key, value = line.strip().split(' ', 1)
			data[key] = value
			return data
		data = read_data_from_txt("F:/Learn/mohirdev/Python_asoslari/oop/hayot_yoli.txt")
try:
	# Ma'lumotlar kiritish
	ism = input("Ismingizni kiriting: ").title()
	familya = input("Familyangizni kiriting: ").title()
	yosh = int(input("Yoshingizni kiriting: "))
	mail = input("Elektron manzilingiz: ").lower()
	t_yil = int(input("Tug'igan yilingiz: "))
	t_oy = int(input("Tug'ulgan oy: "))
	t_kun = int(input("Tug'ulgan kun: "))

	# Ma'lumotlarni Personga yuborish
	person = Days(ism, familya, yosh, mail, t_yil, t_oy, t_kun)
	print(person.get_info())
	print(f"Tug'ilgan kuni: {person.birth_day()}")
	print(f"Life path number: {person.get_life_path_number()}")
	print(person.get_info_by_number())

except ValueError:
	# Xatolik
	print("yil, oy, kun kiritishda butun sonlardan foydalaning")




# import json

# class Person:
#     def __init__(self, first_name, last_name, age, email):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.email = email

#     def get_info(self):
#         return f"Ism sharifi: {self.first_name} {self.last_name}, yoshi: {self.age}, elektron manzili: {self.email}"

# class Days(Person):
#     def __init__(self, first_name, last_name, age, email, year, month, day):
#         super().__init__(first_name, last_name, age, email)
#         self.year = year
#         self.month = month
#         self.day = day

#     def birth_day(self):
#         return f"{self.year}-{self.month}-{self.day}"

#     def get_life_path_number(self):
#         def t_sum(n):
#             return sum(int(toplam) for toplam in str(n))

#         day_sum = t_sum(self.day)
#         month_sum = t_sum(self.month)
#         year_sum = t_sum(self.year)

#         total_sum = day_sum + month_sum + year_sum

#         while total_sum >= 10:
#             total_sum = t_sum(total_sum)

#         return total_sum

#     def get_info_by_number(self):
#         life_path_number = self.get_life_path_number()
#         with open("F:/Learn/mohirdev/Python_asoslari/oop/hayot_yoli.json") as f:
#             data = json.load(f)
#         numbers = ["Rahbar", "Uygunlikni_izlovchi", "Muloqotchi", "Jamiyatning_band_arisi", "Erkin_qush", "Tarbiyachi", "Qidiruvchi", "Ozini_namoyon_qiluvchi_xojayin", "Gumanitar"]
#         return data["Hayot_Yoli"].get(numbers[life_path_number - 1])

# try:
#     # Ma'lumotlar kiritish
#     ism = input("Ismingizni kiriting: ").title()
#     familya = input("Familyangizni kiriting: ").title()
#     yosh = int(input("Yoshingizni kiriting: "))
#     mail = input("Elektron manzilingiz: ").lower()
#     t_yil = int(input("Tug'ilgan yilingiz: "))
#     t_oy = int(input("Tug'ilgan oy: "))
#     t_kun = int(input("Tug'ilgan kun: "))

#     # Ma'lumotlarni Personga yuborish
#     person = Days(ism, familya, yosh, mail, t_yil, t_oy, t_kun)
#     print(person.get_info())
#     print(f"Tug'ilgan kuni: {person.birth_day()}")
#     print(f"Life path number: {person.get_life_path_number()}")
#     print(person.get_info_by_number())

# except ValueError:
#     # Xatolik
#     print("Yil, oy, kun kiritishda butun sonlardan foydalaning")
