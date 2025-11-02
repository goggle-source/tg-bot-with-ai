import logging
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from app.generate import ai_generate

logging.basicConfig(level=logging.INFO, filename="logs.log", filemode="a")

class Chat(StatesGroup):
    wait = State()

rout = Router()

@rout.message(CommandStart())
async def cmd_start(message: Message):
    logging.info(f"User {message.from_user.id} started the bot")
    await message.answer("Привет! Это чат бот с искусственным интеллектом, способный ответить на все твои вопросы")

@rout.message(Chat.wait)
async def stop_message(message: Message):
    logging.info(f"User {message.from_user.id} wait the response")
    await message.answer("ваш запрос обрабатывается, подождите")

@rout.message()
async def generating(message: Message, state: FSMContext):
    logging.info(f"User {message.from_user.id} is generating the response")
    await state.set_state(Chat.wait)
    response = await ai_generate(message.text)
    await message.answer(response, parse_mode="Markdown")
    await state.clear()
    logging.info(f"User {message.from_user.id} got the response")