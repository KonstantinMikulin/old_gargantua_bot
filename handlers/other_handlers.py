from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon import LEXICON_RU

router = Router()


@router.message()
async def process_any(message: Message):
    await message.answer(text=LEXICON_RU['other_answers'])
    await message.answer(text=LEXICON_RU['/help'])
