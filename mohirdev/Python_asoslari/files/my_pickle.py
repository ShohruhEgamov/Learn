# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:40:47 2024

@author: Shaxruh
"""

import pickle

talaba1 = {"ism": "hasan", "familiya": "husanov", "tyil": 2003, "kurs": 2}
talaba2 = {"ism": "alijon", "familiya": "valiyev", "tyil": 2004, "kurs": 1}

# Bu yerdagi info ni faqat pythonda ochin ko'rish mumkin
with open("info", "wb") as file: 
    # Bu yerda biz pickle ga yozayapmiz
    pickle.dump(talaba1, file)
    pickle.dump(talaba2, file)