
# #####################################-------Python kurs------######################################

# sonlar = list(range(1,11))
# for son in sonlar:
#    print(f"{son} sonining kvadrati {son** 2} ga teng")

# son = int(input("Son kirit: "))
# print(f"{son} ni kvadrati {son**2} ga teng")

# dostlar = []
# print("5 ta eng yaqin do\'stingizni kiriting")
# for n in range(5):
#    dostlar.append(input(f"{n+1}-do\'stingizni kiriting "))
# print(dostlar)


# Kod = []
# print("Kod kiriting")

# for n in range(5):
#    Kod.append(input(f"{n+1} kodni kiriting: "))
# print(f"Kod {len(Kod)} marta takrorlandi")


# odam = int(input("Bugun nicha odam bilan gaplashding: "))
# otlari = []
# for n in range((odam)):
#     otlari.append(input(f"{n+1} odamlarni kiriting "))
# print(otlari)

# txt = "The best things in life are free!"
# x = input("soz kirit ")
# if x in txt:
#   print(f"Yes, {x} is present.")



# thislist = ["apple", "banana", "cherry"]
# a = int(input("son kirit "))
# b = input("soz kirit ")
# thislist[a] = b

# print(thislist)

# meva = ["apple", "banana", "cherry"]
# yangi =[x if x != "banana" else "orange" for x in meva]
# print(yangi)


# ismlar = ['Javohir', 'Zayniddin']

# print('Salom ' + ismlar[0] + ', bugun choyhona bormi?\n' + 
#      ismlar[1] + ', choyxonaga borasanmi')


# son = list(range(120,1200,2))

# print(sum(son))

# print(max(son))
# print(min(son))


# #...................................................................For stikli

# ismlar = ['Aziz', 'Olim', 'Anvar', 'Muzaffar', 'Oktam']
# for ism in ismlar:
#    print(f"Salom {ism}")
# print(f"Kod {len(ism)} marta takrolrlandi")



# sonlaar = list(range(11,100,2))
# for son in sonlaar:
#    print(son**3)
# print(sonlaar)


# korilgan = int(input("Nechta kino ko'rgansiz' "))
# kinolar = []
# print("Yaxshi ko`rgan kinoingiz: ")
# for x in range(korilgan):
#    kinolar.append(input(f"{x + 1} Kino nomini kiriting "))
# print(kinolar)


# #......................................................................is else
# login = input("Loginingizni kiriting: ")
# if login == "Admin":
#    print("Xush kelibsiz admin")
# else:
#    print(f'Xush kelibsiz {login}')


# a = input("Birinchi sonni kiriting: ")
# b = input("Ikkinchi sonni kiriting: ")
# if a == b:
#    print("Ikkalasi bir biriga teng")
# else:
#    print("Teng emas")



# #.................................................................. elif or and

# kun = input("Bu gun qaysi gun: ")
# harorat = float(input("Harorat nechi gradus: "))

# if kun.lower() == 'yakshanba' and harorat <=30:
#   print(f"Harorat {harorat} gradus cho'milishga kettik")
# elif  kun.lower() == 'yakshanba' and harorat >=30:
#    print(f"Harorat {harorat} gradus. bu hafli uyda otiramiz")
    

# son = int(input("Bironta juft son kiriting: "))

# if son % 2 == 0:
#    print('Bu juft son')
# else:
#    print('Bu juft son emas')
    

# yosh = int(input("Yoshingiz nechida: "))

# if (yosh <= 4 or yosh >= 60):
#    narx = 0
# elif yosh <= 18:
#    narx = 10000
# elif yosh >= 18:
#    narx = 20000

# print(f"Sizning blet pulingiz {narx} so'm")
    
    
    
# birinchi_son = int(input("Birinchi sonni kiriting: "))
# ikkinchi_son = int(input("ikkinchi sonni sonni kiriting: "))

# if birinchi_son > ikkinchi_son:
#    print(f"{birinchi_son} katta {ikkinchi_son} dan")
# else:
#    print(f"{birinchi_son} kichkina {ikkinchi_son} dan")
    
    
# mahsulotlar =  ['olma', 'shaftoli', 'anor', 'nok', 'behi', 'ananas', 'banan', 'olcha', 'kivi', 'tarvuz']
# savat = []
# bor_mahsulot = []
# yoq_mahsulot = []
# n = 5

# for x in range(n):
#    savat.append(input(f"{x + 1} chi meva: "))
# for meva in savat:
#    if meva in mahsulotlar:
#        print(f"Do'konimizda {meva} bor")
#        bor_mahsulot.append(meva)
#    else:
#        print(f"Do'konimizda {meva} yo'q")
#        yoq_mahsulot.append(meva)


# if len(yoq_mahsulot) == 0:
#    print("Siz so'ragan hamma narsa bor")
# else:
#    print(f"Bizning do'konda {yoq_mahsulot} mevalar yo'q")



# foydalanuvchilar = ['Shohruh', 'Farrux', 'Diyorbek', 'Bekmirza', 'Gulmira']
# foydalanuvchi = input('Nomingizni kiriting: ')

# if foydalanuvchi.capitalize() in foydalanuvchilar:
#    print("Bu nom band!")
# else:
#    print("Xush kelibsiz")

# son = int(input("Biron bir son kiriting: "))

# if (son % 2 == 0):
#    print(f"Bu {son} soni 2 ga qoldiqsiz bo'linadi")
# else:
#    print(f"Bu {son} soni 2 ga qoldiqli bo'linadi {son % 2}")




# #..............................................................Lug'atlar

# otam = {
#        'ism':'Shuxrat',
#       'familya': 'Ortikov',
#        'kasbi': 'o\'qtuvchi',
#       'yil': '1968'
#        }
# print(f"Otamning ismi {otam['ism']}, Familyasi {otam['familya']}, Kasbi {otam['kasbi']}, Tug'ilgan yili {otam['yil']}")


# inputn = str(input("Biron bir so'z kiriting: "))

# lugat = {
#    'olma': 'apple',
#    'nok' : 'grusha',
#    'float' : 'butun son',
#    'int' : 'sonli qiymat',
#    'str' : 'matinli qiymat'
#    }


# malumot = lugat.get(inputn, 'Bunday so\'z yo\'q')
# print(malumot)





# mahsulotlar = {
#     'non' : 1000,
#     'baliq' : 2000,
#     'olma' : 500,
#     'un' : 5600,
#     'gosht' : 80000
#     }
# bozorlik = ['anor', 'behi', 'olma', 'gosht']


# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} narxi {mahsulotlar[mahsulot]} so'm")

