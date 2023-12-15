from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import yes_no_keyboard, url_keyboard, callback_keyboard
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


@router.message(F.text.in_(['Yes', 'No']))
async def process_yes_no(message: Message):
    await message.answer(
        text='OK',
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(Command(commands='call'))
async def process_url_command(message: Message):
    await message.answer(
        text='Here are your big buttons',
        reply_markup=callback_keyboard
    )
    # print(message.model_dump_json(indent=4, exclude_none=True))


@router.callback_query(F.data.in_(['button_1 pressed', 'button_2 pressed']))
async def process_callback(callback: CallbackQuery):
    await callback.answer(text='We have your callback')
    print(callback.model_dump_json(indent=4, exclude_none=True))

