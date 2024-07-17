from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

filial = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("1️⃣Toshkent"),KeyboardButton("2️⃣Samarqand")],
        [KeyboardButton("⬅️Orqaga")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)