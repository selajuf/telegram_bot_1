from aiogram.utils import executor
from run import dp

from handlers import client, admin, other

client.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True)
