from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.redis import Redis, RedisStorage

redis = Redis(host='localhost')
storage = RedisStorage(redis=redis)

user_dict: dict[int, dict[str, str | int]] = {}


class FSMProfile(StatesGroup):
    fill_name = State()
    fill_age = State()
    fill_gender = State()
    fill_weight = State()
