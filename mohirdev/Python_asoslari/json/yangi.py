# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:33:29 2024

@author: Shaxruh
"""

import json

# JSON faylini yuklash
with open("students.json") as f:
    # load ham jsondan malumot oladi
    data = json.load(f)
    



# Bu yerda consolda chiqishi
# Tom Price Fakulteti: Engineering
# Nick Thameson Fakulteti: Computer Science
# John Doe Fakulteti: ICT



# Bu yerda esa ikkinchi talabani ismini chaqirish
# data['student'][1]['name']
#  'Nick'

ism = input("Ismingiz: ")
fam = input("Familya: ")
fak = input("FAqultet: ")
# Yangi talaba ma'lumotlari
new_student = {
    "id": "04",
    "name": ism,
    "lastname": fam,
    "year": 1,
    "faculty": fak
    }

# Yangi talabani mavjud ro'yxatga qo'shish    
data['student'].append(new_student)

# Yangilangan JSON ma'lumotlarini faylga saqlash
with open('students.json', 'w') as file:
    json.dump(data, file, indent=4)
    
    for item in data['student']:
        print(f"{item['name']} {item['lastname']} Fakulteti: {item['faculty']}")
