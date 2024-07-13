import random as r
# #..............................Bu yerda oddiy usuli
# import avto_info

# avto1 = avto_info.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# avto_info.info_chiqarish(avto1)



# #..............................Bu yerda qisqartirib chaqirish usuli

# import avto_info as aim

# avto1 = aim.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# aim.info_chiqarish(avto1)


# #..............................Bu yerda faqat kerakli funksiyalarni olish usuli

# from avto_info import avto_info, info_chiqarish

# avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# info_chiqarish(avto1)


# #..............................Bu yerda faqat kerakli funksiyalarni olish va ularni qisqartirish usuli

# from avto_info import avto_info as ainfo, info_chiqarish as iprint

# avto1 = ainfo("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# iprint(avto1)


# #..............................Bu yerda hammasini chaqirish uculi usuli
# # ! Bunday foydalanmang
# from avto_info import *

# avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# info_chiqarish(avto1)

# avtolar = avtoil.avto_kirit()

# for avto in avtolar:
#     avtoil.info_chiqarish(avto)

# ismlar = ['olim','anvar','hasan','husan']
# ism = r.choice(ismlar)
# print(ism)

# x = list(range(0,51,5))
# print(x)
# print(r.choice(x))


x = list(range(11))
print(x)
r.shuffle(x)
print(x)