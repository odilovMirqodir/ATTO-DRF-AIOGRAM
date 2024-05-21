from aiogram.fsm.state import StatesGroup, State


class Royxat(StatesGroup):
    full_name = State()
    phone_number = State()
    total_amount = State()
    tarif_name = State()
    tarif_price = State()
