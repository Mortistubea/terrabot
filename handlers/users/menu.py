from aiogram import types 

from loader import dp
from keyboards.inline.main_menu import website_button
from keyboards.reply.tillar import tillar
from keyboards.reply.menu import main_menu
from keyboards.reply.sozlamalar import sozlamalar
from keyboards.reply.filial import filial
from keyboards.inline.websitebtn import websitebtn





@dp.message_handler(text="🇺🇿 Uzbek tili")
async def order_handler(message: types.Message):
    await message.answer("Siz uzbek tilini tanladingiz️️️️️: ",
                    reply_markup=main_menu)
    
@dp.message_handler(text="🇷🇺 Русский язык")
async def order_handler(message: types.Message):
    await message.answer("Вы выбрали узбекский язык: ",
                    reply_markup=main_menu)

@dp.message_handler(text="💳 Mening imtiyoz kartam")
async def card_handler(message: types.Message):
    
    await message.answer_photo(
        photo="https://idum.uz/wp-content/uploads/2016/11/Kak_proverit_shtrih-kod.jpg",
        caption="""Balans: 15599.0\nBir oyda sarflangan: 0.0\nBir yilga sarflangan: 0.0\nBor davr mobaynida sarflangan: 0.0"""
    )
    

@dp.message_handler(text="🛍 Saytdan buyurtma qilish")
async def order_handler(message: types.Message):
    await message.answer("Buyutma uchun quyidagi <a href='https://terrapro.uz/uz/'>link</a> ni ustiga bosing👇️️️️️️: ",
                    reply_markup=website_button,parse_mode='HTML')
    
@dp.message_handler(text="🇷🇺|🇺🇿в Tilni o'zgartirish")
async def order_handler(message: types.Message):
    text = "Здравствуйте! 🌟 Давайте для начала выберем язык обслуживания! 🌐\n\n"
    text += "Assalomu aleykum! 🌟 Keling, avvaliga xizmat ko’rsatish tilini tanlab olaylik. 🌐\n\n"
    text += "Choose a language, please"
    await message.answer(text, reply_markup=tillar)


@dp.message_handler(text="⚙️ Sozlamalar")
async def order_handler(message: types.Message):
    await message.answer("⚙️ Sozlamalar",reply_markup=sozlamalar)

@dp.message_handler(text="🔖 Shaxsiy ma'lumotlarni o'zgartirish")
async def order_handler(message: types.Message):
    await message.answer("Ustoz o'rgatmadilar!🤣")



@dp.message_handler(text="⬅️Orqaga")
async def order_handler(message: types.Message):
    await message.answer("⬅️Orqaga", reply_markup=main_menu)

@dp.message_handler(text="📍 Do'konlarimiz")
async def order_handler(message: types.Message):
    await message.answer("📍 Do'konlarimiz", reply_markup=filial)



@dp.message_handler(text="1️⃣Toshkent")
async def order_handler(message: types.Message):
    text = """

        1.  Самарканд Дарвоза
        Адрес: г.Ташкент ул. Караташ 5 "а" ТРЦ "Самарканд Дарваза" 3-этаж (https://maps.google.com/maps?q=41.316586,69.230498&ll=41.316586,69.230498&z=16)
        График работы:
        Будние дни: 10:00 – 22:00
        Выходные: 10:00 - 23:00
        Телефон: +998 71 205 10 23

    """
    await message.answer(text)

@dp.message_handler(text="2️⃣Samarqand")
async def order_handler(message: types.Message):
    text = """
        1. Makon Mall
        Адрес:  Город Самарканд Улица Мирзо Улугбек ТРЦ Makon Mall 
        График работы:
        Будние дни: 10:00 – 22:00
        Выходные: 10:00 - 22:00
        Телефон: +998 55 701 24 06

        2. Family Park
        Адрес:  Город Самарканд улица Нарпайская 76  ТРЦ Family Park  
        График работы:
        Будние дни: 10:00 – 22:00
        Выходные: 10:00 - 23:00
        Телефон: +998901044749

    """
    await message.answer(text)




@dp.message_handler(text="☎️ Biz bilan bog'lanish")
async def order_handler(message: types.Message):
    await message.answer("Написать в телеграм: @Terraprocommunity_bot\n\nПозвонить в офис: +998 71 250 93 91 📞")


@dp.message_handler(text="💼 Ish o'rinlari")
async def order_handler(message: types.Message):
    text = (
        "Стань частью нашей дружной семьи TerraPro😇\n\n"
        "Переходи в бот <a href='https://terrapro.uz/uz/'>TerraPro_jbot</a> "
        "или же позвони по номеру +998 90 968 47 42 и присоединяйся к нам.👇️️️️️️"
    )
    await message.answer(text, reply_markup=websitebtn, parse_mode='HTML')


@dp.message_handler(text="🔄 Mahsulotni qaytarish") 
async def order_handler(message: types.Message):
    text = (
    "Правила обмена и возврата товара.\n\n"
    "В соответствии с законом Республики Узбекистан «О защите прав потребителей» покупатель имеет право вернуть или обменять товар надлежащего качества в течение 10 дней со дня приобретения товара, если товар не был в употреблении, т.е. обувь или одежда не ношена, сохранен его товарный вид, отсутствуют любого рода повреждения, сохранены ярлыки, а также документ, подтверждающий факт приобретения товара - товарный или электронный чек.\n\n"
    "Если товар не соответствует вышеуказанным требованиям, в таком случае товар возврату и обмену не подлежит.\n\n"
    "Так же не подлежат возврату носочно-чулочные изделия и нательное белье.\n\n"
    "Потребитель вправе в течение 10 дней со дня покупки обменять товар ненадлежащего качества производственный брак, товар несоответствующий качеству на аналогичный в том магазине, где он был приобретен, а в случае отсутствия аналогичного товара в продаже — получить возврат денежных средств.\n"
)

    await message.answer(text)