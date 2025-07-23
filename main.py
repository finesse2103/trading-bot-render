import os
import asyncio
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

async def send_signal():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text="⚡️ Валютная пара: EUR/USD\n✅ Сигнал: ВНИЗ\n✅ Соглашение открываем до: 12:45")

if __name__ == "__main__":
    asyncio.run(send_signal())