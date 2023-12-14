from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardRemove

from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import yes_no_keyboard

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
