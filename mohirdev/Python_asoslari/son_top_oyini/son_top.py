import random

## Ishlayapdi funksiyani o'chirsangiz
# def son_top(son,b):
# 	while True:
# 		if (son == b):
# 			print("siz togri topdingiz")
# 			break
# 		else:
# 			print("Xato")
# 			break
# a = r.sample(range(10), 1)
# b = int(input("Son kiriting: "))
# son = a[0]
# son_top(a,son)
# print(a)

# a = r.sample(range(10), 1)
# son = a[0]
# def son_top(son,b):
# 	while True:
# b = int(input("Son kiriting: "))
# 		if (son == b):
# 			print("siz togri topdingiz")
# 		elif(son > b):
# 			print("ozgina katta")
# 		elif(son < b):
# 			print("ozgina kichkina")
# 		else:
# 			print("Xato")


# #....................................Bu esa tayyor kod

import random

def sontop(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?", end="")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>> "))
        if taxmin<tasodifiy_son:
            print(f"Xato. Men o'ylagan son {taxmin} dan kattaroq. Yana harakat qiling:", end="")
        elif taxmin>tasodifiy_son:
            print(f"Xato. Men o'ylagan son {taxmin} dan kichikroq. Yana harakat qiling:", end="")
        else:
            break
        
    print(f"Tabriklayman. {taxminlar} ta taxmin bilan topdingiz!")
    return taxminlar
    

def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
                      f"Men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim!")
    return taxminlar

def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        
        if taxminlar_user>taxminlar_pc:
            print(f"Men {taxminlar_pc} taxmin bilan topdim va  yutdim!")
        elif taxminlar_user<taxminlar_pc:
            print(f"Siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0):"))
            
play()