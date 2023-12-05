import json

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

from config.config import TOKEN

BOT_TOKEN = TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands='start'))
async def process_start_cmd(message: Message):
    # print(message.model_dump_json(indent=4, exclude_none=True))
    # print(message.__dict__)
    await message.answer(text=f'This is command "start"{message.from_user.id}')


if __name__ == '__main__':
    dp.run_polling(bot)
