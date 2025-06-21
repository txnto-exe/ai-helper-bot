import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     "Привет! Я AI Helper (HIT) 🤖\n\n"
                     "Мои возможности:\n"
                     "- 📥 Скачать TikTok без водяного знака\n"
                     "- 📥 Скачать YouTube в HD\n"
                     "- 🖼 Генерация картинок (3 в день)\n"
                     "- 📝 Генерация текстов (песни, поздравления, речи)")

bot.polling()