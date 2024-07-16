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