from aiogram import Bot
from aiogram.types import BotCommand


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command='/help',
                   description='How this bot works'),
        BotCommand(command='/profile',
                   description='Setup you profile')
    ]

    await bot.set_my_commands(main_menu_commands)
