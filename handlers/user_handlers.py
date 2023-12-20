from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import yes_no_keyboard, callback_keyboard, inline_keyboard, create_keyboard

router = Router()


@router.message(CommandStart())
async def process_start_cmd(message: Message):
    await message.answer(text=LEXICON_RU[message.text])


@router.message(Command(commands='help'))
async def process_help_cmd(message: Message):
    await message.answer(text=LEXICON_RU[message.text])


