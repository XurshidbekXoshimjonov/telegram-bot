from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


menu = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text='Sherik kerak'),
                KeyboardButton(text='Ish joyi kerak')
            ],   
            [
                KeyboardButton(text='Xodim kerak'),
                KeyboardButton(text='Ustoz kerak')
            ],
            [
                  KeyboardButton(text='Shogird kerak')
            ],
    ],
            resize_keyboard=True
    )


majburiy_obuna = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kanalga o'tish", url="https://t.me/Xoshimjonov_Portfolio")
        ],
        [
            InlineKeyboardButton(text="Tasdiqlash",callback_data="tasdiqlash")
        ]
    ]
)