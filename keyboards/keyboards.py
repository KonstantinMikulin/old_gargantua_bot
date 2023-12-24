from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


# test inline keyboard
inline_button_1 = InlineKeyboardButton(
    text='Name',
    callback_data='name'
)
inline_button_2 = InlineKeyboardButton(
    text='Age',
    callback_data='age'
)
inline_button_3 = InlineKeyboardButton(
    text='Weight',
    callback_data='weight'
)

kb_builder = InlineKeyboardBuilder()
kb_builder.row(inline_button_1, inline_button_2, inline_button_3)

inline_keyboard = kb_builder.as_markup()
