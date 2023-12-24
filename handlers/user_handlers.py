from aiogram import Router, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from lexicon.lexicon import LEXICON_RU, LEXICON_FSM
from keyboards.keyboards import inline_gender_keyboard
from fsm.fsm import FSMFillForm

router = Router()


@router.message(CommandStart())
async def process_start_cmd(message: Message) -> None:
    await message.answer(text=LEXICON_RU[message.text])


@router.message(Command(commands='help'))
async def process_help_cmd(message: Message) -> None:
    await message.answer(text=LEXICON_RU[message.text])
    pass


@router.message(Command(commands='profile'), StateFilter(default_state))
async def process_profile_command(message: Message, state: FSMContext) -> None:
    await message.answer(text=LEXICON_RU[message.text])
    await state.set_state(FSMFillForm.fill_name)


@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext) -> None:
    await message.answer(text=LEXICON_RU[message.text])
    await state.clear()


@router.message(StateFilter(FSMFillForm.fill_name), F.text.isalpha())
async def process_name_sent(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await message.answer(text=LEXICON_FSM['age'])
    await state.set_state(FSMFillForm.fill_age)


@router.message(StateFilter(FSMFillForm.fill_age), lambda x: x.text.isdigit() and 4 <= int(x.text) <= 120)
async def process_age_sent(message: Message, state: FSMContext) -> None:
    await state.update_data(age=message.text)
    await message.answer(
        text=LEXICON_FSM['gender'],
        reply_markup=inline_gender_keyboard
    )
    await state.set_state(FSMFillForm.fill_gender)
