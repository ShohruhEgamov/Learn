# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 16:48:45 2024

@author: Shaxruh
"""
# Xatolar
yosh = input("Yoshingizni kiriting: ")
yosh = int(yosh)
print(f"Siz {2021-yosh} yilda tug'ilgansiz")


# try-except
yosh = input("Yoshingizni kiriting: ")
try:
    yosh = int(yosh)
    print(f"Siz {2021-yosh} yilda tug'ilgansiz")
except ValueError:
    print("Butun son kiritmadingiz")

# try-except-else
print("Dastur Tugadi!")
yosh = input("Yoshingizni kiriting: ")
try:
    yosh = int(yosh)
except ValueError:
    print("Butun son kiritmadingiz")
else:
    print(f"Siz {2021-yosh} yilda tug'ilgansiz")

x,y=5,10
try:
    y/(x-5)
except ZeroDivisionError:
    print("0 ga bo'lib bo'lmaydi")

mevalar = ['olma','anor','anjir','uzum']
try:
    print(mevalar[7])
except IndexError:
    print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")

user = {"username":"sariqdev",
        "status":"admin",
        "email":"admin@sariq.dev",
        "phone":"99897123456"}

key="username"
try:
    print(f'Foydalanuvchi: {user[key]}')
except KeyError:
    print("Bunday kalit mavjud emas")

# filename = "data.txt" # bunday fayl mavjud emas
# with open(filename) as f:
#     text = f.read()

filename = "data.txt" # bunday fayl mavjud emas
try:
    with open(filename) as f:
        text = f.read()
except FileNotFoundError:
    print(f"Kechirasiz, {filename} fayli mavjud emas. Boshqa fayl tanlang.")

n = input("Butun son kiriting: ")
try:
    n = int(n)
    x=20/n
except ValueError:
    print("Butun son kiritmadingiz")
except ZeroDivisionError:
    print("0 ga bo'lib bo'lmaydi")
else:
    pass

import json
files = ['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
for filename in files:
    try:
        with open(filename) as f:
            talaba = json.load(f)
    except FileNotFoundError:
        print(f"{filename} mavjud emas")
    else:
        print(talaba['ism'])
        # fayl ustida turli amallar

import json
files = ['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
for filename in files:
    try:
        with open(filename) as f:
            talaba = json.load(f)
    except FileNotFoundError:
        pass
    else:
        print(talaba['ism'])
        # fayl ustida turli amallar

try:
    yosh = input("Yoshingiz kiriting: ")
    yosh = int(yosh)
except NameError:
    print('Bu xato yozildi')
except ValueError:
    print("Iltimos son kiriting")
else:
    print(f'Siz {2024 - yosh} yilda tug\'ilgansiz')
    print(yosh/20)
    

while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        yosh = int(yosh)
        break
    else:
        print("Butun son kiriting")
print(f"siz {2024-yosh} yilsiz")




