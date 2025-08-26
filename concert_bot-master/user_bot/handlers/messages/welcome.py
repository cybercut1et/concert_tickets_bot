from aiogram.types import Message
from ...keyboards.inline.start import welcome


async def send_welcome_message(message: Message):
    await message.answer(
        'Здарова бандит, хочешь на конц?',
        reply_markup = welcome()
    )