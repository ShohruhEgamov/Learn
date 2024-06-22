# f = open ("demofile.txt")
# print(f)

s=d=f="oryol"
print(s)
print(d)

meva = ["Bu", "orash", "usuli"]
x, d, f = meva
print(d)

def myfunc():
   global x
   x = "salom"
   print(x)
myfunc()

print("Shohruh senga " + x)

def myfunc():
   global x
   x = "alik"
   print("shohruh senga " + x)
myfunc()
print('Farruh senga ' + x)

# Matn turi:	str
# Raqamli turlar:	           int, float, complex
# Tartib turlari:	           list, tuple, range
# Xaritalash turi:	           dict
# To'plam turlari:	           set,frozenset
# Mantiqiy turi:	               bool
# Ikkilik turlari:	           bytes, bytearray, memoryview
# Yo'q turi:                    NoneType

# x = "Hello World"	           str	
# x = 20	                       int	
# x = 20.5	                   float	
# x = 1j	                       complex	
# x = ["apple", "banana", "cherry"]	list	
# x = ("apple", "banana", "cherry")	tuple	
# x = range(6)	                    range	
# x = {"name" : "John", "age" : 36}	dict	
# x = {"apple", "banana", "cherry"}	set	
# x = frozenset({"apple", "banana", "cherry"})	frozenset	
# x = True	                        bool	
# x = b"Hello"                   	bytes	
# x = bytearray(5)	                bytearray	
# x = memoryview(bytes(5))	        memoryview	
# x = None	                        NoneType

x = {"name" : "John", "age" : 36}
print(type(x))

a = input()                   # shu soz bor bolsa true beradi
print('keladi' in a)

x = input()                   # shu soz bor bolsa true bomasa false beradi
if "salom" in x:
  print("ha, 'salom' bor sozda")
else:
  print("yoq,'salom' bu sozda yoq ")

x = input()                   # shu soz bolsa false beradi
print("terorizm" not in x)

x = input()                       # bu yerda ham soz bolsa true bolmasa false
if "21" in x:
    print("ha, '21' bor")
elif "21" not in x:
    print("yoq, '21' yoq")

a = "shohruh egamov"
print(a.replace("e", "E"))

a = input()
b = a.split(".")
print(b)
['Kurslar', 'Web dastur', 'python', ' dars']

age = 23                                          # son bilan sozni qoshish uchun format() kerak boladi
txt = "mening ismim shohruh, yoshim {}"
print(txt.format(age))


a = input("bozorda nechi ")
b = input('dokonda nechi ')
d = input('internetta nechi ')
x = int(a) + int(b) + int(d) 
elementlar = "bozor {} dokonda {} internetta {} dollar. hammasi {}"         # aniq bolishi un {0}, {1}, {2} deyish mumkin
print(elementlar.format(a, b, d, x)) 


x = ["apple", "banana"]
y = input()
print(y in x)

import sys                    # python versiyasini aniqlash
print(sys.version)

mevalar = ["olma", "banan", "olcha"]
meva = input()
if meva in mevalar:
  meva = meva.upper()
  mevalar = "Ha bu {} mevasi bor"
  print(mevalar.format(meva))

thislist = ["apple", "banana", "cherry"]      
thislist[1] = "blackcurrant"
print(thislist)

mevalar = ["olma", "banan", "olcha"]      # bu elementni ozgartirish funksiyasi
mevalar[1] = "nok"
print(mevalar)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
element = input("Mevalarni kiriting: ").split()
thislist[1:3] = element
print(thislist)

text = "apple.banana.cherry"
result = text.split('.')
print(result)

mevalar = ["Olma", "Nok", "Anor"]
meva = input("mevalarni kiriting: ")
meva = meva.split(" ")
mevalar.append(meva)

print(mevalar)

mevalar = ["olma", "banan", "olcha"]
mevalardan = ["mango", "nok", "olhori"]

mevalar.extend(mevalardan)

print(mevalar)

mevalar = ["olma", "banan", "olcha"]
meva = input("Meva kiriting: ")
mevalar.remove(meva)
print(mevalar)

mevalar = ["olma", "banan", "olcha"]
meva = input("Qaysi meva: ")
if meva in mevalar:
    mevalar.pop(mevalar.index(meva))
    print(mevalar)
else:
    print("meva topilmadi!")

mevalar = ["olma","nok", "olcha"]
meva = int(input("Qaysi mevani olib tashlay? "))
if meva < len(mevalar):
    mevalar.pop(meva)
    print(mevalar)
else:
    print("Notogri son!")

mevalar = ["olma","nok", "olcha"]
del mevalar[0]
print(mevalar)

mevalar = ["olma","nok", "olcha"]
meva = int(input("Qaysi mevani olib tashlay? "))
if int(meva) < len(mevalar):
     del mevalar[meva]
     print(mevalar)
