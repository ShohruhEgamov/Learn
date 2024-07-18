import json

x = 10
x_json = json.dumps(x) # dumps Bu jsonga otkazishi uchun

y = 5.5
y_json = json.dumps(y)

m = True
m_json = json.dumps(m)

# ism = "anvar"
# ism_json = json.dumps(ism)
# familiya_json = json.dumps('narzullaev')

sonlar = (12, 45, 23, 67)
sonlar_json = json.dumps(sonlar)

bemor = {
    "ism": "Alijon Valiyev",
    "yosh": 30,
    "oila": True,
    "farzandlar": ("Ahmad", "Bonu"),
    "allergiya": None,
    "dorilar": [
        {"nomi": "Analgin", "miqdori": 0.5},
        {"nomi": "Panadol", "miqdori": 1.2},
    ],
}
# indent = 2 Bu jsonni yaxshi korinishi uchun. boshidan joy qoldiradi
bemor_json = json.dumps(bemor, indent=4)
# print(bemor_json)

with open("bemor.json", "w") as f:
    json.dump(bemor, f)

# Bu loads json ni python farmatga o'tkazadi
bemor2 = json.loads(bemor_json)

# Bu yerda lugatga kirishlar
bemor['dorilar'][0]['nomi']