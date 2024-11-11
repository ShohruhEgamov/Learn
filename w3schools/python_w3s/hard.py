import math
from turtle import *

# Yurak shaklini chizish uchun x koordinatasi
def heart_a(n):
    return 15 * math.sin(n) ** 3

# Yurak shaklini chizish uchun y koordinatasi
def heart_b(n):
    return 12 * math.cos(n) - 5 * math.cos(2 * n) - 2 * math.cos(3 * n) - math.cos(4 * n)

# Turtle sozlamalari
tracer(2)  # Chizish tezligini oshirish
bgcolor("black")  # Oynaning fon rangi

# Yurak shaklini chizish
for i in range(800):
    goto(heart_a(i)*15, heart_b(i)*15)
    for j in range(1):
        color('red')
        hideturtle()
        goto(0,0)

# Chizishni yakunlash
done()