else:
     print("Notogri son!")

meva = input("Meva kiriting: ")
meva = meva.split(" ")
for x in range(len(meva)):
    print(meva[x])

thislist = ["salom", "alik"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

mevalar = input("Meva kiriting: ")
mevalar = mevalar.split(" ")
yangi = []

for x in mevalar:
    if "a" in x:
        yangi.append(x)

print(yangi)

meva = {"olma", "olcha", "nok", "behi"}
bor = [x for x in meva if "a" in x]                           # a hafi bor bolganlarini oladi

print(bor)

meva = {"olma", "olcha", "nok", "behi"}                        # oxshashlarini olmaydi
bor = [x for x in meva if x != "olma"]

print(bor)

son = [x for x in range(10) if x <= 5]      

print(son)

meva = ["olma", "olcha", "nok"]
list = [x.upper() for x in meva]
print(list)

meva = ["olma", "olcha", "nok"]
list = ['salom' for x in meva]
print(list)

meva = ["olma", "olcha", "nok"]
list = [x if x != "olma" else "olcha" for x in meva]
print(list)

son = [1,2,4,5,7,3,8,7]
son.sort()
print(son)                        # son yoki sozni alfobit yoki son ketmaketligida yozadi


son = [1,2,4,5,7,3,8,7]
son.sort(reverse = True)
print(son)

def myfunc(n):
    return abs(n-50)
son = [100,50,65,86,55,25]
son.sort(key = myfunc)
print(son)

son = ["olma", "Olcha", "nOk"]
son.sort(key = str.lower)
print(son)

meva = ["olma", "olcha", "nok", 100, 20, 50]                      # bu sonlarni al yoki son tartibiga teskari tuzadi
meva.reverse()
print(meva)


import math
import turtle

def xt(t):
     return 16*math.sin(t)**3

def yt(t):
     return 13*math.cos(t)-5*\
     math.cos(2*t)-2*\
     math.cos(3*t)-\
     math.cos(4*t)

t = turtle.Turtle()
t.speed(500)
turtle.bgcolor("black")

for i in range (2550):
     t.goto((xt(i)*20, yt(i)*20))
     t.pencolor('red')
     t.goto(0, 0)


list = ["a", "b", "s"]
list2 = [1, 2, 3, 5]

for x in list2:
    list.append(x)
print(list)

mevalar = ("olma", "olcha", "nok")
x = list(mevalar)
x.append("banan")
mevalar = tuple(x)
print(mevalar)

MEVA = ("OLMA", "OLCHA", "BANAN")
( OQ, QIZIL, SARIQ) = MEVA

print(QIZIL)
print(OQ)




class Car:
   def __init__(self, brand, model):
      self.brand = brand
      self.model = model

    # def move(self):
    # 	print("Drive!")


class Boat:
   def __init__(self, brand, model):
       self.brand = brand
       self.model = model

   def move(self):
       print("Sail!")


class Plane:
   def __init__(self, brand, model):
       self.brand = brand
       self.model = model

   def move(self):
       print("Fly!")


car1 = Car("Ford", "Mustang")  # Create a Car class
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat class
plane1 = Plane("Boeing", "747")  # Create a Plane class

for x in (car1, boat1, plane1):
   x.move()


# import shoh as mix  # shoh ga laqab berish

# mix.egamov("shohruh")
# a = mix.personal["mamlakat"]
# print(a)


# import platform

# x = platform.__dict__()
# print(x)


# x = dir(platform) # hamma platformalarni chop etish
# print(x)

# from shoh import egamov

# egamov("shoh")

# import shoh
# print(dir(shoh))

import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
print(x.ctime())


x = min(3, 5, 10)
y = max(5, 8, 13)

print(x)
print(y)

x = abs(-7.25)  #faqat musbat qaytaradi
print(x)

x = pow(5, 10)  # 5 ni 10 chi darajasini qaytaradi
print(x)


import math

x = math.sqrt(81)
print(math.ceil(x))
print(math.floor(x))


import json

x = '{"name": "Shohruh", "age": 23, "city": "Urgench"}'

y = json.loads(x)  # jsonni pythonga aylantirish

print(y["name"])


x = {
   "name": "shohruh",
   "age": 23,
   "city": "Urgench"
}

y = json.dumps(x)    # pythonni jsonga aylantirish
print(y)

x = {
   "name": "shohruh",
   "age": 23,
   "city": "Urgench",
   "married": True,
   "divorced": False,
   "children": ("Ann", "Billy"),
   "pets": None,
   "cars": [
       {"model": "BMW 230", "mpg": 27.5},
       {"model": "Ford Edge", "mpg": 24.1}
   ]
}

print(json.dumps(x, indent=50)) # bu orasini ochish un hizmat qiladi
print(json.dumps(x, indent=4, separators=("Shoh ", " = "))) # bu hamma boglanishlarni shu belgilar bilan boglaydi

x = {"name": "shohruh", "age": 23, "city": "Urgench", "married": True, "divorced": False, "children":
    ["Ann", "Billy"], "pets": None, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}

y = json.loads(x)
print(y)

import re

txt = "Assalomu alaykum 2 Men 5 Uzbek"
son = "11, 2, 36, 6"
x = re.search("^Salom.*Uzbek$", txt)
if x:
   print("ha bu so\'zlar bor")
else:
   print("yo\'q bu so\'lar")

x = re.findall("[a-e]", txt)  # alifbo tartibida a da e gacha bolgan kichik harflarni toplaydi
print(x)

x = re.findall("\d", txt)     # barcha raqamlarni topadi
print(x)

x = re.findall("m.n", txt)    # qaysi bilan boshlab qaysi bilan tugashi
print(x)

x = re.findall("S.*k", txt)    # qaysi harf bilan boshlab qaysi bilan tugashi
print(x)

x = re.findall("S.{7}m", txt)   # nuqta qoyib otirmaydi nechta bosh bolsa shuni yozasan
print(x)

x = re.findall("Salom|Assalomu alaykum", txt)    # ikkisidan birining borligini tekshiradi
print(x)

if x:
	print("Ha salom berdi")
else:
	print("Salom bermadi")

x = re.findall("\W", txt)             # satir qaysi soz bilan boshlangani ni tek

print(x)

if x:
 print("Yes, there is a match!")
else:
 print("No match")

a = ['A', 's', 's', 'a', 'l', 'o', 'm', 'u', ' ', 'a', 'l', 'a', 'y', 'k', 'u', 'm', ' ', ' ', 'm', 'e', 'n', ' ', ' ', 'u', 'z', 'b', 'e', 'k']
print(len(a))

x = re.findall("[a-zA-Z]", txt)  # [anm] bu shu harflarni topadi
print(x)                         # [a-m] bu adan m gacha bolgan harflarni chiqara
									# [^and] bu shu hariflardan boshqa harflarni topadi
if x:
	print("Ha, bu harflar bor")
else:
	print("Yo\'q, bu harflar")

x = re.sub("\S","9", txt)
print(x)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())    # .SPAN PAZITSIYASINI COP ETADI

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)     # kiritilgan matinni chop etadi

