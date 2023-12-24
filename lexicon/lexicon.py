LEXICON_RU: dict[str, str] = {
    '/start': 'Привет!\n\nЗдесь можно записать и сохранить свой текущий вес.\n'
              'Или записать замеры своего тела и сохранить их.\n'
              'Помощь по команде /help',
    '/help': 'Список команд бота:\n'
             '/start - запустить бот\n'
             '/help - список команд\n',
    '/profile': 'Let`s fill your profile\n'
                'If you want to stop filling profile - senf /cancel\n\n'
                'What is your name?',
    '/cancel': 'You have stopped FSM\n'
               'If you want to fill your profile - send /profile',
    'other_answers': 'Я понимаю не все сообщения.\n'
                     '/help - cписок доступных команд'
}

LEXICON_COMMANDS_RU: dict[str, str] = {
    '/help': 'How this bot works'
}

LEXICON_CALLBACK: dict[str, str] = {
    'name': 'How old are you?',
    'age': 'What is your current weight?',
    'weight': 'Thank you. Your profile was created'
}
