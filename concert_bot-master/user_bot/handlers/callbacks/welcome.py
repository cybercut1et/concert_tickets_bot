from aiogram import Router, F
from aiogram.types import CallbackQuery

from user_bot.handlers.messages import send_ticket_selection_message

from user_bot.keyboards.inline.start import to_start_message


router = Router()

@router.callback_query(F.data == 'ticket')
async def buy_ticket_message(callback_query: CallbackQuery):
    await callback_query.message.delete()
    await send_ticket_selection_message(callback_query.message)
    await callback_query.answer()



@router.callback_query(F.data == 'faq')
async def about_event_message(callback_query: CallbackQuery):
    await callback_query.message.delete()
    await callback_query.message.answer(text='Инфо о мероприятии', reply_markup=to_start_message())
    await callback_query.answer()