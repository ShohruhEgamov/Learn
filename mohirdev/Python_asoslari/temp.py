
######################################-------Python kurs------######################################

sonlar = list(range(1,11))
for son in sonlar:
   print(f"{son} sonining kvadrati {son** 2} ga teng")

son = int(input("Son kirit: "))
print(f"{son} ni kvadrati {son**2} ga teng")

dostlar = []
print("5 ta eng yaqin do\'stingizni kiriting")
for n in range(5):
   dostlar.append(input(f"{n+1}-do\'stingizni kiriting "))
print(dostlar)


Kod = []
print("Kod kiriting")

for n in range(5):
   Kod.append(input(f"{n+1} kodni kiriting: "))
print(f"Kod {len(Kod)} marta takrorlandi")


odam = int(input("Bugun nicha odam bilan gaplashding: "))
otlari = []
for n in range((odam)):
    otlari.append(input(f"{n+1} odamlarni kiriting "))
print(otlari)

txt = "The best things in life are free!"
x = input("soz kirit ")
if x in txt:
  print(f"Yes, {x} is present.")



thislist = ["apple", "banana", "cherry"]
a = int(input("son kirit "))
b = input("soz kirit ")
thislist[a] = b

print(thislist)

meva = ["apple", "banana", "cherry"]
yangi =[x if x != "banana" else "orange" for x in meva]
print(yangi)


ismlar = ['Javohir', 'Zayniddin']

print('Salom ' + ismlar[0] + ', bugun choyhona bormi?\n' + 
     ismlar[1] + ', choyxonaga borasanmi')


son = list(range(120,1200,2))

print(sum(son))

print(max(son))
print(min(son))


#...................................................................For stikli

ismlar = ['Aziz', 'Olim', 'Anvar', 'Muzaffar', 'Oktam']
for ism in ismlar:
   print(f"Salom {ism}")
print(f"Kod {len(ism)} marta takrolrlandi")



sonlaar = list(range(11,100,2))
for son in sonlaar:
   print(son**3)
print(sonlaar)


korilgan = int(input("Nechta kino ko'rgansiz' "))
kinolar = []
print("Yaxshi ko`rgan kinoingiz: ")
for x in range(korilgan):
   kinolar.append(input(f"{x + 1} Kino nomini kiriting "))
print(kinolar)


#......................................................................is else
login = input("Loginingizni kiriting: ")
if login == "Admin":
   print("Xush kelibsiz admin")
else:
   print(f'Xush kelibsiz {login}')


a = input("Birinchi sonni kiriting: ")
b = input("Ikkinchi sonni kiriting: ")
if a == b:
   print("Ikkalasi bir biriga teng")
else:
   print("Teng emas")



#.................................................................. elif or and

kun = input("Bu gun qaysi gun: ")
harorat = float(input("Harorat nechi gradus: "))

if kun.lower() == 'yakshanba' and harorat <=30:
  print(f"Harorat {harorat} gradus cho'milishga kettik")
elif  kun.lower() == 'yakshanba' and harorat >=30:
   print(f"Harorat {harorat} gradus. bu hafli uyda otiramiz")
    

son = int(input("Bironta juft son kiriting: "))

if son % 2 == 0:
   print('Bu juft son')
else:
   print('Bu juft son emas')
    

yosh = int(input("Yoshingiz nechida: "))

if (yosh <= 4 or yosh >= 60):
   narx = 0
elif yosh <= 18:
   narx = 10000
elif yosh >= 18:
   narx = 20000

print(f"Sizning blet pulingiz {narx} so'm")
    
    
    
birinchi_son = int(input("Birinchi sonni kiriting: "))
ikkinchi_son = int(input("ikkinchi sonni sonni kiriting: "))

if birinchi_son > ikkinchi_son:
   print(f"{birinchi_son} katta {ikkinchi_son} dan")
else:
   print(f"{birinchi_son} kichkina {ikkinchi_son} dan")
    
    
mahsulotlar =  ['olma', 'shaftoli', 'anor', 'nok', 'behi', 'ananas', 'banan', 'olcha', 'kivi', 'tarvuz']
savat = []
bor_mahsulot = []
yoq_mahsulot = []
n = 5