# for buyum in mahsulotlar:
#     if buyum not in bozorlik:
#         print(f"Iltimos, Do'koningizga {buyum} ham olib keling")




# #.............................................royhat va setlarni lugatlani bir biriga qoshish

# # Bu yerda for tsikli bilan 10 ra lug'at yaratamiz
# lasetti = []
# for n in range(10):
# 	new_car = {
# 		'model' : 'Lasetti',
# 		'rang' : None,
# 		'yil' : 2020,
# 		'narx' : None,
# 		'km' : 0,
# 		'korobka' : 'avto'
# 	}

# 	lasetti.append(new_car)


# # Bu ro'yhatga kirib ranglarini o'zgartirish uchun
# for m in lasetti[:3]:
# 	m['rang']='oq'

# for m in lasetti[3:6]:
# 	m['rang']='qora'

# for m in lasetti[6:]:
# 	m['rang']='mokriy asfalt'

# # Bu yerda 6 dan keyingilarnini karobkasini almashladik
# for m in lasetti[6:]:
# 	m['korobka']='mehanik'

# # Bu yerda korobkasiga qarab narxini baholadik
# for m in lasetti:
# 	if m ['korobka'] == 'avto':
# 		m['narx'] = 40000
# 	else:
# 		m['narx'] = 35000

# print(lasetti)



# # Bu yerda dasturchilar berilga va ularning qaysi tillarni bilishi
# # Lug'at ichidag royhatlar quydagicha ko'rinadi

# dasturchilar = {
# 	'ali' : ['python', 'c++'],
# 	'vali' : ['java', 'javascript'],
# 	'olim' : ['html', 'css', 'sass'],
# 	'gani' : ['php', 'go'],
# 	'azim' : ['R', 'c#'],
# }

# # bu yerda ism bu 0 elementlar yani ismlarni oladi
# # tillar degan esa royhatlari oladi 
# for ism, tillar in dasturchilar.items():
# 	print(f"\n{ism.title()} quydagi dasturlashni biladi: ")
# 	# Bu lug'at ichidagi ro'yhatlarni aylantirish uchun
# 	for til in tillar:
# 		print(til.upper())


# for ism, tillar in dasturchilar.items():
# 	print(f"\n{ism.title()} quydagi dasturlashni biladi: ", end='')
# 	# Bu lug'at ichidagi ro'yhatlarni aylantirish uchun
# 	for til in tillar:
# 		print(til.upper(), end=' ')  # bu end=' ' malumotlar bir birining izidan davom qilib chiqishi uchun


# #.....................................................lug'at ichidagi lugatlarga misollar
# hamkasblar = {
# 	'Shohruh':{
# 		'familya':'Egamov',
# 		't_yil':2000,
# 		'malumot':'oliy',
# 		'til':['Python', 'JavaScript', 'php'],
# 		'oylik': []
# 	},
# 	'Farrux':{
# 		'familya':'Egamov',
# 		't_yil':1998,
# 		'malumot':'oliy',
# 		'til':['Java', 'SQL'],
# 		'oylik': []
# 	},
# 	'Bekmirza':{
# 		'familya':'Egamov',
# 		't_yil':1996,
# 		'malumot':'oliy',
# 		'til':['html', 'css', 'bootstrap'],
# 		'oylik': []
# 	},
# 	'Diyorbek':{
# 		'familya':'Egamov',
# 		't_yil':1994,
# 		'malumot':'oliy',
# 		'til':['Kali', 'Linux'],
# 		'oylik': []
# 	},
# }
# #Bu yerda ismlar va malumotlar alohida olingan
# for ism, info in hamkasblar.items():
# 	print(f"\n {ism.title()} {info['familya'].title()},"
# 		f"{info['t_yil']}-yilda tug'ilgan, "
# 		f"Malumoti {info['malumot']}. \n"
# 		"Quyidagi dasturlash tillarini biladi:"
# 		)
# 	#Bu yerda agar dasturlash tilining ichida Python bolsa qimmat aks holda arzon
# 	a = info['oylik']
# 	t = info['til']
# 	for maosh in t:
# 			if 'Python' in maosh:
# 				a.append(400)
# 			else:
# 				a.append(300)
# 			print(f"{maosh.upper()}")
# 	def datsur_ucun_pul(nomi,haqqi):
# 		b = {}
# 		# b = []
# 		for nom,haq in zip(nomi,haqqi):
# 			# b.append(f"{nom} uchun {haq}") #Bu yerda royhatga yuborish uchun
# 			b[nom] = haq
# 			# bu royhatni (Kali: 300), (Linux: 300) Quyidagi korinishda chiqaradi
# 			format = ', '.join([f'({nom}: {haq}$)' 
# 				for nom,haq in b.items()])  
# 		return format
# 	tillar = t
# 	haqlar = a
# 	d = datsur_ucun_pul(tillar, haqlar)
# 	print(d)
# 	toplam = sum(a)
# 	print(f"Toplam oylik {toplam}")


# #...........................................................while loop

# son = 1
# while son <= 5:
# 	print(son, end=" ") # end bu izidan davom qilishlik uchun
# 	son += 1

# #.................................Soni kvadratini chiqaradigan dastur

# print("Sonning kvadratini beradigan dastur")
# savol = "Istalgan son kiriting "
# savol += ("dasturni to'xtatish uchun 'exit' yozing: ")
# qiymat = ""
# # while qiymat != 'exit':  #Bu exitgacha ishlaydi 
# while True:                #Bu esa abadiy davom etadi
# 	qiymat = input(savol)
# 	# if qiymat != 'exit':   # Bu exit ni yozganda to'xtashi uchun
# 	if qiymat == 'exit':
# 		break                # Bu yerda exit bolganda toxtaydi
# 	else:
# 		print(float(qiymat)**2)
# print('Dastur tugadi...')


# #.................................Bu juft yoki toq bilish uchun

# son = 0
# while son < 10:
# 	son += 1
# 	if son % 2 != 0:    # Bu toq bolsa chiqarmaydi va boshiga qaytadi
# 	# if son % 2 == 0:  # Bu juft bolsa chiqarmaydi va boshiga qaytadi
# 		continue
# 	else:
# 		print(son)

# #....................................kitob soraydigan dastur

# kitob = "Sevgan kitobingizni kiriting: "
# kitoblar = ""
# hammasi = []
# while True:
# 	kitoblar = input(kitob)
# 	if kitoblar == 'stop':
# 		break
# 	else:
# 		hammasi.append(kitoblar)
# print(hammasi)


