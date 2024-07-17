from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("💳 Mening imtiyoz kartam")],
        [KeyboardButton("🛍 Saytdan buyurtma qilish")],
        [
            KeyboardButton("⚙️ Sozlamalar"),
            KeyboardButton("📍 Do'konlarimiz")
        ],
        [
            KeyboardButton("☎️ Biz bilan bog'lanish"),
            KeyboardButton("✍️ Izoh qoldirish")
        ],
        [
            KeyboardButton("💼 Ish o'rinlari"),
            KeyboardButton("🔄 Mahsulotni qaytarish")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)