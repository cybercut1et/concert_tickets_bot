from aiogram.types import Message


async def send_wish_message(message: Message):
    await message.answer(
        'Хорошего настроения :]',
    )