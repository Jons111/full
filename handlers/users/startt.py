
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from keyboards.default.menu import asosiy








@dp.message_handler(CommandStart())
async def bot_echo(message: types.Message):
    await message.answer(text="📌 Assalomu alaykum! Obod MFY yoshlari! Ushbu bot orqali siz o'z ariza va shikoyatlarinigizga javob olishingiz mumkin.",reply_markup=asosiy)






