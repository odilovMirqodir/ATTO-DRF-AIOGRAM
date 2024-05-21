from uuid import uuid4
import qrcode
import datetime
from api.api import GetRequests

api = GetRequests()


async def get_text_language_user(language_user):
    if language_user == 'uz':
        return "*Tillardan birini tanlang*"
    elif language_user == 'ru':
        return "*Выберите один из языков*"
    else:
        return "*Choose one of the languages*"


async def get_hello_text1(language_user):
    if language_user == 'uz':
        return "*Kategoriyalardan birini tanlang*"
    elif language_user == 'ru':
        return "*Выберите одну из категорий*"
    else:
        return "*Choose one of the categories*"


async def get_hello_text():
    text = f"*Assalomu aleykum ATTO QR botga xush kelibsiz\n*"
    text += "*Здравствуйте и добро пожаловать в ATTO QR-бот\n*"
    text += "*Hello and welcome to ATTO QR bot*"
    return text


async def get_registration_text(language_user):
    if language_user == 'uz':
        return "*Siz ro'yxatdan o'tmagansiz ❗*"
    elif language_user == 'ru':
        return "*Вы не зарегистрированы ❗*"
    else:
        return "*You are not registered ❗*"


async def get_menu_text(language_user):
    if language_user == 'uz':
        return "*Kategoriyalardan birini tanlang*"
    elif language_user == 'ru':
        return "*Выберите одну из категорий*"
    else:
        return "*Select one of the categories*"


async def name_surname_text(language_user):
    if language_user == 'uz':
        return "*Ism Familyangizni kiriting\nNamuna:Aziz Azizov*"
    elif language_user == 'ru':
        return "*Введите свое имя и фамилию\nПример: Азиз Азизов*"
    else:
        return "*Enter your first and last name\nExample: Aziz Azizov*"


async def send_phone_number_text(language_user):
    if language_user == 'uz':
        return "*Telefon raqamingizni yuboring 👇🏻*"
    elif language_user == 'ru':
        return "*Отправьте свой номер телефона 👇🏻*"
    else:
        return "*Send your phone number 👇🏻*"


async def success_all(language_user):
    if language_user == 'uz':
        return "*Ro'yxatdan o'tdingiz ✅*"
    elif language_user == 'ru':
        return "*Вы зарегистрировались ✅*"
    else:
        return "*You have registered ✅*"


async def update_langugae_user(langugae):
    if langugae == '🇺🇿 Uzbek':
        return "uz"
    elif langugae == '🇷🇺 Русский':
        return "ru"
    else:
        return "eng"


async def get_qr_code_for_user(langugae, value):
    vaqt = datetime.datetime.now()
    bugun_oy, vaqti = vaqt.strftime("%Y-%m-%d"), vaqt.strftime("%H:%M:%S")
    if langugae == 'uz':
        return f"""*Bekat: Buyuk Ipak Yo'li
Sana: {bugun_oy} yil    Vaqt: {vaqti}
    << TOSHKENT METROPOLITENI>> UZ
Chipta raqami:  #{str(value)[:8]}
DIQQAT! Bir martalik chipta faqat ushbu
bekatda 1 ta qatnov uchun amal qiladi!*"""
    elif langugae == 'ru':
        return f"""*Остановка: Buyuk Ipak Yo'li
Дата: {bugun_oy} год Время: {vaqti}
    << ТАШКЕНТСКИЙ МЕТРОПОЛИТ>> UZ
Номер заявки: #{str(value)[:8]}
ВНИМАНИЕ! Только разовый билет
действует на 1 поездку на вокзале!*"""
    else:
        return f"""*Stop: Buyuk Ipak Yo'li
Date: {bugun_oy} year Time: {vaqti}
    << TASHKENT METROPOLITAN>> UZ
Application number: #{str(value)[:8]}
ATTENTION! Single ticket only
valid for 1 trip at the station*"""


async def get_qr_code_text(languages):
    if languages == 'uz':
        return "*Bir martalik QR kodni olish uchun to'lovni amalga oshiring\nTo'lov narxi 2.000 uzs*"
    elif languages == 'ru':
        return "*Совершите оплату и получите одноразовый QR-код\nСтоимость платежа 2.000 uzs*"
    else:
        return "*Make a payment and receive a one-time QR code\nPayment cost 2.000 uzs*"


async def get_tarif_text(languages):
    if languages == 'uz':
        return "*Tariflardan birini tanlang*"
    elif languages == 'ru':
        return "*Выберите один из тарифов*"
    else:
        return "*Choose one of the tariffs*"


async def get_tarif_info_text(languages, tarif_info):
    if languages == 'uz':
        return f"*{tarif_info.get('tarif_name', {})} tarifimiz narxi: {tarif_info.get('tarif_price', {})} uzs*"
    elif languages == 'ru':
        return f"*{tarif_info.get('tarif_name', {})} цена нашего тарифа: {tarif_info.get('tarif_price', {})} uzs*"
    else:
        return f"*{tarif_info.get('tarif_name', {})} our tariff price: {tarif_info.get('tarif_price', {})} uzs*"


