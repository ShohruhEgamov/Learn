class Person:
    def __init__(self, first_name, last_name, age, email, day, month, year):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self._day = day
        self._month = month
        self._year = year

    @property
    def birth_day(self):
        return self._day, self._month, self._year

    def get_info(self):
        return (f"Ismi: {self.first_name}\n"
                f"Familiyasi: {self.last_name}\n"
                f"Yoshi: {self.age}\n"
                f"Elektron manzili: {self.email}\n"
                f"Tug'ilgan kuni: {self.birth_day[0]:02d}-{self.birth_day[1]:02d}-{self.birth_day[2]}")

    def get_life_path_number(self):
        def digit_sum(n):
            return sum(int(digit) for digit in str(n))
        
        day_sum = digit_sum(self._day)
        month_sum = digit_sum(self._month)
        year_sum = digit_sum(self._year)

        total_sum = day_sum + month_sum + year_sum

        while total_sum >= 10:
            total_sum = digit_sum(total_sum)

        return total_sum

    def get_info_by_number(self, number):
        try:
            with open('data.txt', 'r') as file:
                for line in file:
                    if line.startswith(f"#{number}"):
                        return line.strip().split('\n', 1)[1].strip()
            return "Ma'lumot topilmadi."
        except FileNotFoundError:
            return "Ma'lumot fayli topilmadi."

def main():
    try:
        first_name = input("Ismingizni kiriting: ")
        last_name = input("Familyangizni kiriting: ")
        age = int(input("Yoshingizni kiriting: "))
        email = input("Elektron manzilingizni kiriting: ")
        day = int(input("Tug'ilgan kuningizni kiriting: "))
        month = int(input("Tug'ilgan oyingizni kiriting: "))
        year = int(input("Tug'ilgan yilingizni kiriting: "))
        
        # Person ob'ektini yaratish
        person = Person(first_name, last_name, age, email, day, month, year)
        
        # Ma'lumotlarni chiqarish
        print(person.get_info())
        
        # Life path number hisoblash
        life_path_number = person.get_life_path_number()
        print(f"Life path number: {life_path_number}")
        
        # Raqamga mos ma'lumot
        info_by_number = person.get_info_by_number(life_path_number)
        print(f"Raqamga mos ma'lumot: {info_by_number}")
    
    except ValueError:
        print("Iltimos, raqamlarni to'g'ri kiriting.")
    except Exception as e:
        print(f"Xatolik: {e}")

if __name__ == "__main__":
    main()
