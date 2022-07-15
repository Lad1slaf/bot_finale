from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from tauth.views import register


class PasswordState(StatesGroup):
    password1 = State()
    password2 = State()


async def answer(message: types.Message):
    await message.answer('Welcome to registration bot \nEnter /register for registration')


async def enter_pass(message: types.Message):
    await message.answer('Enter password:')
    await PasswordState.password1.set()


async def process_pas1(message: types.Message, state: FSMContext):
    if '@' and '/' and ' ' not in message.text and len(message.text) >= 8:
        await state.update_data(password1=message.text)
        await message.answer('Confirm password')
        await PasswordState.password2.set()
    else:
        await message.answer('Password must have minimum 8 simbols and not contains special symbols ')


async def process_pas2(message: types.Message, state: FSMContext):
    await state.update_data(password2=message.text)
    username = message.from_user.username.lower()
    user_id = message.from_user.id
    name = message.from_user.first_name
    link = message.from_user.url
    if '@' and '/' and ' ' not in message.text and len(message.text) >= 8:
        await state.update_data(password2=message.text)
        data = await state.get_data()
        p1 = data.get('password1')
        p2 = data.get('password2')
        print(p1, p2)

        if p2 != p1:
            await message.answer(
                'Passwords must be the same ')

        else:
            await register(username=username, password=p2, name=name, user_id=user_id, link=link)
            await state.finish()
            await message.answer('Registration successful')
    else:
        await message.answer(
            'Password must have minimum 8 simbols and not contains special symbols ')


def register_answer(dp: Dispatcher):
    dp.register_message_handler(answer, is_user=False)


def register_enter_pass(dp: Dispatcher):
    dp.register_message_handler(enter_pass, commands=["register"], is_user=False)


def register_process_pas1(dp: Dispatcher):
    dp.register_message_handler(process_pas1, state=PasswordState.password1, is_user=False)


def register_process_pas2(dp: Dispatcher):
    dp.register_message_handler(process_pas2, state=PasswordState.password2, is_user=False)
