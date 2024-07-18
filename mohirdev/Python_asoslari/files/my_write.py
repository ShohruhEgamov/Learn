# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:12:11 2024

@author: Shaxruh
"""

faylnomi = "new_file.txt"
ism = input("Ism kiriting: ")
tyil = str(input("Tug'ilgan yilingiz: "))

# Bu yerda yozish uchun
# with open(faylnomi, "w") as fayl: # W ni sababi biz bunga yozishimiz mumkin
#     fayl.write(ism + "\n")
#     fayl.write(str(tyil) + "\n")
    
# Bu yerda esa qoshish uchun
with open(faylnomi, "a") as fayl: # A esa qoshish uchun
    fayl.write(ism + "\n")
    fayl.write(tyil + "\n")
    