for x in range(n):
   savat.append(input(f"{x + 1} chi meva: "))
for meva in savat:
   if meva in mahsulotlar:
       print(f"Do'konimizda {meva} bor")
       bor_mahsulot.append(meva)
   else:
       print(f"Do'konimizda {meva} yo'q")
       yoq_mahsulot.append(meva)


if len(yoq_mahsulot) == 0:
   print("Siz so'ragan hamma narsa bor")
else:
   print(f"Bizning do'konda {yoq_mahsulot} mevalar yo'q")



foydalanuvchilar = ['Shohruh', 'Farrux', 'Diyorbek', 'Bekmirza', 'Gulmira']
foydalanuvchi = input('Nomingizni kiriting: ')

if foydalanuvchi.capitalize() in foydalanuvchilar:
   print("Bu nom band!")
else:
   print("Xush kelibsiz")

son = int(input("Biron bir son kiriting: "))

if (son % 2 == 0):
   print(f"Bu {son} soni 2 ga qoldiqsiz bo'linadi")
else:
   print(f"Bu {son} soni 2 ga qoldiqli bo'linadi {son % 2}")




#..............................................................Lug'atlar

otam = {
       'ism':'Shuxrat',
      'familya': 'Ortikov',
       'kasbi': 'o\'qtuvchi',
      'yil': '1968'
       }
print(f"Otamning ismi {otam['ism']}, Familyasi {otam['familya']}, Kasbi {otam['kasbi']}, Tug'ilgan yili {otam['yil']}")


inputn = str(input("Biron bir so'z kiriting: "))

lugat = {
   'olma': 'apple',
   'nok' : 'grusha',
   'float' : 'butun son',
   'int' : 'sonli qiymat',
   'str' : 'matinli qiymat'
   }


malumot = lugat.get(inputn, 'Bunday so\'z yo\'q')
print(malumot)





mahsulotlar = {
    'non' : 1000,
    'baliq' : 2000,
    'olma' : 500,
    'un' : 5600,
    'gosht' : 80000
    }
bozorlik = ['anor', 'behi', 'olma', 'gosht']


for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} narxi {mahsulotlar[mahsulot]} so'm")

for buyum in mahsulotlar:
    if buyum not in bozorlik:
        print(f"Iltimos, Do'koningizga {buyum} ham olib keling")




#.............................................royhat va setlarni lugatlani bir biriga qoshish

# Bu yerda for tsikli bilan 10 ra lug'at yaratamiz
lasetti = []
for n in range(10):
	new_car = {
		'model' : 'Lasetti',
		'rang' : None,
		'yil' : 2020,
		'narx' : None,
		'km' : 0,
		'korobka' : 'avto'
	}

	lasetti.append(new_car)


# Bu ro'yhatga kirib ranglarini o'zgartirish uchun
for m in lasetti[:3]:
	m['rang']='oq'

for m in lasetti[3:6]:
	m['rang']='qora'

for m in lasetti[6:]:
	m['rang']='mokriy asfalt'

# Bu yerda 6 dan keyingilarnini karobkasini almashladik
for m in lasetti[6:]:
	m['korobka']='mehanik'

# Bu yerda korobkasiga qarab narxini baholadik
for m in lasetti:
	if m ['korobka'] == 'avto':
		m['narx'] = 40000
	else:
		m['narx'] = 35000

print(lasetti)



# Bu yerda dasturchilar berilga va ularning qaysi tillarni bilishi
# Lug'at ichidag royhatlar quydagicha ko'rinadi

dasturchilar = {
	'ali' : ['python', 'c++'],
	'vali' : ['java', 'javascript'],
	'olim' : ['html', 'css', 'sass'],
	'gani' : ['php', 'go'],
	'azim' : ['R', 'c#'],
}

# bu yerda ism bu 0 elementlar yani ismlarni oladi
# tillar degan esa royhatlari oladi 
for ism, tillar in dasturchilar.items():
	print(f"\n{ism.title()} quydagi dasturlashni biladi: ")
	# Bu lug'at ichidagi ro'yhatlarni aylantirish uchun
	for til in tillar:
		print(til.upper())


