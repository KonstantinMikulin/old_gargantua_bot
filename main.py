from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

from config.config import TOKEN

BOT_TOKEN = TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands='start'))
async def process_start_cmd(message: Message):
    await message.answer(text='This is command "start"')

if __name__ == '__main__':
    dp.run_polling(bot)