# #....................................Kino teatirga chipta

# tamoshabin = "Yoshingiz nechida: "
# chiptalar = ""

# while True:
# 	chiptalar = input(tamoshabin)
# 	if chiptalar == 'exit' or chiptalar == 'quit':
# 		print("Chipta sotilishi toxtadi")
# 		break
# 	sonuchun = int(chiptalar)
# 	if sonuchun <= 7:
# 		print("Chipta narxi 2000 So'm" )
# 		continue
# 	elif 7<= sonuchun <= 18:
# 		print("Chipta narxi 3000 So'm" )
# 		continue
# 	if 18<= sonuchun <= 65:
# 		print("Chipta narxi 10000 So'm" )
# 		continue
# 	if sonuchun >= 65:
# 		print("Chipta narxi 0 So'm" )
# 		continue
# print('Raxmat')

# # While siklini o'rganamiz

# print("Yaqin do'stingizni ro'yxatini tuzamiz.")    #Bu yerda ism kiritamiz
# ismlar = []                                        # Bu yerda ro'yxat shakillanadi
# n = 1                                              # N = 1 boshlanishi
# while True:
#       ism = input(f"{n}-do'stingizni ismini kiriting: ")
#       ismlar.append(ism)
#       javob = input("Yana (ha/yo'q): ")
#       n += 1
#       if javob != 'ha':
#         break
# print(ismlar)


# dostlar = {}
# ishora = True
# while ishora:
# 	ism = input("Ismingizni kiriting: ")
# 	familiya = input("Familiyangizni kiriting: ")
# 	dostlar[ism] = familiya
# 	navbat = input("Yana (ha/yo'q): ")
# 	if navbat == "yo'q":
# 		ishora = False

# for ism, familiya in dostlar.items():
# 	print(f"{ism.title()} {familiya.title()}")


# # qiymatni o'chirish
# cars = ["lasetti", "Cobalt", 'nexia','matiz', 'nexia','damas']
# while 'nexia' in cars:
# 	cars.remove('nexia')
# print(cars)


# talabalar = ["hasan", "husan", "olim", "botir"]
# baholangan_talabalar = {}

# while talabalar:  # Bu yerda buni yozganimiz sababi bu boshamaguncha u davom qiladi
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = int(baho)


# # Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir 
# # qabul qilib, yangi ro'yxatga joylang.
# mahsulot = []
# n = 1
# while True:
# 	foydalanuvchi = (f"{n} mahsulotingizni yozing: ")
# 	mahsulot.append(input(foydalanuvchi))
# 	javob = input("Yana (ha/yo'q): ")
# 	n += 1
# 	if javob != 'ha':
# 		break
# print(mahsulot)


# # e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. 
# #Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.

# e_bozor = {}
# ishora = True
# while ishora:
# 	mahsulot = input("Mahsulotni kiriting: ")
# 	narxi = int(input("Narxini kiriting: "))
# 	e_bozor[mahsulot] = narxi
# 	navbat = input("Yana (ha/yo'q): ")
# 	if navbat == "yo'q":
# 		ishora = False

# for mahsulot, narxi in e_bozor.items():
# 	print(f"{mahsulot.title()} {narxi} so'm")


# # Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni 
# # e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). 
# # Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu 
# # mahsulot yo'q" degan xabarni kor'sating.

# buyurtmalar = ['olma','anjir','uzum','qovun']
# mahsulotlar = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000}

# while buyurtmalar:
# 	buyurtma = buyurtmalar.pop()
# 	if buyurtma in mahsulotlar.keys():
# 		print(f"{buyurtma.title()} {mahsulotlar[buyurtma]}")
# 	else:
# 		print(f"{buyurtma.title()} bizda yo'q")


# #............................................Funksiyalar

# #.__doc__ Bu hamma narsa haqida malumotni olish uchun

# # Yoshini topish
# def yosh_hisobla(ism, tugilgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2020-tugilgan_yil} yoshda")

# yosh_hisobla('olim',1997)


# def yosh_hisobla(tugilgan_yil, joriy_yil=2024):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")


# # yosh_hisobla(1995,2020)
# yosh_hisobla(2000)


# # Sonning kubini va kvadratini topish

# def Son_k(son):
# 	"""Sonning kubini va kvadratini topish"""
# 	print(f"Sonning kvadrati {son**2} va kubi {son**3}")
# son_kirit = int(input("Son kiriting: "))
# Son_k(son_kirit)

# # Bu yerda sonlarni kattasini chiqarish
# def katta_chiq(bir_son,ikki_son):
# 	"""Sonlarni kattasini chiqarish"""
# 	if bir_son > ikki_son:
# 		print(f"{bir_son} soni {ikki_son} sonidan katta")
# 	elif bir_son < ikki_son:
# 		print(f"{bir_son} soni {ikki_son} sonidan kichkina")
# 	else:
# 		print(f"{bir_son} soni {ikki_son} ga teng")
# bir_son = int(input("Birinchi son: "))
# ikki_son = int(input("Ikkinchi son: "))
# katta_chiq(bir_son,ikki_son)

# def sonlar():
# 	son1 = int(input("son kiriting"))
# 	son2 = int(input("son kiriting"))
# 	if son1 > son2:
# 		print(son1)
# 	elif son1 == son2:
# 		print("sonlar teng")
# sonlar()


# def bolinishlar():
# 	son = int(input("Son kiriting: "))
# 	for n in range(1,10):
# 		if son % n == 0:
# 			print(f"{son} soni {n} ga bolinadi")
# bolinishlar()

# # While bilan yasalishi

# def bolinishlar():
# 	son = int(input("Son kiriting: "))
# 	n = 1
# 	while n <= 10:
# 		if son % n == 0:
# 			print(f"{son} soni {n} ga bolinadi")
# 		n += 1
# bolinishlar()

# def toliq_ism_yasa(ism, familiya):
#     """Toliq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism


# talaba1 = toliq_ism_yasa("olim", "hakimov")
# talaba2 = toliq_ism_yasa("hakim", "olimov")
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
# print(f"{talaba1} darsga kechikib keldi")


# def toliq_ism_yasa(ism, familiya, otasining_ismi=""): # Bu yerdagi ='' bilan biz argumentlarni ixtiyoriy qilamiz
#     """Toliq isma qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()


# talaba1 = toliq_ism_yasa("olim", "hakimov")
# talaba2 = toliq_ism_yasa("hakim", "olimov", "abrorovich")
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")


# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {
#         "kompaniya": kompaniya,
#         "model": model,
#         "rang": rangi,
#         "korobka": korobka,
#         "yil": yili,
#         "narh": narhi,
#     }
#     return avto