for ism, tillar in dasturchilar.items():
	print(f"\n{ism.title()} quydagi dasturlashni biladi: ", end='')
	# Bu lug'at ichidagi ro'yhatlarni aylantirish uchun
	for til in tillar:
		print(til.upper(), end=' ')  # bu end=' ' malumotlar bir birining izidan davom qilib chiqishi uchun


#.....................................................lug'at ichidagi lugatlarga misollar
hamkasblar = {
	'Shohruh':{
		'familya':'Egamov',
		't_yil':2000,
		'malumot':'oliy',
		'til':['Python', 'JavaScript', 'php'],
		'oylik': []
	},
	'Farrux':{
		'familya':'Egamov',
		't_yil':1998,
		'malumot':'oliy',
		'til':['Java', 'SQL'],
		'oylik': []
	},
	'Bekmirza':{
		'familya':'Egamov',
		't_yil':1996,
		'malumot':'oliy',
		'til':['html', 'css', 'bootstrap'],
		'oylik': []
	},
	'Diyorbek':{
		'familya':'Egamov',
		't_yil':1994,
		'malumot':'oliy',
		'til':['Kali', 'Linux'],
		'oylik': []
	},
}
#Bu yerda ismlar va malumotlar alohida olingan
for ism, info in hamkasblar.items():
	print(f"\n {ism.title()} {info['familya'].title()},"
		f"{info['t_yil']}-yilda tug'ilgan, "
		f"Malumoti {info['malumot']}. \n"
		"Quyidagi dasturlash tillarini biladi:"
		)
	#Bu yerda agar dasturlash tilining ichida Python bolsa qimmat aks holda arzon
	a = info['oylik']
	t = info['til']
	for maosh in t:
			if 'Python' in maosh:
				a.append(400)
			else:
				a.append(300)
			print(f"{maosh.upper()}")
	def datsur_ucun_pul(nomi,haqqi):
		b = {}
		# b = []
		for nom,haq in zip(nomi,haqqi):
			# b.append(f"{nom} uchun {haq}") #Bu yerda royhatga yuborish uchun
			b[nom] = haq
			# bu royhatni (Kali: 300), (Linux: 300) Quyidagi korinishda chiqaradi
			format = ', '.join([f'({nom}: {haq}$)' 
				for nom,haq in b.items()])  
		return format
	tillar = t
	haqlar = a
	d = datsur_ucun_pul(tillar, haqlar)
	print(d)
	toplam = sum(a)
	print(f"Toplam oylik {toplam}")


#...........................................................while loop

son = 1
while son <= 5:
	print(son, end=" ") # end bu izidan davom qilishlik uchun
	son += 1

#.................................Soni kvadratini chiqaradigan dastur

print("Sonning kvadratini beradigan dastur")
savol = "Istalgan son kiriting "
savol += ("dasturni to'xtatish uchun 'exit' yozing: ")
qiymat = ""
# while qiymat != 'exit':  #Bu exitgacha ishlaydi 
while True:                #Bu esa abadiy davom etadi
	qiymat = input(savol)
	# if qiymat != 'exit':   # Bu exit ni yozganda to'xtashi uchun
	if qiymat == 'exit':
		break                # Bu yerda exit bolganda toxtaydi
	else:
		print(float(qiymat)**2)
print('Dastur tugadi...')


#.................................Bu juft yoki toq bilish uchun

son = 0
while son < 10:
	son += 1
	if son % 2 != 0:    # Bu toq bolsa chiqarmaydi va boshiga qaytadi
	# if son % 2 == 0:  # Bu juft bolsa chiqarmaydi va boshiga qaytadi
		continue
	else:
		print(son)

#....................................kitob soraydigan dastur

kitob = "Sevgan kitobingizni kiriting: "
kitoblar = ""
hammasi = []
while True:
	kitoblar = input(kitob)
	if kitoblar == 'stop':
		break
	else:
		hammasi.append(kitoblar)
print(hammasi)


#....................................Kino teatirga chipta

tamoshabin = "Yoshingiz nechida: "
chiptalar = ""

