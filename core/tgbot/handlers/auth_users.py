from aiogram import Dispatcher
from aiogram.types import Message


async def answer(message: Message):
    username = message.from_user.username.lower()
    await message.answer(f'You are already registered.\nYour username: {username}')


def register_auth_user(dp: Dispatcher):
    dp.register_message_handler(answer, is_user=True)
