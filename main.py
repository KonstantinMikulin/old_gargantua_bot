import json

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, BaseFilter

from config.config import TOKEN, ADMIN_IDS

BOT_TOKEN = TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


class NumbersInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers = []
        for word in message.text.split():
            normalized_word = word.replace('.', '').replace(',', '').strip()
            if normalized_word.isdigit():
                numbers.append(int(normalized_word))

        if numbers:
            return {'numbers': numbers}

        return False


@dp.message(Command(commands='start'))
async def process_start_cmd(message: Message):
    # print(message.model_dump_json(indent=4, exclude_none=True))
    # print(message.__dict__)
    await message.answer(text='This is command "start"')


@dp.message(F.text.lower().startswith('найди числа'),
            NumbersInMessage())
# Помимо объекта типа Message, принимаем в хэндлер список чисел из фильтра
async def process_if_numbers(message: Message, numbers: list[int]):
    await message.answer(
            text=f'Нашел: {", ".join(str(num) for num in numbers)}')


# Этот хэндлер будет срабатывать, если сообщение пользователя
# начинается с фразы "найди числа", но в нем нет чисел
@dp.message(F.text.lower().startswith('найди числа'))
async def process_if_not_numbers(message: Message):
    await message.answer(
            text='Не нашел что-то :(')


if __name__ == '__main__':
    dp.run_polling(bot)