while True:
	chiptalar = input(tamoshabin)
	if chiptalar == 'exit' or chiptalar == 'quit':
		print("Chipta sotilishi toxtadi")
		break
	sonuchun = int(chiptalar)
	if sonuchun <= 7:
		print("Chipta narxi 2000 So'm" )
		continue
	elif 7<= sonuchun <= 18:
		print("Chipta narxi 3000 So'm" )
		continue
	if 18<= sonuchun <= 65:
		print("Chipta narxi 10000 So'm" )
		continue
	if sonuchun >= 65:
		print("Chipta narxi 0 So'm" )
		continue
print('Raxmat')

# While siklini o'rganamiz

print("Yaqin do'stingizni ro'yxatini tuzamiz.")    #Bu yerda ism kiritamiz
ismlar = []                                        # Bu yerda ro'yxat shakillanadi
n = 1                                              # N = 1 boshlanishi
while True:
      ism = input(f"{n}-do'stingizni ismini kiriting: ")
      ismlar.append(ism)
      javob = input("Yana (ha/yo'q): ")
      n += 1
      if javob != 'ha':
        break
print(ismlar)


dostlar = {}
ishora = True
while ishora:
	ism = input("Ismingizni kiriting: ")
	familiya = input("Familiyangizni kiriting: ")
	dostlar[ism] = familiya
	navbat = input("Yana (ha/yo'q): ")
	if navbat == "yo'q":
		ishora = False

for ism, familiya in dostlar.items():
	print(f"{ism.title()} {familiya.title()}")


# qiymatni o'chirish
cars = ["lasetti", "Cobalt", 'nexia','matiz', 'nexia','damas']
while 'nexia' in cars:
	cars.remove('nexia')
print(cars)


talabalar = ["hasan", "husan", "olim", "botir"]
baholangan_talabalar = {}

while talabalar:  # Bu yerda buni yozganimiz sababi bu boshamaguncha u davom qiladi
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] = int(baho)


# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir 
# qabul qilib, yangi ro'yxatga joylang.
mahsulot = []
n = 1
while True:
	foydalanuvchi = (f"{n} mahsulotingizni yozing: ")
	mahsulot.append(input(foydalanuvchi))
	javob = input("Yana (ha/yo'q): ")
	n += 1
	if javob != 'ha':
		break
print(mahsulot)


# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. 
#Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.

e_bozor = {}
ishora = True
while ishora:
	mahsulot = input("Mahsulotni kiriting: ")
	narxi = int(input("Narxini kiriting: "))
	e_bozor[mahsulot] = narxi
	navbat = input("Yana (ha/yo'q): ")
	if navbat == "yo'q":
		ishora = False

for mahsulot, narxi in e_bozor.items():
	print(f"{mahsulot.title()} {narxi} so'm")


# Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni 
# e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). 
# Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu 
# mahsulot yo'q" degan xabarni kor'sating.

buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
	buyurtma = buyurtmalar.pop()
	if buyurtma in mahsulotlar.keys():
		print(f"{buyurtma.title()} {mahsulotlar[buyurtma]}")
	else:
		print(f"{buyurtma.title()} bizda yo'q")


#............................................Funksiyalar

#.__doc__ Bu hamma narsa haqida malumotni olish uchun

# Yoshini topish
def yosh_hisobla(ism, tugilgan_yil):
    """Foydalanuvchi yoshini hisoblaydigan dastur"""
    print(f"{ism.title()} {2020-tugilgan_yil} yoshda")

yosh_hisobla('olim',1997)


def yosh_hisobla(tugilgan_yil, joriy_yil=2024):
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")


# yosh_hisobla(1995,2020)
yosh_hisobla(2000)


# Sonning kubini va kvadratini topish

def Son_k(son):
	"""Sonning kubini va kvadratini topish"""
	print(f"Sonning kvadrati {son**2} va kubi {son**3}")
son_kirit = int(input("Son kiriting: "))
Son_k(son_kirit)

# Bu yerda sonlarni kattasini chiqarish
def katta_chiq(bir_son,ikki_son):
	"""Sonlarni kattasini chiqarish"""
	if bir_son > ikki_son:
		print(f"{bir_son} soni {ikki_son} sonidan katta")
	elif bir_son < ikki_son:
		print(f"{bir_son} soni {ikki_son} sonidan kichkina")
	else:
		print(f"{bir_son} soni {ikki_son} ga teng")
