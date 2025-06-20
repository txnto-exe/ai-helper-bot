import telebot

# 🔒 ВСТАВЬ СЮДА СВОЙ ТОКЕН от BotFather
BOT_TOKEN = "7881957521:AAFA1klvJnCL5JFIlQCwi5_NBqtu5odDef8"

bot = telebot.TeleBot(BOT_TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "👋 Привет! Я бот-помощник AI Helper.\n\n"
        "📌 Вот что я умею:\n"
        "- Автоматически публиковать новости\n"
        "- Отвечать на команды\n"
        "- Помогать с Telegram-каналом\n\n"
        "Напиши /help чтобы узнать больше!"
    )
    bot.send_message(message.chat.id, welcome_text)

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "🤖 Доступные команды:\n"
        "/start – Приветствие и описание функций\n"
        "/help – Помощь по командам\n"
        # Добавь свои команды здесь
    )
    bot.send_message(message.chat.id, help_text)

# Запуск бота (вечный цикл)
if __name__ == "__main__":
    print("✅ Бот запущен...")
    bot.infinity_polling()
