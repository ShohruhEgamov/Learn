a = input("bozorda nechi ")
b = input('dokonda nechi ')
d = input('internetta nechi ')
x = int(a) + int(b) + int(d) 
elementlar = "bozor {} dokonda {} internetta {} dollar. hammasi {}"         # aniq bolishi un {0}, {1}, {2} deyish mumkin
print(elementlar.format(a, b, d, x)) 