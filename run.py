import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from app.handlers import rout
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import TOKEN

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("logs.log")
    ]
)

async def main():
    logging.info("Start polling")
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    dp.include_router(router=rout)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    logging.info("Polling stopped")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("close and stop bot")
        sys.exit(1)
    
    logging.info("stop bot")
            