bir_son = int(input("Birinchi son: "))
ikki_son = int(input("Ikkinchi son: "))
katta_chiq(bir_son,ikki_son)

def sonlar():
	son1 = int(input("son kiriting"))
	son2 = int(input("son kiriting"))
	if son1 > son2:
		print(son1)
	elif son1 == son2:
		print("sonlar teng")
sonlar()


def bolinishlar():
	son = int(input("Son kiriting: "))
	for n in range(1,10):
		if son % n == 0:
			print(f"{son} soni {n} ga bolinadi")
bolinishlar()

# While bilan yasalishi

def bolinishlar():
	son = int(input("Son kiriting: "))
	n = 1
	while n <= 10:
		if son % n == 0:
			print(f"{son} soni {n} ga bolinadi")
		n += 1
bolinishlar()

def toliq_ism_yasa(ism, familiya):
    """Toliq ism qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism


talaba1 = toliq_ism_yasa("olim", "hakimov")
talaba2 = toliq_ism_yasa("hakim", "olimov")
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
print(f"{talaba1} darsga kechikib keldi")


def toliq_ism_yasa(ism, familiya, otasining_ismi=""): # Bu yerdagi ='' bilan biz argumentlarni ixtiyoriy qilamiz
    """Toliq isma qaytaruvchi funksiya"""
    if otasining_ismi:
        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism.title()


talaba1 = toliq_ism_yasa("olim", "hakimov")
talaba2 = toliq_ism_yasa("hakim", "olimov", "abrorovich")
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")


def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {
        "kompaniya": kompaniya,
        "model": model,
        "rang": rangi,
        "korobka": korobka,
        "yil": yili,
        "narh": narhi,
    }
    return avto


avto1 = avto_info("GM", "Malibu", "Qora", "Avtomat", 2018)
avto2 = avto_info("GM", "Gentra", "Oq", "Mexanika", 2016, 15000)
avtolar = [avto1, avto2]
print("Onlayn bozordagi mavjud avtomashinalar:")
for avto in avtolar:
    if avto["narh"]:
        narh = avto["narh"]
    else:
        narh = "Noma'lum"
    print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")



def oraliq(min, max,qadam=1):
    sonlar = []
    while min < max:
        sonlar.append(min)
        min += qadam
    return sonlar


print(oraliq(0, 10,2))
print(oraliq(10, 21,3))


def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
	avto = {
			"kompaniya": kompaniya,
			"model": model,
			"rang": rangi,
			"korobka": korobka,
			"yil": yili,
			"narh": narhi,
		}
	return avto


print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar = []  # salondagi avtolar uchun bo'sh ro'yxat

while True:
    print("\nQuyidagi ma'lumotlarni kiriting", end="")
    kompaniya = input("Ishlab chiqaruvchi: ")
    model = input("Modeli: ")
    rangi = input("Rangi: ")
    korobka = input("Korobka: ")
    yili = input("Ishlab chiqarilgan yili: ")
    narhi = input("Narhi: ")
    # Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida
    # lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    # Yana avto qo'shish-qo'shmaslikni so'raymiz
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob == "no":
        break

print("\nSalonimizdagi avtolar:")
for avto in avtolar:
    if avto["narh"]:
        narh = avto["narh"]
    else:
        narh = "Noma'lum"
    print(
        f"{avto['rang'].title()} {avto['model'].title()}, {korobka} korobka. Narhi: {narh}"
    )

def malumot(ism, familya, t_yili, t_joyi, tel, e_manzil,yosh=2024):
	malumotlar = {
		"ism": ism,
		"familya": familya,
		"t_yili": t_yili,
		"t_joyi": t_joyi,
		"tel": tel,
		"e_manzil": e_manzil,
		"yosh": yosh,
	}
	return malumotlar

print("Siz haqingizdagi malumotlar")
info = []

while True:
	ism = input("Ismingiz: ")
	familya = input("Familyangiz: ")
	t_yili = int(input("Tug'ilgan yilingiz: "))
	t_joyi = input("Tug'ilgan joyingiz: ")
	tel = input("Telefon raqamingiz: ")
	e_manzil = input("Elektron manzilingiz: ")
	yosh = 2024 - int(t_yili)
	info.append(malumot(ism, familya, t_yili, t_joyi, tel, e_manzil, yosh))
	javob = input("Yana info qo'shasizmi? (yes/no): ")
	if javob == "no":
		break

print("Shaxsiy Malumotlaringiz", end="")
for i in info:
	print(f"\n{i['ism'].title()} {i['familya'].title()}, {i['t_yili']}-yilda {i['t_joyi']}da tug'ilgan {i['yosh']} yoshda. Telefon raqami:{i['tel']} {i['e_manzil']} bu elektronmanzil")




def mijoz_info(ism, familiya, tyil, tjoy, email="", tel=None):
    """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    mijoz = {
        "ism": ism,
        "familiya": familiya,
        "tyil": tyil,
        "yoshi": 2020 - tyil,
        "tjoy": tjoy,
        "email": email,
        "telefon": tel,
    }
    return mijoz


