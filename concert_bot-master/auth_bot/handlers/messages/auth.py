from aiogram.types import Message


async def send_auth_message(message: Message):
    args = message.text.split()  # Разделяем текст команды

    if len(args) > 1:
        param = args[1]
        await message.answer(f"принял, гости зареганы: {param}")
    else:
        await message.answer("чорт. qr хуевый")
