class Shaxs:
    def __init__(self, ism, familya, tyil):
        self.ism = ism
        self.familya = familya
        self.tyil = tyil
    
    def get_info(self):
        return f"{self.ism.title()} {self.familya.title()}. Tug'ilgan yil: {self.tyil}"
    
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
        return f"{self.ism.title()} {self.familya.title()}"
    def get_info(self):
        return f"{self.ism.title()} {self.familya.title()}. {self.bosqich}-bosqich talabasi"
    
    def set_bosqich(self, bosqich):
        self.bosqich = bosqich
        
    def update_bosqich(self):
        self.bosqich += 1
        
class Fan():
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar = []

    def add_student(self,talaba):
        self.talabalar.append(talaba)

    def get_talabalar(self):
        return [talaba.get_fullname() for talaba in self.talabalar]

    def get_info(self):
        talabalar = ", ".join([talaba.ism for talaba in self.talabalar])
        return f"Fan: {self.nomi}, Talabalar: {talabalar}"
    