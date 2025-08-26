from aiogram import Router, F, types
from ..messages import confirm_buying_ticket_message

router = Router()

@router.callback_query(F.data.regexp(r"^\d+_confirm_buying_ticket$"))
async def welcome_message(callback_query: types.CallbackQuery):
    ticket_number = int(callback_query.data.split("_")[0])
    await callback_query.message.delete()
    await confirm_buying_ticket_message(callback_query.message, ticket_number)
    await callback_query.answer()