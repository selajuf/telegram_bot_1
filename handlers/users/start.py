from aiogram import types, Dispatcher


async def start_user(message: types.Message):
    await message.answer('Привет, напиши команду /questions')


def register_handlers_users(dp: Dispatcher):
    dp.register_message_handler(start_user, commands='start')