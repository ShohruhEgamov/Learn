import numpy
from scipy import stats
import matplotlib.pyplot as plt
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
import pandas

# Bu yerda mean ortacha sonni topadi
# Bu (10,20)/2 shu korinishni soddalashtiradi 
x = numpy.mean(speed)

# Bu medisan ortadagi sonni qaytaradi
# Agar o'rtada ikkita raqam bo'lsa, bu raqamlarning yig'indisini ikkiga bo'ling.
x = numpy.median(speed)

# mode()Eng ko'p ko'rinadigan raqamni topish uchun SciPy usulidan foydalaning :
x = stats.mode(speed)

# Bu standart og'ishga misollar
# 1. O‘rtachani toping:

# (32+111+138+28+59+77+97) / 7 = 77.4

# 2. Har bir qiymat uchun: o'rtachadan farqni toping:

#  32 - 77.4 = -45.4
# 111 - 77.4 =  33.6
# 138 - 77.4 =  60.6
#  28 - 77.4 = -49.4
#  59 - 77.4 = -18.4
#  77 - 77.4 = - 0.4
#  97 - 77.4 =  19.6

# 3. Har bir farq uchun: kvadrat qiymatini toping:
# (-45.4)2 = 2061.16
#  (33.6)2 = 1128.96
#  (60.6)2 = 3672.36
# (-49.4)2 = 2440.36
# (-18.4)2 =  338.56
# (- 0.4)2 =    0.16
#  (19.6)2 =  384.16
# 4. Dispersiya - bu kvadratik farqlarning o'rtacha soni:

# (2061.16+1128.96+3672.36+2440.36+338.56+0.16+384.16) / 7 = 1432.2
x = numpy.std(speed)

# var()Farqni topish uchun NumPy usulidan foydalaning :
x = numpy.var(speed)

# percentile()Protsentillarni topish uchun NumPy usulidan foydalaning :
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 90)
# print(x)


x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

# print(r)


x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22,23]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100,50]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
myline = numpy.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()


