
fayl_nomi = "F:/Learn/mohirdev/Python_asoslari/oop/hayot_yoli.txt"
with open(fayl_nomi, "r") as fayl:
    mazmun = fayl.read()

    # Holatlarni bo'lish
    holatlar = mazmun.split("#")
    holatlar_dict = {}
print(holatlar)
