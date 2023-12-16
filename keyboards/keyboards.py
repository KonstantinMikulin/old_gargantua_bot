from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

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

inline_button_1 = InlineKeyboardButton(text='Вес', callback_data='one')
inline_button_2 = InlineKeyboardButton(text='Замеры', callback_data='two')

inline_kb_builder = InlineKeyboardBuilder()
inline_kb_builder.row(inline_button_1, inline_button_2)

inline_keyboard: InlineKeyboardMarkup = inline_kb_builder.as_markup()

# Callback buttons
callback_button_1 = InlineKeyboardButton(
    text='BUTTON 1',
    callback_data='button_1 pressed'
)

callback_button_2 = InlineKeyboardButton(
    text='BUTTON 2',
    callback_data='button_2 pressed'
)

callback_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[callback_button_1], [callback_button_2]]
)