# avto1 = avto_info("GM", "Malibu", "Qora", "Avtomat", 2018)
# avto2 = avto_info("GM", "Gentra", "Oq", "Mexanika", 2016, 15000)
# avtolar = [avto1, avto2]
# print("Onlayn bozordagi mavjud avtomashinalar:")
# for avto in avtolar:
#     if avto["narh"]:
#         narh = avto["narh"]
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")



# def oraliq(min, max,qadam=1):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += qadam
#     return sonlar


# print(oraliq(0, 10,2))
# print(oraliq(10, 21,3))


# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
# 	avto = {
# 			"kompaniya": kompaniya,
# 			"model": model,
# 			"rang": rangi,
# 			"korobka": korobka,
# 			"yil": yili,
# 			"narh": narhi,
# 		}
# 	return avto


# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar = []  # salondagi avtolar uchun bo'sh ro'yxat

# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting", end="")
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("Modeli: ")
#     rangi = input("Rangi: ")
#     korobka = input("Korobka: ")
#     yili = input("Ishlab chiqarilgan yili: ")
#     narhi = input("Narhi: ")
#     # Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida
#     # lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob == "no":
#         break

# print("\nSalonimizdagi avtolar:")
# for avto in avtolar:
#     if avto["narh"]:
#         narh = avto["narh"]
#     else:
#         narh = "Noma'lum"
#     print(
#         f"{avto['rang'].title()} {avto['model'].title()}, {korobka} korobka. Narhi: {narh}"
#     )

# def malumot(ism, familya, t_yili, t_joyi, tel, e_manzil,yosh=2024):
# 	malumotlar = {
# 		"ism": ism,
# 		"familya": familya,
# 		"t_yili": t_yili,
# 		"t_joyi": t_joyi,
# 		"tel": tel,
# 		"e_manzil": e_manzil,
# 		"yosh": yosh,
# 	}
# 	return malumotlar

# print("Siz haqingizdagi malumotlar")
# info = []

# while True:
# 	ism = input("Ismingiz: ")
# 	familya = input("Familyangiz: ")
# 	t_yili = int(input("Tug'ilgan yilingiz: "))
# 	t_joyi = input("Tug'ilgan joyingiz: ")
# 	tel = input("Telefon raqamingiz: ")
# 	e_manzil = input("Elektron manzilingiz: ")
# 	yosh = 2024 - int(t_yili)
# 	info.append(malumot(ism, familya, t_yili, t_joyi, tel, e_manzil, yosh))
# 	javob = input("Yana info qo'shasizmi? (yes/no): ")
# 	if javob == "no":
# 		break

# print("Shaxsiy Malumotlaringiz", end="")
# for i in info:
# 	print(f"\n{i['ism'].title()} {i['familya'].title()}, {i['t_yili']}-yilda {i['t_joyi']}da tug'ilgan {i['yosh']} yoshda. Telefon raqami:{i['tel']} {i['e_manzil']} bu elektronmanzil")




