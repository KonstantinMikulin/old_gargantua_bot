from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from config_data.config import Config, load_config

config: Config = load_config()

bot = Bot(token=config.tg_bot.token)
dp = Dispatcher()

kb_builder = ReplyKeyboardBuilder()

buttons: list[KeyboardButton] = [KeyboardButton(text=f'{i + 1}') for i in range(10)]

kb_builder.add(*buttons)
kb_builder.adjust(1, 2, 4)

keyboard = kb_builder.as_markup(resize_keyboard=True)


@dp.message(CommandStart())
async def process_start_cmd(message: Message):
    await message.answer(text='Чего кошки боятся больше?',
                         reply_markup=keyboard
                         )


@dp.message(F.text == 'Собак 🦮')
async def process_dog_answer(message: Message):
    await message.answer(text='Да, собак'
                         )


@dp.message(F.text == 'Огурцов 🥒')
async def process_dog_answer(message: Message):
    await message.answer(text='Конечно, огурцов'
                         )

if __name__ == '__main__':
    dp.run_polling(bot)
