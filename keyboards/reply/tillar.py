from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

tillar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("🇺🇿 Uzbek tili"), KeyboardButton("🇷🇺 Русский язык")],     
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)