# def mijoz_info(ism, familiya, tyil, tjoy, email="", tel=None):
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     mijoz = {
#         "ism": ism,
#         "familiya": familiya,
#         "tyil": tyil,
#         "yoshi": 2020 - tyil,
#         "tjoy": tjoy,
#         "email": email,
#         "telefon": tel,
#     }
#     return mijoz


# print("Mijoz haqida ma'lumotlarni kiriting.")
# mijozlar = []
# while True:
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug'ilgan yili: "))
#     tjoy = input("Tug'ilgan joyi: ")
#     email = input("Email: ")
#     telefon = input("Telefon raqami: ")
#     mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
#     javob = input("Davom etasizmi? (ha/yo'q)")
#     if javob != "ha":
#         break
# print("Mijozlar:")
# for mijoz in mijozlar:
#     telefon = mijoz['telefon'] # Bu yerda agar telefon raqami bolmasa
#     if telefon:
#         telefon = mijoz['telefon']
#     else:
#         telefon = "Telefon raqami mavjud emas"  # bu yozuv chiqaradi
#     print(
#         f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
#         f"{mijoz['yoshi']} yoshda, telefoni: {telefon}"
#     )


# def kattasi(x,z,y):
# 	if x > z and x > y:
# 		print(f"{x} soni {z} va {y} dan katta")
# 	elif z > x and z > y:
# 		print(f"{z} soni {x} va {y} dan katta")
# 	elif y > x and y > z:
# 		print(f"{y} soni {x} va {z} dan katta")
# kattasi(4,5,6)


# def kattasi(x, y, z):
#     max = x
#     if y >= max:
#         max = y
#     if z >= max:
#         max = z
#     return max

# x = int(input("Son kirit "))
# y = int(input("Son kirit "))
# z = int(input("Son kirit "))
# print(kattasi(x, y, z))


# def aylana(radius, pi=3.14):
# 	aylana_info = {
# 		"radius": radius,
# 		"diametr": 2 * radius, # diametr radusni kvadratiga teng
# 		"perimetr": 2 * pi * radius, #parametr teng pini kvadrati va radiusni kopaytmasiga
# 		"yuza": pi * radius ** 2 # Yuza teng pini radiusga kopaytir va kvadratga kotar
# 	}
# 	return aylana_info
# aylana(5,3.14)

# def tub_sonlar(x):
# 	tub_sonlar = []
# 	for i in range(10):
# 		if i % x != 0:
# 			tub_sonlar.append(i)
# 	return tub_sonlar
# tub_sonlar(5)

# def tub_sonlar_top(min, max):
#     tub_sonlar = []
#     for n in range(min, max + 1):
#         tub = True
#         if n == 1:
#             tub = False
#         elif n == 0:
#             tub = True
#         else:
#             for x in range(2, n):
#                 if n % x == 0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)

#     return tub_sonlar
# tub_sonlar_top(1,10)

# def aylana_info(radius, pi=3.14159):
#     aylana = {
#         "radius": radius,
#         "diametr": 2 * radius,
#         "perimetr": 2 * radius * pi,
#         "yuza": pi * radius ** 2,
#     }
#     return aylana
# aylana_info(4)

# def tub_sonlar(min, max):
#   tub_sonlar = []
#   for n in range(min, max + 1):
#     tub = True
#     if n <= 1:  # 1 va 2 ni o'z ichiga olish uchun
#       tub = False
#     else:
#       for x in range(2, int(n**0.5) + 1):  # Ichki tsiklni optimallashtirish
#         if n % x == 0:
#           tub = False
#           break  # Bo'linuvchi topilsa, ichki tsiklni to'xtating
#     if tub:
#       tub_sonlar.append(n)
#   return tub_sonlar

# prime_numbers = tub_sonlar(1, 100)
# print(prime_numbers)  # Chiqish: [2, 3, 5, 7, 11]

# # Bu yerda shundayki agar tasodifiy son 0.5 ga kopayganda qoldiqli son chiqsa u juft boladi
# # Agar son hech qoldiqsiz bolsa tub boladi

# def financhain(n):
# 	sonlar = []
# 	for x in range(n):             # x = [0,1,2,3,4,5,6,7,8,9,10]
# 		if x == 0 or x == 1:
# 			sonlar.append(1)
# 		else:
# 			sonlar.append(sonlar[x-1] + sonlar[x-2])     # Bu yerda x ni aylantiradi
# 	return sonlar                                        # (sonlar[x-1] + sonlar[x-2]) bu metodda x ni navbatdagi sonidan 1 ni ayiradi [x-1]
# 														 # #  keyin ikkini ayiradi [x-2] va shu indexsda turgan sonlardagi sonlarni bir biriga 
# print(financhain(10))                                  # qoshadi (sonlar[x-1] + sonlar[x-2])

# # # Agar 0 bolsa 1 qoshiladi
# # # Agar 1 bolsa 1 qoshiladi
# # # agar 2 bolsa 'sonlar.append(sonlar[x-1] + sonlar[x-2])' Bu ishga tushadi yani
# # # sonlar[2 - 1] + sonlar[2-2]
# # # sonlar[1,1,2,3,4,5] Bu massiv sonlar[2 - 1] 1 ni chaqiradi yani 1 ni chaqiradi
# # # sonlar[1,1,2] Bu massiv sonlar[2 - 2] 0 ni chaqiradi yani 1 ni chaqiradi
# # # Ikkalasini qoshganda 2 boladi
# # # Matematikada Fibonachchi ketma-ketligi har bir raqam oldingi ikkitasining yig'indisi teng bo'lishi 
# a = [0,1,2,3,4,5,6,7,8,9,10]
# b = [1,1,2,3,5,8,13,21,34,55,89]
# print(b[9])
# print(b[8])

# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism] = int(baho)
#     return baholar


# talabalar = ["ali", "vali", "hasan", "husan"]
# baholar = bahola(talabalar[:]) # Agar bu  yerdan [:] Bunday belgi qoyilsa asil nusxasiham qoladi
# print(baholar)
# print(talabalar)



# def katta_harf(ism):
# 	ism = ism[:]
# 	for i in range(len(ism)):
# 		ism[i] = ism[i].title()
# 	return x
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# matin = katta_harf(ismlar)
# print(matin)
# print(ismlar)

# talabalar = ["ali", "vali", "hasan", "husan"]

# def bahola(ballar):
# 	baholar = {}
# 	for bal in ballar:
# 		baho = input(f"Talaba {bal.title()}ning bahosini kiriting: ")
# 		baholar[bal] = int(baho)
# 	return baholar

# baholar = bahola(talabalar)
# print(baholar)
# print(talabalar)

# def summa(*sonlar):
# 	yigindi = 0
# 	for son in sonlar:
# 		yigindi += son
# 	return yigindi

# print(summa(1,2,5,2,5,7))
# print(summa(1,2,5,2,5,7,8,6,9,45,4))
# print(summa(1,2,5,2,5,7,96,3,5,8))

# def kopaytma(*sonlar):
# 	natija = 1
# 	for son in sonlar:
# 		natija *= son
# 	return natija

# print(kopaytma(1,2,5,2,5,7))
# print(kopaytma(1,2,5,2,5,7,8,6,9,45,4))
# print(kopaytma(1,2,5,2,5,7,96,3,5,8))

# def talaba_info(ism, familiya, **kwargs):
# 	kwargs['ism'] = ism
# 	kwargs['familiya'] = familiya
# 	return kwargs
# a = int(input('Yilingiz: '))
# kasb = input('Kasbingiz: ').title()
# maosh = int(input('Oylik maoshingiz'))
# talaba = talaba_info('Shohruh', 'Egamov', yili = a, kasbi = kasb, maoshi = f'{maosh} $')
# print(talaba)

# for i in range(1, 6):
#   for j in range(1, i + 1):
#     print("*", end=" ")
#   print()


# #...............................lambada funksiyasi
# import math

# # def nom(argument):
# # 	return ifoda

# uzunlik = lambda pi, r : 2*pi*r
# print(uzunlik(math.pi,10))

# kvadrat = lambda x, y : x ** y
# print(kvadrat(3, 2))


# def daraja(n):
#     return lambda x: x ** n


# kvadrat = daraja(2)
# kub = daraja(3)


# #...............................map funksiyasi

# from math import sqrt  # sqrt - kvadrat ildiz

# sonlar = list(range(11))  # 0 dan 10 gacha sonlar ro'yxati
# ildizlar = list(map(sqrt,sonlar))
# print(ildizlar)


# def daraja2(x):
#     """Berilgan sonning kvadratini qaytaruvchi funksiya"""
#     return x*x

# print(list(map(daraja2,sonlar)))

# kvadratlar = list(map(lambda x: x * x, sonlar))
# print(kvadratlar)


# a = [4, 5, 6]
# b = [7, 8, 9]
# a_plus_b = list(map(lambda x, y: x + y, a, b))
# print(a_plus_b)

# ismlar = ['hasan','husan','olim','umid']
# print(list(map(lambda matn:matn.upper(),ismlar)))



# #...............................filter funksiyasi
# import random as r

# sonlar = r.sample(range(100), 10)  # 0-99 oralig'ida 10 ta tasodifiy sonlar
# print(sonlar)
# def juftmi(x):
#     """x juft bo'lsa True, aks holda False qaytaruvchu funksiya"""
#     return x % 2 == 0


# juft_sonlar = list(filter(juftmi,sonlar))
# print(juft_sonlar)

# juft_sonlar = list(filter(lambda x: x % 2 == 0, sonlar))
# print(juft_sonlar)

# mevalar = ["olma", "anor", "anjir", "shaftoli", "o'rik", "tarvuz", "qovun", "banan"]
# harf = "o"
# mevalar_b = list(filter(lambda meva: meva.startswith(harf), mevalar))  # Bu yerda startswith shu matn shu harf 
# print(mevalar_b)														# bilan boshlanadimi yoqmi aytadi

# mevalar2 = list(filter(lambda meva: len(meva) <= 5, mevalar))
# print(mevalar2)

# list(filter(lambda meva: (meva.startswith("a") and meva.endswith("r")), mevalar))

# # # sonlar = r.sample(range(100),10)
# # # juft = [son for son in sonlar if son%2==0]

# f1 = lambda x: x * 10
# print(f1(10))

# f2 = lambda x, y: x * y
# print(f2(5, 4))


# from random import sample
# from math import sqrt

# x = list(range(0, 1001))
# y = sample(x, k=100)   # Bu yerda k ning vazifasi qancha son olish
# print(y)

# ildizlar = list(map(lambda n: sqrt(n), y))
# print(ildizlar)

# toq_sonlar = list(filter(lambda n: n % 2 == 0, y))
# print(toq_sonlar)


# #...........................................................OOP darslari

# class Talaba:
#     """Talaba nomli klass yaratamiz"""

#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1

#     def get_name(self):
#         return self.ism

#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "

#     def set_bosqich(self, bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich

#     def update_bosqich(self):
#         """Talabanining bosqichini 1taga ko'paytirish"""
#         self.bosqich += 1

#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism

#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya

#     def get_fullname(self):
#         """Talabaning ism-familiyasini qaytaradi"""
#         return f"{self.ism} {self.familiya}"

#     def get_age(self, yil):
#         """Talabaning yoshini qaytaradi"""
#         return yil - self.tyil

#     def tanishtir(self):
#         print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")


# # talaba1 = Talaba("Alijon","Valiyev",2000)
# # print(talaba1.get_info())
# # talaba1.update_bosqich() # 1 bosqichga oshiramiz
# # print(talaba1.get_info())
# # talaba1.update_bosqich() # 1 bosqichga oshiramiz
# # print(talaba1.get_info())

# # # talaba1.set_bosqich(3)
# # # print(talaba1.bosqich)



# class Talaba:
#     """Talaba nomli klass yaratamiz"""

#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1

#     def set_bosqich(self, yangi_bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = yangi_bosqich # Bu yerda bosqichni funksiyasii

#     def update_bosqich(self):
#         """Talabanining bosqichini 1taga ko'paytirish"""
#         self.bosqich += 1    # Bu funksiya ishga tushganda 1dan kopayib borishi uchun

#     def get_info(self): # Bu yerda full ism chiqaradi
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi"

#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism 

#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya

#     def get_fullname(self):
#         """Talabaning ism-familiyasini qaytaradi"""
#         return f"{self.ism} {self.familiya}"

#     def get_age(self, yil):  # Bu yerda yoshni hisoblab chiqaradi
#         """Talabaning yoshini qaytaradi"""
#         return yil - self.tyil 


# class Fan:
#     """Fan nomli klass"""

#     def __init__(self, nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0  #Bu yerda talaba soni
#         self.talabalar = []  # Bu yerda talaba royhati

#     def add_student(self, talaba): # Bu yerda talabani royhatini va sonini shakillantiradi
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1

#     def get_name(self):
#         """Fan nomi"""
#         return self.nomi

#     def get_students(self):
#         """Fanga yozilgan talabalar haqida ma'lumot"""
#         return [talaba.get_fullname() for talaba in self.talabalar]

#     def get_students_num(self):
#         """Fanga yozilgan talabalar soni"""
#         return self.talabalar_soni


# def see_methods(klass): # Bu yerda metodlarni korish
#     return [method for method in dir(klass) if method.startswith("__") is False]

# # dir(class nomi) Bu yeda turli metodlarni chiqaradi

# matem = Fan("Oliy Matematika")
# talaba1 = Talaba("Alijon", "Valiyev", 2000)
# talaba2 = Talaba("Hasan", "Alimov", 2001)
# talaba3 = Talaba("Akrom", "Boriyev", 2001)
# matem.add_student(talaba1)
# matem.add_student(talaba2)
# matem.add_student(talaba3)

# # print(matem.talabalar_soni)
# print(matem.talabalar)
# mat_talabalar = matem.get_students()
# print(mat_talabalar)

# print(see_methods(Talaba))
# print(see_methods(talaba1))
# print(see_methods(str))
# print(talaba1.__dict__)
# print(talaba1.__dict__.keys())

# print(talaba1.get_info())
# print(matem.add_student())
# print(see_methods(Talaba))

# print(talaba1.set_bosqich())
# print(talaba1.update_bosqich())


# class Car:
#     def __init__(self, make, model, rang, korobka, narh):
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.korobka = korobka
#         self.narh = narh
#         self.km = 0

#     def get_make(self):
#         return self.make

#     def get_model(self):
#         return [moshna.get_model() for talaba in self.talabalar]

#     def get_rang(self):
#         return self.rang

#     def get_gear(self):
#         self.km += 1

# moshna = Car('GM','Lasetti', 'oq','mehanika',1150000)

# #.................................Bu yerda Shaxs malumot qaytaradigan metod

# class Shaxs:
#     """Shaxslar haqida ma'lumot"""

#     def __init__(self, ism, familiya, passport, tyil):
#         """Shaxsning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil

#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
#         return info

#     def get_age(self, yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil


# class Talaba(Shaxs):
#     """Talaba klassi"""

#     def __init__(self, ism, familiya, passport, tyil, idraqam, manzil,fanlar):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1
#         self.manzil = manzil
#         self.fanlar = []

#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam

#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich

#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
#         return info


# class Manzil:
#     """Manzil saqlash uchun klass"""

#     def __init__(self, uy, kocha, tuman, viloyat):
#         """Manzil xususiyatlari"""
#         self.uy = uy
#         self.kocha = kocha
#         self.tuman = tuman
#         self.viloyat = viloyat

#     def get_manzil(self):
#         """Manzilni ko'rish"""
#         manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
#         manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
#         return manzil
# class Fan(Talaba):
#     def __init__(self,matem,ingliztili):
#         self.matem = matem
#         self.ingliztili = ingliztili
        
        
# fan = Fan('oliy matematika', 'About my self')
# talaba1_manzil = Manzil(12, "Olmazor", "Bog'bon", "Samarqand")
# talaba1 = Talaba("Valijon", "Aliyev", "FA112299", 2000, "0000012", talaba1_manzil,fan)


# class Shaxs:
#     """Shaxslar haqida ma'lumot"""

#     def __init__(self, ism, familiya, passport, tyil):
#         """Shaxsning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil

#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
#         return info

#     def get_age(self, yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil


# class Talaba(Shaxs):
#     """Talaba klassi"""

#     def __init__(self, ism, familiya, passport, tyil, idraqam):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1

#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam

#     # def get_bosqich(self):
#     #     """Talabaning o'qish bosqichi"""
#     #     self.bosqich = 1
#     def get_bosqich_yangi(self):
#         """Talabaning o'qish bosqichi"""
#         self.bosqich += 1

#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"{self.bosqich}-bosqich. ID raqami: {self.idraqam}"
#         return info
    
# talaba1 = Talaba("Valijon", "Aliyev", "FA112299", 2000, "0000012")


# #....................................................uyga vazifa 30 dars

# class Shaxs:
#     def __init__(self, ism, familya, tyil):
#         self.ism = ism
#         self.familya = familya
#         self.tyil = tyil
    
#     def get_info(self):
#         return f"{self.ism} {self.familya}. Tug'ilgan yil: {self.tyil}"

# class Talaba(Shaxs): # Bu yerda Shaxsdan meros oladi
#     def __init__(self, ism, familya, tyil):
#         super().__init__(ism, familya, tyil)  # Bu yerda esa toliq merosiga egalik qiladi
#         self.fanlar = []

#     def tanishuv(self):
#         return f"Men {self.ism} {self.familya}. Tug'ilgan yilim {self.tyil}. Yoshim {2024 - self.tyil} da"

#     def fanga_yozil(self, fan):  # Bu yerda fanga yozilish uchun
#         self.fanlar.append(fan)
#         print(f"{self.ism} {fan.nomi} faniga yozildi.")

#     # def remove_fan(self, fan): # Bu yerda yozilgan fanlarni ochirish uchun
#     #     if fan in self.fanlar:
#     #         self.fanlar.remove(fan)
#     #         print(f"{self.ism} {fan.nomi} fanidan o'chirildi.")
#     #     else:
#     #         print("Siz bu fanga yozilmagansiz")
    
#     def get_yozilish(self):
#         return [self.nomi for fan in self.fanlar]
    
#     def get_info(self):
#         fanlar = ", ".join([fan.nomi for fan in self.fanlar])
#         return f"{self.ism} {self.familya}. Tug'ilgan yil: {self.tyil}. Yoshim {2024 - self.tyil} da. Yozilgan fanlar: {fanlar}"

# class Fan:
#     def __init__(self, nomi):
#         self.nomi = nomi

# # Voris klasslar
# class Professor(Shaxs):
#     def __init__(self, ism, familya, tyil, kafedra):
#         super().__init__(ism, familya, tyil)
#         self.kafedra = kafedra

#     def get_info(self):
#         return f"Professor {self.ism} {self.familya}. Tug'ilgan yil: {self.tyil}. Kafedra: {self.kafedra}"

# class Foydalanuvchi(Shaxs):
#     def __init__(self, ism, familya, tyil, login):
#         super().__init__(ism, familya, tyil)
#         self.login = login
    
#     def get_info(self):
#         return f"Foydalanuvchi {self.ism} {self.familya}. Tug'ilgan yil: {self.tyil}. Login: {self.login}"

# class Admin(Foydalanuvchi):
#     def __init__(self, ism, familya, tyil, login):
#         super().__init__(ism, familya, tyil, login)
    
#     def ban_user(self):
#         print("Foydalanuvchi bloklandi")

# # Testlar
# talaba = Talaba("Shohruh", "Egamov", 2000)  # Bu yerda Talabaga obyekt berish
# talaba2 = Talaba("Farruh", "Egamov", 1998)

# # Fan obyektlarini yaratish
# fan1 = Fan("Matematika")
# fan2 = Fan("Ingliz tili")  # Bu yerda esa Fan berish

# # Fanlarga yozilish
# talaba.fanga_yozil(fan1) 
# talaba.fanga_yozil(fan2) # bu yerda fanga yozilish

# # # Fanlarni olib tashlash
# # talaba.remove_fan(fan1)  # Bu yerda fanni ochirish
# # talaba.remove_fan(fan1)

# # get_info metodi
# print(talaba.get_info())
# print(talaba2.get_info())

# professor = Professor("Akmal", "Ismatov", 1975, "Fizika")
# print(professor.get_info())

# foydalanuvchi = Foydalanuvchi("Olim", "Karimov", 1990, "olim123")
# print(foydalanuvchi.get_info())

# admin = Admin("Sardor", "Xolmatov", 1985, "admin_sardor")
# print(admin.get_info())
# admin.ban_user()


# print(talaba.fanlar)
# fan3 = talaba.get_yozilish()
# print(fan3)


# #......................................................Bu yerda tuzatilgan varyanti


# class Shaxs:
#     def __init__(self, ism, familya, tyil):
#         self.ism = ism
#         self.familya = familya
#         self.tyil = tyil
    
#     def get_info(self):
#         return f"{self.ism} {self.familya}. Tug'ilgan yil: {self.tyil}"

# class Talaba(Shaxs):
#     def __init__(self, ism, familya, tyil):
#         super().__init__(ism, familya, tyil)
#         self.fanlar = []

#     def tanishuv(self):
#         return f"Men {self.ism} {self.familya}. Tug'ilgan yilim {self.tyil}. Yoshim {2024 - self.tyil} da"

#     def fanga_yozil(self, fan):
#         self.fanlar.append(fan)
#         print(f"{self.ism} {fan.nomi} faniga yozildi.")

#     def remove_fan(self, fan):
#         if fan in self.fanlar:
#             self.fanlar.remove(fan)
#             print(f"{self.ism} {fan.nomi} fanidan o'chirildi.")
#         else:
#             print("Siz bu fanga yozilmagansiz")
    
#     def get_info(self):
#         fanlar = ", ".join([fan.nomi for fan in self.fanlar])
#         return f"{self.ism} {self.familya}. Tug'ilgan yil: {self.tyil}. Yoshim {2024 - self.tyil} da. Yozilgan fanlar: {fanlar}"
    
#     def __str__(self):
#         fanlar = ", ".join([str(fan) for fan in self.fanlar])
#         return f"Talaba: {self.ism} {self.familya}, Fanlar: [{fanlar}]"

# class Fan:
#     def __init__(self, nomi):
#         self.nomi = nomi
    
#     def __str__(self):  # Bu yerda fanlarni royhatga qoshish uchun
#         return self.nomi

# # Voris klasslar
# class Professor(Shaxs):
#     def __init__(self, ism, familya, tyil, kafedra):
#         super().__init__(ism, familya, tyil)
#         self.kafedra = kafedra

#     def get_info(self):
#         return f"Professor {self.ism} {self.familya}. Tug'ilgan yil: {self.tyil}. Kafedra: {self.kafedra}"

# class Foydalanuvchi(Shaxs):
#     def __init__(self, ism, familya, tyil, login):
#         super().__init__(ism, familya, tyil)
#         self.login = login
    
#     def get_info(self):
#         return f"Foydalanuvchi {self.ism} {self.familya}. Tug'ilgan yil: {self.tyil}. Login: {self.login}"

# class Admin(Foydalanuvchi):
#     def __init__(self, ism, familya, tyil, login):
#         super().__init__(ism, familya, tyil, login)
    
#     def ban_user(self):
#         print("Foydalanuvchi bloklandi")

# # Testlar
# talaba = Talaba("Shohruh", "Egamov", 2000)
# talaba2 = Talaba("Farruh", "Egamov", 1998)

# # Fan obyektlarini yaratish
# fan1 = Fan("Matematika")
# fan2 = Fan("Ingliz tili")
# fan3 = Fan("Ona-tili")

# # Fanlarga yozilish
# talaba.fanga_yozil(fan1)
# talaba.fanga_yozil(fan2)
# talaba.fanga_yozil(fan3)
# talaba2.fanga_yozil(fan1)
# talaba2.fanga_yozil(fan2)
# talaba2.fanga_yozil(fan3)

# #Fanlarni olib tashlash
# # talaba.remove_fan(fan1)
# talaba.remove_fan(fan3)

# #get_info metodi
# print(talaba.get_info())
# print(talaba2.get_info())

# # __str__ metodi
# print(talaba)
# print(talaba2)

# # professor = Professor("Akmal", "Ismatov", 1975, "Fizika")
# # print(professor.get_info())

# # foydalanuvchi = Foydalanuvchi("Olim", "Karimov", 1990, "olim123")
# # print(foydalanuvchi.get_info())

# # admin = Admin("Sardor", "Xolmatov", 1985, "admin_sardor")
# # print(admin.get_info())
# # admin.ban_user()


# # fnx = talaba.__str__()
# # print(fnx)


# from uuid import uuid4 # Bu id berishi uchun


# class Avto:
#     """Avtomobil klassi"""

#     def __init__(self, make, model, rang, yil, narh, km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4() # Bu yerda kirib korib bolmasligi uchun

#     def get_km(self):
#         return self.__km # bu yerda km i ko'rish uchun

#     def get_id(self):
#         return self.__id #Bu yerda id ni ko'rish

#     def add_km(self, km):
#         """Mashinaning km ga yana km qo'shish"""
#         if km >= 0:
#             self.__km += km
#         else:
#             print("Mashina km kamaytirib bo'lmaydi")


# # avto1 = Avto("GM","Malibu","Qora",2020,40000,100000)
# # print(f"ID: {avto1.get_id()}")
# # avto1.add_km(1500)
# # print(avto1.get_km())



# from uuid import uuid4


# class Avto:
#     """Avtomobil klassi"""

#     __num_avto = 0

#     def __init__(self, make, model, rang, yil, narh, km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
#         Avto.__num_avto += 1

#     @classmethod
#     def get_num_avto(cls):  # incapsul bolgan __num_avto = 0 n korish uchun
#         return cls.__num_avto

#     def get_km(self):
#         return self.__km

#     def get_id(self):
#         return self.__id

#     def add_km(self, km):
#         """Mashinaning km ga yana km qo'shish"""
#         if km >= 0:
#             self.__km += km
#         else:
#             print("Mashina km kamaytirib bo'lmaydi")


# class Bus:
#     pass


# class Train:
#     pass

# avto = Avto("GM","Malibu","Qora",2020,40000)
# avto = Avto("GM","Malibu","Qora",2020,40000)
# print(Avto.get_num_avto())
# # #...........................................................32 Dars DONDR metodlar


class Avto:
    __num_avto = 0
    """Avtomobil klassi"""

    def __init__(self, make, model, rang, yil, narh):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1

    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
# Bu funksiyani vazifasi oqilishiga yordam beradi
# Bu yozilmasa <__main__.Avto at 0x1fdf9d9bc10> Bunday chgiqariladi

    def __str__(self):   
        """Obyekt haqida ma'lumot"""
        return f"Avto: {self.make} {self.model}. {self.narh}$"
# Bu ham __str__ ning turlaridan
# Eng yaxshisi bu
    def __repr__(self):
        """Obyekt haqida ma'lumot"""
        return f"Avto: {self.make} {self.model}. {self.narh}$"
# Taqqoslash metodlari
    def __eq__(self, boshqa_avto):
        return self.narh == boshqa_avto.narh

    def __lt__(self, boshqa_avto):
        return self.narh < boshqa_avto.narh

    def __le__(self, boshqa_avto):
        return self.narh <= boshqa_avto.narh

    def get_info(self):
        return (
            f"{self.rang} {self.make} {self.model}.{self.yil}-yil. Narhi:{self.narh}$"
        )


class AvtoSalon:
    """Avtosalon klassi"""

    def __init__(self, name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosaloni"

    def __len__(self):
        return len(self.avtolar)

# Bu yerda shu indexsdagi elementni qaytarish uvhun
    def __getitem__(self, index):
        return self.avtolar[index]
# Bu yerda ozgartirish uchun
    def __setitem__(self, index, value):
        if isinstance(value, Avto):
            self.avtolar[index] = value
            
    def __add__(self, qiymat):
        if isinstance(qiymat, AvtoSalon):
            yangi_salon = AvtoSalon(f"{self.name} {qiymat.name}")
            yangi_salon.avtolar = self.avtolar + qiymat.avtolar
            return yangi_salon
        elif isinstance(qiymat, Avto):
            self.add_avto(qiymat)
        else:
            print(f"AvtoSalon ga {type(qiymat)} qo`shib bo`lmaydi")

    def __call__(self, *param):
        if param:
            for avto in param:
                self.add_avto(avto)
        else:
            return [avto for avto in self.avtolar]
# Bu yerda biz avtasalonga moshina qoshamiz
    def add_avto(self, *qiymat):
        for avto in qiymat:
            #Bu reda ichida bolsa true bolmasa false qaytaradi
            if isinstance(avto, Avto): 
                self.avtolar.append(avto)
            else:
                print("Avto obyketini kiriting")

    def get_list(self):
        return [avto for avto in self.avtolar]
    
avto1 = Avto('Gm', 'Lasetti', 'oq', 2021, 1150000)
avto2 = Avto('Gm', 'Nexia', 'oq', 2012, 110000)

salon1 = AvtoSalon('BekShoh')

