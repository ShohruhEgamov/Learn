# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
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





































































    
    