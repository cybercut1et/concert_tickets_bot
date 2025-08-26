from aiogram.types import Message
from ...keyboards.inline.ticket import ticket_selection


async def send_ticket_selection_message(message: Message):
    await message.answer(
        'Сколько билетов возжелаешь?',
        reply_markup = ticket_selection()
    )