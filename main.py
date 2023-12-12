from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from config_data.config import Config, load_config

config: Config = load_config()

bot = Bot(token=config.tg_bot.token)
dp = Dispatcher()

kb_builder = ReplyKeyboardBuilder()

contact_button = KeyboardButton(
    text='Send your number',
    request_contact=True
)

geo_btn = KeyboardButton(
    text='Send you location',
    request_location=True
)

poll_btn = KeyboardButton(
    text='Create poll',
    request_poll=KeyboardButtonPollType()
)

kb_builder.row(contact_button, geo_btn, poll_btn, width=1)
keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)


@dp.message(CommandStart())
async def process_start_cmd(message: Message):
    await message.answer(
        text='Here you go',
        reply_markup=keyboard
    )


if __name__ == '__main__':
    dp.run_polling(bot)
