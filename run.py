import asyncio

from aiogram import Bot, Dispatcher
from app.handlers import rout
from config import TOKEN
from app.handlers import rout


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router=rout)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exist")