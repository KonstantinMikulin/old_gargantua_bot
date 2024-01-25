from aiogram import Router, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from lexicon.lexicon import LEXICON_RU, LEXICON_FSM
from keyboards.keyboards import inline_gender_keyboard
from fsm.fsm_profile import FSMProfile, user_dict

router = Router()


async def process_start_cmd(message: Message) -> None:
    await message.answer(text=LEXICON_RU[message.text])


@router.message(Command(commands='help'))
async def process_help_cmd(message: Message) -> None:
    await message.answer(text=LEXICON_RU[message.text])
    pass


@router.message(Command(commands='profile'), StateFilter(default_state))
async def process_profile_command(message: Message, state: FSMContext) -> None:
    await message.answer(text=LEXICON_RU[message.text])
    await state.set_state(FSMProfile.fill_name)


@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext) -> None:
    await message.answer(text=LEXICON_RU[message.text])
    await state.clear()


@router.message(StateFilter(FSMProfile.fill_name), F.text.isalpha())
async def process_name_sent(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await message.answer(text=LEXICON_FSM['age'])
    await state.set_state(FSMProfile.fill_age)


@router.message(StateFilter(FSMProfile.fill_age), lambda x: x.text.isdigit() and 4 <= int(x.text) <= 120)
async def process_age_sent(message: Message, state: FSMContext) -> None:
    await state.update_data(age=message.text)
    await message.answer(
        text=LEXICON_FSM['gender'],
        reply_markup=inline_gender_keyboard
    )
    await state.set_state(FSMProfile.fill_gender)


@router.callback_query(StateFilter(FSMProfile.fill_gender), F.data.in_(['male', 'female']))
async def process_gender_press(callback: CallbackQuery, state: FSMContext) -> None:
    await state.update_data(gender=callback.data)
    await callback.message.delete()
    await callback.message.answer(text=LEXICON_FSM['weight'])
    await state.set_state(FSMProfile.fill_weight)


@router.message(StateFilter(FSMProfile.fill_weight), lambda x: x.text.isdigit() and 20 <= int(x.text) <= 700)
async def process_weight_sent(message: Message, state: FSMContext) -> None:
    await state.update_data(weight=message.text)
    user_dict[message.from_user.id] = await state.get_data()
    await state.clear()
    await message.answer(text=LEXICON_FSM['profile_done'])


@router.message(Command(commands='showdata'), StateFilter(default_state))
async def process_showdata_sent(message: Message) -> None:
    if message.from_user.id in user_dict:
        await message.answer(
            text=f'Name: {user_dict[message.from_user.id]["name"]}\n'
                 f'Age: {user_dict[message.from_user.id]["age"]}\n'
                 f'Gender: {user_dict[message.from_user.id]["gender"]}\n'
                 f'Weight: {user_dict[message.from_user.id]["weight"]}'
        )
    else:
        await message.answer(text='To fill - /profile')
