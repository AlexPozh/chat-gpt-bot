from aiogram import Dispatcher, Bot

import asyncio

from config import BotConfig

from handlers import user_handlers

from  aiogram.utils.chat_action import ChatActionMiddleware

async def main():
    
    bot = Bot(token=BotConfig.tg_token, parse_mode="HTML")

    dp = Dispatcher()


    dp.include_router(user_handlers.router)

    dp.message.middleware(ChatActionMiddleware())

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    

asyncio.run(main())