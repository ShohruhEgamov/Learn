class Person:
	def __init__(self, first_name, last_name, age, email):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.email = email

	def get_info(self):
		return f"Ism sharifi: {self.first_name} {self.last_name}, yoshi: {self.age}, elektron manzili: {self.email}"

class Days(Person):
	def __init__(self, first_name, last_name, age, email, year, month, day):
		super().__init__(first_name, last_name, age, email)
		self.year = year
		self.month = month
		self.day = day

# Tug'olgan kunlarni chiqarish uchun
	def birth_day(self):
		return f"{self.year}-{self.month}-{self.day}"
	
# Bu yerda tugulgan kunlarini hisoblarini olish uchun
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

# Bu yerda hoyot yoli raqamiga asoslanib matinni qaytarish uchun
	def get_info_by_number(self, son):
		# Bu yerga txt ning joylashuvi beriladi
		fayl_nomi = "hayot_yoli.txt"
		with open(fayl_nomi, "r") as fayl:
			mazmun = fayl.read()

		holatlar = mazmun.split("#")
		holatlar_dict = {}
		for holat in holatlar[1:]:
			qatorlar = holat.split("\n")
			holat_soni = int(qatorlar[0].split()[0].replace('-', '').strip())
			holat_mazmuni = "\n".join(qatorlar[1:]).strip()
			holatlar_dict[holat_soni] = holat_mazmuni

		return holatlar_dict.get(son)

try:
# Ma'lumotlar kiritish
	ism = input("Ismingizni kiriting: ").title()
	familya = input("Familyangizni kiriting: ").title()
	yosh = int(input("Yoshingizni kiriting: "))
	mail = input("Elektron manzilingiz: ").lower()
	t_yil = int(input("Tug'ilgan yilingiz: "))
	t_oy = int(input("Tug'ilgan oy: "))
	t_kun = int(input("Tug'ilgan kun: "))

# Ma'lumotlarni Personga yuborish
	person = Days(ism, familya, yosh, mail, t_yil, t_oy, t_kun)
	print(person.get_info())
	print(f"Tug'ilgan kuni: {person.birth_day()}")
	life_path_number = person.get_life_path_number()
	print(f"Hayot Yo'li raqami: {life_path_number}")
	print(person.get_info_by_number(life_path_number))

except ValueError:
	# Xatolik
	print("Yil, oy, kun kiritishda butun sonlardan foydalaning")
