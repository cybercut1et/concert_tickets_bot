from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from auth_bot.handlers.messages import send_auth_message,send_wish_message

on_auth_router = Router()

@on_auth_router.message(Command('auth'))
async def on_auth_command(message:Message):
    if message.from_user.id == 703955895:
        await send_auth_message(message)
    else:
        await send_wish_message(message)
