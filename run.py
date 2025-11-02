import asyncio
import logging
from aiogram import Bot, Dispatcher
from app.handlers import rout
from config import TOKEN
from app.handlers import rout

logging.basicConfig(level=logging.INFO, filename="logs.log", filemode="a")

async def main():
    logging.info("Start polling")
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router=rout)
    await dp.start_polling(bot)
    logging.info("Polling stopped")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exist")