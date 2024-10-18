from transliterate import to_cyrillic, to_latin
import telebot
from my_token import token

# print(to_latin("Шоҳруҳ"))
# print(to_cyrillic("Shohruh"))
TOKEN = token
bot = telebot.TeleBot("TOKEN", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Assalomu alaykum. Xush kelibsiz")

bot.polling()
# matn = input('Matn kiriting: ')   # Bu yerda biz transleteni ishlatdik
# if matn.isascii():  # Bu agar lotin bolsa true aks holda false qaytaradi
# 	print(to_cyrillic(matn))
# else:
#  	print(to_latin(matn))