async def get_pay_text(languages):
    if languages == 'uz':
        return "*To'lov turini tanlang*"
    elif languages == 'ru':
        return "*Выберите тип оплаты*"
    else:
        return "*Select the payment type*"


async def users_tarif_date(date):
    if date == '1':
        return 15
    elif date == '2':
        return 30
    else:
        return 365


async def get_profile_text(languages, data):
    ism_fam = data.get('ism_fam', {})
    phone_number = data.get('phone_number', {})
    telegram_language = data.get('language', {})
    is_active = data.get('is_active', {})
    start_tarif_time = data.get('active_tarif_user_start', {})
    end_tarif_time = data.get('active_tarif_user_end', {})
    qolgan_tarif_vaqti = data.get('tarif_end', {})
    user_tarif_id = data.get('user_tarif', {})

    if user_tarif_id != 'Tarif mavjud emas':
        select_tarif_category = await api.select_category_by_id(int(user_tarif_id))
    else:
        select_tarif_category = {'tarif_name': 'Tarif mavjud emas'}

    text = ""

    if is_active and languages == 'uz':
        if user_tarif_id != 'Tarif mavjud emas' and start_tarif_time is not None:
            is_active = 'Faol'
            if start_tarif_time:
                start_tarif_time = start_tarif_time[:10]
            text = f"*Sizning Malumotlaringiz\n\nIsm Familyangiz: {ism_fam}\nTel raqamingiz: {phone_number}\n*"
            text += f"*Telegram tili: {telegram_language}\nTarifingiz holati: {is_active}\nTarif Faol bolgan vaqt: {start_tarif_time}\n*"
            text += f"*Tarif tugash sanasi: {end_tarif_time}\nTarif tugashiga qolgan kun: {qolgan_tarif_vaqti}\nSizning Tarifingiz: {select_tarif_category.get('tarif_name', {})}*"
            return text
    elif is_active is False and languages == 'uz':
        is_active = 'Faol emas'
        text = f"*Sizning Malumotlaringiz\n\nIsm Familyangiz: {ism_fam}\nTel raqamingiz: {phone_number}\n*"
        text += f"*Telegram tili: {telegram_language}\nTarifingiz holati: {is_active}\nTarif Faol bolgan vaqt: Tarif mavjud emas\n*"
        text += f"*Tarif tugash sanasi: Tarif mavjud emas\nTarif tugashiga qolgan kun: Tarif mavjud emas\nSizning Tarifingiz: {select_tarif_category.get('tarif_name', {})}*"
        return text

    if is_active and languages == 'ru':
        if user_tarif_id != 'Tarif mavjud emas' and start_tarif_time is not None:
            is_active = 'Активный'
            if start_tarif_time:
                start_tarif_time = start_tarif_time[:10]
            text = f"*Ваша информация\n\nИмя: {ism_fam}\nНомер телефона: {phone_number}\n*"
            text += f"*Язык Telegram: {telegram_language}\nСтатус вашего тарифа: {is_active}\nВремя активности тарифа: {start_tarif_time}\n*"
            text += f"*Дата окончания тарифа: {end_tarif_time}\nДней до окончания действия тарифа: {qolgan_tarif_vaqti}\nВаш тариф: {select_tarif_category.get('tarif_name', {})}*"
            return text
    elif is_active is False and languages == 'ru':
        is_active = 'Не активен'
        text = f"*Ваша информация\n\nИмя: {ism_fam}\nНомер телефона: {phone_number}\n*"
        text += f"*Язык телеграммы: {telegram_language}\nСтатус вашего тарифа: {is_active}\nВремя активности тарифа: Тариф недоступен\n*"
        text += f"*Дата истечения срока действия тарифа: тариф недоступен.\nДней до истечения срока действия тарифа: тариф недоступен.\nВаш тариф: тариф недоступен*"
        return text

    if is_active and languages == 'eng':
        if user_tarif_id != 'Tarif mavjud emas' and start_tarif_time is not None:
            is_active = 'Активный'
            if start_tarif_time:
                start_tarif_time = start_tarif_time[:10]
            text = f"*Your information\n\nName: {ism_fam}\nPhone number: {phone_number}\n*"
            text += f"*Telegram language: {telegram_language}\nYour tariff status: {is_active}\nTariff active time: {start_tarif_time}\n*"
            text += f"*Tariff expiration date: {end_tarif_time}\nDays until tariff expiration: {qolgan_tarif_vaqti}\nYour tariff: {select_tarif_category.get('tarif_name', {})}*"
            return text
    elif is_active is False and languages == 'eng':
        is_active = 'Not active'
        text = f"*Your information\n\nName: {ism_fam}\nPhone number: {phone_number}\n*"
        text += f"*Telegram language: {telegram_language}\nYour tariff status: {is_active}\nTariff active time: Tariff unavailable\n*"
        text += f"*Tariff expiration date: tariff unavailable.\nDays until tariff expiration: tariff unavailable.\nYour tariff:  tariff unavailable*"
        return text