print("Mijoz haqida ma'lumotlarni kiriting.")
mijozlar = []
while True:
    ism = input("Ismi: ")
    familiya = input("Familiyasi: ")
    tyil = int(input("Tug'ilgan yili: "))
    tjoy = input("Tug'ilgan joyi: ")
    email = input("Email: ")
    telefon = input("Telefon raqami: ")
    mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
    javob = input("Davom etasizmi? (ha/yo'q)")
    if javob != "ha":
        break
print("Mijozlar:")
for mijoz in mijozlar:
    telefon = mijoz['telefon'] # Bu yerda agar telefon raqami bolmasa
    if telefon:
        telefon = mijoz['telefon']
    else:
        telefon = "Telefon raqami mavjud emas"  # bu yozuv chiqaradi
    print(
        f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
        f"{mijoz['yoshi']} yoshda, telefoni: {telefon}"
    )


def kattasi(x,z,y):
	if x > z and x > y:
		print(f"{x} soni {z} va {y} dan katta")
	elif z > x and z > y:
		print(f"{z} soni {x} va {y} dan katta")
	elif y > x and y > z:
		print(f"{y} soni {x} va {z} dan katta")
kattasi(4,5,6)


def kattasi(x, y, z):
    max = x
    if y >= max:
        max = y
    if z >= max:
        max = z
    return max

x = int(input("Son kirit "))
y = int(input("Son kirit "))
z = int(input("Son kirit "))
print(kattasi(x, y, z))


def aylana(radius, pi=3.14):
	aylana_info = {
		"radius": radius,
		"diametr": 2 * radius, # diametr radusni kvadratiga teng
		"perimetr": 2 * pi * radius, #parametr teng pini kvadrati va radiusni kopaytmasiga
		"yuza": pi * radius ** 2 # Yuza teng pini radiusga kopaytir va kvadratga kotar
	}
	return aylana_info
aylana(5,3.14)

def tub_sonlar(x):
	tub_sonlar = []
	for i in range(10):
		if i % x != 0:
			tub_sonlar.append(i)
	return tub_sonlar
tub_sonlar(5)

def tub_sonlar_top(min, max):
    tub_sonlar = []
    for n in range(min, max + 1):
        tub = True
        if n == 1:
            tub = False
        elif n == 0:
            tub = True
        else:
            for x in range(2, n):
                if n % x == 0:
                    tub = False
        if tub:
            tub_sonlar.append(n)

    return tub_sonlar
tub_sonlar_top(1,10)

def aylana_info(radius, pi=3.14159):
    aylana = {
        "radius": radius,
        "diametr": 2 * radius,
        "perimetr": 2 * radius * pi,
        "yuza": pi * radius ** 2,
    }
    return aylana
aylana_info(4)

def tub_sonlar(min, max):
  tub_sonlar = []
  for n in range(min, max + 1):
    tub = True
    if n <= 1:  # 1 va 2 ni o'z ichiga olish uchun
      tub = False
    else:
      for x in range(2, int(n**0.5) + 1):  # Ichki tsiklni optimallashtirish
        if n % x == 0:
          tub = False
          break  # Bo'linuvchi topilsa, ichki tsiklni to'xtating
    if tub:
      tub_sonlar.append(n)
  return tub_sonlar

