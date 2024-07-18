import pickle
try:
    # file = open("F:\Learn\mohirdev\Python_asoslari\/files\matn.txt")  # Faylni ochish 
    file = open("F:\Learn\mohirdev\Python_asoslari\/files\/amalyot\pi_milliyon_digits.txt")
    matn = file.read()  # Faylni o'qish
    # print(matn)  # Fayl tarkibini chop etish
    matn = matn.rstrip()
    matn = matn.replace('\n', '')
    matn = matn.replace(' ', '')
    # Bu yerda agar bolsa true bolmasa false qaytaradi 
    b = '01021975'
    # print(b in matn)
    file.close()  # Faylni yopish
    
    matn = float(matn)
    
	# Bu yerda pickle faylga joylashtirdik
    with open('F:\Learn\mohirdev\Python_asoslari\/files\/amalyot\pi_float.dat','wb') as file:
     	pickle.dump(matn,file)
except FileNotFoundError:
    print("Fayl topilmadi, iltimos fayl yo'lini tekshiring.")
    

while True: #False bolguncha ishlaydi
    kitob = input("Yaxshi koʻrgan kitobingizni kiriting (to'xtash uchun Enter bosing): ")
    # Bu yerda kitobdan boshqa narsa bolsa to'xtaydi
    if not kitob:
        break
    # Bu yerda kirtish uchun
    with open('F:\Learn\mohirdev\Python_asoslari\/files\/amalyot\/books.txt', "a") as file:
        file.write(kitob + "\n")