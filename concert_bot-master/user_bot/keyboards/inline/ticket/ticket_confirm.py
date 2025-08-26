from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def ticket_confirm(num_of_tickets: int)-> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    keyboard.add(InlineKeyboardButton(
        text='confirm choose',
        callback_data=f'{num_of_tickets}_confirm_buying_ticket'
        ),
        InlineKeyboardButton(
        text='step back',
        callback_data='to_ticket_selection'
        )
    )
    keyboard.adjust(2)
    return keyboard.as_markup()