prime_numbers = tub_sonlar(1, 100)
print(prime_numbers)  # Chiqish: [2, 3, 5, 7, 11]

# Bu yerda shundayki agar tasodifiy son 0.5 ga kopayganda qoldiqli son chiqsa u juft boladi
# Agar son hech qoldiqsiz bolsa tub boladi

def financhain(n):
	sonlar = []
	for x in range(n):             # x = [0,1,2,3,4,5,6,7,8,9,10]
		if x == 0 or x == 1:
			sonlar.append(1)
		else:
			sonlar.append(sonlar[x-1] + sonlar[x-2])     # Bu yerda x ni aylantiradi
	return sonlar                                        # (sonlar[x-1] + sonlar[x-2]) bu metodda x ni navbatdagi sonidan 1 ni ayiradi [x-1]
														 # #  keyin ikkini ayiradi [x-2] va shu indexsda turgan sonlardagi sonlarni bir biriga 
print(financhain(10))                                  # qoshadi (sonlar[x-1] + sonlar[x-2])

# # Agar 0 bolsa 1 qoshiladi
# # Agar 1 bolsa 1 qoshiladi
# # agar 2 bolsa 'sonlar.append(sonlar[x-1] + sonlar[x-2])' Bu ishga tushadi yani
# # sonlar[2 - 1] + sonlar[2-2]
# # sonlar[1,1,2,3,4,5] Bu massiv sonlar[2 - 1] 1 ni chaqiradi yani 1 ni chaqiradi
# # sonlar[1,1,2] Bu massiv sonlar[2 - 2] 0 ni chaqiradi yani 1 ni chaqiradi
# # Ikkalasini qoshganda 2 boladi
# # Matematikada Fibonachchi ketma-ketligi har bir raqam oldingi ikkitasining yig'indisi teng bo'lishi 
a = [0,1,2,3,4,5,6,7,8,9,10]
b = [1,1,2,3,5,8,13,21,34,55,89]
print(b[9])
print(b[8])

def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = int(baho)
    return baholar


talabalar = ["ali", "vali", "hasan", "husan"]
baholar = bahola(talabalar[:]) # Agar bu  yerdan [:] Bunday belgi qoyilsa asil nusxasiham qoladi
print(baholar)
print(talabalar)



def katta_harf(ism):
	ism = ism[:]
	for i in range(len(ism)):
		ism[i] = ism[i].title()
	return x
ismlar = ['ali', 'vali', 'hasan', 'husan']
matin = katta_harf(ismlar)
print(matin)
print(ismlar)

talabalar = ["ali", "vali", "hasan", "husan"]

def bahola(ballar):
	baholar = {}
	for bal in ballar:
		baho = input(f"Talaba {bal.title()}ning bahosini kiriting: ")
		baholar[bal] = int(baho)
	return baholar

baholar = bahola(talabalar)
print(baholar)
print(talabalar)

def summa(*sonlar):
	yigindi = 0
	for son in sonlar:
		yigindi += son
	return yigindi

print(summa(1,2,5,2,5,7))
print(summa(1,2,5,2,5,7,8,6,9,45,4))
print(summa(1,2,5,2,5,7,96,3,5,8))

def kopaytma(*sonlar):
	natija = 1
	for son in sonlar:
		natija *= son
	return natija

print(kopaytma(1,2,5,2,5,7))
print(kopaytma(1,2,5,2,5,7,8,6,9,45,4))
print(kopaytma(1,2,5,2,5,7,96,3,5,8))

def talaba_info(ism, familiya, **kwargs):
	kwargs['ism'] = ism
	kwargs['familiya'] = familiya
	return kwargs
a = int(input('Yilingiz: '))
kasb = input('Kasbingiz: ').title()
maosh = int(input('Oylik maoshingiz'))
talaba = talaba_info('Shohruh', 'Egamov', yili = a, kasbi = kasb, maoshi = f'{maosh} $')
print(talaba)

for i in range(1, 6):
  for j in range(1, i + 1):
    print("*", end=" ")
  print()

