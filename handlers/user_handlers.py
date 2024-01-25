from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import yes_no_keyboard, callback_keyboard, inline_keyboard, create_keyboard

router = Router()


@router.message(CommandStart())
async def process_start_cmd(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


@router.message(Command(commands='help'))
async def process_help_cmd(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.message(Command(commands='profile'))
async def process_profile_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/profile'],
        reply_markup=yes_no_keyboard
    )


@router.message(Command(commands='record'))
async def process_record_command(message: Message):
    await message.answer(
        text='Какие значение записать?',
        reply_markup=inline_keyboard
    )


@router.message(F.text.lower().in_(['yes', 'no']))
async def process_yes_no(message: Message):
    await message.answer(
        text='OK',
        reply_markup=ReplyKeyboardRemove()
    )


# testing handler for callback_keyboard
@router.message(Command(commands='call'))
async def process_url_command(message: Message):
    await message.answer(
        text='Here are your big buttons',
        reply_markup=callback_keyboard
    )
    # print(message.model_dump_json(indent=4, exclude_none=True))


@router.callback_query(F.data == 'button_1 pressed')
async def process_button_1_press(callback: CallbackQuery):
    if callback.message.text != 'Button 1 was pressed':
        await callback.message.edit_text(
            text='Button 1 was pressed',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer()


@router.callback_query(F.data == 'button_2 pressed')
async def process_button_1_press(callback: CallbackQuery):
    if callback.message.text != 'Button 2 was pressed':
        await callback.message.edit_text(
            text='Button 2 was pressed',
            reply_markup=callback.message.reply_markup
        )
    await callback.answer()
