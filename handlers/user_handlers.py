from aiogram import Router, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

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


@router.message(Command(commands='profile'), StateFilter(default_state))
async def process_profile_command(message: Message) -> None:
    await message.answer(
        text=LEXICON_RU[message.text]
    )


@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_RU[message.text])
    await state.clear()



