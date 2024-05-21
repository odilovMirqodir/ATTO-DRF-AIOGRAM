import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.filters import CommandStart
from aiogram.types import Message, LabeledPrice, ShippingQuery, PreCheckoutQuery
from config.config import BOT_TOKEN, PROVIDER_TOKEN_CLICK, PROVIDER_TOKEN_PAYME
from api.api import GetRequests
from buttons.buttons import *
from function_text.reply_text import *
from aiogram.fsm.context import FSMContext
from states.states import Royxat
from uuid import uuid4
import os
import datetime

TOKEN = BOT_TOKEN

dp = Dispatcher()
api = GetRequests()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    telegram_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    user_exists = await api.get_user(telegram_id)
    language_user = await api.get_language_by_user_id(telegram_id)
    text = await get_hello_text()
    text1 = await get_hello_text1(language_user)
    if user_exists:
        await message.answer(text1, reply_markup=await main_menu(language_user), parse_mode='markdown')
    else:
        await api.create_user(telegram_id, username, first_name)
        await message.answer(text, reply_markup=await languages(), parse_mode='markdown')


@dp.message(lambda message: message.text in ['🇺🇿 Uzbek', '🇷🇺 Русский', "🇺🇸 English"])
async def reaction_lang_ru_uz(message: types.Message):
    user_id = message.from_user.id
    await api.update_language(user_id, await update_langugae_user(message.text))
    language_user = await api.get_language_by_user_id(user_id)
    registration = (await api.registration_user(user_id))[0]
    registration_text = await get_registration_text(language_user)
    menu_text = await get_menu_text(language_user)
    if registration is None:
        await message.answer(registration_text, reply_markup=await get_registration(language_user),
                             parse_mode='markdown')
    else:
        await message.answer(menu_text, parse_mode='markdown', reply_markup=await main_menu(language_user))


