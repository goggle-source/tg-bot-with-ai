from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from app.generate import ai_generate

class Chat(StatesGroup):
    wait = State()

rout = Router()

@rout.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет! Это чат бот с искусственным интеллектом, способный ответить на все твои вопросы")

@rout.message(Chat.wait)
async def stop_message(message: Message):
    await message.answer("ваш запрос обрабатывается, подождите")

@rout.message()
async def generating(message: Message, state: FSMContext):
    await state.set_state(Chat.wait)
    response = await ai_generate(message.text)
    await message.answer(response, parse_mode="Markdown")
    await state.clear()