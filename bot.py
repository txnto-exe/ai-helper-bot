
from telebot import TeleBot, types
import os
from dotenv import load_dotenv

load_dotenv()
bot = TeleBot(os.getenv("BOT_TOKEN"))

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📥 Скачать TikTok без водяного знака")
    btn2 = types.KeyboardButton("🎥 Скачать YouTube в HD")
    btn3 = types.KeyboardButton("🖼 Генерация картинки (3/день)")
    btn4 = types.KeyboardButton("✍️ Генерация текста (песни, речи...)")
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    bot.send_message(message.chat.id,
                     f"Привет, {message.from_user.first_name}! 👋\n\n"
                     "Я — AI Helper. Что будем делать?",
                     reply_markup=markup)

@bot.message_handler(func=lambda msg: msg.text == "📥 Скачать TikTok без водяного знака")
def handle_tiktok(msg):
    bot.send_message(msg.chat.id, "🔗 Пришли ссылку на видео из TikTok:")

@bot.message_handler(func=lambda msg: msg.text == "🎥 Скачать YouTube в HD")
def handle_youtube(msg):
    bot.send_message(msg.chat.id, "🔗 Вставь ссылку на YouTube-видео:")

@bot.message_handler(func=lambda msg: msg.text == "🖼 Генерация картинки (3/день)")
def handle_image(msg):
    bot.send_message(msg.chat.id, "🖌 Напиши, что хочешь увидеть на изображении:")

@bot.message_handler(func=lambda msg: msg.text == "✍️ Генерация текста (песни, речи...)")
def handle_text(msg):
    bot.send_message(msg.chat.id, "📝 Напиши тему или запрос для текста:")

bot.infinity_polling()
