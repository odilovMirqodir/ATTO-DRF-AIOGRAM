import asyncio

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from api.api import GetRequests

api = GetRequests()


async def languages():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🇺🇿 Uzbek"),
            ],
            [
                KeyboardButton(text="🇷🇺 Русский"),
            ],
            [
                KeyboardButton(text="🇺🇸 English"),
            ],
        ],
        resize_keyboard=True
    )
    return keyboard


async def get_registration(language):
    if language == 'uz':
        registration_text = "Ro'yxatdan o'tish"
    elif language == 'ru':
        registration_text = "Зарегистрироваться"
    else:
        registration_text = "Registration"

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=registration_text)
            ],
        ],
        resize_keyboard=True
    )
    return keyboard


async def send_user_phone(language):
    if language == 'uz':
        number = "Raqam Yuborish"
    elif language == 'ru':
        number = "Отправить номер"
    else:
        number = "Send number"

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=number, request_contact=True)
            ],
        ],
        resize_keyboard=True
    )
    return keyboard


async def main_menu(language):
    button_texts = {
        'uz': ["QR kod", "Biz bilan boglanish", "Tariflar", "Sozlamalar ⚙", "Mening Profilim"],
        'ru': ["QR код", "Связаться с нами", "Тарифы", "Настройки ⚙", "Мой профиль"],
        'en': ["QR code", "Contact us", "Tariffs", "Settings ⚙", "My Profile"]
    }
    buttons = [KeyboardButton(text=text) for text in
               button_texts.get(language, ["QR code", "Contact us", "Tariffs", "Settings ⚙", "My Profile"])]

    row1 = buttons[:2]
    row2 = buttons[2:4]
    row3 = buttons[4:]

    keyboard = ReplyKeyboardMarkup(keyboard=[row1, row2, row3], resize_keyboard=True)

    return keyboard


async def get_new_qr_code(language):
    if language == 'uz':
        registration_text = "Yangi QR kode"
    elif language == 'ru':
        registration_text = "Новый QR-код"
    else:
        registration_text = "New QR code"

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=registration_text, callback_data='new_qr_generate')
            ],
        ],
    )
    return keyboard


async def get_payments_button():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Click", callback_data='click_uz')],
            [InlineKeyboardButton(text="Payme", callback_data='payme_uz')],
            [InlineKeyboardButton(text="Uzum", callback_data='uzum_uz')],
            [InlineKeyboardButton(text="Paynet", callback_data='uzum_uz')],
            [InlineKeyboardButton(text="Rahmat", callback_data='rhmt_uz')],

        ],
    )
    return keyboard


async def get_categories_button():
    categories = await api.get_categories()
    keyboard_buttons = []

    for category in categories:
        button_text = category['tarif_name']
        callback_data = f"category|{category['id']}"
        keyboard_buttons.append([InlineKeyboardButton(text=button_text, callback_data=callback_data)])

    keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)
    return keyboard


async def get_activate_tarif(language):
    if language == 'uz':
        registration_text = "Tarifni faollashtirish"
    elif language == 'ru':
        registration_text = "Активация тарифа"
    else:
        registration_text = "Activating the tariff"

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=registration_text, callback_data='tarif_activate')
            ],
        ],
    )
    return keyboard
