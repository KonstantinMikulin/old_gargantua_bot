from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Reply keyboard buttons
button_yes = KeyboardButton(text='Yes')
button_no = KeyboardButton(text='No')

yes_no_kb_builder = ReplyKeyboardBuilder()
yes_no_kb_builder.row(button_yes, button_no, width=2)

yes_no_keyboard: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True,
    input_field_placeholder='Yes please'
)

# Inline keyboard buttons
url_button_1 = InlineKeyboardButton(
    text='Watch some',
    url='https://www.youtube.com/'
)

url_button_2 = InlineKeyboardButton(
    text='Buy some',
    url='https://www.avito.ru/'
)

channel_button = InlineKeyboardButton(
    text='Read some',
    url=f'https://t.me/redakciya_channel'
)

url_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[url_button_1], [url_button_2], [channel_button]]
)
