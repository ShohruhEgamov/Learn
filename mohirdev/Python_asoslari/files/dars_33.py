#!!! Quyidagi usul tavsiya qilinmaydi
# try:
#     file = open("F:\Learn\mohirdev\Python_asoslari\/files\pi.txt")  # Faylni ochish 
#     PI = file.read()  # Faylni o'qish
#     print(PI)  # Fayl tarkibini chop etish
#     file.close()  # Faylni yopish
# except FileNotFoundError:
#     print("Fayl topilmadi, iltimos fayl yo'lini tekshiring.")


##....................................Boshqa usuli haqida
try:
# Bu try: xatolikni boshqarish uchun
	with open("F:\Learn\mohirdev\Python_asoslari\/files\pi.txt") as pi_file: # Bu yerda matindan qaytgan obj ni faylga yukladik
		pi = pi_file.read()
# Qachonki widthdan chiqib ketsak fayl yopiladi
	# print(pi)

	pi = pi.rstrip()
	pi = pi.replace("\n", "")
	pi = float(pi)
	# print(pi)


 	# filename = 'F:\Learn\mohirdev\Python_asoslari\/files\data\/talabalar.txt'
	filename = "data/talabalar.txt"
	with open(filename) as file:
		for line in file:
			print(line)

	with open(filename) as file:
		talabalar = file.readlines()

	print(talabalar)

# bu yerda har bir talabaning oxiridagi bosh joy olib tasjlanadi
	talabalar = [talaba.rstrip() for talaba in talabalar] 
	print(talabalar)

except FileNotFoundError:
# Bu esa Xatolikga javob yozish uchun
     print("Fayl topilmadi, iltimos fayl yo'lini tekshiring.")