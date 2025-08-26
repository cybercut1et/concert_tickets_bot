from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


from user_bot.handlers.callbacks import to_start_message, welcome, ticket_confirm, to_ticket_selection, confirm_buying_ticket
from user_bot.handlers.messages.welcome import send_welcome_message
#from user_bot.keyboards.inline.ticket import ticket_selection

on_start_router = Router()

on_start_router.include_router(to_start_message.router)
on_start_router.include_router(welcome.router)
on_start_router.include_router(ticket_confirm.router)
on_start_router.include_router(to_ticket_selection.router)
on_start_router.include_router(confirm_buying_ticket.router)

@on_start_router.message(Command('start'))
async def on_start_command(message: Message):
    #todo добавление юзера в бд + if not success

    await send_welcome_message(message)