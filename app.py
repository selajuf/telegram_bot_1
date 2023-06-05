from aiogram.utils import executor
from loader import dp
from utils.set_bot_commands import set_default_commands
from handlers import client, admin, other


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)

client.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True)
