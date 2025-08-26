from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def welcome()-> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    keyboard.add(InlineKeyboardButton(
        text='Купить билеты',
        callback_data='ticket'
        ),
        InlineKeyboardButton(
        text='FAQ',
        callback_data='faq'
        )
    )
    keyboard.adjust(1)
    return keyboard.as_markup()