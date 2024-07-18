class Shaxs:
    def __init__(self, ism, familya, tyil):
        self.ism = ism
        self.familya = familya
        self.tyil = tyil
    
    def get_info(self):
        return f"{self.ism} {self.familya}. Tug'ilgan yil: {self.tyil}"
    
class Talaba(Shaxs):
    __talabalar_soni = 0

    def __init__(self, ism, familya, tyil):
        super().__init__(ism, familya, tyil)
        self.bosqich = 1
        Talaba.__talabalar_soni += 1
    
    @classmethod 
    # Bu yerda yashirin fayilni korish uchun
    def get_num_talaba(cls):
        return cls.__talabalar_soni
    
    def get_fullname(self):
        return f"{self.ism} {self.familya}"
    def get_info(self):
        return f"{self.ism} {self.familya}. {self.bosqich}-bosqich talabasi"
    
    def set_bosqich(self, bosqich):
        self.bosqich = bosqich
        
    def update_bosqich(self):
        self.bosqich += 1
        
class Fan():
    def __init__(self,nomi):
        self.nomi = nomi
        self.__talabalar = []

    def add_student(self,talaba):
        self.__talabalar.append(talaba)

    def get_talabalar(self):
        return [talaba.get_fullname() for talaba in self.__talabalar]

    def get_info(self):
        talabalar = ", ".join([talaba.ism for talaba in self.__talabalar])
        return f"Fan: {self.nomi}, Talabalar: {talabalar}"

inson = Shaxs('Shohruh','Egamov', 2000)
talaba = Talaba('Farrux', 'Egamov',2000)
talaba3 = Talaba('diyorbek', 'Egamov',2000)
fan = Fan('Matematika')
fan.add_student(talaba)
fan.add_student(talaba3)
# print(inson.get_info())
# print(talaba.get_info())
# print(talaba.get_num_talaba())
# print(fan.get_talabalar())
# print(talaba.get_info())
print(fan.get_talabalar())

#...........................................Bu yerda dunder uyga vazifa
class Shaxs:
    def __init__(self, ism, familya, tyil):
        self.ism = ism
        self.familya = familya
        self.tyil = tyil
    
    def __repr__(self):
        return f"{self.ism} {self.familya}. Tug'ilgan yil: {self.tyil}"
    
class Talaba(Shaxs):
    __talabalar_soni = 0

    def __init__(self, ism, familya, tyil):
        super().__init__(ism, familya, tyil)
        self.bosqich = 1
        Talaba.__talabalar_soni += 1
    
    @classmethod 
    # Bu yerda yashirin fayilni korish uchun
    def get_num_talaba(cls):
        return cls.__talabalar_soni
    
    def __repr__(self):
        return f"{self.ism} {self.familya}"
    # Taqqoslash uchun
    def __eq__(self, boshqa_talaba):
        return self.bosqich == boshqa_talaba.bosqich

    def __lt__(self, boshqa_talaba):
        return self.bosqich < boshqa_talaba.bosqich
    
    def get_info(self):
        return f"{self.ism} {self.familya}. {self.bosqich}-bosqich talabasi"
    
    def set_bosqich(self, bosqich):
        self.bosqich = bosqich
        
    def update_bosqich(self):
        self.bosqich += 1
        
class Fan():
    def __init__(self,nomi):
        self.nomi = nomi
        self.__talabalar = []
# Bu yerda indexidagini qaytarish uchun
    def __getitem__(self, index):
        return self.__talabalar[index]
    
# Bu yerda ozgartirish uchun
    def __setitem__(self, index, value):
        if isinstance(value, Talaba):
            self.__talabalar[index] = value
            
    def add_student(self,talaba):
        self.__talabalar.append(talaba)

    def get_talabalar(self):
        return [talaba.__repr__() for talaba in self.__talabalar]

    def get_info(self):
        talabalar = ", ".join([talaba.ism for talaba in self.__talabalar])
        return f"Fan: {self.nomi}, Talabalar: {talabalar}"
