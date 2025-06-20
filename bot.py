import telebot
import os

TOKEN = os.getenv("7881957521:AAFA1klvJnCL5JFIlQCwi5_NBqtu5odDef8")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я AI Helper 🤖. Напиши, что тебе нужно!")

bot.infinity_polling()
