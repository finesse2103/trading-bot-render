import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Бот запущен и готов присылать сигналы!")

# Команда /signal (латиницей!)
async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚡️ Валютная пара: `EUR/USD`\n"
        "✅ Сигнал: ВВЕРХ\n"
        "✅ Соглашение открываем до: 15:27",
        parse_mode="Markdown"
    )

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    # Обработка команд латиницей
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("signal", signal))

    # Запуск без asyncio.run() — для Render
    application.run_polling()

if __name__ == "__main__":
    main()
