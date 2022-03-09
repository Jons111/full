from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
royxat = ['a','b']
asosiy = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Murojat qilish"),
            KeyboardButton(text="Takliflar"),

           ],
        [
            KeyboardButton(text="Xavfsiz mahalla"),
        ]

    ],
  resize_keyboard=True
)
