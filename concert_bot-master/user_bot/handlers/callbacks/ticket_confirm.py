from aiogram import Router, F, types
from ..messages import send_ticket_selection_message, send_ticket_confirm_message

router = Router()


@router.callback_query(F.data.regexp(r"^\d+_ticket$"))
async def ticket_callback_handler(callback_query: types.CallbackQuery):
    ticket_number = int(callback_query.data.split("_")[0])
    await callback_query.message.delete()
    await send_ticket_confirm_message(callback_query.message, ticket_number)
    await callback_query.answer()