from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

from lexicon.lexicon import LEXICON_RU, LEXICON_CALLBACK
from keyboards.keyboards import inline_keyboard

router = Router()


@router.message(CommandStart())
async def process_start_cmd(message: Message) -> None:
    await message.answer(text=LEXICON_RU[message.text])


@router.message(Command(commands='help'))
async def process_help_cmd(message: Message) -> None:
    await message.answer(text=LEXICON_RU[message.text])
    pass


@router.message(Command(commands='profile'))
async def process_profile_command(message: Message) -> None:
    await message.answer(
        text=LEXICON_RU[message.text],
        reply_markup=inline_keyboard
    )


@router.callback_query(F.data.in_(list(LEXICON_CALLBACK.keys())))
async def process_name_cb(callback: CallbackQuery) -> None:
    if callback.data == 'weight':
        await callback.message.edit_text(text=LEXICON_CALLBACK[callback.data])

    else:
        await callback.message.edit_text(
            text=LEXICON_CALLBACK[callback.data],
            reply_markup=inline_keyboard
        )