@dp.message(lambda message: message.text in ['Зарегистрироваться', 'Ro\'yxatdan o\'tish', 'Registration'])
async def resgistration_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    language_user = await api.get_language_by_user_id(user_id)
    text = await name_surname_text(language_user)
    await message.answer(text, parse_mode='markdown', reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(Royxat.full_name)


@dp.message(Royxat.full_name)
async def resgistration_full_name(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    language_user = await api.get_language_by_user_id(user_id)
    if message.text.replace(' ', '').isalpha() and len(message.text.split()) == 2:
        await state.update_data(full_name=message.text)
        text = await send_phone_number_text(language_user)
        await message.answer(text, parse_mode='markdown', reply_markup=await send_user_phone(language_user))
        await state.set_state(Royxat.phone_number)
    else:
        text = await name_surname_text(language_user)
        await message.answer(text, parse_mode='markdown')


@dp.message(Royxat.phone_number)
async def user_phone(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    language_user = await api.get_language_by_user_id(user_id)
    await state.update_data(phone_number=message.contact.phone_number)
    data = await state.get_data()
    user_name, phone_number = data.get('full_name', {}), data.get('phone_number', {})
    await api.patch_user_full_name_username(user_id, user_name, phone_number)
    text = await success_all(language_user)
    await message.answer(text=text, parse_mode='markdown', reply_markup=await main_menu(language_user))
    await state.clear()


@dp.message(lambda message: message.text in ['QR kod', 'QR код', 'QR code'])
async def get_qr_code(message: types.Message, bot: Bot):
    user_id = message.from_user.id
    language_user = await api.get_language_by_user_id(user_id)
    is_active = await api.get_is_active_by_user_id(user_id)
    if is_active:
        value = uuid4()
        img = qrcode.make(str(value))
        img_path = f'qrcodes/{value}.png'
        img.save(img_path)
        await bot.send_photo(message.chat.id, types.FSInputFile(img_path),
                             caption=await get_qr_code_for_user(language_user, value), parse_mode='markdown',
                             reply_markup=await get_new_qr_code(language_user))
        os.remove(img_path)
    else:
        await message.answer(await get_qr_code_text(language_user), parse_mode='markdown',
                             reply_markup=await get_payments_button())


async def send_invoice_and_payme(bot, user_id, total_amount, state):
    try:
        product_name = 'ATTO'
        prices = [LabeledPrice(label=product_name, amount=total_amount)]

        await bot.send_invoice(user_id,
                               title="ATTO",
                               description=f"{product_name}  {total_amount}",
                               provider_token=PROVIDER_TOKEN_PAYME,
                               currency="uzs",
                               need_email=True,
                               prices=prices,
                               start_parameter="example",
                               payload="some_invoice")
    except Exception as e:
        await bot.send_message(user_id, f"Xatolik yuz berdi: {e}")
    finally:
        await state.clear()


@dp.callback_query(lambda call: call.data == 'payme_uz')
async def submit_card_payment(call: types.CallbackQuery, bot: Bot, state: FSMContext):
    user_id = call.from_user.id
    data = await state.get_data()
    tarif_name = data.get('tarif_name', None)
    if tarif_name:
        category_info = await api.select_category_by_id(int(tarif_name))
        await api.patch_user_tarif_name(user_id, tarif_name)
        total_amount = category_info.get('tarif_price', 200000)
        await send_invoice_and_payme(bot, user_id, total_amount, state)
    else:
        total_amount = 200000
        await send_invoice_and_payme(bot, user_id, total_amount, state)


async def send_invoice_and_clear(bot, user_id, total_amount, state):
    try:
        product_name = 'ATTO'
        prices = [LabeledPrice(label=product_name, amount=total_amount)]

        await bot.send_invoice(user_id,
                               title="ATTO",
                               description=f"{product_name}  {total_amount}",
                               provider_token=PROVIDER_TOKEN_CLICK,
                               currency="uzs",
                               need_email=True,
                               prices=prices,
                               start_parameter="example",
                               payload="some_invoice")
    except Exception as e:
        await bot.send_message(user_id, f"Xatolik yuz berdi: {e}")
    finally:
        await state.clear()


@dp.callback_query(lambda call: call.data == 'click_uz')
async def submit_card_payment(call: types.CallbackQuery, bot: Bot, state: FSMContext):
    user_id = call.from_user.id
    data = await state.get_data()
    tarif_name = data.get('tarif_name', None)
    if tarif_name:
        category_info = await api.select_category_by_id(int(tarif_name))
        await api.patch_user_tarif_name(user_id, tarif_name)
        total_amount = category_info.get('tarif_price', 200000)
        await send_invoice_and_clear(bot, user_id, total_amount, state)
    else:
        total_amount = 200000
        await send_invoice_and_clear(bot, user_id, total_amount, state)


@dp.pre_checkout_query(lambda q: True)
async def check(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message(F.successful_payment)
async def handle_successful_payment(message: Message, bot: Bot):
    user_id = message.from_user.id
    language_user = await api.get_language_by_user_id(user_id)
    await api.patch_user_is_activate(user_id, True)
    tarif_user = await api.get_is_tarif_by_user_id(user_id)
    current_date = datetime.datetime.now()
    data = current_date.strftime("%Y-%m-%d")
    future_date = current_date + datetime.timedelta(days=int(await users_tarif_date(tarif_user)))
    future_date_str = future_date.strftime("%Y-%m-%d")
    end_tarif = (future_date - current_date).days
    is_active = await api.get_is_active_by_user_id(user_id)

    if is_active and tarif_user != 'Tarif mavjud emas':
        await api.update_datetime_start(user_id, data, future_date_str, end_tarif)
        value = uuid4()
        img = qrcode.make(str(value))
        img_path = f'qrcodes/{value}.png'
        img.save(img_path)
        await bot.send_photo(message.chat.id, types.FSInputFile(img_path),
                             caption=await get_qr_code_for_user(language_user, value), parse_mode='markdown',
                             reply_markup=await get_new_qr_code(language_user))
        os.remove(img_path)
    else:
        value = uuid4()
        img = qrcode.make(str(value))
        img_path = f'qrcodes/{value}.png'
        img.save(img_path)
        await bot.send_photo(message.chat.id, types.FSInputFile(img_path),
                             caption=await get_qr_code_for_user(language_user, value), parse_mode='markdown',
                             reply_markup=await get_new_qr_code(language_user))
        os.remove(img_path)
        await api.patch_user_is_activate(user_id, False)
    while True:
        if is_active and tarif_user != 'Tarif mavjud emas':
            start_date, end_date, remaining_days = await api.get_tarif_users(user_id)

            if remaining_days > 0:
                remaining_days -= 1
                await api.update_day_users(user_id, remaining_days)
            else:
                await api.patch_user_is_activate(user_id, False)
            await asyncio.sleep(86400)
        else:
            break


@dp.message(lambda message: message.text in ['Sozlamalar ⚙', 'Настройки ⚙', 'Settings ⚙'])
async def get_my_profile(message: types.Message):
    user_id = message.from_user.id
    language_user = await api.get_language_by_user_id(user_id)
    text = await get_text_language_user(language_user)
    await message.answer(text, parse_mode='markdown', reply_markup=await languages())


@dp.message(lambda message: message.text in ['Mening Profilim', 'Мой профиль', 'My Profile'])
async def get_my_profile(message: types.Message):
    user_id = message.from_user.id
    language_user = await api.get_language_by_user_id(user_id)
    data = await api.get_all_user_information(user_id)
    text = await get_profile_text(language_user, data)
    await message.answer(text, parse_mode='markdown')


@dp.message(lambda message: message.text in ['Tariflar', 'Тарифы', 'Tariffs'])
async def get_tarif(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    language_user = await api.get_language_by_user_id(user_id)
    await message.answer(await get_tarif_text(language_user), parse_mode='markdown',
                         reply_markup=await get_categories_button())
    await state.set_state(Royxat.tarif_name)


@dp.callback_query(Royxat.tarif_name, lambda call: call.data.startswith('category|'))
async def reaction_to_categories(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    language_user = await api.get_language_by_user_id(user_id)
    category_id = call.data.split('|')[1]
    category_info = await api.select_category_by_id(category_id)
    await state.update_data(tarif_name=category_id)
    tarif_info = await get_tarif_info_text(language_user, category_info)
    await call.message.answer(tarif_info, parse_mode='markdown', reply_markup=await get_activate_tarif(language_user))


@dp.callback_query(lambda call: call.data.startswith('tarif_activate'))
async def reaction_to_categories(call: types.CallbackQuery):
    user_id = call.from_user.id
    language_user = await api.get_language_by_user_id(user_id)
    await call.message.answer(await get_pay_text(language_user), parse_mode='markdown',
                              reply_markup=await get_payments_button())


@dp.callback_query(lambda call: call.data == 'new_qr_generate')
async def reaction_to_generate_qr(call: types.CallbackQuery, bot: Bot):
    user_id = call.from_user.id
    language_user = await api.get_language_by_user_id(user_id)
    is_active = await api.get_is_active_by_user_id(user_id)
    if is_active:
        value = uuid4()
        img = qrcode.make(str(value))
        img_path = f'qrcodes/{value}.png'
        img.save(img_path)
        await bot.send_photo(call.message.chat.id, types.FSInputFile(img_path),
                             caption=await get_qr_code_for_user(language_user, value), parse_mode='markdown',
                             reply_markup=await get_new_qr_code(language_user))
        os.remove(img_path)
    else:
        await call.message.answer(await get_qr_code_text(language_user), parse_mode='markdown',
                                  reply_markup=await get_payments_button())


async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
