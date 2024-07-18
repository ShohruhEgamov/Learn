# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:07:35 2024

@author: Shaxruh
"""
import json

data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
data_json = json.dumps(data)

with open('moshina.json', 'w') as m:
    json.dump(data,m)

talaba = {"ism": "Hasan", "familiya": "Husanov", "tyil":2000}
talaba_json = json.dumps(talaba)

with open('men.json', 'w') as s:
    json.dump(talaba,s)
    
with open('students_json', 'b') as s:
    students = json.loads(s)
