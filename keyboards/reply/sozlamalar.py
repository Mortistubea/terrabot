from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

sozlamalar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("🇷🇺|🇺🇿в Tilni o'zgartirish")],
        [KeyboardButton("🔖 Shaxsiy ma'lumotlarni o'zgartirish")],
        [KeyboardButton("⬅️Orqaga")],      
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)