# async def get_profile_text(languages, data):
#     ism_fam = data.get('ism_fam', {})
#     phone_number = data.get('phone_number', {})
#     telegram_language = data.get('language', {})
#     is_active = data.get('is_active', {})
#     start_tarif_time = data.get('active_tarif_user_start', {})
#     end_tarif_time = data.get('active_tarif_user_end', {})
#     qolgan_tarif_vaqti = data.get('tarif_end', {})
#     user_tarif_id = data.get('user_tarif', {})
#
#     if user_tarif_id != 'Tarif mavjud emas':
#         select_tarif_category = await api.select_category_by_id(int(user_tarif_id))
#     else:
#         select_tarif_category = {'tarif_name': 'Tarif mavjud emas'}
#
#     text = ""
#     status_text = {
#         'uz': {'active': 'Faol', 'inactive': 'Faol emas'},
#         'ru': {'active': 'Активный', 'inactive': 'Не активен'},
#         'eng': {'active': 'Active', 'inactive': 'Not active'}
#     }
#     lang_text = {
#         'uz': {
#             'header': '*Sizning Malumotlaringiz\n\n',
#             'tariff_unavailable': 'Tarif mavjud emas',
#             'inactive_time': 'Tarif mavjud emas',
#             'inactive_days': 'Tarif mavjud emas',
#             'tariff': 'Sizning Tarifingiz: ',
#             'tariff_status': 'Tarifingiz holati: ',
#             'tariff_active_time': 'Tarif Faol bolgan vaqt: ',
#             'tariff_expiration_date': 'Tarif tugash sanasi: ',
#             'days_until_expiration': 'Tarif tugashiga qolgan kun: '
#         },
#         'ru': {
#             'header': '*Ваша информация\n\n',
#             'tariff_unavailable': 'тариф недоступен',
#             'inactive_time': 'Тариф недоступен',
#             'inactive_days': 'тариф недоступен',
#             'tariff': 'Ваш тариф: ',
#             'tariff_status': 'Статус вашего тарифа: ',
#             'tariff_active_time': 'Время активности тарифа: ',
#             'tariff_expiration_date': 'Дата истечения срока действия тарифа: ',
#             'days_until_expiration': 'Дней до истечения срока действия тарифа: '
#         },
#         'eng': {
#             'header': '*Your information\n\n',
#             'tariff_unavailable': 'tariff unavailable',
#             'inactive_time': 'Tariff unavailable',
#             'inactive_days': 'tariff unavailable',
#             'tariff': 'Your tariff: ',
#             'tariff_status': 'Your tariff status: ',
#             'tariff_active_time': 'Tariff active time: ',
#             'tariff_expiration_date': 'Tariff expiration date: ',
#             'days_until_expiration': 'Days until tariff expiration: '
#         }
#     }
#
#     if is_active and languages in lang_text:
#         is_active_text = status_text[languages]['active']
#         if user_tarif_id != 'Tarif mavjud emas' and start_tarif_time is not None:
#             start_tarif_time = start_tarif_time[:10]
#             text = lang_text[languages]['header']
#             text += f"Ism Familyangiz: {ism_fam}\nTel raqamingiz: {phone_number}\n"
#             text += f"Telegram tili: {telegram_language}\n"
#             text += f"{lang_text[languages]['tariff_status']}{is_active_text}\n"
#             text += f"{lang_text[languages]['tariff_active_time']}{start_tarif_time}\n"
#             text += f"{lang_text[languages]['tariff_expiration_date']}{end_tarif_time}\n"
#             text += f"{lang_text[languages]['days_until_expiration']}{qolgan_tarif_vaqti}\n"
#             text += f"{lang_text[languages]['tariff']}{select_tarif_category.get('tarif_name', lang_text[languages]['tariff_unavailable'])}*"
#             return text
#         else:
#             is_active_text = status_text[languages]['inactive']
#             text = lang_text[languages]['header']
#             text += f"Ism Familyangiz: {ism_fam}\nTel raqamingiz: {phone_number}\n"
#             text += f"Telegram tili: {telegram_language}\n"
#             text += f"{lang_text[languages]['tariff_status']}{is_active_text}\n"
#             text += f"{lang_text[languages]['tariff_active_time']}{lang_text[languages]['inactive_time']}\n"
#             text += f"{lang_text[languages]['tariff_expiration_date']}{lang_text[languages]['inactive_time']}\n"
#             text += f"{lang_text[languages]['days_until_expiration']}{lang_text[languages]['inactive_days']}\n"
#             text += f"{lang_text[languages]['tariff']}{select_tarif_category.get('tarif_name', lang_text[languages]['tariff_unavailable'])}*"
#             return text
