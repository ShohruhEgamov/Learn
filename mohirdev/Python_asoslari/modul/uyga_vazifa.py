from datetime import datetime, timedelta
import datatime
import re

#Bugungi sanani olish
bugun = datetime.today()



# ...................................................Har 2 haftalik farq bilan 10 ta sanani chiqarish
for i in range(10):
    sana = bugun + timedelta(weeks=2*i)
    print(sana.strftime("%Y-%m-%d"))


from datetime import timedelta
delta = timedelta(
    days=1,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=1,
    weeks=1
)
# Only days, seconds, and microseconds remain
print(delta)

qurbon = datetime(2025,4,20)
# qurbon = datetime.date.today()
ramazon = datetime(2025,1,20)
farq = qurbon - ramazon
# print(farq)
print(f"Ramazonga {farq.days} kun qoldi")




#....................................................Tug'ilgan kun qancha bolgani

def hisoblash_tugilgan_va_joriy(ism, tugilgan_kun, tugilgan_oy, tugilgan_yil):
    # Joriy sana va tug'ilgan sana obyektlari
    joriy_sana = datetime.now()
    tugilgan_sana = datetime(tugilgan_yil, tugilgan_oy, tugilgan_kun)
    
    # Yosh, oy va kunlarni hisoblash
    yosh = joriy_sana.year - tugilgan_sana.year
    oy = joriy_sana.month - tugilgan_sana.month
    kun = joriy_sana.day - tugilgan_sana.day
    
    # Kun uchun qondirish
    if kun < 0:
        oy -= 1
        kun += 30  # To'g'ri kunlar soni

    # Oy uchun qondirish
    if oy < 0:
        yosh -= 1
        oy += 12  # To'g'ri oylar soni
    
    # Natija chiqarish
    print(f"{ism} {yosh} yil, {oy} oy, {kun} kun")

# Test qilish
hisoblash_tugilgan_va_joriy("Shohruh", 15, 7, 2000)
hisoblash_tugilgan_va_joriy("Farrux", 1, 1, 1998)


#..................................................................Bu yana bir turi
from datetime import date

def calculate_age(birthdate):
    today = date.today()
    
    # Yillarni hisoblash
    years = today.year - birthdate.year
    
    # Agar bugungi oy tug'ilgan oyning oldidan kelsa yoki bugungi oy bir xil bo'lib, bugungi kun tug'ilgan kunning oldidan kelsa
    if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
        years -= 1
    
    # Tug'ilgan sanadan bugungi yilgacha vaqtni hisoblash
    this_year_birthday = date(today.year if today.month > birthdate.month or (today.month == birthdate.month and today.day >= birthdate.day) else today.year - 1, birthdate.month, birthdate.day)
    
    # Oy va kunlarni hisoblash
    delta = today - this_year_birthday
    months = delta.days // 30
    days = delta.days % 30
    
    return years, months, days

# Tug'ilgan sana: YYYY, MM, DD
birthdate = date(2000, 12, 21)
age = calculate_age(birthdate)
print(f"Sizning yoshingiz: {age[0]} yil, {age[1]} oy, {age[2]} kun")


#....................................................................Url manzildan nusxa olish

def extract_urls(text):
    # Veb sahifa manzillarini topish uchun muntazam ifoda
    url_pattern = r'https?://[^\s]+'
    
    # Topilgan barcha mosliklarni ro'yxatga olish
    urls = re.findall(url_pattern, text)
    
    return urls

# Matn
text = """
Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI

Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test
"""

# Funksiyani chaqirish
urls = extract_urls(text)
print(urls)