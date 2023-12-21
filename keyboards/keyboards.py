from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


# test inline keyboard
inline_button_1 = InlineKeyboardButton(
    text='1',
    callback_data='one'
)
inline_button_2 = InlineKeyboardButton(
    text='2',
    callback_data='two'
)
inline_button_3 = InlineKeyboardButton(
    text='3',
    callback_data='three'
)

kb_builder = InlineKeyboardBuilder()
kb_builder.row(inline_button_1, inline_button_2, inline_button_3)

inline_keyboard = kb_builder.as_markup()
