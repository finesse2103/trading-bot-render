import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Обработка команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот запущен и готов к работе!")

# Обработка команды !сигнал
async def handle_signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.lower() == "!сигнал":
        await update.message.reply_text(
            "⚡️ Валютная пара: EUR/USD\n"
            "✅ Сигнал: ВВЕРХ\n"
            "✅ Соглашение открываем до: 15:45"
        )

# Запуск бота
async def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_signal))

    print("✅ Бот запущен...")
    await application.run_polling()

# Точка входа
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
