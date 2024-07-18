# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:46:01 2024

@author: Shaxruh
"""

import pickle
# Bu yerda biz o'qiyapmizs
with open("info", "rb") as file:
    talaba1 = pickle.load(file) # Bu load o'qish uchun
    talaba2 = pickle.load(file)

print(talaba1)
print(talaba2)

# Bu yerda biz uyga vazifadagi pi ni yukladik
# Bu yerda biz o'qiyapmizs
with open("F:\Learn\mohirdev\Python_asoslari\/files\/amalyot\pi_float.dat", "rb") as file:
    matn = pickle.load(file) # Bu load o'qish uchun

print(matn)