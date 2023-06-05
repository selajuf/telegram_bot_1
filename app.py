from aiogram.utils import executor
from loader import dp
from utils.set_bot_commands import set_default_commands
from handlers.users import start, questions


async def on_startup(dp):
    await set_default_commands(dp)

start.register_handlers_users(dp)
questions.register_handlers_users(dp)

executor.start_polling(dp, skip_updates=True)
