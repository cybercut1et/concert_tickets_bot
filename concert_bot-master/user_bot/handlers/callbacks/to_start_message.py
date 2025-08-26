from aiogram import Router, F, types
from ..messages import send_welcome_message


router = Router()

@router.callback_query(F.data == 'to_start_message')
async def welcome_message(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    await send_welcome_message(callback_query.message)
    await callback_query.answer()
