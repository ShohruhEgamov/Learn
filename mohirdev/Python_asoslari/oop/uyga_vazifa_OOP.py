class Person:
	def __init__(self,name,firstname,age,email): 
		self.name = name
		self.firstname= firstname
		self.age = age
		self.email = email

# To'liq ism familyasi
	def get_info(self):
		return f"Ism sharifi {self.name} {self.firstname} yoshi {self.age} da. Elektron manzili {self.email}."

class Days(Person):
		def __init__(self,name,firstname,age,email,year, month, day,):
			super().__init__(name,firstname,age,email)
			self.year = year
			self.month = month
			self.day = day

# Tug'ilgan kuni
		def birth_day(self):
			return f"{self.year}-{self.month}-{self.day}"

# Tu'g'ilgan kunini (life_path_number) qilish
		def get_life_path_number(self):
			def t_sum(n):
				return sum(int(toplam) for toplam in str(n))

			day_sum = t_sum(self.day)
			month_sum = t_sum(self.month)
			year_sum = t_sum(self.year)

			total_sum = day_sum + month_sum + year_sum

			while total_sum >= 10:
				total_sum = t_sum(total_sum)

			return total_sum

# Bu yerda raqamga mos hususiyatlar
		def get_info_by_number(self):
			life_path_number = self.get_life_path_number()
			tariflar = {
				1: "Siz rahbarlikni yaxshi ko'rasiz! Siz innovatsiya ruhiga ega mehnatkashsiz. Sizda ham san'atga \n ishtiyoq bor. Siz o'zingizni osonlikcha namoyon qila olasiz va har qanday ishda doimo birinchi  \n bo'lishni xohlaysiz. Siz va orzularingizga hech narsa yoki hech kim to'sqinlik qilishiga yo'l \n qo'ymaysiz. Siz qilishingiz kerak bo'lgan narsa - o'zingiz xohlagan narsaga e'tiboringizni qaratishdir \n va siz bunga erisha olasiz! Sizning halokatingiz: siz o'zingizni va boshqalarni tanqid qilasiz. \n Siz dangasalik bilan qattiq ro'za tutasiz va siz o'zingizdan va shuning uchun atrofingizdagilardan  \n eng yaxshisini kutasiz. Sizda o'zini o'ylashga va talabchanlikka moyillik bor. \n Siz eng zo'r bo'lishga ishtiyoqli bo'lganingiz uchun, ba'zida takabbur yoki maqtanchoq bo'lib qolishingiz mumkin. \n Ammo bu sizning muvaffaqiyatga erishish uchun tug'ma xohishingiz.",
				2: "Hayotdagi ikkalasini ham o'ylab ko'ring. Ular hamkorlikda va boshqalar bilan ishlashda \n muvaffaqiyat qozonasiz. Siz juda sezgirsiz va atrofingizdagi dunyo bilan uyg'unsiz. Siz boshqalarga yordam  \n berishda va sahna ortida shizz sodir etishda o'zingizning eng yaxshi shaxsingizsiz. Siz \n tafsilotlarni yaxshi bilasiz. Sizning e'tiboringiz guruhning katta foydasiga xizmat qilishga qaratilgan  \n bo'lsa, siz gullab-yashnaysiz. Siz tabiatan tinchlikparvarsiz va har qanday vaziyatning barcha \n qarashlarini ko'ra olasiz. Bu sizning super kuchingiz.Sizning halokatingiz: berasiz, berasiz  \n va yana bir oz ko'proq berasiz, toki bu sizni xafagarchilik bilan chekinishga majbur qiladi. \n Maqsadingizni boshqalar sizni ko'rishiga ishonganingizdek emas, balki o'zingizga xos tarzda topishingiz  \n muhim. Siz mamnunsiz, lekin ko'pincha sizni xafa qiladigan narsa. Siz sezgirsiz, bu ba'zan  \n sizning yiqilishingizga olib kelishi mumkin. Siz xafa bo'lishdan qo'rqasiz va bu odatda  \n qarama-qarshilikdan qochishingizga olib keladi, bu esa odamga yoki vaziyatga nisbatan o'z  \n noroziligingizni keltirib chiqaradi.",
				3: "Siz kuchli tebranish va yuqori darajadagi ijodkorlik va o'zingizni ifoda etishda yashaysiz. \n Siz mustaqilsiz va muloqotda muvaffaqiyat qozonasiz. Og'zaki va yozma muloqot qobiliyatingiz tufayli siz \n shoir, yozuvchi, aktyor, rassom yoki musiqachi sifatida juda mos kelasiz. Siz optimistik  \n va juda saxiysiz. Siz har doim har qanday vaziyatda ijobiy tomonlarni topishingiz mumkin. Siz  \n atrofingizdagilarni osongina qulay va qulay his qilasiz. Muvaffaqiyatli bo'lish uchun sizda, xususan,  \n san'atda juda yuqori salohiyat bor va agar siz pul ishlash yo'lini o'ylab topsangiz; siz \n ajoyib martaba uchun tayyorlanasiz. Sizning kamchiliklaringiz: siz hozirgi paytda yashayotganingiz  \n uchun pul va mas'uliyat bilan unchalik yaxshi emassiz. Siz hamma narsa amalga oshishiga ishonasiz va  \n ertangi kun haqida tashvishlanmang. Agar siz hissiy jihatdan xafa bo'lsangiz, boshqalarga  \n achchiq so'zlarni aytishingiz mumkin.",
				4: "Siz barcha qismlarni birlashtirib, uni ishga tushirishga harakat qilyapsiz. Siz mehnatkash, \n juda asosli, qat'iyatli, amaliy va intizomlisiz. Siz \"jamiyatning qurilish bloklari\"siz, chunki siz \n boshqalarning rivojlanishi uchun poydevor yaratasiz. Siz cho'qqiga chiqishning oson yo'lini \n izlamaysiz va sizni odatda juda tubdan deb hisoblaysiz. Siz tartibli va rejali bo'lishni yaxshi ko'rasiz. \n Agar rejangiz bo'lsa, hech qachon tugamaydigan ishlar ro'yxatini osongina engishingiz mumkin. \n Uy - bu sizning boshpanangiz va sizning uyingizdagi hamma narsa joyida bo'lishi kerak. \n Agar sizning uyingiz tartibsiz va tartibsiz bo'lsa, bu sizning yaxshi ishlamayotganligingizning  \n aniq belgisidir. Sizning kamchiliklaringiz: ongingizda juda ko'p narsa sodir bo'ladi, shuning uchun  \n fikringizni tinchlantirish yo'llarini topishingiz juda muhimdir. Aks holda, buyuk g'oyalar sizning boshingizda yashaydi va o'ladi. Sizda yaxshilik va noto'g'rilikni juda kuchli his qilasiz  \n va o'zingizga va boshqalarga nisbatan halollikni qadrlaysiz. Biroq, bu ba'zida o'zingizga  \n va boshqalarga nisbatan hukm chiqarishga olib kelishi mumkin. Siz o'z yo'llaringiz bilan \n shunchalik o'jar bo'lishingiz mumkinki, siz o'jar yoki juda jiddiy bo'lib qolasiz. Siz his-tuyg'ularingizni \n osongina ko'rsatasiz va hech narsani ushlab turmaysiz, bu ba'zan boshqalarni yuz o'girishi mumkin.  \n Bundan tashqari, siz juda ehtiyotkorsiz, bosh rejangizdan chetga chiqishdan nafratlanasiz, \n bu sizni imkoniyatlarni qo'ldan boy beradi.",
				5: "Sizning raqamingiz erkinlik va o'zgarishdir. Siz hamma narsadan ustun erkinlikni qidirasiz. \n Siz sarguzashtli bo'lishni yaxshi ko'rasiz va juda oson bezovtalanishingiz mumkin. Siz doimo yo'ldasiz, \n hayotingizda o'zgarish va xilma-xillikni xohlaysiz. Siz yangi odamlar bilan tanishishni, \n yangi narsalarni sinab ko'rishni va doimo hozirgi paytda yashashni yaxshi ko'rasiz. Siz odatda \n  o'zingizning xo'jayiningiz bo'lishni xohlaysiz va ajoyib sayohatchi sotuvchi bo'lasiz. Siz oddiy yoki takroriy \n narsalarni yoqtirmaysiz, shuning uchun siz doimo yangi narsaga intishingiz kerak.  \n Sizning hayotingiz his-tuyg'ularga bog'liq va tajribaga bo'lgan xohishingiz ko'p jihatdan o'zini  \n namoyon qilishi mumkin.Sizning kamchiliklaringiz: Agar siz sarguzasht bilan yashamasangiz, siz juda  \n dramatik bo'lasiz. Siz munosabatlarda tuzoqqa tushib qolish yoki bo'g'ilib qolishdan qo'rqasiz, \n shuning uchun siz o'rnashishingiz qiyin. Sarguzashtlarga bo'lgan ehtiyoj sizni chalg'itadi  \n va sizni atrofingizdagilarning his-tuyg'ularidan bexabar qoldirishi mumkin. Siz boshqalarni \n osongina manipulyatsiya qilasiz va boshqarasiz. Sizning maqsadingiz intizom, diqqat  \n va tajriba orqali hayotingizda muvozanat va ichki erkinlikni topishdir.",
				6: "Sizda kuchli tug'ma mas'uliyat va xabardorlik tuyg'usi bor, bu sizni tarbiyalashda ajoyib \n qiladi. Siz oila, uy va jamiyat haqidasiz. Siz mehribon, iliq, rahm-shafqatlisiz va boshqalarni xursand \n qilishga qiziqasiz. Siz qo'riqchi va provayder sifatida rivojlanasiz. Siz oilangiz va  \n do'stlaringizga xizmat qilishdan boshqa hech narsani yoqtirmaysiz. Sizning ota-onalik instinktlaringiz ham  \n juda kuchli. Siz ajoyib odamsiz va nima qilish kerakligini aytishni yoqtirmaysiz. Siz o'z uyingizni  \n va uning atrofidagilarni boyitish bilan shug'ullanasiz va bu sizga katta quvonch keltiradi.  \n Sizning kamchiliklaringiz: Siz osongina o'zingizni haqli deb bilasiz va boshqalarni tanqid qilasiz. \n Siz juda bag'ishlayotganingiz uchun siz boshqalarning ehtiyojlariga qul bo'lishingiz va o'z  \n ehtiyojlaringizga e'tibor bermasligingiz mumkin. Sizda yordam berish va aralashish o'rtasida  \n yaxshi muvozanat bo'lmasligi mumkin. Shuningdek, siz boshqa birovning, xususan, \n farzandlaringizning hayotida yordamchi bo'lishingiz mumkin va ularni hayot va uning barcha saboqlarini \n boshdan kechirishlariga to'sqinlik qilishingiz mumkin. Siz nazoratsiz odamsiz, shuning  \n uchun nomukammallikni qabul qilishga intiling.",
				7: "Siz juda ma'naviy jihatdan harakatlanasiz va bizning dunyomizdagi kuchga ega bo'lishingiz \n mumkin. Sizda yuksaklikka erishish potentsialingiz bor va boshqalardan ko'ra boshqacha ruhiy tekislikda \n yashashingiz mumkin. Sizning raqamingiz yuqoriroq xabardorlik va kengroq nuqtai nazarni \n beradi. Sizda sirli havo bor, lekin osongina yolg'iz bo'lib qolishingiz mumkin. Siz dono va bilimdonsiz. \n Siz har doim hamma narsaning haqiqiy ma'nosini va asosiy javobini qidirasiz. Sizda tabiiy go'zallikni \n yaxshi ko'rasiz: okean, yashil o'tlar, rejalar, gullar va boshqalar. Siz haqiqat izlovchi \n bo'lish uchun keldingiz. Buni quchoqlang. Sizning kamchiliklaringiz: imonga ega bo'lishni  \n o'rganishingiz kerak, go'yo bunday qilmasangiz, siz juda bema'ni bo'lib, giyohvandlik, spirtli ichimliklar, \n ish va geografiya orqali qochib qutulasiz. Sizning yolg'izlikka bo'lgan muhabbatingiz  \n yaqin munosabatlarni topishni qiyinlashtirishi mumkin. Odamlar sizni bilgandek his qilish \n uchun kurashadilar va siz eksantrik bo'lib qolishingiz mumkin. Moslashmaganingizda osongina \n xafa bo'lishingiz va tanqidiy fikrga tushishingiz mumkin.",
				8: "Siz kuchsiz va u bilan faxrlanasiz! Sizda xarakterning ajoyib hakami bor va atrofingizdagi \n odamlarni o'ziga jalb qiladi. Siz biznes yoki siyosiy dunyoda ajoyib rahbar bo'lar edingiz. Sizda  \n muvaffaqiyatga bo'lgan ehtiyoj va muvaffaqiyatga erishish uchun kuchli istak bor. Sizning  \n raqamingiz hokimiyat, moddiy boylik, shuhratparastlik va ehtiyotkorlikni anglatadi. Maqsadlaringizga erishish \n uchun astoydil harakat qilasiz. Sizning kamchiliklaringiz: moliyaviy xavfsizlikka ega bo'lmasangiz, \n o'zingizni \"xavfsiz\" his qilyapsiz. Sizning maqomingiz siz uchun muhim, bu sizning  \n imkoniyatlaringizdan yuqori yashashingizga olib kelishi mumkin. Siz uchun maslahat olish juda qiyin.  \n Siz mehnatkash bo'lishga moyil bo'lishingiz mumkin va ba'zan moliyaviy boylikka intilishda oilangiz  \n va do'stlaringizni e'tiborsiz qoldirishingiz mumkin. Muvozanat ustida ishlang va ichki \n muvaffaqiyat va boylikni topish uchun bu hayotda yangi saboqlar uchun imkoniyatlardan \n foydalaning. Katta orzu qiling va unga intiling!",
				9: "Numerologiyada to'qqiz raqam - bu to'liqlik soni. Siz tug'ma etakchisiz va odamlar sizni \n mas'ul deb o'ylashadi, hatto siz bo'lmasangiz ham. Siz boshqalarga g'amxo'rlik qilasiz, lekin \n qo'llab-quvvatlash va o'zingizni sevishingiz kerak bo'lganda gapirishingiz kerak. Sizda juda kuchli \n rahm-shafqat va saxiylik tuyg'usi bor va boshqalarga yordam berish siz uchun juda muhimdir. Sizning  \n saxiyligingiz chegara bilmaydi va siz atrofingizdagi odamlarni juda qulay his qilasiz. Sizning asosiy \n maqsadingiz yaxshiroq dunyoga intilishdir. Sizning kamchiliklaringiz: o'tmishdan voz \n kechish siz uchun qiyin. Siz o'zingizni onangiz yoki otangiz tomonidan sevilmagan yoki tashlab ketilgan  \n his qilishingiz mumkin, bu esa ular uchun javobgarlikni his qilishingizga sabab bo'ladi. \n Siz shunchalik beryapsizki, moliyaviy ahvolingiz yaxshi holatda bo'lmasligi mumkin. Shuningdek, \n sizda tartibsizlik bo'lsa, tarqoq bo'lish istagi bor. Agar siz o'zingizning haqiqiy berish  \n tuyg'usingizdan tashqari moddiy manfaatlarga intilayotgan bo'lsangiz, o'zingizdan chuqur norozi  \n bo'lishingiz mumkin."
			}
			return tariflar[life_path_number]

try:
	# Ma'lumotlar kiritish
	ism = input("Ismingizni kiriting: ").title()
	familya = input("Familyangizni kiriting: ").title()
	yosh = int(input("Yoshingizni kiriting: "))
	mail = input("Elektron manzilingiz: ").lower()
	t_yil = int(input("Tug'igan yilingiz: "))
	t_oy = int(input("Tug'ulgan oy: "))
	t_kun = int(input("Tug'ulgan kun: "))

	# Ma'lumotlarni Personga yuborish
	person = Days(ism, familya, yosh, mail, t_yil, t_oy, t_kun)
	print(person.get_info())
	print(f"Tug'ilgan kuni: {person.birth_day()}")
	print(f"Life path number: {person.get_life_path_number()}")
	print(person.get_info_by_number())

except ValueError:
	# Xatolik
	print("yil, oy, kun kiritishda butun sonlardan foydalaning")