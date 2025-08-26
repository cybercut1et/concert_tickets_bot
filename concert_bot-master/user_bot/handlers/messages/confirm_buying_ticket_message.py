from aiogram.types import Message
from ...keyboards.inline.ticket import ticket_confirm


async def confirm_buying_ticket_message(message: Message, num_of_tickets: int):
    await message.answer(
        f'Вот реквизиты для оплаты:....\nплати {270*num_of_tickets} рублей',
        reply_markup = None
                         )