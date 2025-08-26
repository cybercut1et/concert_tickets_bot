import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types

from auth_bot.handlers.commands.on_auth_command import on_auth_router
from user_bot.handlers.commands.on_start_command import on_start_router

load_dotenv()

async def main():
    user_bot = Bot(token=os.getenv('USER_BOT_TOKEN'))
    user_dp = Dispatcher()
    user_dp.include_router(on_start_router)

    auth_bot = Bot(token=os.getenv('ADMIN_BOT_TOKEN'))
    auth_dp = Dispatcher()
    auth_dp.include_router(on_auth_router)



    await asyncio.gather(
        user_dp.start_polling(user_bot),
        auth_dp.start_polling(auth_bot)
    )

if __name__ == '__main__':
    asyncio.run(main())

'''
    # Обработчик команды /start для админ-бота
    @auth_dp.message(CommandStart())
    async def start_admin_handler(message: types.Message):
        args = message.text.split()  # Разделяем текст команды
        if len(args) > 1:  # Если передан аргумент
            param = args[1]
            await message.answer(f"Вы передали аргумент: {param}")
        else:
            await message.answer("Привет! Я чорт.")

    # Обработчик команды /start для обычного бота
    @user_dp.message(CommandStart())
    async def start_user_handler(message: types.Message):
        args = message.text.split()  # Разделяем текст команды
        if len(args) > 1:  # Если передан аргумент
            param = args[1]
            await message.answer(f"Вы передали аргумент: {param}")
        else:
            await message.answer("Привет! Я бот.")
    '''
