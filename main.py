import json

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, BaseFilter

from config.config import TOKEN, ADMIN_IDS

BOT_TOKEN = TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]):
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids


@dp.message(Command(commands='start'))
async def process_start_cmd(message: Message):
    # print(message.model_dump_json(indent=4, exclude_none=True))
    # print(message.__dict__)
    await message.answer(text=f'This is command "start"{message.from_user.id}')


@dp.message(IsAdmin(ADMIN_IDS))
async def answer_if_admin(message: Message):
    await message.answer(text='You are admin')


@dp.message()
async def answer_if_not_admin(message: Message):
    await message.answer(text='You are not admin')


@dp.message(F.photo)
async def process_send_phot(message: Message):
    await message.answer(text='You sent photo')


if __name__ == '__main__':
    dp.run_polling(bot)
