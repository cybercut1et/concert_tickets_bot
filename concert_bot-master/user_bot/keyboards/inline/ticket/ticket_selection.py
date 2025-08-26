from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def ticket_selection()-> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    keyboard.add(InlineKeyboardButton(
        text='1',
        callback_data='1_ticket'
        ),
        InlineKeyboardButton(
        text='2',
        callback_data='2_ticket'
        ),
        InlineKeyboardButton(
            text='3',
            callback_data='3_ticket'
        ),
        InlineKeyboardButton(
            text='4',
            callback_data='4_ticket'
        ),
        InlineKeyboardButton(
            text='5',
            callback_data='5_ticket'
        )
    )
    keyboard.adjust(5)
    return keyboard.as_markup()