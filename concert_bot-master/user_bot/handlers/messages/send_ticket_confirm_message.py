from aiogram.types import Message
from ...keyboards.inline.ticket import ticket_confirm


async def send_ticket_confirm_message(message: Message, num_of_tickets: int):
    if num_of_tickets == 1:
        await message.answer(
        f'Вы выбрали {num_of_tickets} билет',
            reply_markup = ticket_confirm(num_of_tickets)
        )
    elif num_of_tickets == 5:
        await message.answer(
            f'Вы выбрали {num_of_tickets} билетов',
            reply_markup=ticket_confirm(num_of_tickets)
        )

    else:
        await message.answer(
            f'Вы выбрали {num_of_tickets} билетa',
            reply_markup=ticket_confirm(num_of_tickets)
        )
