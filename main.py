import os
from environs import Env

env = Env()
env.read_env()

bot_token = env('BOT_TOKEN')

print(bot_token)

print(os.getenv('BOT_TOKEN'))
