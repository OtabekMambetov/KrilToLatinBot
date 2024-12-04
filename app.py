from telebot import TeleBot
from transliterate import to_cyrillic, to_latin

# Bot tokeningiz
TOKEN = "7935872938:AAFS_Nfb31y6O5B4HqCsMPAf9bPljAeVFlo"  # <-- Tokeningizni shu yerga kiriting
bot = TeleBot(token=TOKEN)

# "/start" komandasi uchun mas'ul funksiyani yozamiz
@bot.message_handler(commands=["start"])
def send_welcome(message):
    username = message.from_user.username  # Foydalanuvchi nomini olish
    if username:  # Agar foydalanuvchi usernamega ega bo'lsa
        xabar = f"Assalomu alaykum, @{username}!\n"
    else:
        xabar = "Assalomu alaykum!\n"
    xabar += "Kirill-Lotin-Kirill botiga xush kelibsiz!\nMatningizni yuboring."
    bot.reply_to(message, xabar)

# Matnni transliteratsiya qilish uchun funksiya
@bot.message_handler(func=lambda msg: msg.text is not None)
def translit(message):
    msg = message.text  # Foydalanuvchi yuborgan matn
    # Kirill yoki Lotin asosida transliteratsiya
    javob = to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob)  # Foydalanuvchiga javobni yuborish

# Botni ishga tushirish
bot.polling()
