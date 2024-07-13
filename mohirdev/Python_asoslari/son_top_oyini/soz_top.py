import random
from uzword import words
# Bu soz olish uchun
def get_word():
    word = random.choice(words)
    # Bu yerda agar - va bosh joy bolsa boshqadan qidiradi
    while "-" in word or ' ' in word: 
        word = random.choice(words)
    return word.upper()


## Bu yerda esa harfni izlash
def display(user_letters,word):
    display_letter=""  # bu yerda topilgan harflar
    for letter in word:
        if letter in user_letters:
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter

def play():
    word = get_word()
    # So'zdagi harflar
    word_letters = set(word)
    # Foydalanuvchi kiritgan harflar
    user_letters = ''
    print(f"Мен {len(word)} хонали сўз ўйладим. Топа оласизми?")
    # print(word)
    while word_letters:
        print(display(user_letters,word))
        if user_letters:
            print(f"Шу вақтгача киритган ҳарфларингиз: {user_letters}")
        
        letter = input("Ҳарф киритинг: ").upper()
        if letter in user_letters:
            print("Бу ҳарфни аввал киритгансиз. Бошқа ҳарф киритинг.")
            continue        
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} ҳарфи тўғри.")
        else:
            print("Бундай ҳарф йўқ.")
        user_letters += letter
    print(f"Табриклайман! {word} сўзини {len(user_letters)} та уринишда топдингиз.")
play()