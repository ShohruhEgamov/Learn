
# import requests
# from bs4 import BeautifulSoup


# sahifa = "https://kun.uz/news/main"
# r = requests.get(sahifa)
# # print(r.text)

# soup = BeautifulSoup(r.text, "html.parser")
# # print(soup.prettify())
# news = soup.find_all(class_="news-title")
# print(news[0].text)



# import requests
# from bs4 import BeautifulSoup

# # URL manzil
# sahifa = "https://kun.uz/news/main"
# r = requests.get(sahifa)

# # HTML ni pars qilish
# soup = BeautifulSoup(r.text, "html.parser")

# # Sahifaning to'liq HTML ni chop etish
# # print(soup.prettify())

# news = soup.find_all('div', class_='news-title')
# print(news[0].text)



# import requests
# from bs4 import BeautifulSoup

# # URL manzil
# sahifa = "https://kun.uz/news/main"
# r = requests.get(sahifa)

# # HTML ni pars qilish
# soup = BeautifulSoup(r.text, "html.parser")

# # Sahifadagi yangilik sarlavhalarini topish
# news = soup.find_all('div', class_='news-title')

# # Topilgan elementlarning uzunligini chop etish
# print(f"Topilgan yangiliklar soni: {len(news)}")

# # Elementlarni indeks orqali olish va chop etish
# for i in range(len(news)):
#     print(f"Yangilik {i+1}: {news[i].text.strip()}")



import requests
from bs4 import BeautifulSoup

# URL manzil
sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)

# HTML ni pars qilish
soup = BeautifulSoup(r.text, "html.parser")

# Sahifaning to'liq HTML ni chop etish
print(soup.prettify())

# Sahifadagi yangilik sarlavhalarini topish
news = soup.find_all('div', class_='news-title')

# Topilgan elementlarning uzunligini chop etish
print(f"Topilgan yangiliklar soni: {len(news)}")

# Elementlarni indeks orqali olish va chop etish
for i in range(len(news)):
    print(f"Yangilik {i+1}: {news[i].text.strip()}")
