# Этот хэндлер будет срабатывать на команду "/delmenu"
# и удалять кнопку Menu c командами
@dp.message(Command(commands='delmenu'))
async def del_main_menu(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer(text='Кнопка "Menu" удалена')