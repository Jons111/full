
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ContentTypes, CallbackQuery

from loader import dp,db
from keyboards.default.menu import asosiy







tg_idlar =set( db.select_all_users_ids())
for idd in tg_idlar:
    @dp.callback_query_handler(chat_id =1892438581,text=f'idd{idd}')
    async def fun(call:CallbackQuery):
        pass







