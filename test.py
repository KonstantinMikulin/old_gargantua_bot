res: dict = {'btn_tel': 'Телефон', 'btn_email': 'email', 'btn_website': 'Web-сайт', 'btn_vk': 'VK',
             'btn_tgbot': 'Наш телеграм-бот'}

a = res.get('btn_email', 'btn_tel')

print(a)
