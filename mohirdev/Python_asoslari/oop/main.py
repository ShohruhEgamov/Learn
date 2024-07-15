# class Talaba:
# 	def __init__(self,ism,familya,tyil):
# 		self.ism = ism
# 		self.familya = familya
# 		self.tyil = tyil
# 	def tanishuv(self):
# 		return f"Men {self.ism} {self.familya} Tug'ilgan yilim {self.tyil} yoshim {2024 - self.tyil} da"
# men = Talaba("Shohruh","Egamov",2000)
# akam = Talaba("Farruh","Egamov",1998)
# print(men.tanishuv())
# print(akam.tanishuv())


# #......................................................Bu yerda tugilgan kun hisoblanadi
# from datetime import datetime

# def hisoblash(ism, tugilgan_kun, tugilgan_oy, tugilgan_yil):
#     # Joriy sanani olish
#     joriy_sana = datetime.now()
    
#     # Tug'ilgan sanani datetime obyektiga o'tkazish
#     tugilgan_sanasi = datetime(tugilgan_yil, tugilgan_oy, tugilgan_kun)
    
#     # Yoshni hisoblash
#     yosh = joriy_sana.year - tugilgan_sanasi.year
    
#     # Tug'ilgan sanadan oldingi tug'ilgan kunlarni hisoblash
#     if (joriy_sana.month, joriy_sana.day) < (tugilgan_sanasi.month, tugilgan_sanasi.day):
#         yosh -= 1
    
#     # Natijani chiqarish
#     print(f"{ism} {tugilgan_kun}-{tugilgan_oy}-{tugilgan_yil} tug'ilgan, {yosh} yoshda")
    
# # Test qilish
# hisoblash("Shohruh", 21, 12, 2000)



# #......................................................Bu yerda tugilgan kun hisoblanadi

# from datetime import datetime

# def hisoblash_tugilgan_va_joriy(ism, tugilgan_kun, tugilgan_oy, tugilgan_yil):
#     # Joriy sana va tug'ilgan sana obyektlari
#     joriy_sana = datetime.now()
#     tugilgan_sana = datetime(tugilgan_yil, tugilgan_oy, tugilgan_kun)
    
#     # Yoshni hisoblash
#     yosh = joriy_sana.year - tugilgan_sana.year
#     oy = joriy_sana.month - tugilgan_sana.month
#     kun = joriy_sana.day - tugilgan_sana.day
    
#     # Ay va kun uchun qondirilishi
#     if kun < 0:
#         oy -= 1
#         kun += 30  # To'g'ri kunlar soni
#     if oy < 0:
#         yosh -= 1
#         oy += 12  # To'g'ri oylar soni

#     # Natija chiqarish
#     print(f"{ism} {yosh} yil, {oy} oy, {kun} kun")
    
# # Test qilish
# hisoblash_tugilgan_va_joriy("Shohruh", 21, 12, 2000)
# hisoblash_tugilgan_va_joriy("Farrux", 15, 11, 1998)
# hisoblash_tugilgan_va_joriy("Bekmirza", 21, 11, 1996)
# hisoblash_tugilgan_va_joriy("Diyorbek", 14, 4, 1994)