txt = "The rain in Shohruh"
x = re.search(r"\bS\w+", txt)
print(x.group()) # S bilan boshlaangan sozni chop etadi

try:
 print(x)
except NameError:
 print("Variable x is not defined")
except:
 print("Something else went wrong")

try:
	print(x)
except:
	print("ha bu xato")
finally:
	print("hato yo\'q")


try:
	f = open("shohruh.txt")
	try:
		f.write("lorum ipsum")
	except:
		print("ha bu yerda bor")
	finally:
		f.close()
except:
	print("yoiq bu yerda")

# x = -1
# f x < 0:
# 	raise Exception("Kechrasiz bu hato")
# else:
# 	print("ha katta")

x = "hello"
if not type(x) is int:
	raise TypeError("bu yerda son yoq")

f = open("salom.txt", "w")
f.write(" salom men shohruh ")
f.close()
f = open("salom.txt", "r")
print(f.read())


f = open("salom.txt", "r")   
print(f.readline())
f.close

f = open("salom.txt", "w")  # "a" qoshadi "w" qaytadan yozadi
f.write("Salom mening ismim Shohruh")
f.close()

f = open("salom.txt", "r")
print(f.read())

f = open("men.txt", "w")
f.write("Salom mening ismim Shohruh")
f.close()

f = open("men.txt", "r")
print(f.read())

import os
os.remove("men.txt")   # faylni ochiradi

if os.path.exists("salom.txt"):
	os.remove("salom.txt")
else:
	print("Bu fayl yo\'q")


import random

a = random.randint(1,10)
b = random.randint(1,10)

c = int(input(f"{a} * {b} = "))
s = a * b
if c ==s:
	print("bu togri ")
else:
	print("notogri")



'''class myclass():
    def __len__(self):
        x = int(input("son kirit "))
        return x

myobj = myclass()
print(bool(myobj))'''



'''def myfunc(v):
  return abs(v - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)


thislist = [1,7,9,4,5]

thislist.sort(key=int)

print(thislist)'''



'''i = 1
while i < 6:
  print(i)
  i += 1'''

'''import datetime

x = datetime.datetime.now()

print(x)

a = range(0,7)
for x in a:
     print(x)'''

'''i = 1
while i < 6:
  print(i)
  i += 1'''