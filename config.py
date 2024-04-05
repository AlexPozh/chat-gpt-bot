from dataclasses import dataclass

from environs import Env

env = Env()
env.read_env()



@dataclass
class BotConfig:
    tg_token = env("BOT_TOKEN")