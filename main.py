#Primer fer aquestes comandes:
# pip install pyTelegramBotAPI
import telebot
# posar el token del teu bot de teelegram
bot = telebot.TeleBot("5116615089:AAEJ0sIz4lSAxLKvgMCuj68iM7Gx_25Ktyo")
@bot.message_handler(commands=["help", "start"])

def enviar(message):
    bot.reply_to(message, "Hola, ¿Como estas?")

@bot.message_handler(func=lambda message:True)
def mensaje(message):
    bot.reply_to(message, message.text)


bot.polling()