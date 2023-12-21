from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from lexicon.lexicon import LEXICON_RU, LEXICON_CALLBACK
from keyboards.keyboards import inline_keyboard

router = Router()


@router.message(CommandStart())
async def process_start_cmd(message: Message) -> None:
    await message.answer(text=LEXICON_RU[message.text],
                         reply_markup=inline_keyboard)


@router.message(Command(commands='help'))
async def process_help_cmd(message: Message) -> None:
    await message.answer(text=LEXICON_RU[message.text])


@router.message(Command(commands='profile'))
async def process_profile_command(message: Message) -> None:
    pass


@router.callback_query(F.data == 'one')
async def process_one_cb(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        text=LEXICON_CALLBACK[callback.data],
        reply_markup=inline_keyboard
    )


@router.callback_query(F.data == 'two')
async def process_one_cb(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        text=LEXICON_CALLBACK[callback.data],
        reply_markup=inline_keyboard
    )


@router.callback_query(F.data == 'three')
async def process_one_cb(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        text=LEXICON_CALLBACK[callback.data],
        reply_markup=inline_keyboard
    )
