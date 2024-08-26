'''Ob'ektni/sinfni iterator sifatida yaratish uchun siz usullarni __iter__()va __next__()ob'ektingizga amal qilishingiz kerak.

Python sinflari/ob'ektlari bo'limida bilib olganingizdek , barcha sinflar __init__()ob'ekt yaratilayotganda bir oz ishga tushirishni amalga oshirish imkonini beruvchi deb nomlangan funktsiyaga ega .

Usul __iter__()shunga o'xshash ishlaydi, siz operatsiyalarni bajarishingiz mumkin (boshlash va h.k.), lekin har doim iterator ob'ektining o'zini qaytarishingiz kerak.

Usul __next__()shuningdek, operatsiyalarni bajarishga imkon beradi va keyingi elementni ketma-ketlikda qaytarishi kerak.'''
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# Bu yerda iter va next to'xtatish
class MyNumbers:
  def __iter__(self): 
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration   # Bu to'xtatish uchun

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:         # Bu aylantirish uchun
  print(x) 



'''Sinf polimorfizmi
Polimorfizm ko'pincha Class usullarida qo'llaniladi, bu erda biz bir xil usul nomi bilan bir nechta sinflarga ega bo'lishimiz mumkin.

Masalan, bizda uchta sinf bor deylik: Car, Boat, va Plane, va ularning barchasida , deb nomlangan usul bor move():'''
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()