talaba = Talaba('Farrux', 'Egamov',1998)
talaba3 = Talaba('diyorbek', 'Egamov',1994)
# print(talaba3.update_bosqich())
# print(talaba.update_bosqich())
# print(talaba.get_info())
# print(talaba3.get_info())
# print(talaba == talaba3)
# # Farrux Egamov. 2-bosqich talabasi
# # diyorbek Egamov. 2-bosqich talabasi
# # True
fan = Fan('Matematika')
fan.add_student(talaba)
fan.add_student(talaba3)
print(fan[0]) # Farrux Egamov
talaba4 = Talaba('Shohruh', 'Egamov',2000) # Qoshamiz
fan[0] = talaba4 
print(fan[0]) # Shohruh Egamov
print(fan.get_talabalar())



# # ......................................upgrade Uyga vazifa
# # Shaxs classini yaratdik
class Shaxs:
    def __init__(self, ism, familya, tyil):
        self.ism = ism
        self.familya = familya
        self.tyil = tyil
        
#__repr__ metodi Shaxs, Talaba va Fan klasslariga qo'shildi.
    def __repr__(self):
        return f"Shaxs: {self.ism} {self.familya}, Tug'ilgan yil: {self.tyil}"
    
# Talaba classini yaratdik
class Talaba(Shaxs):
    __talabalar_soni = 0

    def __init__(self, ism, familya, tyil, id):
        super().__init__(ism, familya, tyil)
        self.bosqich = 1
        self.id = id
        Talaba.__talabalar_soni += 1
        
    @classmethod
    def get_num_talaba(cls):
        return cls.__talabalar_soni
    
    def __repr__(self):
        return f"{self.ism} {self.familya}. {self.bosqich}-bosqich talabasi, ID: {self.id}"
    
	#  Bu qolda qoshish uchun
    def set_bosqich(self, bosqich):
        self.bosqich = bosqich
        # Bu avramatik qoshish uchun
    def update_bosqich(self):
        self.bosqich += 1

#__lt__ va __eq__ metodlari Talaba klassida qo'shildi, bu talabalarni bosqich bo'yicha solishtirish imkonini beradi.
    def __lt__(self, other):
        return self.bosqich < other.bosqich

    def __eq__(self, other):
        return self.bosqich == other.bosqich
    

class Fan:
    def __init__(self, nomi):
        self.nomi = nomi
        self.__talabalar = []
        
    def add_student(self, talaba):
        self.__talabalar.append(talaba)

#Fan klassiga __getitem__, __setitem__, __len__, __add__, __sub__, va __call__ metodlari qo'shildi.
    def __getitem__(self, index):
        return self.__talabalar[index]
    
    def __setitem__(self, index, talaba):
        self.__talabalar[index] = talaba
        
    def __len__(self):
        return len(self.__talabalar)

#__add__ metodi + operatori yordamida talabani qo'shish imkonini beradi.
    def __add__(self, talaba):
        self.add_student(talaba)
        return self

#__sub__ metodi - operatori yordamida talabani olib tashlash imkonini beradi.
    def __sub__(self, talaba_id):
        self.__talabalar = [talaba for talaba in self.__talabalar if talaba.id != talaba_id]
        return self

#__call__ metodi Fan obyektini chaqiriladigan qilib qo'yadi. Agar argument sifatida talaba berilsa,
# uni ro'yxatga qo'shadi, aks holda ro'yxatdagi talabalar haqida ma'lumot chiqaradi.
    def __call__(self, talaba=None):
        if talaba:
            self.add_student(talaba)
        else:
            for talaba in self.__talabalar:
                print(talaba.__repr__())

    def __repr__(self):
        return f"Fan(nomi='{self.nomi}', talabalar={len(self.__talabalar)})"

    def get_talabalar(self):
        return [talaba.__repr__() for talaba in self.__talabalar]

    def get_info(self):
        talabalar = ", ".join([talaba.ism for talaba in self.__talabalar])
        return f"Fan: {self.nomi}, Talabalar: {talabalar}"
    
inson = Shaxs('Shohruh', 'Egamov', 2000)
talaba1 = Talaba('Farrux', 'Egamov', 2000,457454)
talaba2 = Talaba('Ali', 'Valiyev', 1999,445956)
talaba3 = Talaba('Diyorbek', 'Egamov', 2001,8784)

fan = Fan('Matematika')
fan + talaba1
fan + talaba2
fan - talaba3.id

print(inson)
print(talaba1)
print(Talaba.get_num_talaba())
print(fan.get_talabalar())
fan()
print(fan.get_info())