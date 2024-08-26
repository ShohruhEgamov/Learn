import matplotlib.pyplot as plt
import numpy as np

# x_p = np.array([2,3,5])
y_p = np.array([5,6,3,3, 8, 1, 10])
x_p = np.array([6, 2, 7, 11])

# Bu ekranni bolish uchun
# plt.subplot(3, 3, 5) 
# plt.scatter(x, y) # Bu tarqalgan chizmalar

plt.plot(y_p, "X--g",mec ="r")
plt.plot(x_p, "X--r",mec ="g")

# Fon yasash
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
# Bu yerda nom berish
plt.title("Sports Watch Data",fontdict=font1)
plt.xlabel("Trnofkaning davomiyligi",fontdict=font2)
plt.ylabel("Trnofkaning o'sishi",fontdict=font2)
# plt.plot(y_p, marker = 'o', ms = 20, mec = 'r', mfc = 'r') 

# Bu gris panjara qoshadi
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()

# marker = "p" va boshqa raqamlar markerni burchaklar shaklini bildiradi
# ms bu marker hajmini bildirasdi
# mec Bu marker chekkalarining rangini bildiradi
# mfc esa ichining rangini bildiradi
# Chizilgan chiziq uslubini o'zgartirish uchun argument linestyleyoki undan qisqa kalit so'zdan foydalanishingiz mumkin :ls
# linestyle = 'dotted'
# Chiziq kengligini o'zgartirish uchun kalit so'z argumentidan linewidthyoki undan qisqaroq so'zdan foydalanishingiz mumkin .lw
# Qaysi panjara chiziqlarini ko'rsatishni belgilash uchun funktsiyadagi axisparametrdan foydalanishingiz mumkin .grid()
# Argument uchun qiymat sifatida ranglar qatoridan foydalanib, har bir nuqta uchun ma'lum bir rangni o'rnatishingiz mumkin c:
# plt.scatter(x, y, c=colors)
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.show()

# Argument yordamida nuqtalar hajmini o'zgartirishingiz mumkin s.
# plt.scatter(x, y, s=sizes)

# Argument yordamida nuqtalarning shaffofligini sozlashingiz mumkin alpha.
# plt.scatter(x, y, alpha=0.5)

# bar()Pyplot yordamida siz shtrixli grafiklarni chizish uchun funktsiyadan foydalanishingiz mumkin :
# Agar siz garizantal chiqishini istasangiz barh() dan foydalaning

# Matplotlib-da biz hist()histogrammalar yaratish uchun funksiyadan foydalanamiz.

# pie()Pyplot yordamida siz dumaloq diagrammalarni chizish uchun funktsiyadan foydalanishingiz mumkin :

# Balki siz takozlardan biri ajralib turishini xohlaysizmi? Parametr explodebuni amalga oshirishga imkon beradi.

# shadowsParametrni o'rnatib, doira diagrammasiga soya qo'shing True:

# Har bir takoz uchun tushuntirishlar ro'yxatini qo'shish uchun funktsiyadan foydalaning legend():
# plt.pie(y, labels = (Bu yerda elementlar))
