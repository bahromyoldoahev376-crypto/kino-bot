import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "7556805552:AAEaGmx2Cw7og-cAFuLfzJX_liY-wjJHx0k"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

KINOLAR = {
    "101": "Avatar",
    "102": "Fast & Furious",
    "103": "John Wick"
}

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        f"🎬 Salom, {message.from_user.full_name}!
\n"
        "Kino kodini yuboring."
    )

@dp.message(F.text)
async def kino_handler(message: Message):
    kod = message.text.strip()

    if kod in KINOLAR:
        await message.answer(
            f"🎥 Kino topildi:
{KINOLAR[kod]}"
        )
    else:
        await message.answer(
            "❌ Bunday kino topilmadi."
        )

async def main():
    print("Bot ishga tushdi!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())